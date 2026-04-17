import httpx

client = httpx.Client()

# Login as admin
login_resp = client.post('http://localhost:8000/api/v1/auth/login/access-token', 
                         data={'username': 'admin', 'password': 'password123'})
token = login_resp.json()['access_token']

# Get all posts (raw query)
all_posts_resp = client.get('http://localhost:8000/api/v1/posts',
                           headers={'Authorization': f'Bearer {token}'})
print(f'All Posts Status: {all_posts_resp.status_code}')
if all_posts_resp.status_code == 200:
    all_posts = all_posts_resp.json()
    print(f'Total Posts in DB: {len(all_posts)}')
    for post in all_posts:
        print(f'  - ID={post["id"]}, Owner={post.get("owner_id")}, Title={post["title"]}')

print()

# Get explore posts  
explore_resp = client.get('http://localhost:8000/api/v1/feed/explore',
                          headers={'Authorization': f'Bearer {token}'})
print(f'Explore Status: {explore_resp.status_code}')
if explore_resp.status_code == 200:
    explore_posts = explore_resp.json()
    print(f'Explore Posts: {len(explore_posts)}')
    for post in explore_posts:
        print(f'  - {post["title"]} by {post["author"]["username"]} (owner_id={post["owner_id"]})')
