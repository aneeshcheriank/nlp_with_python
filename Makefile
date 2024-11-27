install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora

test:
	python -m pytest -vv test_*.py

format:
	black *.py
	black ./nlplogic/*.py

lint:
	pylint --disable=R,C *.py
	pylint --disable=R,C ./nlplogic/*.py

all: install lint test