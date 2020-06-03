FROM python:3.7-alpine

ADD . /app
WORKDIR /app

RUN python3 -m venv venv
ENV PATH="venv/bin:$PATH"
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD . venv/bin/activate & python3 app/main.py
