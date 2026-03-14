import re

def validar_rfc(rfc: str) -> bool:
    patron = r'^[A-ZÑ&]{4}\d{6}[A-Z0-9]{3}$'
    return bool(re.match(patron, rfc.upper()))

def validar_email(email: str) -> bool:
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, email))
