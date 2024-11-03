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
2) Change bot_token and chat_id
3) First method is `make up`
4) Second method is `docker-compose up`

### What this app do?

- Simple CRUD operation on posts in blog.

### Why I create pkg.common?

This is my base structure for all projects. 
List of abstraction, for writing like SOLID.