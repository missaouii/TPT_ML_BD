FROM ubuntu:16.04
FROM python:3.8.13

USER root
USER 1001

ADD app.py /usr/local/bin/
ADD model.pkl /usr/local/bin/

USER root
RUN  apt-get update 
RUN  apt-get install -y python3-pip \ 
						unzip \
						curl \
						wget \
						libglib2.0-0 \
						libnss3 \
						libgconf-2-4 \
						python3-dev \
						libfontconfig1

RUN pip3 install fastapi uvicorn pandas scikit-learn jinja2 python-multipart

RUN cd /usr/local/bin/
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]