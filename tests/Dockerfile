FROM python:3.9
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /tests
WORKDIR /tests
CMD ["pytest", "-v"]