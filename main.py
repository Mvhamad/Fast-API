from fastapi import FastAPI
from src.API.books import bookRoutes
from db import create_table

# Créer l'application FastAPI
app = FastAPI(
    title="Books API",
    description="API pour gérer une collection de livres",
    version="1.0.0"
)

# Créer les tables au démarrage
create_table()

# Inclure les routes des livres
app.include_router(bookRoutes.router)

# Route de base optionnelle
@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API Books!"}