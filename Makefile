req-freeze:
	python -m pip freeze > requirements.txt

req-install:
	python -m pip -r requirements.txt