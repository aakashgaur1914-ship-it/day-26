#!/usr/bin/env python
"""Create database tables directly using SQLAlchemy"""

from app.db.database import engine
from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment
from app.models.like import Like
from app.models.notification import Notification
from app.models.image import Image, ImageLike
from app.db.database import Base

print("Creating all tables...")
Base.metadata.create_all(bind=engine)
print("✓ All tables created successfully!")
print("\nTables created:")
for table in Base.metadata.tables:
    print(f"  - {table}")
