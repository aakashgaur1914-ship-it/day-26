# ⚡ Quick Start Guide

Get the project running in 5 minutes!

## Prerequisites
- Python 3.10+ installed
- Node.js 16+ installed  
- PostgreSQL running on port 5433
- PostgreSQL user: `postgres` / password: `postgres`

## Step 1: Backend Setup (2 minutes)

```bash
# Navigate to project
cd c:\Users\aakas\Desktop\day\ 28

# Install Python packages
pip install -r requirements.txt

# Create database (in PostgreSQL)
createdb -U postgres -p 5433 social_media_db

# Run migrations
alembic upgrade head

# Seed test data (if seed_data.py exists)
python scripts/seed_data.py
```

## Step 2: Start Backend (1 minute)

```bash
uvicorn app.main:app --reload --port 8000
```

✅ Backend running at: `http://localhost:8000`
✅ API Docs at: `http://localhost:8000/docs`

## Step 3: Frontend Setup (1 minute)

```bash
cd frontend
npm install
```

## Step 4: Start Frontend (1 minute)

```bash
npm run dev
```

✅ Frontend running at: `http://localhost:3000`

## Done! 🎉

Open `http://localhost:3000` in your browser and:

1. **Register** - Create a new account
2. **Create Posts** - Share your thoughts
3. **View Feed** - See all posts
4. **Delete Posts** - Remove your posts

## Common Issues & Fixes

### "Cannot connect to database"
```bash
# Make sure PostgreSQL is running
# Or change connection string in app/core/config.py
```

### "CORS error" 
✅ Already fixed! CORS is enabled in `app/main.py`

### "Module not found"
```bash
# Make sure you're in right directory
pip install -r requirements.txt
npm install
```

### "Port already in use"
```bash
# Change port in frontend:
# Edit vite.config.ts and change port: 3000

# Or for backend:
uvicorn app.main:app --port 8001
```

## Test the Application

### Register a User
1. Go to `http://localhost:3000/register`
2. Fill in email, username, password
3. Click Register

### Create a Post
1. You'll be auto-logged in
2. Click "✍️ Create New Post"
3. Enter title and content
4. Click "Post"

### View Posts
- Posts appear in feed
- Shows author and creation date

### Delete a Post
- Click "Delete" on any of your posts
- Confirm when asked

## API Testing (Optional)

```bash
# Register
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","username":"testuser","password":"password123"}'

# Login
curl -X POST "http://localhost:8000/api/v1/auth/login/access-token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=password123"

# Get Posts
curl -X GET "http://localhost:8000/api/v1/posts/"
```

## Production Build

```bash
# Backend
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app

# Frontend
npm run build
# Static files in dist/ folder
```

## Key Files

- ✅ **Frontend**: `frontend/src/App.tsx` (main app)
- ✅ **Backend**: `app/main.py` (FastAPI app)
- ✅ **Auth**: `app/api/auth.py` (login/register)
- ✅ **Posts**: `app/api/v1/posts.py` (CRUD)
- ✅ **Docs**: Read `BACKEND_ANALYSIS.md` and `SETUP_GUIDE.md`

## Helpful Links

- Frontend Docs: `frontend/README.md`
- Backend Analysis: `BACKEND_ANALYSIS.md`
- Complete Guide: `SETUP_GUIDE.md`
- Project Summary: `PROJECT_SUMMARY.md`

## Need Help?

1. Check the relevant README file
2. Look at error messages in console
3. Verify database is running
4. Ensure ports 3000 and 8000 are free
5. Check that .env file has correct config

---

**You're all set!** 🚀

Start with Step 1 and follow through. It should take about 5 minutes total.

Questions? Check the documentation files in the project root.
