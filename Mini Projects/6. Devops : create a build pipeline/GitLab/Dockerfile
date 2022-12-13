FROM python:3.10.8-alpine3.16
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /application

COPY . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload"]

