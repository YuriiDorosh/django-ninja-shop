DC = docker compose
STORAGES_FILE = docker_compose/storages.yaml
EXEC = docker exec -it
DB_CONTAINER = example-db
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app
MANAGE_PY = python manage.py

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} down

.PHONY: postgres
postgres:
	${EXEC} ${DB_CONTAINER} psql

.PHONY: storages-logs
storages-logs:
	${LOGS} ${DB_CONTAINER} -f

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${env} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: db-logs
db-logs:
	${DC} -f ${STORAGES_FILE} logs -f


.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} down

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} migrate

.PHONY: migrations
migrations:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} makemigrations

.PHONY: superuser
superuser:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} createsuperuser

.PHONY: collectstatic
collectstatic:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} collectstatic


.PHONY: run-test
run-test:
	${EXEC} ${APP_CONTAINER} pytest

.PHONY: install-deps
install-deps:
	${EXEC} ${APP_CONTAINER} poetry install

.PHONY: add-dep
add-dep:
	${EXEC} ${APP_CONTAINER} poetry add twilio

.PHONY: remove-dep
remove-dep:
	${EXEC} ${APP_CONTAINER} poetry remove ${DEP}

.PHONY: update-deps
update-deps:
	${EXEC} ${APP_CONTAINER} poetry update

.PHONY: lock-deps
lock-deps:
	${EXEC} ${APP_CONTAINER} poetry lock

.PHONY: export-requirements
export-requirements:
	${EXEC} ${APP_CONTAINER} poetry export -f requirements.txt --output requirements.txt --without-hashes