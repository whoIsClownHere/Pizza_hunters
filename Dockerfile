FROM python:3.11-slim

RUN pip install Flask
RUN pip install pandas

CMD python main.py
