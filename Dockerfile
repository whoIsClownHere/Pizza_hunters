FROM python:3.11-slim
FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install Flask
RUN pip install pandas

ADD . /var/my_app
RUN pip3 install -r /var/my_app/requirements.txt
CMD ["python3", "/var/my_app/runserver.py"]
