.DEFAULT_GOAL := help

.PHONY: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install i
install i: ## Install dependencies
	python3        --version
	python3 -m pip --version
	poetry         --version
	make           --version
	docker         --version
	docker-compose --version
	# entr
	poetry install
	poetry env list --full-path

.PHONY: run r
run r: ## Run main file, without live reload.
	# Makesure that the selenium RemoteWebDriver has been running on 4444 (sudo docker-compose up)
	SELENIUM_REMOTE_WEBDRIVER_URL=http://localhost:4444/wd/hub poetry run python ./seleniumdockerexample/__main__.py

.PHONY: dev d
dev d: ## Run main file with live reload.
	# Makesure that the selenium RemoteWebDriver has been running on 4444 (sudo docker-compose up)
	ls -d ./seleniumdockerexample/* | entr sh -c "date && SELENIUM_REMOTE_WEBDRIVER_URL=http://localhost:4444/wd/hub poetry run python ./seleniumdockerexample/__main__.py"
