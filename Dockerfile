FROM python:3.11-slim
FROM ubuntu:14.04

RUN pip install Flask
RUN pip install pandas

CMD python main.py
