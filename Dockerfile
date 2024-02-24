FROM python:3.11-slim

RUN mkdir code
WORKDIR code

ADD . /code/

RUN pip install Flask

CMD python main.py
