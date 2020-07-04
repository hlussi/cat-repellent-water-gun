venv:
	python3 -m venv venv

python: venv
	. venv/bin/activate && python3

install: venv
	. venv/bin/activate && pip install --upgrade pip setuptools wheel
	. venv/bin/activate && pip install --requirement requirements.txt
	. venv/bin/activate && pip install --editable .
	. venv/bin/activate && python3 setup.py install

dist: install
	. venv/bin/activate && python setup.py sdist bdist_wheel

test:
	. venv/bin/activate && pytest -s --verbose tests/ --config_file=resources/config.yml

freeze: venv
	. venv/bin/activate	&& pip freeze > requirements.txt

clean:
	rm -rf venv build dist src/adn_binrepo_test/__pycache__ tests/__pycache__ .pytest_cache __pycache__

PHONY: python install test freeze clean
