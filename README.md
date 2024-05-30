# PPAI DSI 3k4 -Grupo3

<h2> Grupo N° 3 - Integrantes: </h2>

- `Dario Lopez`
- ` `
- ` `
- ` `
- ` `
- ` `
- ` `

<h2>Descripcion del CU 24 Generar ranking de vinos</h2>
<img alt="CU 24 Generar ranking de vinos" src="https://github.com/d4riolopez/grupo3PPAI3k4/blob/dario/CU24%20Generar%20ranking%20de%20vinos.png" title="CU 24 Generar ranking de vinos"/>

<h2>Diagrama de Secuencia de la realizacion del CU 24 Generar ranking de vinos</h2>
<img alt="Diagrama de Secuencia de la realizacion del CU 24" src="" title="Diagrama de Secuencia de la realizacion del CU 24"/>

<h2>Diagrama de Clases de Analisis UML</h2>
<img alt="Diagrama de Clases de Analisis" src="" title="Diagrama de Clases de Analisis"/>


<h2>Ubicacion del proyecto</h2>
- git clone https://github.com/d4riolopez/grupo3PPAI3k4


# <H3>Trabajo Práctico Integrador: </H3>

## Funcionamiento de Negocio:

### Descripción

Descripción del Funcionamiento de Negocio:
Un grupo de profesionales apasionados por el mundo del vino deciden crear una aplicación para compartir experiencias entre los enófilos. Decidieron nombrar a esta aplicación BonVino y permitirá a los enófilos que utilicen la aplicación explorar, calificar y revisar vinos, así como recibir recomendaciones personalizadas.
Esta aplicación mobile tendrá por objetivo formar comunidad entre los amantes del vino orientándose en dos tipos de usuarios, los enófilos y los dueños de bodegas y/o productores. La idea principal de la aplicación es que los enófilos puedan compartir sus reseñas a través del escaneo de la etiqueta del vino que están probando en tiempo real.

Catálogo de vinos
BonVino obtiene información detallada de los vinos de varias fuentes, combinando datos proporcionados por los usuarios, colaboradores de la industria del vino y fuentes públicas.
La app brindará un perfil especial para bodegas y productores de vino que podrán cargar información sobre sus productos manualmente o conectar sus sitios web a través de una API que permita mantener la información de los vinos actualizada de manera automática. Para cada vino se podrá registrar: nombre, varietal/les, añada, imagen calidad 4k de la etiqueta, precio en ARS, bodega, región vinícola, provincia, país, nota de cata de la bodega origen y maridajes sugeridos.

Evaluaciones de Críticos Profesionales
BonVino permitirá crear perfiles para sommelier reconocidos que luego de un proceso de validación de identidad que realizan los administradores del sistema (App), podrán realizar puntuaciones y reseñas lo que brinda a los consumidores una perspectiva más amplia sobre la calidad y el perfil de un vino. Este tipo de reseñas de vino serán destacadas como premium dentro del listado de reseñas para cada vino. Los sommeliers podrán incluir en su perfil información detallada de cursos realizados y premios obtenidos para respaldar su conocimiento y experiencia.

Exploración y Búsqueda de Vinos
La aplicación permitirá buscar vinos utilizando diferentes criterios, como el nombre del vino, la bodega a la que pertenece, la región vinícola o el tipo de uva. Una de las características distintivas de la aplicación BonVino es que deberá tener la capacidad de escanear etiquetas de vinos con la cámara del teléfono y comparar contra su base de datos para encontrar el vino escaneado proporcionando información instantánea o indicar que no se obtuvo coincidencia.

Calificaciones y Reseñas
En BonVino, los propios usuarios enófilos también podrán registrar un vino en la aplicación, en caso de que el escaneo no resulte en coincidencia. Una vez que un enófilo se ha registrado como usuario, podrá registrar un vino o si encuentra el deseado, podrá calificarlo (puntuación de 1 a 5 estrellas), dejar una reseña detallada
y seleccionar los sabores que percibe al probar el vino. Cada enófilo podrá mantener una colección de vinos favoritos, así como la colección de vinos escaneados. Se debe permitir compartir reseñas con otros usuarios de la aplicación.
Una vez por mes la aplicación enviará a cada enófilo un resumen de las reseñas realizadas por él y de las etiquetas escaneadas. La aplicación contará con una sección de vinos mejor rankeados organizados por una característica según región, varietal, precio, etc.

Exploración de Bodegas y Regiones
La aplicación además permitirá explorar diferentes bodegas y regiones vinícolas, aprender sobre su historia y descubrir los vinos que producen, esta información será registrada por los administradores del sistema utilizando un sitio web.
La aplicación permitirá que los consumidores se suscriban a las novedades de las bodegas para enterarse de nuevos lanzamientos de vinos a través de notificaciones dentro de la aplicación.
Las bodegas y vinotecas también pueden publicar cupones de descuento para compra de vinos o información de eventos como catas o degustaciones a través de la aplicación que solo podrán ser accedidas por usuarios premium.

Cuenta Premium
Los enófilos que lo deseen podrán contratar una cuenta premium que por un costo fijo mensual o anual permitirá acceder a otras funciones de la aplicación como códigos de descuento y prioridad para acceder a catas de bodegas o vinotecas registradas en la app. El sistema permitirá pagar la opción premium utilizando Mercado Pago.

Comunidad y Redes Sociales
BonVino también tendrá una comunidad activa de enófilos (amantes del vino). Allí se podrá seguir a otros enófilos, ver sus calificaciones y reseñas dentro de la aplicación, y compartir experiencias propias con ellos.
La App Bonvino deberá integrarse con Meta para permitir compartir por Instagram y/o WhatsApp las reseñas cargadas.

### Entregas

#### Entrega 1
Entrega 1
Análisis del Sistema
Realización del caso de uso de análisis
Referencia para el modelado, las clases del Modelo de Dominio entregado por la Cátedra y la solución desarrollada en clase.

1. Vista de clases de análisis
Construido con un diagrama de clases.
La vista incluye clases de análisis necesarias para el modelado del escenario del caso de uso asignado.
2. Vista de interacción
Modelar el escenario descripto en el caso de uso, utilizando un diagrama de secuencia. Considerar la aplicación de los patrones GRASP de análisis.

## Consideraciones
Consideraciones
Implementación de la realización del caso de uso de análisis
Implementación caso de uso modelado, 24 Generar ranking de vinos.
Describir los detalles de la implementación mencionados a continuación:
- Lenguaje de programación utilizado Python
- Framework de programación utilizado
- Tecnología Escritorio
- Implementación de los siguientes aspectos arquitectónicos:
o La conexión con la API emulado con un atributo string del gestor
o El esquema de persistencia no considerado
o Las notificaciones push no considerado
o La exportación a un archivo o Excel solo lo mostramos por pantalla. 
   
#### Entrega 2

   
   
