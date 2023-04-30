FROM python:3.10

WORKDIR /b_b_copy-docker

# Copiez le fichier requirements.txt dans le répertoire courant
COPY backend/requirements.txt .

# Installez les dépendances de l'application
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copiez l'ensemble du code dans le répertoire courant
COPY . .
WORKDIR /b_b_copy-docker/backend
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]