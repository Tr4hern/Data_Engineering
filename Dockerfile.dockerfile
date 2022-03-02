FROM python:3.6

WORKDIR /usr/src/app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . .

RUN pip install -r requirements.txt

WORKDIR /usr/src/app

EXPOSE 5000

CMD ["flask", "run"]

WORKDIR /usr/src/app/work

RUN pytest ./test.py