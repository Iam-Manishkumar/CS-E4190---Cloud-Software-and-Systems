FROM python:3.10.8-alpine3.16
WORKDIR /usr/app
COPY . /usr/app
ENV FLASK APP=app.py
ENV FLASK RUN HOST=0.0.0.0
ENV DEBIAN_FRONTEND=noninteractive
RUN apk add gcc libc-dev linux-headers zlib-dev jpeg-dev libjpeg
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt



EXPOSE 5000


CMD ["flask", "run", "--host=0.0.0.0"]