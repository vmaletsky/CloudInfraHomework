FROM python:alpine3.7
COPY . /app
WORKDIR /app
EXPOSE 81
CMD python ./main.py