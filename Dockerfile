FROM python:3.8

EXPOSE 5000
WORKDIR /auth-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD [ "gunicorn", "-b", "0.0.0.0:5000", "auth:create_app()" ]