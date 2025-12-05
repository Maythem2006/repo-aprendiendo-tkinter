def validar_numero(valor):
    try:
        return float(valor)
    except:
        raise ValueError("El valor ingresado debe ser numérico.")

def validar_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("El correo no es válido.")
    return email

def validar_texto(texto):
    if len(texto.strip()) == 0:
        raise ValueError("El texto no puede estar vacío.")
    return texto