## Imports chidoris UwUr
from fastapi import FastAPI
from routes.dni import dni

## Iniciando con el server
app = FastAPI()

app.include_router(dni)