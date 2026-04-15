# API Reference - SocialHub

Complete API documentation for all endpoints. All endpoints (except auth) require `Authorization: Bearer {token}` header.

## 🔐 Authentication

### Register
```http
POST /api/v1/auth/auth/register
Content-Type: application/json

{
  "username": "alice",
  "email": "alice@example.com",
  "password": "securepass123"
}

Response: 201
{
  "id": 1,
  "username": "alice",
  "email": "alice@example.com",
  "access_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

### Login
```http
POST /api/v1/auth/auth/token
Content-Type: application/x-www-form-urlencoded

username=alice&password=securepass123

Response: 200
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

---

## 👥 Users

### Get User Profile
```http
GET /api/v1/users/profile/{user_id}
Authorization: Bearer {token}

Response: 200
{
  "id": 2,
  "username": "bob",
  "email": "bob@example.com",
  "bio": "Software developer",
  "profile_picture": "https://...",
  "followers_count": 15,
  "following_count": 8,
  "posts_count": 12,
  "is_following": true,
  "created_at": "2024-01-15T10:30:00"
}
```

### Update User Profile
```http
PUT /api/v1/users/me
Authorization: Bearer {token}
Content-Type: application/json

{
  "bio": "New bio text",
  "profile_picture": "https://..."
}

Response: 200
{
  "id": 1,
  "username": "alice",
  "bio": "New bio text",
  ...
}
```

### Follow User
```http
POST /api/v1/users/follow/{user_id}
Authorization: Bearer {token}

Response: 200
{
  "message": "Successfully followed user"
}

Side Effect: Creates notification for target user
```

### Unfollow User
```http
POST /api/v1/users/unfollow/{user_id}
Authorization: Bearer {token}

Response: 200
{
  "message": "Successfully unfollowed user"
}
```

### Get User's Followers
```http
GET /api/v1/users/{user_id}/followers
Authorization: Bearer {token}

Response: 200
[
  {
    "id": 1,
    "username": "alice",
    "bio": "Designer",
    "profile_picture": "https://..."
  },
  ...
]
```

### Get User's Following List
```http
GET /api/v1/users/{user_id}/following
Authorization: Bearer {token}

Response: 200
[
  {
    "id": 2,
    "username": "bob",
    "bio": "Developer",
    "profile_picture": "https://..."
  },
  ...
]
```

### Get Notifications
```http
GET /api/v1/users/notifications
Authorization: Bearer {token}

Response: 200
[
  {
    "id": 1,
    "notification_type": "like",
    "related_user": {
      "id": 2,
      "username": "bob"
    },
    "message": "liked your post",
    "is_read": false,
    "created_at": "2024-01-20T14:30:00"
  },
  ...
]
```

### Mark Notification as Read
```http
PUT /api/v1/users/notifications/{notification_id}/read
Authorization: Bearer {token}

Response: 200
{
  "id": 1,
  "is_read": true
}
```

---

## 📝 Posts

### List All Posts
```http
GET /api/v1/posts
Authorization: Bearer {token}

Response: 200
[
  {
    "id": 1,
    "content": "This is my first post",
    "author": {
      "id": 1,
      "username": "alice"
    },
    "image_url": "https://...",
    "comments_count": 3,
    "likes_count": 15,
    "is_liked": true,
    "created_at": "2024-01-20T10:00:00"
  },
  ...
]
```

### Create Post
```http
POST /api/v1/posts
Authorization: Bearer {token}
Content-Type: application/json

{
  "content": "My new post content"
}

Response: 201
{
  "id": 5,
  "content": "My new post content",
  "author": {
    "id": 1,
    "username": "alice"
  },
  "image_url": null,
  "comments_count": 0,
  "likes_count": 0,
  "is_liked": false,
  "created_at": "2024-01-20T15:30:00"
}
```

### Get Specific Post
```http
GET /api/v1/posts/{post_id}
Authorization: Bearer {token}

Response: 200
{
  "id": 1,
  "content": "Post content",
  "author": {...},
  "image_url": "https://...",
  "comments_count": 3,
  "likes_count": 15,
  "is_liked": false,
  "created_at": "2024-01-20T10:00:00"
}
```

### Update Post
```http
PUT /api/v1/posts/{post_id}
Authorization: Bearer {token}
Content-Type: application/json

{
  "content": "Updated content"
}

Response: 200
{
  "id": 1,
  "content": "Updated content",
  ...
}

Note: Only post author can update
```

### Delete Post
```http
DELETE /api/v1/posts/{post_id}
Authorization: Bearer {token}

Response: 200
{
  "message": "Post deleted successfully"
}

Note: Only post author can delete
```

### Upload Post Image
```http
POST /api/v1/posts/upload
Authorization: Bearer {token}
Content-Type: multipart/form-data

file: [binary image data]

Response: 200
{
  "file_path": "/uploads/images/uuid-here.jpg",
  "file_size": 245632,
  "file_type": "image/jpeg"
}
```

---

## 💬 Comments

### Create Comment
```http
POST /api/v1/comments
Authorization: Bearer {token}
Content-Type: application/json

{
  "post_id": 1,
  "content": "Great post!"
}

Response: 201
{
  "id": 5,
  "post_id": 1,
  "author": {
    "id": 2,
    "username": "bob"
  },
  "content": "Great post!",
  "created_at": "2024-01-20T15:00:00"
}

Side Effect: Creates notification for post author
```

