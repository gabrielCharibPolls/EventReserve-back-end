from pydantic import BaseModel
from datetime import date
from typing import List, Optional
import datetime
from pydantic import BaseModel, field_validator
# from pydantic.v1 import BaseModel  # Not needed, already importing BaseModel from pydantic


class ReservationBase(BaseModel):
    nom_reservation: str
    date_debut: date
    date_fin: date
    prix: float


@field_validator('date_debut')
def start_date_not_in_past(cls, v):
    if v < datetime.date.today():
        raise ValueError('date_debut cannot be in the past')
    return v    

@field_validator('date_fin')
def end_date_after_start_date(cls, v, values):
    if 'date_debut' in values and v <= values['date_debut']:
        raise ValueError('date_fin must be after date_debut')
        print('date_fin must be after date_debut')
        logging.warning('date_fin must be after date_debut')
        Warning.warn('date_fin must be after date_debut')
    return v



class ReservationCreate(ReservationBase):
    id_client: int


class ReservationResponse(ReservationBase):
    id: int

    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    nom: str
    prenom: str
    mail: str
    adresse: Optional[str] = None
    numero: Optional[str] = None


class ClientCreate(ClientBase):
    pass


class ClientResponse(ClientBase):
    id: int
    reservations: List[ReservationResponse] = []

    class Config:
        orm_mode = True
