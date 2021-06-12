# django-restapi-compdist

# todo
   testar se as dependencias do requirements.txt esta correta



# Tabela de conteúdos
   * [Introdução](##Introdução)
      * [Tecnologias utilizadas](###Tecnologias)
   * [Entidades](##Entidades)
   * [Funcionalidades](##Funcionalidades)
   * [Como utilizar](##Como-utilizar)
      * [Clonando repositório](###Clonando-repositório)  




## Introdução
O sistema apresentado simula nesse repositório simula o ambiente de uma Clinica veterinária. Tal sistema é uma API-Rest construída em python, fazendo uso do framework Django.

### Tecnologias


## Entidades
![Diagrama ER](diagrama_er.png)

## Funcionalidades
- [x] O sistema deve permitir o cadastro de usuários e superusuários (admintradores)
- [x] Os usuários cadastrados podem realizar login
- [x] Apenas administradores podem realizar ações
- [x] O sistema deve permitir o cadastro, leitura, edição e remoção de Clientes
- [x] O sistema permite o cadastro, leitura, edição e remoção de Animais
- [x]  O sistema permite o cadastro, leitura, edição e remoção de Veterinários
- [x] O sistema permite o cadastro, leitura, edição e remoção de Consultas


## Como Utilizar

### Clonando repositório
```bash
git clone
```

### Executando
```bash
docker-compose build
docker-compose up -d
docker-compose exec web python manage.py createseruser
```