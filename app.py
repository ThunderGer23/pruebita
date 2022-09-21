## Imports chidoris UwUr
from fastapi import FastAPI
from routes.dni import dni
from routes.bdd import bdd

## Iniciando con el server
app = FastAPI()

app.include_router(dni)
app.include_router(bdd)