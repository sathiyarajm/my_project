FROM python:3.10-slim

WORKDIR /hello
COPY hello.py .

CMD ["python3", "hello.py"]

