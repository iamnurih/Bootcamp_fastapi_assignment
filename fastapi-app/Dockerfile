FROM python: 3.13
WORKDIR /code
RUN pip3 install poetry
COPY poetry.lock pyproject.toml /code/
RUN poetry install --no-root --no-dev
COPY ./app /code/app
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
