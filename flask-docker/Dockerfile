# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.7-alpine
RUN apk --no-cache add musl-dev linux-headers g++ && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=flask-docker Version=0.0.1
EXPOSE 5000

WORKDIR /app_flask
ADD . /app_flask

# Using pip:
RUN python3 -m pip install -r requirements.txt 

COPY ./entrypoint.sh /app_flask/entrypoint.sh
RUN chmod +x /app_flask/entrypoint.sh

# CMD [ "/app_flask/entrypoint.sh" ]
ENTRYPOINT ["sh", "/app_flask/entrypoint.sh"]

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "flask-docker"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m flask-docker"
