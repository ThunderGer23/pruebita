from fastapi import APIRouter
from routes.apis_net_pe import ApisNetPe

dni = APIRouter()
peapi = ApisNetPe()

@dni.get('/dates')
def get_info(DNI: str):
    person = peapi.get_person(DNI)
    return person