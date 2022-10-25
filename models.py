from sqlalchemy import Column, Integer, String, Table, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/juvelyrikos_gamyba.db')
Base = declarative_base()


uzsakymo_gaminiai = Table('uzsakymo_gaminiai', Base.metadata,
    Column('uzsakymo_id', Integer, ForeignKey("uzsakymas.id")),
    Column('gaminio_id', Integer, ForeignKey("gaminys.id"))
)


class Uzsakymas(Base):
    __tablename__ = "uzsakymas"
    id = Column(Integer, primary_key=True)
    uzsakovas_id = Column(Integer, ForeignKey("uzsakovas.id"))
    uzsakovas = relationship("Uzsakovas", back_populates="uzsakymai")
    uzsakymo_data = Column(String)
    atidavimo_uzsakovui_data = Column(String)
    atsakingas_darbuotojas_id = Column(Integer, ForeignKey("darbuotojas.id"))
    atsakingas_darbuotojas = relationship("Darbuotojas", back_populates="uzsakymai")
    statusas_id = Column(Integer, ForeignKey("statusas.id"))
    statusas = relationship("Statusas")
    modifikacijos = Column(String, nullable=True)
    gaminiai = relationship("Gaminys", secondary=uzsakymo_gaminiai, back_populates="uzsakymai")

    def __repr__(self):
        return f"({self.id}, {self.uzsakovas},{self.uzsakymo_data}, {self.atidavimo_uzsakovui_data}, {self.atsakingas_darbuotojas}, {self.statusas}, {self.modifikacijos})"


class Statusas(Base):
    __tablename__ = "statusas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)

    def __repr__(self):
        return f"({self.id}, {self.pavadinimas})"


class Darbuotojas(Base):
    __tablename__ = "darbuotojas"
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    asmens_kodas = Column(Integer)
    pareigos = Column(String)
    telefono_numeris = Column(Integer)
    uzsakymai = relationship("Uzsakymas", back_populates="atsakingas_darbuotojas")
    
    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.asmens_kodas}, {self.pareigos}, {self.telefono_numeris})"


class Uzsakovas(Base):
    __tablename__ = "uzsakovas"
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    gimimo_data = Column(String)
    adresas = Column(String)
    telefono_numeris = Column(Integer)
    el_pastas = Column(String)
    uzsakymai = relationship("Uzsakymas", back_populates="uzsakovas")
    
    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.gimimo_data}, {self.adresas}, {self.telefono_numeris}, {self.el_pastas})"


class Gaminys(Base):
    __tablename__ = "gaminys"
    id = Column(Integer, primary_key=True)
    modelis = Column(String)
    tipas_id = Column(Integer, ForeignKey("gaminio_tipas.id"))
    tipas = relationship("GaminioTipas")
    kategorija_id = Column(Integer, ForeignKey("gaminio_kategorija.id"))
    kategorija = relationship("GaminioKategorija")
    uzsakymai = relationship("Uzsakymas", secondary=uzsakymo_gaminiai, back_populates="gaminiai")


    def __repr__(self):
        return f"({self.id}, {self.modelis}, {self.tipas}, {self.kategorija})"


class GaminioTipas(Base):
    __tablename__ = "gaminio_tipas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)
    
    def __repr__(self):
        return f"({self.id}, {self.pavadinimas})"


class GaminioKategorija(Base):
    __tablename__ = "gaminio_kategorija"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)
    
    def __repr__(self):
        return f"({self.id}, {self.pavadinimas})"


if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)