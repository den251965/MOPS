FROM python:latest

RUN pip install --user --upgrade pip
RUN python -m pip install pymongo
RUN pip show pymongo
RUN python -m pip install pika
RUN pip show pika

ADD rule_engine.py /rule_engine/

WORKDIR /rule_engine/

CMD ["python3", "rule_engine.py"]




