# Day 26: Performance and Scaling Laboratory

Welcome to the Performance and Scaling Laboratory. This project is a hands-on environment designed to teach you how to identify and fix common backend performance bottlenecks.

## Getting Started

### 1. Requirements
- Docker and Docker Compose
- Python 3.11+ (for local development)

### 2. Launch the Stack
```bash
docker-compose up --build
```

### 3. Seed the Database
Wait for the database to be healthy, then run:
```bash
docker-compose exec app python src/seed_data.py
```

## 🛠️ Components
- **FastAPI App**: `localhost:8000` (Docs at `/docs`)
- **Prometheus**: `localhost:9090`
- **Grafana**: `localhost:3000` (Login: `admin`/`admin`)
- **Locust (Load Testing)**: `localhost:8089`

## 📚 Learning Modules
Detailed guides are available in the `docs/` folder:

1. [Database Optimization](docs/database_optimization.md): Learn about N+1, Query Plans, and JOINs.
2. [Indexing Strategy](docs/index_strategy.md): Understand B-Tree, Composite, and GIN indexes.
3. [Caching Improvements](docs/caching_implementation.md): Patterns and implementation details.
4. [Scaling Strategy](docs/scaling_proposal.md): Vertical vs Horizontal scaling concepts.
5. [Optimization Checklist](docs/optimization_checklist.md): A handy guide for your future projects.

## Experiments to Try
1. **The N+1 Comparison**: Compare `/posts/n-plus-one` and `/posts/optimized`. Notice the `X-Process-Time` header.
2. **Indexing Power**: Compare `/users/search/unindexed` and `/users/search/optimized`.
3.  **Cache Impact**: Hit `/stats/cached` twice. The first takes ~1s, the second takes ~0.001s.
4. **Load Testing**: Open Locust, set users to 50, and watch the Prometheus metrics in Grafana.
