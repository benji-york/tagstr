ve:
	python -m venv ve
	ve/bin/pip install manuel

.PHONY: manuel
manuel:
	ve/bin/python tests/documentation.py
