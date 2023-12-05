.PHONY: build upload

build:
	rm -rf dist/ build/
	poetry build -f sdist

upload:
	python -m pip install twine
	python -m twine upload dist/zerolink-*
	rm -rf dist

client:
	cp ../../Demo/openapi.json ./
	rm -rf zero_link_client
	poetry run openapi-python-client generate --path openapi.json --meta none
	# Horible hack to fix the generated code per a bug
	# https://github.com/openapi-generators/openapi-python-client/issues/791
	git checkout zero_link_client/models/entity.py
	# Another horrible hack to fix the generated code bug with datetimes
	git checkout zero_link_client/models/attribute.py
	isort -q zero_link_client
