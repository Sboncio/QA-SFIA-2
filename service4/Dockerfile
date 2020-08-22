FROM python:3.7.9
EXPOSE 5003
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]