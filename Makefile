default: lint test

.venv: requirements.txt
	virtualenv .venv
	. .venv/bin/activate && pip install -r requirements.txt

lint: .venv
	. .venv/bin/activate && flake8 clio tests

test: .venv
	. .venv/bin/activate && python -m pytest .

login: .venv
	. .venv/bin/activate && python cli.py login

run: .venv
	. .venv/bin/activate && python cli.py run

clean:
	rm -rf .venv .pytest_cache
