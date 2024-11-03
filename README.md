# blog

The simple CRUD for blog.

## Stack

- **framework**: FastAPI, Apache Airflow
- **migrations**: Alembic
- **ORM**: Sqlalchemy
- **Dependencies manager**: Poetry, python venv
- **Automation**: Docker, Makefile, Dokploy CI/CD, but u can not see this :^)

### How to set up?
1) Change .env.example to .env
2) Add your telegram token and channel_id 
3) First method is `make up` (see more command in Makefile)
4) Second method is `docker-compose up`

### What this app do?

- Simple CRUD operation on posts in blog.
- Simple Airflow Dag in ETT style (Extract Transform Trigger)

### Why I create pkg/common?

This is my base structure for all projects. 
List of abstraction, for writing like SOLID.


