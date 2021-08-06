#FROM python:3.8-slim
FROM centos/python-36-centos7

COPY . /codigo

WORKDIR /codigo

RUN pip install uvicorn
RUN pip install pandas
RUN pip install fastapi
RUN pip install sklearn

COPY ./codigo/model/Titanic.pkl /codigo/model/Titanic.pkl

CMD ["uvicorn", "codigo.main:app","--host", "0.0.0.0", "--port", "80", "--reload"]
