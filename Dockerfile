FROM python:3.11-slim

RUN mkdir code
WORKDIR code

ADD . /code/

RUN pip install Flask
RUN pip install pandas
RUN pip install flask-restful

CMD python main.py
