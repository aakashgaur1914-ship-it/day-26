#!/usr/bin/env python
"""Seed test data via API"""
import httpx
import time

client = httpx.Client()

# Wait for backend to be ready
time.sleep(1)

# Register multiple users
users = [
    {'email': 'admin@example.com', 'username': 'admin', 'password': 'password123'},
    {'email': 'john@example.com', 'username': 'john_doe', 'password': 'password123'},
    {'email': 'jane@example.com', 'username': 'jane_smith', 'password': 'password123'},
]

print("Registering/Using test users...")
tokens = {}
for user_data in users:
    # Try to register
    response = client.post(
        'http://localhost:8000/api/v1/auth/register',
        json=user_data
    )
    if response.status_code == 200:
        print(f"✓ Registered {user_data['email']}")
    elif response.status_code == 400:
        print(f"✓ User {user_data['email']} already exists")
    else:
        print(f"✗ Error registering {user_data['email']}: {response.status_code}")
    
    # Always try to login
    login_data = {
        'username': user_data['username'], 
        'password': user_data['password']
    }
    login_response = client.post(
        'http://localhost:8000/api/v1/auth/login/access-token',
        data=login_data
    )
    if login_response.status_code == 200:
        tokens[user_data['username']] = login_response.json()['access_token']
        print(f"  ✓ Got access token for {user_data['username']}")
    else:
        print(f"  ✗ Failed to login {user_data['username']}: {login_response.status_code}")

print(f"\n✓ Successfully registered {len(tokens)} users")

# Create posts for users
posts = [
    {'username': 'john_doe', 'title': 'First Post', 'content': 'Just launched my new project! 🚀'},
    {'username': 'jane_smith', 'title': 'Design Tips', 'content': 'Here are my top design principles for 2026'},
    {'username': 'john_doe', 'title': 'React Best Practices', 'content': 'Let me share my favorite React patterns'},
    {'username': 'jane_smith', 'title': 'Art Showcase', 'content': 'Check out my new digital art collection!'},
]

print("\nCreating posts...")
for post_data in posts:
    username = post_data['username']
    if username in tokens:
        response = client.post(
            'http://localhost:8000/api/v1/posts/',
            json={'title': post_data['title'], 'content': post_data['content']},
            headers={'Authorization': f"Bearer {tokens[username]}"}
        )
        if response.status_code == 200:
            print(f"✓ Created post by {username}")
        else:
            print(f"✗ Failed to create post: {response.status_code} - {response.text}")

print("\n✓ Done!")
