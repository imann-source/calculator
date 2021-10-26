FROM python:3
RUN apt-get update && apt-get install -y python
CMD ["python3","calculator.py","*","Running on 0.0.0.0:80"]
