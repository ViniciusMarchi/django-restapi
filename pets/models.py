from django.db import models
from polymorphic import models as polymodels
from clientes.models import Cliente

# https://medium.com/@lokeshsharma596/model-inheritance-styles-in-django-698296f5de06

# Modelos dos animais ue serão consultados

# ----------------------- modelos --------------------------------
class Animal(polymodels.PolymorphicModel):
    nome = models.CharField(max_length=100, blank=False)
    raca = models.CharField(max_length=40, blank=False)
    data_nasc = models.DateField(blank=False)
    dono = models.ForeignKey(Cliente, default='1', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        db_table = "animal"


    def __str__(self):
        return str(self.nome)

class Cachorro(Animal):
    cor_pelo = models.CharField(max_length=80, blank=False)

    class Meta:
        db_table = "cachorro"

    def __str__(self):
        return str('Cachorro: ' + self.nome)

class Gato(Animal):
    cor_pelo = models.CharField(max_length=80, blank=False)

    class Meta:
        db_table = "gato"

    def __str__(self):
        return str('Gato: ' + self.nome)

class Passaro(Animal):
    cor_pena = models.CharField(max_length=80, blank=False)
    licensa_ambiental = models.CharField(max_length=200)

    class Meta:
        db_table = "passaro"

    def __str__(self):
        return str('Passaro: ' + self.nome)