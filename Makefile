include .env
export $(shell sed -E '/^\s*#/d;/^\s*$$/d;s/=.*//' .env)

msg?=new migration
START_DOCK=docker-compose
APP=migrations
POSTGRES=postgres

up:
	$(START_DOCK) up
upb:
	$(START_DOCK) up --build
upd:
	$(START_DOCK) down
psql:
	docker-compose exec postgres sh -c "psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)"
gen_migration:
	$(START_DOCK) run $(APP) sh -c "alembic revision --autogenerate -m '$(msg)'"
	$(START_DOCK) stop $(APP)
