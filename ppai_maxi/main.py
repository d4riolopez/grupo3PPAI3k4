from Vino import Vino
from Bodega import Bodega
from Pais import Pais
from RegionVitivinicola import RegionVitivinicola
# Importa otras clases según sea necesario
# Creamos instancias de países
argentina = Pais("Argentina")
francia = Pais("Francia")

# Creamos instancias de regiones vitivinícolas
mendoza = RegionVitivinicola("Mendoza", argentina)
borgoña = RegionVitivinicola("Borgoña", francia)

# Creamos instancias de bodegas
bodega_1 = Bodega("Bodega 1", mendoza)
bodega_2 = Bodega("Bodega 2", borgoña)

# Creamos instancias de vinos
vino_1 = Vino("Vino 1", "Añada 2020", bodega_1, "2023-05-10", "imagen1.jpg", "Nota de cata vino 1", 100)
vino_2 = Vino("Vino 2", "Añada 2019", bodega_2, "2023-05-11", "imagen2.jpg", "Nota de cata vino 2", 120)
# Crea instancias para los otros vinos, completando sus datos

# Ahora puedes trabajar con estas instancias de vinos como desees
