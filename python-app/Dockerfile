FROM python:3.8

WORKDIR /python-app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]

# docker-compose ip --build
