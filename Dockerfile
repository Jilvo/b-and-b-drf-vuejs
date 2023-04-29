FROM python:3.10

WORKDIR /b_b_copy-docker

COPY requirements.txt .
RUN  pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
