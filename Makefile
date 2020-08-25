setup:
	python3 -m venv ~/.TimeTracker

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb

lint:
	#hadolint Dockerfile 
	pylint --disable=C0301 main.py

all: install lint test
