from django.db import models

# Create your models here.

class Infonabo(models.Model):
    usuario=models.CharField(max_length=60)     #Nombre de usuario en página.
    precio=models.IntegerField()                #Precio al que están sus nabos.
    entrada=models.CharField(max_length=100)    #Coste de entrada a su isla.
    contacto=models.CharField(max_length=60)    #Forma de contacto, twitter, discord o similar...
    time=models.TimeField()                     #Hora española a la que se destruirá esta entrada.
    
    def __str__(self):
        return self.usuario

