FROM python:3.7.9
EXPOSE 5001
COPY . .
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:5001", "app:app"]