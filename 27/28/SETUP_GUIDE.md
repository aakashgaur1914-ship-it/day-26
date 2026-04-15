# Project Setup Guide

## Quick Start

### Prerequisites
- Python 3.10+
- Node.js 16+
- PostgreSQL 12+
- Redis (optional, for Celery)

### Backend Setup

1. **Install Python Dependencies**
   ```bash
   cd c:\Users\aakas\Desktop\day\ 28
   pip install -r requirements.txt
   ```

2. **Create `.env` file** (or use existing)
   ```bash
   # .env
   DATABASE_URL=postgresql://postgres:postgres@127.0.0.1:5433/social_media_db
   SECRET_KEY=your-secret-key-here
   ```

3. **Setup Database**
   ```bash
   # Run migrations
   alembic upgrade head
   
   # Seed initial data (if seed_data.py exists)
   python scripts/seed_data.py
   ```

4. **Run Backend Server**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   
   Access at: `http://localhost:8000`
   - API Docs: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Frontend Setup

1. **Install Dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Start Development Server**
   ```bash
   npm run dev
   ```
   
   Access at: `http://localhost:3000`

3. **Build for Production**
   ```bash
   npm run build
   ```

## Important Backend Fixes Required

### 1. Enable CORS (Critical for Frontend)

Edit `app/main.py` and add after FastAPI initialization:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 2. Add Missing Post Endpoints

Edit `app/api/v1/posts.py` and add:

```python
@router.put("/{id}", response_model=PostResponse)
def update_post(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    post_in: PostUpdate,
    current_user: User = Depends(get_current_user),
) -> Any:
    """Update a post."""
    post = crud_post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    post = crud_post.update(db=db, db_obj=post, obj_in=post_in)
    return post

@router.delete("/{id}")
def delete_post(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: User = Depends(get_current_user),
) -> Any:
    """Delete a post."""
    post = crud_post.get(db=db, id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    crud_post.remove(db=db, id=id)
    return {"message": "Post deleted"}
```

## Testing the Application

### Test User Registration
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "testuser",
    "password": "password123"
  }'
```

### Test User Login
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login/access-token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=password123"
```

### Get Posts
```bash
curl -X GET "http://localhost:8000/api/v1/posts/"
```

## Database Connection

Default configuration:
- **Host**: 127.0.0.1
- **Port**: 5433
- **Database**: social_media_db
- **User**: postgres
- **Password**: postgres

To modify, update environment variables or `app/core/config.py`

## Frontend Features

✅ Implemented:
- User Registration
- User Login
- Create Posts
- View Posts Feed
- Delete Posts
- Authentication State Management
- Protected Routes
- Responsive Design

## API Integration Points

Frontend API calls to backend:
1. `POST /api/v1/auth/register` - User registration
2. `POST /api/v1/auth/login/access-token` - User login
3. `GET /api/v1/posts/` - Fetch posts
4. `POST /api/v1/posts/` - Create post
5. `GET /api/v1/posts/{id}` - Get single post
6. `DELETE /api/v1/posts/{id}` - Delete post

## Troubleshooting

### Frontend can't connect to backend
- Check if backend is running on port 8000
- Verify CORS is enabled (see Backend Fixes section)
- Check browser console for errors

### Database connection failed
- Verify PostgreSQL is running
- Check connection string in `.env`
- Ensure database exists

### Login not working
- Verify user exists in database
- Check backend logs for authentication errors
- Ensure SECRET_KEY matches

## Project Files Created

### Frontend
```
frontend/
├── src/
│   ├── pages/        # Login, Register, Home
│   ├── components/   # Navbar, PostCard
│   ├── services/     # API client
│   ├── context/      # Auth context
│   ├── types/        # TypeScript interfaces
│   └── App.tsx       # Main app
├── package.json
├── vite.config.ts
├── tailwind.config.js
└── README.md
```

## Running Both Simultaneously

### Terminal 1 - Backend
```bash
cd c:\Users\aakas\Desktop\day\ 28
uvicorn app.main:app --reload --port 8000
```

### Terminal 2 - Frontend
```bash
cd c:\Users\aakas\Desktop\day\ 28\frontend
npm install  # Only first time
npm run dev
```

Then visit: `http://localhost:3000`

## Production Build

### Backend
```bash
# Use gunicorn for production
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

### Frontend
```bash
cd frontend
npm run build
# Static files in dist/ folder
```

## Next Steps

1. ✅ Frontend created
2. ⚠️ Add CORS to backend (critical)
3. ⚠️ Add PUT/DELETE endpoints
4. Setup PostgreSQL database
5. Run both servers
6. Test application flow
7. Deploy to production
