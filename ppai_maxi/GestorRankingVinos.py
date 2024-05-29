from Vino import Vino
class GestorRankingVinos:
    def __init__(self):
        self.fecha_desde = None
        self.fecha_hasta = None
        self.tipo_ranking_seleccionada = None
        self.vinos_ordenados = []
        self.vinos_que_cumplen_filtros = []
        #self.vino = Vino()
    def opcion_generar_ranking_vinos(self, estado):
        if estado:
            print("Solicitar fechas")
            return True
        
    def tomarSelFechaDesdeHasta(self,fechaDesde, fechaHasta):
        self.fecha_desde = fechaDesde
        self.fecha_hasta = fechaHasta
        return True
    
    def tomarSelTipoReseña(self,tipo_reseña):
        tipo_reseña = str(tipo_reseña)
        return True
    
    def tomarSelTipoVisualizacion(self,tipo_visualizacion):
        visualizacion = str(tipo_visualizacion)
        if visualizacion == "Excel":
            self.confirmarExportacion()
        return True
    
    def confirmarExportacion(self,):
        pass
    
    def tomarConfirmacionGenRepo(self):
            return True
    
    def buscarVinosConReservasEnPeriodo(self, fechaDesde, fechaHasta):
        for vino in self.vinos:
            if self.vino.tenesReseñasDeTipoEnPeriodo(fechaDesde, fechaHasta):
                nombreVino = vino.nombre
                bodega = vino.bodega.nombre
                region, pais = vino.obtenerRegionYPais()
                varietal_descripcion = vino.varietal.descripcion
                self.vinos_que_cumplen_filtros.append({
                    "nombre_vino": nombreVino,
                    "bodega": bodega,
                    "region": region,
                    "pais": pais,
                    "varietal_descripcion": varietal_descripcion
                })
        return self.buscarVinosConReservasEnPeriodo
    
    def calcularPuntajeDeSommelierEnPeriodo():
        pass

    def finCu(self,resp):
        if resp:
            return True