FROM art.pmideep.com/dockerhub/python:3.12
COPY app.py test.py requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt 
CMD ["python", "app.py"]