
import db
from models import User

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)

    # Borra todas las filas de la tabla
    db.session.query(User).delete()
    db.session.commit()

    # CREATE: añadimos un usuario (No olvidar el commit)
    nuevo = User("ana@local.com", "ana", "12345678", 36)
    db.session.add(nuevo)
    print(nuevo.id)
    db.session.commit()
    print(nuevo.id)

    # CREATE: añadimos varios usuarios (commit tras bucle)
    dataset = [
        ('artist@local.com', 'artist', '1234', 34),
        ('boss@local.com', 'boss', '123456', 27),
        ('carpet@local.com', 'carpet', '123478', 21),
        ('otraana@local.com', 'ana', '87654321', 56)
    ]

    for data in dataset:
        db.session.add(User(data[0], data[1], data[2], data[3]))
    db.session.commit()

    # READ Consultas
    todos = db.session.query(User).all()
    print("Todos: \n ", todos)

    primero = db.session.query(User).first()
    print("El primero es:\n", primero)

    numUsers = db.session.query(User).count()
    print("Número  de usarios: ", numUsers)

    users = db.session.query(User).filter_by(username='ana').all()
    print("Filtra por nombre ", users)

    menores30 = db.session.query(User).filter(User.edad < 30).all()
    print("Filtra por edad menor que 30: \n", menores30)

    # UPDATE: modificamos un registro (No olvidar commit)
    user = db.session.query(User).filter_by(email='boss@local.com').one()
    user.edad += 1
    db.session.commit()
    print("Modificamos la edad de boss\n ", user)

    # DELETE : Borrar (No olvidar commit)
    print("Borramos el user con email='carpet@local.com'")
    user = db.session.query(User).filter_by(email='carpet@local.com').one()
    db.session.delete(user)
    db.session.commit()

    todos = db.session.query(User).all()
    db.session.commit()
    print("Todos: \n ", todos)

    db.session.close()
    # Borramos la tabla
    User.__table__.drop(db.engine)
