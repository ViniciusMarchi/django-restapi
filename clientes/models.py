from django.db import models

ESTADOS = ( 
	('AC', 'Acre'), 
    ('AL', 'Alagoas'), 
    ('AP', 'Amapá'), 
	('AM', 'Amazonas'), 
    ('BA', 'Bahia'),
    ('CE', 'Ceará'), 
	('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'), 
	('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'), 
	('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'), 
	('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'), 
	('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
	('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), 
	('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'), 
	('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)

class Endereco(models.Model):
    estado = models.CharField('Estado', max_length=2, choices=ESTADOS, blank=False)
    cidade = models.CharField('Cidade', max_length=40, blank=False)
    bairro = models.CharField('Bairro', max_length=100, blank=False)
    numero = models.IntegerField('Numero', blank=False)
    cep    = models.CharField('Cep', max_length=60, blank=False)
 
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        db_table = "endereco"

    def __str__(self):
        return str(self.cidade + ' - ' + self.bairro)

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False)
    sobrenome = models.CharField('Sobrenome', max_length=100, blank=False)
    data_nasc = models.DateField('Nascimento', null=False, blank=False)
    cpf = models.CharField('CPF', max_length=11, blank=False)
    rg = models.CharField('RG', max_length=9, blank=False)
    telefone = models.CharField('Telefone', max_length=100, blank=False)
    email = models.EmailField('Email', max_length=100)
    endereco = models.ForeignKey(Endereco, default='1', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = "cliente"

    def __str__(self):
        return str(self.nome + ' ' + self.sobrenome)


