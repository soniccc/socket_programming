FROM python:alpine3.7
LABEL author="B Chahal"
LABEL description="Server using python sockets"
RUN mkdir /usr/src/python
WORKDIR /usr/src/python
COPY server.py /usr/src/python
EXPOSE 12345
CMD python server.py
