FROM python:3.7.9
EXPOSE 5003
COPY . .
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:5003", "app:app"]