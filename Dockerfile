FROM python:3.11-slim

RUN apt-get -y install python3-pip
RUN pip install Flask
RUN pip install pandas

CMD python main.py
