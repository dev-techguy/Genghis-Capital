# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies files to the working directory
COPY venv .
COPY .gitignore .
COPY .gitignore .
COPY main.py .
COPY README.md .

# command to run on container start
CMD [ "python", "./main.py" ]