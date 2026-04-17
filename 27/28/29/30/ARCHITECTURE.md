# Architecture & Flow Diagrams

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Client Browser                            │
│               http://localhost:3000                          │
└─────────────────────────────────────────────────────────────┘
                           ↕
                    (HTTP/HTTPS)
                           ↕
┌─────────────────────────────────────────────────────────────┐
│              React Frontend (Vite SPA)                       │
│                                                              │
│  ┌────────────────┐  ┌─────────────┐  ┌──────────────┐    │
│  │  Login Page    │  │ Register    │  │  Home/Feed   │    │
│  │                │  │  Page       │  │  Page        │    │
│  └────────────────┘  └─────────────┘  └──────────────┘    │
│         ↓                    ↓                 ↓             │
│  ┌────────────────────────────────────────────────────┐    │
│  │         App.tsx (Router & Layout)                  │    │
│  ├────────────────────────────────────────────────────┤    │
│  │ - Routes protection                                │    │
│  │ - Navigation                                       │    │
│  │ - Layout management                               │    │
│  └────────────────────────────────────────────────────┘    │
│         ↕                                                    │
│  ┌────────────────────────────────────────────────────┐    │
│  │    AuthContext (State Management)                  │    │
│  ├────────────────────────────────────────────────────┤    │
│  │ - User state                                       │    │
│  │ - Login/Logout logic                              │    │
│  │ - Token management                                │    │
│  └────────────────────────────────────────────────────┘    │
│         ↕                                                    │
│  ┌────────────────────────────────────────────────────┐    │
│  │    APIClient Service (api.ts)                      │    │
│  ├────────────────────────────────────────────────────┤    │
│  │ - Axios instance                                   │    │
│  │ - Token injection                                  │    │
│  │ - Error handling                                   │    │
│  │ - Request/Response interceptors                   │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                           ↕
                   (REST API with JWT)
                           ↕
┌─────────────────────────────────────────────────────────────┐
│           FastAPI Backend (uvicorn)                         │
│          http://localhost:8000                              │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │          API Router (FastAPI)                      │    │
│  │                                                    │    │
│  │  ┌──────────────┐  ┌──────────────────┐           │    │
│  │  │ /auth        │  │ /posts           │           │    │
│  │  │ - register   │  │ - GET (list)     │           │    │
│  │  │ - login      │  │ - POST (create)  │           │    │
│  │  └──────────────┘  │ - GET (single)   │           │    │
│  │                    │ - PUT (update)   │           │    │
│  │                    │ - DELETE (remove)│           │    │
│  │                    └──────────────────┘           │    │
│  └────────────────────────────────────────────────────┘    │
│                    ↕ (Depends on)                           │
│  ┌────────────────────────────────────────────────────┐    │
│  │     CRUD & Business Logic Layer                    │    │
│  │                                                    │    │
│  │  - CRUDBase (Generic operations)                   │    │
│  │  - User authentication                            │    │
│  │  - Authorization checks                           │    │
│  │  - Post logic service                             │    │
│  └────────────────────────────────────────────────────┘    │
│                    ↕ (ORM)                                  │
│  ┌────────────────────────────────────────────────────┐    │
│  │      SQLAlchemy ORM Layer                          │    │
│  │                                                    │    │
│  │  - User model                                      │    │
│  │  - Post model                                      │    │
│  │  - Comment model                                   │    │
│  │  - Like model                                      │    │
│  └────────────────────────────────────────────────────┘    │
│                    ↕ (SQL)                                  │
│  ┌────────────────────────────────────────────────────┐    │
│  │      Database Connection Pool                      │    │
│  └────────────────────────────────────────────────────┘    │
│                    ↕ (PostgreSQL wire)                      │
└─────────────────────────────────────────────────────────────┘
                           ↕
┌─────────────────────────────────────────────────────────────┐
│             PostgreSQL Database                             │
│          (Port 5433)                                        │
│                                                              │
│  Tables:                                                     │
│  - users (id, username, email, hashed_password)            │
│  - posts (id, title, content, owner_id, created_at)        │
│  - comments (id, content, post_id, user_id)                │
│  - likes (id, post_id, user_id)                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Authentication Flow

```
┌─────────────────────────────────────────────────────────┐
│ USER ACTION: Click Login Button                          │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ FRONTEND: Show Login Form                                │
│ (Login.tsx)                                              │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ USER ACTION: Enter username & password, Click Login      │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ FRONTEND: Send POST /api/v1/auth/login/access-token     │
│ Body: {username, password}                              │
│ Service: apiClient.login()                              │
└─────────────────────────────────────────────────────────┘
            ↓ (HTTP Request)
┌─────────────────────────────────────────────────────────┐
│ BACKEND: Receive login request                          │
│ Route: @router.post("/login/access-token")              │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ BACKEND: Validate Credentials                           │
│ - Query user from database by username                  │
│ - Verify password with bcrypt                           │
│ - Check if user is active                               │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ BACKEND: Create JWT Token                               │
│ - Subject: user_id                                      │
│ - Expiration: 8 days                                    │
│ - Algorithm: HS256                                      │
│ - Sign with SECRET_KEY                                  │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ BACKEND: Response to Frontend                           │
│ Status: 200                                             │
│ Body: {                                                 │
│   "access_token": "eyJhbGc...",                        │
│   "token_type": "bearer"                                │
│ }                                                       │
└─────────────────────────────────────────────────────────┘
            ↓ (HTTP Response)
┌─────────────────────────────────────────────────────────┐
│ FRONTEND: Receive token                                 │
│ - Store in localStorage                                 │
│ - Update AuthContext                                    │
│ - Set axios default headers                             │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ FRONTEND: Redirect to Home                              │
│ (User is now authenticated)                             │
└─────────────────────────────────────────────────────────┘
```

