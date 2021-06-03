from django.db import models
from pets.models import Animal
from clientes.models import Cliente
from veterinarios.models import Veterinario

class Consulta(models.Model): 
    cliente = models.ForeignKey(Cliente, related_name='cliente', on_delete=models.CASCADE, editable=False) 
    animal = models.ForeignKey(Animal, related_name='animal', on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, related_name='veterinario', on_delete=models.CASCADE)
    data_consulta = models.DateTimeField(blank=False)
    
    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        db_table = "consulta"
    
    def save(self):
        if not self.id:
            self.cliente = self.animal.dono
        super(Consulta, self).save()
    
    
    def __str__(self):
        return str(self.cliente)

