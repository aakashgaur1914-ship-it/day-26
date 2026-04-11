# Social Media Platform Backend

A production-ready, scalable backend for a social media application built with FastAPI, PostgreSQL, Redis, and Celery.

##  Features

- **User System**: Auth (JWT), Profile management, Search.
- **Social Graph**: Follow/unfollow mechanism.
- **Content**: Multi-media posts, Likes, and Comments.
- **Feed**: Personalized feed generation logic.
- **Asynchronous**: Background processing for images and notifications.
- **Containerized**: Fully Dockerized environment for development and production.

##  Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [PostgreSQL](https://www.postgresql.org/)
- **ORM**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/)
- **Caching/Broker**: [Redis](https://redis.io/)
- **Task Queue**: [Celery](https://docs.celeryq.dev/)
- **Documentation**: [Swagger UI](https://github.com/swagger-api/swagger-ui)

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.11+ (for local development)

##  Setup Guide

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-org/social-media-backend.git
    cd social-media-backend
    ```

2.  **Environment Variables**:
    Copy the example environment file and update the values:
    ```bash
    cp .env.example .env
    ```

3.  **Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```
    This will start the API, Database, Redis, and Celery Worker.

4.  **Access the API**:
    - API: `http://localhost:8000`
    - Documentation (Swagger): `http://localhost:8000/docs`
    - Alternative Docs (ReDoc): `http://localhost:8000/redoc`

##  Testing

Run the test suite using `pytest`:
```bash
docker-compose run api pytest
```

##  Project Structure

```text
├── app/
│   ├── api/          # Endpoint routers and logic
│   ├── core/         # Global config, security, celery setup
│   ├── crud/         # Database abstraction layer
│   ├── models/       # Database schemas (SQLAlchemy)
│   ├── schemas/      # API validation models (Pydantic)
│   ├── db/           # Session and migration management
│   └── main.py       # FastAPI entry point
├── tests/            # Automated test suite
├── Dockerfile        # Backend container definition
├── docker-compose.yml # Service orchestration
└── requirements.txt  # Python dependencies
```

##  Contributing

Please refer to the [Team Roles Document](file:///C:/Users/aakas/.gemini/antigravity/brain/f0485225-778f-4887-9078-efd511e952e3/team_roles.md) for individual responsibilities.
