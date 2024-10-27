# blog

The simple CRUD for blog.

## Stack

- **freamwork**: FastAPI
- **migrations**: Alembic
- **ORM**: Sqlalchemy
- **Dependencies manager**: Poetry
- **Automation**: Docker, Makefile

### How to set up?
1) Change .env.example to .env
2) First method is `make up`
3) Second method is `docker-compose up`

### What this app do?

- Simple CRUD operation on posts in blog.

### Why I create pkg.common?

This is my base structure for all projects. 
List of abstraction, for writing like SOLID.

### Why I don't create prod.yml and tests?

This is simple project and I don't want waste more time.
