FROM python:latest
MAINTAINER khw7385 "khw73850@gmail.com"
COPY webclient.py /app/
RUN apt-get update \
	&& apt-get install -y python3-pip \
	&& pip install requests

CMD ["python3", "/app/webclient.py"]
