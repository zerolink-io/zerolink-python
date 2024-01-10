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
	rm -rf zerolink_client
	#poetry run openapi-python-client generate --path openapi.json --meta none
	poetry run openapi-python-client generate --config api.yml --path openapi.json --meta none
	# Horible hack to fix the generated code per a bug
	# https://github.com/openapi-generators/openapi-python-client/issues/791
	#git checkout zerolink_client/models/entity.py
	# Another horrible hack to fix the generated code bug with datetimes
	git checkout zerolink_client/models/attribute.py
	git checkout zerolink_client/models/__init__.py
	git checkout zerolink_client/models/date.py
	git checkout zerolink_client/models/datetime_.py
	git checkout zerolink_client/models/dimensional_quantity.py
	git checkout zerolink_client/models/dimensionless_quantity.py
	git checkout zerolink_client/models/gps.py
	git checkout zerolink_client/models/monolingual_text.py
	git checkout zerolink_client/models/url.py
	#isort -q zerolink_client
