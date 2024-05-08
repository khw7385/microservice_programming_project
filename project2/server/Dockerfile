FROM python:latest
MAINTAINER khw7385 "khw73850@gmail.com"
COPY webserver.py /app/
RUN apt-get update \
	&& apt-get install -y python3-pip \
	&& pip install flask

CMD ["python3", "/app/webserver.py"]
EXPOSE 5001
