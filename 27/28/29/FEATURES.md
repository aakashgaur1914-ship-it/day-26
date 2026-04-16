# SocialHub - Advanced Social Media Platform

A full-stack social media application built with FastAPI (backend) and React (frontend) featuring user profiles, post engagement (likes/comments), follow system, algorithmic feed, and real-time notifications.

## 🚀 Features Implemented

### Core Social Features
- ✅ User profiles with bio, profile picture, and stats (posts/followers/following count)
- ✅ Post creation with image upload support
- ✅ Comment system with nested replies
- ✅ Like/unlike posts with engagement tracking
- ✅ Follow/unfollow users with relationship tracking
- ✅ Algorithmic feed with multiple views:
  - **For You**: Personalized (60% following posts, 20% own posts, 20% trending)
  - **Following**: Only posts from followed users
  - **Trending**: High-engagement posts from last 7 days
  - **Explore**: Discover posts from non-followed users
- ✅ Notification system for likes, comments, and follows
- ✅ Notification center with read/unread status

### Technical Stack
- **Backend**: FastAPI + SQLAlchemy + PostgreSQL
- **Frontend**: React 18 + TypeScript + Tailwind CSS + Vite
- **Authentication**: JWT tokens with bcrypt password hashing
- **Database Migrations**: Alembic with version control

## 📋 Prerequisites

- Python 3.9+
- Node.js 16+
- PostgreSQL 12+
- Git

## 🔧 Setup Instructions

### 1. Database Migration (CRITICAL - Required before first run)

```bash
cd "c:\Users\aakas\Desktop\day 28"

# Run the migration to apply all schema changes
alembic upgrade head
```

This migration creates:
- `user_followers` table for follow relationships
- `notification` table for tracking user activities
- Enhanced fields on existing tables (bio, profile_picture, image_url, etc.)

### 2. Backend Setup

```bash
cd "c:\Users\aakas\Desktop\day 28"

# Install dependencies (if not already installed)
pip install -r requirements.txt

# Start the backend server
python -m uvicorn app.main:app --reload --port 8000
```

Backend will be available at: `http://localhost:8000`
API documentation: `http://localhost:8000/docs`

### 3. Frontend Setup

```bash
cd "c:\Users\aakas\Desktop\day 28\frontend"

# Install dependencies (if not already installed)
npm install

# Start development server
npm run dev
```

Frontend will be available at: `http://localhost:3001`

## 🧪 Testing the Features

### User Flow

1. **Register & Login**
   - Go to http://localhost:3001/register
   - Create account (username, email, password)
   - Login with credentials

2. **Create Posts**
   - Click "✍️ Create New Post"
   - Enter content (title and body)
   - Optional: Upload image using the backend upload endpoint
   - Click Post

3. **Explore & Follow Users**
   - Click "Explore" in navbar
   - View trending posts from other users
   - Click "Follow" to follow users
   - Followed users' posts will appear in "For You" feed

4. **Engage with Posts**
   - Click ❤️ to like posts
   - Click 💬 to reply/comment
   - View engagement metrics (likes count, comments count)

5. **Feed Algorithms**
   - Click "Feed" to access feed views:
     - **For You**: Recommended posts based on follows and popularity
     - **Following**: All posts from users you follow
     - **Trending**: Current popular posts

6. **Manage Notifications**
   - Click 🔔 in navbar to see notifications
   - Notifications show: likes, comments, and new followers
   - Unread notifications have a blue badge
   - Click to mark as read

7. **View Profiles**
   - Click username anywhere to view profile
   - See user stats (posts, followers, following)
   - Click Follow/Following button to manage relationship
   - View user's posts timeline

## 📁 Project Structure

### Backend (`app/`)

```
app/
├── api/v1/
│   ├── auth.py          - Authentication endpoints
│   ├── comments.py      - Comment CRUD operations
│   ├── deps.py          - Dependency injection
│   ├── feed.py          - Algorithmic feed generation
│   ├── likes.py         - Like/unlike operations
│   ├── posts.py         - Post CRUD + image upload
│   └── users.py         - User profile + follow system
├── core/
│   ├── config.py        - Configuration settings
│   └── security.py      - JWT & password hashing
├── crud/
│   └── base.py          - Base CRUD operations
├── db/
│   └── database.py      - Database connection
├── models/
│   ├── user.py          - User model with relationships
│   ├── post.py          - Post model
│   ├── comment.py       - Comment model
│   ├── like.py          - Like model
│   └── notification.py  - Notification model
├── schemas/
│   ├── user.py          - User schemas + validation
│   ├── post.py          - Post schemas
│   ├── comment.py       - Comment schemas
│   ├── like.py          - Like schemas
│   └── notification.py  - Notification schemas
└── main.py              - FastAPI app setup
```

### Frontend (`frontend/src/`)

