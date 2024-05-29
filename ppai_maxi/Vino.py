from Bodega import Bodega
from Reseña import Reseña
class Vino:
    def __init__(self,annada,fecha_actualizacion,imagen_etiqueta,nombre,nota_de_cata_bodega,precio_ars):
        self.annada = annada
        self.fecha_actualizacion = fecha_actualizacion
        self.imagen_etiqueta = imagen_etiqueta
        self.nombre = nombre
        self.nota_de_cata_bodega = nota_de_cata_bodega
        self.precio_ars = precio_ars
        self.reseña = Reseña()
        self.bodega = Bodega()

    def buscar_info_bodega(self):
        pass

    def buscar_varietal(self):
        pass

    def calcular_puntaje_de_sommelier_en_periodo(self,fecha_desde,fecha_hasta):
        pass

    def calcular_puntaje_promedio(self):
        pass

    def conocer_etiqueta(self):
        return self.imagen_etiqueta

    def es_de_region_vitivinicola(self):
        pass

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio_ars

    def set_imagen_etiqueta(self):
        pass

    def set_nota_cata(self):
        pass

    def set_precio(self):
        pass

    def sos_vino_para_actualizar(self):
        pass

    def tenes_reseñas_de_tipo_en_periodo(self, fechaDesde, fechaHasta):
        for self.reseña in self.reseñas:
            if fechaDesde <= self.reseña.fecha_reseña <= fechaHasta and self.reseña.sos_de_sommelier():
                return True
        return False
