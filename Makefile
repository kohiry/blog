MIGRATION_MSG?=new migration
START_DOCK=docker-compose
APP=app
POSTGRES=postgres

up:
	$(START_DOCK) up
upb:
	$(START_DOCK) up --build
gen_migration:
	$(START_DOCK) exec $(APP) alembic revision --autogenerate -m "$(MIGRATION_MSG)"
check_db:
	$(START_DOCK) exec $(POSTGRES) sh
