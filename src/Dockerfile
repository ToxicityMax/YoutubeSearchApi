FROM python:3.10.1-alpine

RUN mkdir /backend
WORKDIR /backend

# Set Environment variables
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev postgresql-client

COPY ./requirements.txt .
RUN python -m pip install wheel && python -m pip install --upgrade pip && python -m pip install -r requirements.txt --no-cache-dir


COPY ./entrypoint.sh /backend/entrypoint.sh
RUN chmod +x /backend/entrypoint.sh

# Copy project
COPY . /backend

ENTRYPOINT ["/backend/entrypoint.sh"]