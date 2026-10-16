# MINI SIMULADOR AAA
# Autenticación - Autorización - Auditoría

usuarios = {
    "admin": {
        "password": "1234",
        "rol": "Administrador",
        "mfa": "2026"
    },
    "tecnico": {
        "password": "tec123",
        "rol": "Técnico",
        "mfa": "1111"
    },
    "docente": {
        "password": "doc123",
        "rol": "Docente",
        "mfa": "2222"
    }
}

print("======================================")
print("   🔐 CENTRO DE DATOS - IESP JULI")
print("======================================")

usuario = input("Usuario: ")
password = input("Contraseña: ")

# AUTENTICACIÓN
if usuario in usuarios and usuarios[usuario]["password"] == password:

    print("\n✅ AUTENTICACIÓN CORRECTA")
    print("Identidad:", usuario)

    # MFA
    codigo = input("Ingrese código MFA: ")

    if codigo == usuarios[usuario]["mfa"]:

        print("✅ MFA CORRECTO")

        # AUTORIZACIÓN
        rol = usuarios[usuario]["rol"]
        print("Rol:", rol)

        if rol == "Administrador":
            print("🟢 Acceso permitido al servidor.")
            print("🟢 Puede configurar la red.")
            print("🟢 Puede administrar usuarios.")

        elif rol == "Técnico":
            print("🟢 Acceso permitido al mantenimiento.")
            print("🟢 Puede revisar equipos.")
            print("🔴 No puede administrar usuarios.")

        elif rol == "Docente":
            print("🟢 Acceso al sistema académico.")
            print("🔴 No puede acceder al servidor.")

        # AUDITORÍA
        print("\n📋 AUDITORÍA")
        print("Usuario:", usuario)
        print("Acción: Inicio de sesión")
        print("Estado: EXITOSO")

    else:
        print("❌ Código MFA incorrecto")
        print("📋 AUDITORÍA: intento rechazado")

else:
    print("❌ Usuario o contraseña incorrectos")
    print("📋 AUDITORÍA: intento de acceso rechazado")