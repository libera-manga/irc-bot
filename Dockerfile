FROM ubuntu:latest

WORKDIR $PWD/home/app
RUN apt-get update --fix-missing && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get install -y python3-pip python-dev build-essential curl openssl


RUN python3.8 -m pip install -U pip

RUN pip3 install pipenv 

# TODO: Convert to multistage build in future using scratch or something

COPY Pipfile*  /tmp/

COPY ingest.py /home/app
RUN pip3 install -i https://test.pypi.org/simple psycopg2-binary==2.9.0.dev0

RUN cd /tmp && pipenv lock --requirements > /tmp/requirements.txt
RUN python3.8 -m pip install -r /tmp/requirements.txt --user
RUN pip3 install fastapi-users[mongodb] #Can potentially move to Pipfile

CMD ["python3.8","ingest.py"]