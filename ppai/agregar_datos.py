from database_setup import Pais, Provincia, RegionVitivinicola, Bodega, Vino, Resena, Session
from datetime import datetime
import random

# Crear una sesión
session = Session()

# Agregar datos de prueba
# Crear un país
pais = Pais(nombre="Argentina")
session.add(pais)
session.commit()

# Crear una provincia
provincia = Provincia(nombre="Mendoza", pais=pais)
session.add(provincia)
session.commit()

# Crear una región vitivinícola
region = RegionVitivinicola(descripcion="Una descripción de la región", nombre="Cuyo", pais=pais)
session.add(region)
session.commit()

# Crear una bodega
bodega = Bodega(
    descripcion="Una descripción de la bodega.",
    fecha_ultima_actualizacion=datetime.now(),
    historia="Una historia interesante",
    nombre="Bodega Ejemplo",
    periodo_actualizacion="Anual",
    region=region
)
session.add(bodega)
session.commit()

# Crear vinos
for i in range(5):
    vino = Vino(
        annada=2015 + i,
        fecha_actualizacion=datetime.now(),
        imagen_etiqueta=f"imagen_{i}.jpg",
        nombre=f"Vino {i}",
        nota_de_cata_bodega=f"Notas de cata {i}",
        precio_ars=100 * (i + 1),
        bodega=bodega
    )
    session.add(vino)
    session.commit()

    # Crear reseñas
    for j in range(3):
        reseña = Resena(
            comentario=f"Comentario {j} para vino {i}",
            fecha_reseña=datetime.now(),
            puntaje=random.uniform(80, 100),
            vino=vino
        )
        session.add(reseña)
        session.commit()

# Consultar los vinos de una bodega
bodega_vinos = session.query(Vino).filter_by(bodega_id=bodega.id).all()
for vino in bodega_vinos:
    print(f"{vino.nombre}, {vino.precio_ars} ARS")

# Consultar las reseñas de un vino
for vino in bodega_vinos:
    vino_resenas = session.query(Resena).filter_by(vino_id=vino.id).all()
    print(f"Reseñas para {vino.nombre}:")
    for resena in vino_resenas:
        print(f" - {resena.comentario}, Puntaje: {resena.puntaje}")

session.close()