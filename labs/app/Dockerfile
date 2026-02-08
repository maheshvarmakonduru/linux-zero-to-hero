FROM python:3.10-slim

WORKDIR /usr/src/app

COPY app.py ./
RUN pip install --no-cache-dir flask

RUN mkdir -p /var/log/myapp
VOLUME ["/var/log/myapp"]

EXPOSE 5000
CMD ["python","app.py"]