### Get Post Comments
```http
GET /api/v1/comments/{post_id}
Authorization: Bearer {token}

Response: 200
[
  {
    "id": 1,
    "post_id": 1,
    "author": {
      "id": 2,
      "username": "bob"
    },
    "content": "Nice post!",
    "created_at": "2024-01-20T14:00:00"
  },
  ...
]
```

### Update Comment
```http
PUT /api/v1/comments/{comment_id}
Authorization: Bearer {token}
Content-Type: application/json

{
  "content": "Updated comment text"
}

Response: 200
{
  "id": 1,
  "content": "Updated comment text",
  ...
}

Note: Only comment author can update
```

### Delete Comment
```http
DELETE /api/v1/comments/{comment_id}
Authorization: Bearer {token}

Response: 200
{
  "message": "Comment deleted successfully"
}

Note: Only comment author can delete
```

---

## ❤️ Likes

### Like Post
```http
POST /api/v1/likes/{post_id}
Authorization: Bearer {token}

Response: 201
{
  "id": 10,
  "post_id": 1,
  "user_id": 2,
  "created_at": "2024-01-20T15:30:00"
}

Side Effect: Creates notification for post author
Error: 400 if already liked
```

### Unlike Post
```http
DELETE /api/v1/likes/{post_id}
Authorization: Bearer {token}

Response: 200
{
  "message": "Post unliked successfully"
}

Error: 404 if not liked
```

### Get Like Count
```http
GET /api/v1/likes/{post_id}/count
Authorization: Bearer {token}

Response: 200
{
  "post_id": 1,
  "likes_count": 42
}
```

### Get Users Who Liked
```http
GET /api/v1/likes/{post_id}/users
Authorization: Bearer {token}

Response: 200
[
  {
    "id": 1,
    "username": "alice"
  },
  {
    "id": 2,
    "username": "bob"
  },
  ...
]
```

---

## 🎯 Feed

### Get Personalized Feed (Default)
```http
GET /api/v1/feed
Authorization: Bearer {token}

Response: 200
[
  {
    "id": 5,
    "content": "Post from someone you follow",
    "author": {...},
    "comments_count": 2,
    "likes_count": 8,
    "is_liked": false,
    "created_at": "2024-01-20T14:00:00"
  },
  ...
]

Algorithm: 60% following, 20% own posts, 20% trending
```

### Get Following Feed
```http
GET /api/v1/feed?algorithm=following
Authorization: Bearer {token}

Response: 200
[posts from users you follow]

Algorithm: Only posts from followed users, sorted by recency
```

### Get Trending Feed
```http
GET /api/v1/feed?algorithm=trending
Authorization: Bearer {token}

Response: 200
[high engagement posts from last 7 days]

Algorithm: Sorted by (likes + comments), then recency
```

### Get Explore Feed
```http
GET /api/v1/feed/explore
Authorization: Bearer {token}

Response: 200
[posts from users you don't follow]

Algorithm: Sorted by engagement score, helps discover new content
```

---

## ⚠️ Error Responses

All errors return appropriate HTTP status codes with messages:

```http
401 Unauthorized
{"detail": "Not authenticated"}

403 Forbidden
{"detail": "Not enough permissions"}

404 Not Found
{"detail": "Post not found"}

400 Bad Request
{"detail": "Invalid input"}

409 Conflict
{"detail": "You already liked this post"}
```

---

## 🔑 Headers Required

All authenticated requests must include:
```http
Authorization: Bearer {access_token}
```

Token obtained from login response and stored in localStorage by frontend.

---

## 📊 Data Models

### User
```json
{
  "id": 1,
  "username": "alice",
  "email": "alice@example.com",
  "bio": "Software developer",
  "profile_picture": "https://...",
  "followers_count": 15,
  "following_count": 8,
  "posts_count": 5,
  "is_following": false,
  "created_at": "2024-01-15T10:30:00"
}
```

### Post
```json
{
  "id": 1,
  "content": "Post content here",
  "author": { "id": 1, "username": "alice" },
  "image_url": "https://...",
  "comments_count": 3,
  "likes_count": 15,
  "is_liked": true,
  "created_at": "2024-01-20T10:00:00"
}
```

### Comment
```json
{
  "id": 1,
  "post_id": 1,
  "author": { "id": 2, "username": "bob" },
  "content": "Great post!",
  "created_at": "2024-01-20T14:00:00"
}
```

### Notification
```json
{
  "id": 1,
  "notification_type": "like|comment|follow",
  "related_user": { "id": 2, "username": "bob" },
  "message": "liked your post",
  "is_read": false,
  "created_at": "2024-01-20T14:30:00"
}
```

---

## 🧪 Testing with cURL

```bash
# Register
curl -X POST http://localhost:8000/api/v1/auth/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@test.com","password":"pass123"}'

# Login
curl -X POST http://localhost:8000/api/v1/auth/auth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=alice&password=pass123"

# Create Post (replace TOKEN with actual token)
curl -X POST http://localhost:8000/api/v1/posts \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"content":"Hello World"}'

# Get Feed
curl -X GET http://localhost:8000/api/v1/feed \
  -H "Authorization: Bearer TOKEN"
```

---

For interactive testing, visit: **http://localhost:8000/docs**
