test:
    poetry run pytest

mypy:
    poetry run mypy meeple

black:
    poetry run black .

flake:
    poetry run flake8 .
