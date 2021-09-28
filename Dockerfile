FROM python:3.6
COPY .  /flask-graphql-api
WORKDIR /flask-graphql-api
RUN pip install -r requirements.txt
EXPOSE  8000
CMD ["python", "api/app.py"]