## Post Creation Flow

```
┌─────────────────────────────────────────────────────────┐
│ USER ACTION: Click "Create New Post"                    │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ FRONTEND: Show Post Creation Form                       │
│ (Home.tsx state)                                        │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ USER ACTION: Enter title & content, Click Post          │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ FRONTEND: Validate Input                                │
│ - Check title not empty                                 │
│ - Check content not empty                               │
│ - Show error if invalid                                 │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ FRONTEND: POST /api/v1/posts/                           │
│ Headers: Authorization: Bearer {token}                  │
│ Body: {                                                 │
│   "title": "My Post",                                   │
│   "content": "Lorem ipsum..."                           │
│ }                                                       │
└─────────────────────────────────────────────────────────┘
            ↓ (HTTP Request with Token)
┌─────────────────────────────────────────────────────────┐
│ BACKEND: Verify Token                                   │
│ - Extract from Authorization header                     │
│ - Decode JWT                                            │
│ - Extract user_id from subject                          │
│ - Check expiration                                      │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ BACKEND: Get Current User                               │
│ - Query user from database using user_id                │
│ - Check if user exists and is active                    │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ BACKEND: Create Post                                    │
│ - Create Post object                                    │
│ - Set owner_id from current user                        │
│ - Set created_at timestamp                              │
│ - Insert into database                                  │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ BACKEND: Response                                       │
│ Status: 200                                             │
│ Body: {                                                 │
│   "id": 1,                                              │
│   "title": "My Post",                                   │
│   "content": "Lorem ipsum...",                          │
│   "owner_id": 1,                                        │
│   "created_at": "2024-01-15T10:30..."                  │
│ }                                                       │
└─────────────────────────────────────────────────────────┘
            ↓ (HTTP Response)
┌─────────────────────────────────────────────────────────┐
│ FRONTEND: Update State                                  │
│ - Add new post to posts array                           │
│ - Clear form input                                      │
│ - Hide form                                             │
│ - Show success message                                  │
└─────────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────────┐
│ FRONTEND: Display Post in Feed                          │
│ (PostCard component renders)                            │
│ User sees their new post at top of feed                 │
└─────────────────────────────────────────────────────────┘
```

## Component Relationship

```
┌────────────────────────────────────────────────────────┐
│                      App.tsx                            │
│                   (Router + Layout)                     │
└────────────────────────────────────────────────────────┘
           ↓              ↓              ↓
    ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
    │    Navbar    │ │    Routes    │ │  AuthProvider │
    └──────────────┘ └──────────────┘ └──────────────┘
         ↓                ↓                    ↓
    Links &        ┌─────────────┐    ┌─────────────┐
    User Menu      │   Home      │    │  useAuth    │
                   │   Page      │    │   Hook      │
                   └─────────────┘    └─────────────┘
                         ↓                    ↓
                   ┌──────────────┐    Token & State
                   │PostCard List │
                   └──────────────┘
                    (renders each
                     post with UI)
```

## Data Flow: Getting Posts

```
1. User visits Home page
                ↓
2. useEffect hook triggers on mount
                ↓
3. Check if authenticated
   - If no: redirect to /login
   - If yes: continue
                ↓
4. Call fetchPosts()
   - apiClient.getPosts()
   - GET /api/v1/posts/
   - Pass token in header
                ↓
5. Backend receives request
   - Route handler: read_posts()
   - Query database
   - Return list of Post objects
                ↓
6. Frontend receives response
   - Parse JSON
   - Update state: setPosts(data)
   - Remove loading indicator
                ↓
7. React re-renders Home component
   - Map posts array
   - Render PostCard for each
   - Display in feed
                ↓
8. User sees posts in feed!
```

## File Dependency Graph

```
App.tsx
├── Router setup
├── AuthProvider wrapper
└── Routes to pages
    ├── Home.tsx (uses)
    │   ├── useAuth()
    │   ├── apiClient.getPosts()
    │   ├── apiClient.createPost()
    │   ├── apiClient.deletePost()
    │   └── PostCard component
    │       └── Takes post as prop
    ├── Login.tsx (uses)
    │   ├── useAuth()
    │   └── apiClient.login()
    ├── Register.tsx (uses)
    │   ├── useAuth()
    │   └── apiClient.register()
    └── Navbar.tsx (uses)
        └── useAuth()

AuthContext.tsx
├── Provides: useAuth hook
├── Uses: apiClient
└── Manages: token, user, isAuthenticated

api.ts (APIClient)
├── axios instance
├── Methods:
│   ├── register()
│   ├── login()
│   ├── getPosts()
│   ├── createPost()
│   ├── deletePost()
│   └── setToken()
└── Feature: Auto-inject token in headers
```

---

This architecture ensures:
✅ Clean separation of concerns
✅ Reusable components
✅ Centralized API management
✅ Proper state management
✅ Type safety with TypeScript
✅ Responsive to user actions
