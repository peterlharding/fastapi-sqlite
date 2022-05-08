

SERVICE_NAME=starter

SERVICE_TEMPLATE=60-service.cf.yaml

# -----------------------------------------------------------------------------

define check_json_data
	@if [ ! -f $(1) ] ; then \
		echo "Cannot find $(!)!" \
		exit 1; \
	fi
	@echo -n -e  "\t$(1) : "
	@cat $(1) | jq empty
	@echo OK
endef

# -----------------------------------------------------------------------------

run:
	uvicorn --host 0.0.0.0 --app-dir src app.main:app

develop:
	uvicorn --host 0.0.0.0 --app-dir src app.main:app --reload

setup:
	@echo - Ignore

compile:
	@echo - Ignore

unit-test:
	@echo - Ignore

chk-data:
	src/scripts/chk_data.py

pylint:
	-(cd src; pylint app)

# ----- Docker Stuff ----------------------------------------------------------

local-build:
	docker build -t basic-auth .

local-run:
	docker run -it --rm  -p 127.0.0.1:8000:8000  basic-auth

local-run-bg:
	docker run -it --rm  -p 127.0.0.1:8000:8000  basic-auth &


local-ngrok:
	ngrok http http://localhost:8000

local-test:
	-(cd tests/examples; echo OK)




