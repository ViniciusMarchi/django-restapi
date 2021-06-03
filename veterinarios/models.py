from django.db import models

class Veterinario(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False)
    sobrenome = models.CharField('Sobrenome', max_length=100, blank=False)
    crmv = models.CharField('CRMV', max_length=20, blank=False)
    especialidade = models.CharField('Especialidade', max_length=100)
    
    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'
        db_table = "veterinario"
    
    
    def __str__(self):
        return str(self.nome + ' ' + self.sobrenome)