from Bodega import Bodega
from Reseña import Reseña
class Vino:
    def __init__(self):
        self.annada = None
        self.fecha_actualizacion = None
        self.imagen_etiqueta = None
        self.nombre = None
        self.nota_de_cata_bodega = None
        self.precio_ars = None

    def buscar_info_bodega(self):
        pass

    def buscar_varietal(self):
        pass

    def calcular_puntaje_de_sommelier_en_periodo(self):
        pass

    def calcular_puntaje_promedio(self):
        pass

    def conocer_etiqueta(self):
        pass

    def es_de_region_vitivinicola(self):
        pass

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio_ars

    def set_imagen_etiqueta(self):
        return self.imagen_etiqueta

    def set_nota_cata(self):
        pass

    def set_precio(self):
        pass

    def sos_vino_para_actualizar(self):
        pass

    def tenes_reseñas_de_tipo_en_periodo(self, fechaDesde, fechaHasta):
        for reseña in self.reseñas:
            if fechaDesde <= reseña.fecha <= fechaHasta and reseña.sommelier_verificado:
                return True
        return False
