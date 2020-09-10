setup:
	python3 -m venv ~/.TimeTracker

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test.py
	#python -m pytest --nbval notebook.ipynb

lint:
	#hadolint Dockerfile 
	pylint --disable=C0301 main.py
	pylint test.py

all: install lint test
