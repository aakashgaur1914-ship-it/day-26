# 🚀 GET STARTED - 3 COMMAND QUICK START

## Copy and paste these commands in order:

### Terminal 1: Database Migration
```bash
cd "c:\Users\aakas\Desktop\day 28" && alembic upgrade head
```
**Expected output**: `INFO [alembic.runtime.migration] Running upgrade...` (should complete successfully)

---

### Terminal 2: Start Backend
```bash
cd "c:\Users\aakas\Desktop\day 28" && python -m uvicorn app.main:app --reload --port 8000
```
**Expected output**:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

---

### Terminal 3: Start Frontend
```bash
cd "c:\Users\aakas\Desktop\day 28\frontend" && npm run dev
```
**Expected output**:
```
➜  Local:   http://localhost:3001/
```

---

## Then Open:
```
http://localhost:3001
```

---

## ✅ Verify Everything Works

### Register
- Exit button in top right → Register
- Create account (username, email, password)
- Click Register

### Test Follow
- Click "Explore"
- Find a post
- Click "Follow" button

### Test Like
- Click "Feed"
- Like a post by clicking ❤️

### Test Comments
- Click 💬 on a post
- Type a comment and submit

### Test Notifications
- Click 🔔 in top right
- Should see your likes/comments/follows

---

## 📚 Documentation
- **Quick Start**: Read `QUICK_START.md`
- **All Features**: Read `FEATURES.md`
- **API Reference**: Read `API_REFERENCE.md`
- **Implementation**: Read `IMPLEMENTATION_SUMMARY.md`

---

**That's it! You're ready to go. 🎉**
