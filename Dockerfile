# Pythonの公式イメージをベースにする
FROM python:3.12

# 環境変数の設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Poetry専用の環境変数を設定
ENV POETRY_VERSION 1.8.2
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VENV="/opt/poetry-venv"
ENV PATH="$POETRY_HOME/bin:$POETRY_VENV/bin:$PATH"

# Poetryをインストール
RUN curl -sSL https://install.python-poetry.org | python -

# prepare app root directory
ENV ROOT_PATH /app
RUN mkdir ${ROOT_PATH}
WORKDIR ${ROOT_PATH}

# transfer local django dev env
# COPY . ${ROOT_PATH}
COPY ./poetry.lock ${ROOT_PATH}
COPY ./pyproject.toml ${ROOT_PATH}

# install common library for Django application
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

