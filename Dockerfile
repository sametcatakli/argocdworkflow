FROM python:3.10-bookworm

# Définit le dossier de travail dans le conteneur
WORKDIR /app

# Copie le fichier depuis le dossier local 'app/' vers le dossier actuel '.' du conteneur (/app)
COPY app/app.py . 

# Installe Flask
RUN pip install --no-cache-dir Flask

# Commande de lancement
ENTRYPOINT [ "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80" ]