FROM python:3.10-slim

RUN apt-get update && apt-get install -y

WORKDIR /hello

COPY simple_print.py .

CMD ["python3", "simple_print.py"]

