import tkinter as tk
from tkinter import PhotoImage, messagebox
from tkcalendar import Calendar  # Librería externa para el calendario
from GestorRankingVinos import GestorRankingVinos
from datetime import datetime
from tkinter import ttk
class PantallaRankingVinos:
    def __init__(self):
        self.fechaDesdelbl = None
        self.fechaHastalbl = None
        self.fechaDesdetxt = None
        self.fechaHastatxt = None
        self.root = tk.Tk()
        self.root.title("Ranking de Vinos")
        self.root.geometry("679x544")  # Establece las dimensiones de la ventana
        self.root.resizable(False, False)  # Hace que la ventana no sea redimensionable

        # Carga la imagen de fondo
        #self.background_image = PhotoImage(file="C:/Users/maxic/Desktop/ppai/pantalla.png")
        self.background_image = PhotoImage(file="/home/dario/proyectosvisualcode/PPAIDSI3k4/grupo3PPAI3k4/ppai/pantalla.png")
        # Coloca la imagen de fondo en un label
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Creamos el botón "Generar ranking vinos"
        self.btn_generar_ranking = tk.Button(self.root, text="Generar ranking vinos", command=self.opcion_generar_ranking_vinos)
        self.btn_generar_ranking.place(relx=0.5, rely=0.5, anchor="center", y=27)

        self.gestor = GestorRankingVinos()

    def opcion_generar_ranking_vinos(self):
        respuesta = self.gestor.opcion_generar_ranking_vinos(True)
        if respuesta:
            self.btn_generar_ranking.destroy()  # Eliminamos el botón "Generar ranking vinos"
            self.mostrar_ingresar_fechas()

    def mostrar_ingresar_fechas(self):
        # Crear los atributos para las fechas
        self.fecha_desde_lbl = tk.Label(self.root, text="Fecha desde:")
        self.fecha_desde_lbl.place(relx=0.3, rely=0.25, anchor="center")  # 1 cm más abajo

        self.calendario_desde = Calendar(self.root, selectmode="day", year=2024, month=1, day=1)
        self.calendario_desde.place(relx=0.3, rely=0.50, anchor="center")  # 1 cm más abajo

        self.fecha_hasta_lbl = tk.Label(self.root, text="Fecha hasta:")
        self.fecha_hasta_lbl.place(relx=0.7, rely=0.25, anchor="center")  # 1 cm más abajo

        self.calendario_hasta = Calendar(self.root, selectmode="day", year=2024, month=1, day=1)
        self.calendario_hasta.place(relx=0.7, rely=0.50, anchor="center")  # 1 cm más abajo

        # Botón para guardar las fechas
        self.btn_guardar_fechas = tk.Button(self.root, text="Guardar", command=self.guardar_fechas)
        self.btn_guardar_fechas.place(relx=0.5, rely=0.75, anchor="center")

    def guardar_fechas(self):
        fecha_desde = self.calendario_desde.get_date()
        fecha_hasta = self.calendario_hasta.get_date()
        
        # Convertir las fechas en objetos datetime
        fecha_desde_dt = datetime.strptime(fecha_desde, "%d/%m/%y")
        fecha_hasta_dt = datetime.strptime(fecha_hasta, "%d/%m/%y")
        
        # Validar las fechas
        if fecha_desde_dt < fecha_hasta_dt:
            print("Fechas válidas. Desde:", fecha_desde, "Hasta:", fecha_hasta)
            self.fechaDesdetxt = fecha_desde
            self.fechaHastatxt = fecha_hasta
            respuesta = self.gestor.tomarSelFechaDesdeHasta(fecha_desde, fecha_hasta)
            if respuesta:
                print('gestor tiene las fechas')
                self.fecha_desde_lbl.destroy()
                self.calendario_desde.destroy()
                self.fecha_hasta_lbl.destroy()
                self.calendario_hasta.destroy()
                self.btn_guardar_fechas.destroy()
                self.tomar_tipo_reseña()
        else:
            messagebox.showerror("Error", "Por favor, ingrese fechas válidas (Fecha desde debe ser menor o igual que Fecha hasta)")
            
            

    def tomar_tipo_reseña(self):
        # Crear el título y el combobox para seleccionar el tipo de reseña
        self.tipo_reseña_lbl = tk.Label(self.root, text="Elegir tipo de Reseña:")
        self.tipo_reseña_lbl.place(relx=0.5, rely=0.55, anchor="center")

        self.tipo_reseña_cb = ttk.Combobox(self.root, values=["Normales", "amigos", "Somelier"], state="readonly")
        self.tipo_reseña_cb.place(relx=0.5, rely=0.65, anchor="center")
        self.tipo_reseña_cb.current(0)  # Establecer el valor por defecto

        # Botón para confirmar la selección de tipo de reseña
        self.btn_confirmar_tipo_reseña = tk.Button(self.root, text="Seleccionar", command=self.confirmar_tipo_reseña)
        self.btn_confirmar_tipo_reseña.place(relx=0.5, rely=0.75, anchor="center")

    def confirmar_tipo_reseña(self):
        tipo_reseña = self.tipo_reseña_cb.get()
        if tipo_reseña:
            print(f"Tipo de reseña seleccionado: {tipo_reseña}")
            # acciones con el tipo de reseña seleccionado
            respuesta = self.gestor.tomarSelTipoReseña(tipo_reseña)
            if respuesta:
                print('Tipo de reseña enviado al gestor')
                # Realizar las acciones necesarias después de enviar el tipo de reseña al gestor
                self.tipo_reseña_lbl.destroy()
                self.tipo_reseña_cb.destroy()
                self.btn_confirmar_tipo_reseña.destroy()
                self.tomarTipoVisualizacion()
        else:
            messagebox.showerror("Error", "Por favor, seleccione un tipo de reseña.")
    

    def tomarTipoVisualizacion(self):
        self.tipo_visualizacion_lbl = tk.Label(self.root, text="Elegir tipo de Visualizacion:")
        self.tipo_visualizacion_lbl.place(relx=0.5, rely=0.55, anchor="center")

        self.tipo_visualizacion_cb = ttk.Combobox(self.root, values=["Pdf", "Excel", "Pantalla"], state="readonly")
        self.tipo_visualizacion_cb.place(relx=0.5, rely=0.65, anchor="center")
        self.tipo_visualizacion_cb.current(0)

        # Botón para confirmar la selección de tipo de visualizacion
        self.btn_confirmar_tipo_visualizacion = tk.Button(self.root, text="Seleccionar", command=self.confirmar_tipo_visualizacion)
        self.btn_confirmar_tipo_visualizacion.place(relx=0.5, rely=0.75, anchor="center")
    
    
    def confirmar_tipo_visualizacion(self):
        tipo_visualizacion = self.tipo_visualizacion_cb.get()
        if tipo_visualizacion:
            print(f"Tipo de visualizacion seleccionado: {tipo_visualizacion}")
            respuesta = self.gestor.tomarSelTipoVisualizacion(tipo_visualizacion)
            if respuesta:
                print('Tipo de visualizacion enviado al gestor')
                self.tipo_visualizacion_lbl.destroy()
                self.tipo_visualizacion_cb.destroy()
                self.btn_confirmar_tipo_visualizacion.destroy()
                self.tomarConfirmacionGenRepo()
        else:
            messagebox.showerror("Error", "Por favor, seleccione un tipo de visualizacion.")
    
    def tomarConfirmacionGenRepo(self):
        self.lbl_pregunta = tk.Label(self.root, text="¿Desea confirmar el registro del reporte?")
        self.lbl_pregunta.place(relx=0.5, rely=0.55, anchor="center")
        self.lbl_preguntapositiva = tk.Button(self.root, text="Generar informe", command=lambda:self.confirmacion_generacion_informe("Si"))
        self.lbl_preguntapositiva.place(relx=0.35, rely=0.65, anchor="center", y=27)
        self.lbl_preguntanegativa = tk.Button(self.root, text="No generar informe", command=lambda:self.confirmacion_generacion_informe("No"))
        self.lbl_preguntanegativa.place(relx=0.65, rely=0.65, anchor="center", y=27)
    
    def confirmacion_generacion_informe(self,eleccion):
        print(eleccion)
        if eleccion == "Si":
            self.gestor.tomarConfirmacionGenRepo(True)
        else:
            print("Se ha cancelado el registro del reporte.")
            # Reinicia la pantalla
            self.lbl_pregunta.destroy()
            self.lbl_preguntapositiva.destroy()
            self.lbl_preguntanegativa.destroy()
            self.iniciar()
        

    
    def iniciar(self):
        self.root.mainloop()

# Creamos una instancia de la clase PantallaRankingVinos
pantalla = PantallaRankingVinos()
# Iniciamos la aplicación
pantalla.iniciar()
