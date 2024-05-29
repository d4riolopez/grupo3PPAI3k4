class Reseña:
    def __init__(self,comentario,fecha_reseña,puntaje):
        self.comentario = comentario
        self.fecha_reseña = fecha_reseña
        self.puntaje = puntaje

    def get_puntaje(self):
        return self.puntaje

    def sos_de_periodo(self):
        pass

    def sos_de_sommelier(self):
        pass