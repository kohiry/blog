include .env
export $(shell sed -E '/^\s*#/d;/^\s*$$/d;s/=.*//' .env)

msg?=new migration
START_DOCK=docker-compose
MIG=migrations
DB=postgres
APP=api
POSTGRES=postgres

up:
	$(START_DOCK) up
upb:
	$(START_DOCK) up --build
upd:
	$(START_DOCK) down
api_shell:
	$(START_DOCK) exec $(APP) sh 
psql:
	docker-compose exec $(DB) sh -c "psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)"
gen_migration:
	$(START_DOCK) run $(MIG) sh -c "alembic revision --autogenerate -m '$(msg)'"
	$(START_DOCK) stop $(MIG)
