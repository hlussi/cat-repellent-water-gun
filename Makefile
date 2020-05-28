venv:
	python3 -m venv venv

python: venv
	. venv/bin/activate && python3

install: venv
	. venv/bin/activate && pip install --upgrade pip setuptools wheel

freeze: venv
	. venv/bin/activate	&& pip freeze > requirements.txt
clean:
	rm -rf venv build dist

PHONY: python install test freeze clean
