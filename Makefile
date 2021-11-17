
# Build in venv (not Docker)
setup:
	python3 -m venv .venv

install:
	pip install -r requirements.txt

run-locally:
	python main.py

# Build in Docker
build:
	docker image build -t msds434-w9 .

run-docker:
	docker run -d -p 5000:5000 msds434-w9

lint:
	pylint --disable=R,C main.py

test: 
	pytest main_test.py