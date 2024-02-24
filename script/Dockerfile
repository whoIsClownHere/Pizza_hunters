FROM python:3.11-slim

RUN mkdir code
WORKDIR code

ADD . /code/

RUN pip install Flask
RUN pip install pandas

CMD python main.py
