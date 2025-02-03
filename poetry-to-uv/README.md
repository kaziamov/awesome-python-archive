# Инструкция по миграции проекта с Poetry на uv

### Шаг 0. Установите uv 

```bash
# For macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Проверьте, что uv установлен:

```bash
uv --version
```

### Шаг 1. Миграция файла зависимостей

```bash
uvx pdm import pyproject.toml
```

После этого шага ваш проект уже будет доступен для создания окружения через `uv sync` (если нет синтаксических ошибок в файле)

#### Пример ошибки
```bash
>> uv sync

error: Failed to parse: `pyproject.toml`
  Caused by: TOML parse error at line 69, column 8
   |
69 | name = "Project Name With Error"
   |        ^^^^^^^^^^^^^^^^^^^^^^^^^
Not a valid package or extra name: "Project Name With Error". Names must start and end with a letter or digit and may only contain -, _, ., and alphanumeric characters.
```
В этом случае нужно исправить ошибки и повторить `uv sync`, чтобы убедиться что все рабоает.


### Шаг 2. Удалите упоминания poetry из файла зависимостей

Найдите в файле `pyproject.toml` все блоки которые начинаются с `[tool.poetry` и удалите их.


### Шаг 3. Переименуйте dev зависимости

Замените эти строки:
```
[tool.pdm.dev-dependencies]
dev = [
```
На эти:
```
[tool.uv]
dev-dependencies = [
```

### Шаг 4. Удалите файл `poetry.lock` и .venv

```bash
rm poetry.lock
```

Удалите папку `.venv` если она существует в директории проекта

```bash
rm -rf .venv
```

### Шаг 5. Посмотрите в зеркало и похвалите себя

Наслаждайтесь новым пакетным менеджером
