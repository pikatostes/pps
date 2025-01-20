import db
from models import User
from passlib.hash import pbkdf2_sha256


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)

    # Borra todas las filas de la tabla
    db.session.query(User).delete()
    db.session.commit()

    # CREATE: añadimos varios usuarios (commit tras bucle)
    dataset = [
        ('artist@local.com', 'artist', '1234', 34),
        ('boss@local.com', 'boss', '123456', 27),
        ('carpet@local.com', 'carpet', 'Dios', 21),
        ('otraana@local.com', 'ana', 'password', 56)
    ]

    # MODIFICAR: hay que almacenar el hash de data[2]
    for data in dataset:
        hash_clave = pbkdf2_sha256.hash(data[2])
        user = User(data[0], data[1], hash_clave, data[3])
        db.session.add(user)
    db.session.commit()

    # Pedir un usuario y su clave
    # usuario = input("usuario: ")
    # clave = input("clave: ")

    # # Buscar el usuario y si existe, verificar clave
    # rows = db.session.query(User).filter_by(username=usuario).all()
    # if rows:
    #     user = rows[0]
    #     print(user.password)
    #     verifica = pbkdf2_sha256.verify(clave, user.password)
    #     print("Verifica: ", verifica)

