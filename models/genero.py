from mongoengine import Document, StringField

#crear clase que la colleccion genero en mongo
class Genero(Document):
    nombre = StringField(max_length=50, unique=True, required=True)


    def __str__(self):
        return self.nombre
    
