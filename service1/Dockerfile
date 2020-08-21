FROM python:3.6.12-alpine
EXPOSE 5000
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3" ,"app.py"]