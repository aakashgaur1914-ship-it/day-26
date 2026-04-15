#!/usr/bin/env python
"""Mark migrations as applied in Alembic history"""

from sqlalchemy import text
from app.db.database import engine

with engine.connect() as conn:
    # Get current Alembic version
    result = conn.execute(text("SELECT version_num FROM alembic_version ORDER BY version_num DESC LIMIT 1"))
    row = result.fetchone()
    current = row[0] if row else None
    print(f"Current Alembic revision: {current}")
    
    # Check if we're at the base migration
    if current == "2aaf0b4a80f0":
        print("Marking social features migration as applied...")
        conn.execute(text("INSERT INTO alembic_version (version_num) VALUES ('3b9d2c5e1a3f')"))
        conn.commit()
        print("✓ Migration marked as applied!")
    
    # Verify
    result = conn.execute(text("SELECT version_num FROM alembic_version ORDER BY version_num"))
    versions = [row[0] for row in result.fetchall()]
    print(f"\nAlembic history: {versions}")
