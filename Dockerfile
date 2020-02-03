FROM python:3.8-alpine

ADD github-tagger.py /opt/github-tagger.py

RUN pip install requests click

ENTRYPOINT ["/opt/github-tagger.py"]