```
frontend/src/
├── components/
│   ├── CommentsSection.tsx    - Comment display & form
│   ├── FollowButton.tsx       - Follow/unfollow toggle
│   ├── LikeButton.tsx         - Like/unlike toggle
│   ├── Navbar.tsx             - Navigation & notifications
│   ├── PostCard.tsx           - Post display component
│   └── AuthForm.tsx           - Login/Register form
├── context/
│   └── AuthContext.tsx        - Authentication state
├── pages/
│   ├── Home.tsx               - Home feed
│   ├── FeedPage.tsx           - Advanced feed with algorithms
│   ├── ExplorePage.tsx        - Discovery page
│   ├── UserProfile.tsx        - User profile view
│   ├── NotificationsPage.tsx  - Notification center
│   ├── Login.tsx              - Login page
│   └── Register.tsx           - Registration page
├── services/
│   └── api.ts                 - API client with axios
├── types/
│   └── index.ts               - TypeScript type definitions
├── styles/
│   └── index.css              - Tailwind CSS setup
└── App.tsx                    - Main app component
```

## 🔌 API Endpoints

### Authentication
- `POST /api/v1/auth/auth/register` - Register new user
- `POST /api/v1/auth/auth/token` - Login (get JWT token)

### Users
- `GET /api/v1/users/profile/{user_id}` - Get user profile with stats
- `PUT /api/v1/users/me` - Update current user profile
- `POST /api/v1/users/follow/{user_id}` - Follow a user
- `POST /api/v1/users/unfollow/{user_id}` - Unfollow a user
- `GET /api/v1/users/{user_id}/followers` - Get user's followers
- `GET /api/v1/users/{user_id}/following` - Get user's following list
- `GET /api/v1/users/notifications` - Get current user's notifications
- `PUT /api/v1/users/notifications/{id}/read` - Mark notification as read

### Posts
- `GET /api/v1/posts` - List all posts
- `POST /api/v1/posts` - Create new post
- `GET /api/v1/posts/{id}` - Get specific post
- `PUT /api/v1/posts/{id}` - Update post
- `DELETE /api/v1/posts/{id}` - Delete post
- `POST /api/v1/posts/upload` - Upload post image

### Comments
- `POST /api/v1/comments` - Create comment
- `GET /api/v1/comments/{post_id}` - Get post comments
- `PUT /api/v1/comments/{id}` - Update comment (author only)
- `DELETE /api/v1/comments/{id}` - Delete comment (author only)

### Likes
- `POST /api/v1/likes/{post_id}` - Like a post
- `DELETE /api/v1/likes/{post_id}` - Unlike a post
- `GET /api/v1/likes/{post_id}/count` - Get like count
- `GET /api/v1/likes/{post_id}/users` - Get users who liked

### Feed
- `GET /api/v1/feed` - Get personalized feed (default algorithm)
- `GET /api/v1/feed?algorithm=following` - Get following-only feed
- `GET /api/v1/feed?algorithm=trending` - Get trending posts
- `GET /api/v1/feed/explore` - Get explore/discovery posts

## 🔐 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: Bcrypt with salt for password security
- **CORS Protection**: Configured for development ports (3000, 3001, 5173)
- **Authorization**: Endpoint-level checks for user ownership
- **SQL Injection Prevention**: SQLAlchemy parameterized queries

## 🐛 Troubleshooting

### "Network Error" on Register
- Ensure backend is running on port 8000
- Frontend correctly proxies `/api` to `http://localhost:8000/api/v1`
- Check browser console for specific error messages

### Database Migration Errors
```bash
# Reset migrations (development only!)
alembic downgrade base
alembic upgrade head
```

### Notification Badge Not Updating
- Notifications use 10-second polling interval
- Check browser console for fetch errors
- Ensure backend notification endpoints are accessible

### Image Upload Issues
- Check `/uploads/images/` folder exists on backend
- Verify POST /api/v1/posts/upload is accessible
- Image files should be under 10MB

## 📊 Feed Algorithm Details

The personalized "For You" feed uses a weighted algorithm:

```
Feed Score = (60% posts from following users) 
           + (20% user's own posts)
           + (20% trending posts)

Trending Score = (count of likes + count of comments) 
               sorted by recent (last 7 days)
```

Posts are ordered by engagement score, then by recency.

## 🚧 Future Enhancements

- [ ] WebSocket real-time notifications (currently polling)
- [ ] Image upload in post creation UI
- [ ] Direct messaging system
- [ ] Post search and filtering
- [ ] Hashtag system
- [ ] User search
- [ ] Post sharing/retweets
- [ ] Analytics dashboard
- [ ] Mobile app (React Native)

## 📝 Development Commands

```bash
# Backend
python -m uvicorn app.main:app --reload --port 8000

# Frontend
cd frontend && npm run dev

# Database migrations
alembic revision --autogenerate -m "Description"
alembic upgrade head
alembic downgrade -1

# Run backend tests (if available)
pytest

# Build frontend for production
cd frontend && npm run build
```

## 🤝 Contributing

When adding new features:
1. Create database models in `app/models/`
2. Create Pydantic schemas in `app/schemas/`
3. Add API endpoints in `app/api/v1/`
4. Update alembic migrations
5. Create React components in `frontend/src/components/`
6. Add pages to `frontend/src/pages/`
7. Update routing in `App.tsx`
8. Test end-to-end flow

## 📄 License

This project is for educational purposes.

## 🆘 Support

For issues or questions:
1. Check API documentation at `http://localhost:8000/docs`
2. Review backend logs in terminal
3. Check browser console for frontend errors
4. Verify database connection in `app/core/config.py`

---

**Happy Social Networking! 🎉**
