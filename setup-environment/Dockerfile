# Пример простого Dockerfile для использования в качестве интерпретатора

FROM python:3.7

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

# Для использования в качестве контейнера в VS Code нужно выбрать в меню функцию "Attach to Running Container"
# Для использования в PyCharm Pro необходимо выбрать в меню Add new interpreter -> On Docker