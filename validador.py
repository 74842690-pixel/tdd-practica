
def validar_password(password):
    errores = []

    if len(password) < 8:
        errores.append("Mínimo 8 caracteres")

    if not any(c.isupper() for c in password):
        errores.append("Al menos una mayúscula")

    if not any(c.islower() for c in password):
        errores.append("Al menos una minúscula")

    if not any(c.isdigit() for c in password):
        errores.append("Al menos un dígito")

    especiales = "!@#$%^&*"

    if not any(c in especiales for c in password):
        errores.append("Al menos un carácter especial")

    return {
        "valida": len(errores) == 0,
        "errores": errores
    }
