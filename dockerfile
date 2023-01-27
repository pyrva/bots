# using ubuntu LTS version
FROM python:3.11-slim AS builder-image

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

# install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements-prod.txt

RUN useradd --create-home myuser

USER myuser
RUN mkdir /home/myuser/code
WORKDIR /home/myuser/code
COPY ./src .

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
