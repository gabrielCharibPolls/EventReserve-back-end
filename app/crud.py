
from sqlalchemy.orm import Session
from app.models.models import Client, Reservation
from app.schemas.schemas import ClientCreate, ReservationCreate
import datetime



# ------------------------
# CRUD Clients
# ------------------------

def create_client(db: Session, client: ClientCreate):
    db_client = Client(
        nom=client.nom,
        prenom=client.prenom,
        mail=client.mail,
        adresse=client.adresse,
        numero=client.numero
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client:
        db.delete(db_client)
        db.commit()
    return db_client

def update_client(db: Session, client_id: int, client_data: ClientCreate):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client:
        db_client.nom = client_data.nom
        db_client.prenom = client_data.prenom
        db_client.mail = client_data.mail
        db_client.adresse = client_data.adresse
        db_client.numero = client_data.numero
        db.commit()
        db.refresh(db_client)
    return db_client

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def get_clients(db: Session):
    return db.query(Client).offset(0).all()

# ------------------------
# CRUD Reservations
# ------------------------

def create_reservation(db: Session, reservation: ReservationCreate,id_client: int):
    db_reservation = Reservation(
        id_client=id_client,
        nom_reservation=reservation.nom_reservation,
        date_debut=reservation.date_debut,
        date_fin=reservation.date_fin,
        prix=reservation.prix
    )

    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation