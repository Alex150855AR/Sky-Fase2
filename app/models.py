from pydantic import BaseModel, field_validator
from app.validators import validar_rfc, validar_email

class ClienteCreate(BaseModel):
    nombre: str
    email: str
    rfc: str
    telefono: str

    @field_validator('rfc')
    def check_rfc(cls, v):
        if not validar_rfc(v):
            raise ValueError('El formato del RFC es inválido')
        return v.upper()

    @field_validator('email')
    def check_email(cls, v):
        if not validar_email(v):
            raise ValueError('El formato del email es inválido')
        return v

class Cliente(ClienteCreate):
    id: str
