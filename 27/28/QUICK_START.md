# 🚀 QUICK START GUIDE

## What's Been Built

You now have a **complete social media platform** with:
- ✅ User profiles with follow system
- ✅ Posts with image upload support  
- ✅ Comments on posts
- ✅ Likes/engagement tracking
- ✅ Algorithmic feed (Personalized, Following, Trending, Explore)
- ✅ Real-time notification center
- ✅ Full React frontend with routing
- ✅ Professional UI with Tailwind CSS

## 🎯 Run This NOW (Critical First Step)

### Step 1: Apply Database Changes
```bash
cd "c:\Users\aakas\Desktop\day 28"
alembic upgrade head
```

**Why**: This creates the missing tables (notifications, followers) and columns (bio, profile_picture, image_url, etc.) that the new features need.

### Step 2: Start Backend
```bash
cd "c:\Users\aakas\Desktop\day 28"
python -m uvicorn app.main:app --reload --port 8000
```

Keep this terminal open. You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 3: Start Frontend (New Terminal)
```bash
cd "c:\Users\aakas\Desktop\day 28\frontend"
npm run dev
```

You should see:
```
➜  Local:   http://localhost:3001/
```

### Step 4: Open Browser
Visit: **http://localhost:3001**

## ✨ Test the Features

### 1. Create Two Test Accounts
- Register user "alice" with email alice@test.com
- Register user "bob" with email bob@test.com

### 2. Test Follow System (as alice)
- Click "Explore" in navbar
- Find bob's post
- Click "Follow" button
- Bob's post now appears in alice's "Following" feed

### 3. Test Engagement (as bob)
- Create a post: "Hello World!"
- Switch to alice's account
- Click ❤️ to like the post
- Bob receives notification "alice liked your post"

### 4. Test Comments (as alice)
- Click 💬 to comment on bob's post
- Type comment: "Great post!"
- Bob receives notification "alice commented on your post"

### 5. Test Feed Algorithms
- Click "Feed" in navbar
- Switch between tabs:
  - **For You**: Mix of your posts, following posts, trending
  - **Following**: Only posts from people you follow
  - **Trending**: Most popular posts
  - **Explore**: Posts from people you don't follow yet

### 6. Check Notifications
- Click 🔔 in navbar
- See all notifications with type indicators (❤️ 💬 👤)
- Click notification to mark as read
- Unread count shows in red badge

### 7. View Profile
- Click "Profile" in navbar (or any username)
- See stats: Posts, Followers, Following
- Click "Follow/Following" to manage relationship

## 📁 New Files Created

### Backend (14 new/modified files)
- `app/models/notification.py` - Notification tracking
- `app/schemas/comment.py`, `like.py`, `notification.py` - Data validation
- `app/api/v1/users.py` (7 endpoints), `comments.py` (4), `likes.py` (4), `feed.py` (3)
- `alembic/versions/3b9d2c5e1a3f_add_social_features.py` - Database migration

### Frontend (8 new/modified files)
- `frontend/src/components/LikeButton.tsx` - Like/unlike toggle
- `frontend/src/components/FollowButton.tsx` - Follow/unfollow toggle
- `frontend/src/pages/FeedPage.tsx` - Algorithmic feed view
- `frontend/src/pages/ExplorePage.tsx` - Discovery page
- `frontend/src/pages/NotificationsPage.tsx` - Notification center
- `frontend/src/pages/CommentsSection.tsx` - Comment threads
- `frontend/src/App.tsx` - Updated routing
- `frontend/src/components/Navbar.tsx` - Updated navigation

## 🔧 Troubleshooting

### Error: "relation 'user_followers' does not exist"
**Solution**: Run `alembic upgrade head` (see Step 1)

### Error: "Network Error" on pages
**Solution**: 
- Check backend is running on port 8000
- Check frontend is running on port 3001
- Try hard refresh (Ctrl+F5) in browser

### Notifications not showing
**Solution**:
- Notifications check every 10 seconds
- Make sure you created content and engaged with it
- Check browser console for errors

### Can't upload images
**Solution**:
- Backend image upload endpoint exists but frontend UI not yet built
- Use `POST /api/v1/posts/upload` endpoint directly if needed
- Frontend image upload coming in next phase

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────┐
│              Browser (http://localhost:3001)        │
│  ┌──────────────────────────────────────────────┐   │
│  │ React App (TypeScript + Tailwind)            │   │
│  │ - Pages: Home, Feed, Explore, Profile        │   │
│  │ - Components: LikeButton, FollowButton, etc. │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
                          │
              Proxy: /api → localhost:8000/api/v1
                          │
┌─────────────────────────────────────────────────────┐
│         FastAPI Backend (http://localhost:8000)     │
│  ┌──────────────────────────────────────────────┐   │
│  │ - Auth: JWT tokens with bcrypt              │   │
│  │ - Users: Profile, follow/followers          │   │
│  │ - Posts: CRUD, image upload                 │   │
│  │ - Comments: CRUD with notifications         │   │
│  │ - Likes: Toggle with metrics                │   │
│  │ - Feed: Algorithmic (personalized/trending) │   │
│  │ - Notifications: Tracking likes/comments    │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
                          │
                   PostgreSQL Database
                          │
        Tables: user, post, comment, like
                notification, user_followers
```

## 📈 Database Schema

### New Tables
- **notification**: Tracks likes, comments, follows
- **user_followers**: Maps follower → following relationships

### Enhanced Tables
- **user**: Added bio, profile_picture, created_at
- **post**: Added image_url, updated_at  
- **comment**: Added updated_at, enforced non-null fields
- **like**: Added created_at, unique constraint (post_id, user_id)

## 💡 Next Steps (Optional)

- [ ] Build image upload UI in post creation
- [ ] Add WebSocket for real-time notifications
- [ ] Create post detail page with full comment thread
- [ ] Add user search functionality
- [ ] Implement direct messaging
- [ ] Add hashtag system
- [ ] Create analytics dashboard

## 📞 Quick Reference

| Action | Where |
|--------|-------|
| Create post | Home page, "Create New Post" button |
| Like/unlike | Click ❤️ on post |
| Comment | Click 💬 on post (use CommentsSection) |
| Follow user | Explore page or user profile |
| View feed | Click "Feed" → choose algorithm |
| See notifications | Click 🔔 in navbar |
| View profile | Click "Profile" or any username |

## ✅ Verification Checklist

Run this to verify everything works:

```bash
# 1. Test database migration
alembic upgrade head  # Should succeed

# 2. Test backend startup
python -m uvicorn app.main:app --reload --port 8000
# Should see: "Uvicorn running on http://127.0.0.1:8000"

# 3. Test API (in another terminal)
curl http://localhost:8000/docs
# Should open API documentation

# 4. Test frontend startup (in another terminal)
cd frontend && npm run dev
# Should see: "Local: http://localhost:3001/"

# 5. Test in browser
# Open http://localhost:3001
# You should see SocialHub homepage
```

---

**🎉 You're all set! Start with Step 1 above to get running.**
