from passlib.hash import pbkdf2_sha256

clave_en_claro = "password"

clave_hasheada = pbkdf2_sha256.hash(clave_en_claro)
print(f"> Calculo hash de {clave_en_claro} ")
print(clave_hasheada)

clave_hasheada1 = pbkdf2_sha256.hash(clave_en_claro)
print(f"> Calculo DE NUEVO hash de {clave_en_claro} ")
print(clave_hasheada1)

clave = input(">¿Clave?: ")
verifica = pbkdf2_sha256.verify(clave, clave_hasheada)
print("Resultado verificación clave: ", verifica)


# Genero 2 hash con la misma password
# cadena = "qwerty"
# print(f"Genero  hash con cadena '{cadena}'")
# print(pbkdf2_sha256.hash(cadena))
# print(f"Genero  hash con cadena '{cadena}' otra vez... ¡¡Son distintos!!")
# print(pbkdf2_sha256.hash(cadena))


# """ Script ejercicio 03 hashing """

# clave = input("Teclee su clave: ")
# clave_hash = pbkdf2_sha256.hash(clave)
# print("Hash de ", clave, clave_hash)

# adivina = input("Adivine la clave: ")
# res = pbkdf2_sha256.verify(adivina, clave_hash)
# if res:
#     print("ok")
# else:
#     print("No es ...")

# print("imprimo hash de qwerty calculado dos veces consecutivas")
# print(pbkdf2_sha256.hash(clave, rounds=10000))
