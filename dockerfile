#Base image
FROM python:3.9

#working directory
WORKDIR app/

#copy code from system
COPY app.py .

#install python library
RUN pip install Flask

#Run application

CMD ["python","app.py"]
