###########
# BUILDER #
###########

# pull official base image
# FROM python:3.11.3-slim-buster AS builder error: Could not build wheels for hnswlib, which is required to install pyproject.toml-based projects
FROM python:3.11 AS builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# lint
RUN pip install --upgrade pip
RUN pip install flake8==6.0.0
COPY . /usr/src/app/
# RUN flake8 --ignore=E501,F401,W291,F841,W605,E402,E128,E122 .

# install python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


###############

# pull official base image
FROM python:3.11

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/owl
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update 
#&& apt-get install -y --no-install-recommends netcat

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint-prod.sh
#COPY ./entrypoint.prod.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

EXPOSE 5000

# run 
CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]####

# pull official base image
FROM python:3.11

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/owl
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update 
#&& apt-get install -y --no-install-recommends netcat

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint-prod.sh
#COPY ./entrypoint.prod.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

EXPOSE 5000

# run 
CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
