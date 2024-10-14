FROM python:3.11.2

WORKDIR /app
COPY . /app/

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["gunicorn", "-b", "0.0.0.0:8000", "page_analyzer.app:app", "--reload"]