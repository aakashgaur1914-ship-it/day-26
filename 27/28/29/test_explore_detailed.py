import httpx
import json

client = httpx.Client(follow_redirects=False)

# Login as admin
login_resp = client.post('http://localhost:8000/api/v1/auth/login/access-token', 
                         data={'username': 'admin', 'password': 'password123'})
token = login_resp.json()['access_token']
print(f"Logged in as admin, token length: {len(token)}")

# Get explore posts directly
explore_resp = client.get('http://localhost:8000/api/v1/feed/explore',
                          headers={'Authorization': f'Bearer {token}'})
print(f'\nExplore Status: {explore_resp.status_code}')
print(f'Explore Content-Type: {explore_resp.headers.get("content-type")}')

if explore_resp.status_code == 200:
    try:
        explore_posts = explore_resp.json()
        print(f'Explore Posts: {len(explore_posts)}')
        if explore_posts:
            print(f'\nFirst post structure:')
            print(json.dumps(explore_posts[0], indent=2, default=str))
        else:
            print("No posts returned")
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        print(f"Response text: {explore_resp.text[:500]}")
elif explore_resp.status_code in [301, 302, 307]:
    print(f"Redirect to: {explore_resp.headers.get('location')}")
