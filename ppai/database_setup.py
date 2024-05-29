from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Boolean, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class Pais(Base):
    __tablename__ = 'pais'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    pais_id = Column(Integer, ForeignKey('pais.id'))
    pais = relationship("Pais", back_populates="provincias")

    def obtener_pais(self):
        return self.pais

Pais.provincias = relationship("Provincia", order_by=Provincia.id, back_populates="pais")

class RegionVitivinicola(Base):
    __tablename__ = 'region_vitivinicola'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
    nombre = Column(String, nullable=False)
    pais_id = Column(Integer, ForeignKey('pais.id'))
    pais = relationship("Pais", back_populates="regiones")

    def obtener_pais(self):
        return self.pais

Pais.regiones = relationship("RegionVitivinicola", order_by=RegionVitivinicola.id, back_populates="pais")

class Bodega(Base):
    __tablename__ = 'bodega'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String)
    fecha_ultima_actualizacion = Column(Date)
    historia = Column(String)
    nombre = Column(String, nullable=False)
    periodo_actualizacion = Column(String)
    region_id = Column(Integer, ForeignKey('region_vitivinicola.id'))
    region = relationship("RegionVitivinicola", back_populates="bodegas")

RegionVitivinicola.bodegas = relationship("Bodega", order_by=Bodega.id, back_populates="region")

class Vino(Base):
    __tablename__ = 'vino'
    id = Column(Integer, primary_key=True)
    annada = Column(Integer)
    fecha_actualizacion = Column(Date)
    imagen_etiqueta = Column(String)
    nombre = Column(String, nullable=False)
    nota_de_cata_bodega = Column(String)
    precio_ars = Column(Float)
    bodega_id = Column(Integer, ForeignKey('bodega.id'))
    bodega = relationship("Bodega", back_populates="vinos")

    resenas = relationship("Resena", back_populates="vino")

Bodega.vinos = relationship("Vino", order_by=Vino.id, back_populates="bodega")

class Resena(Base):
    __tablename__ = 'resena'
    id = Column(Integer, primary_key=True)
    comentario = Column(String)
    fecha_reseña = Column(Date, nullable=False)
    puntaje = Column(Float, nullable=False)
    vino_id = Column(Integer, ForeignKey('vino.id'))
    vino = relationship("Vino", back_populates="resenas")

Vino.resenas = relationship("Resena", order_by=Resena.id, back_populates="vino")

# Conexión a la base de datos
engine = create_engine('sqlite:///vinos.db')
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()