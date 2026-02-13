FROM python:3.10-slim

WORKDIR /hello
COPY simple_print.py .

CMD ["python3", "simple_print.py"]

