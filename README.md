# Tabela de conteúdos
   * [Introdução](#Introdução)
      * [Tecnologias utilizadas](##Tecnologias-utilizadas)
   * [Entidades](#Entidades)
   * [Funcionalidades](#Funcionalidades)
   * [Como utilizar](#Como-utilizar)
      * [Clonando repositório](##Clonando-repositório)  


# Introdução
O sistema apresentado nesse repositório simula o ambiente de uma Clinica veterinária. Tal sistema é uma API-Rest construída em python, fazendo uso do framework Django.

## Tecnologias utilizadas
- [Djando](www.google.com.br)
- [Django Rest Framework]
- Postgresql
- Docker.


# Entidades
O diagrama Entidade-Relacional abaixo representa a estrutura, os dados (e seus relacionamentos) do projeto.
![Diagrama ER](diagrama_er.png)

# Funcionalidades
Os seguintes casos de uso foram satisfeitos por esse projeto:

| Identificador | Descrição  |
|:-------------:|-------------|
| caso_01 | O sistema deve permitir o cadastro, leitura, edição e remoção de Clientes|
| caso_02 | O sistema deve permitir o cadastro, leitura, edição e remoção de Endereços|
| caso_03 | O sistema deve permitir o cadastro, leitura, edição e remoção de Animais|
| caso_04 | O sistema deve permitir o cadastro, leitura, edição e remoção de Veterinários  |
| caso_05 | O sistema deve permitir o cadastro, leitura, edição e remoção de Consultas     |
| caso_06 | O sistema deve permitir o cadastro de superusuários (administradores)     |
| caso_07 | Os superusuários cadastrados podem realizar login e ter acesso a uma visualização privilegiada|

# Como Utilizar

## Instalando Docker
Para utilizar esse projeto é necessário possuir *Docker* e *Docker-Compose* instalados.

### Instalando Docker no Ubuntu (e distros baseadas em Debian)
Como desenvolvi a aplicação toda em um sistema Ubuntu 20.04 LTS acredito que a maneira mais simples de instalar as dependências seja através do script oficial de instalação.

1. Execute os comandos
   ```bash
   $ curl -fsSL https://get.docker.com -o get-docker.sh
   $ sudo sh get-docker.sh
   ```

<br />

2. Verifique se está corretamente instalado com o comando
   ```bash
   $  docker --version
   ```

Se problemas forem encontrados nesse formato de instalação, consulte a documentação oficial.
https://docs.docker.com/engine/install/ubuntu/

### Instalando Docker-Compose no Ubuntu (e distros baseadas em Debian)


1. Baixe o arquivo binário com o comando comandos
   ```bash
   $ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   ```

<br />

2. Conceda as permissões para que o arquivo binário baixado possa executar
   ```bash
   $  sudo chmod +x /usr/local/bin/docker-compose
   ```
Se problemas forem encontrados nesse formato de instalação, consulte a documentação oficial.
https://docs.docker.com/compose/install/

### Instalando Docker e Docker-Compose no Windows
No Windows existe a ferramenta *Docker Desktop* a qual abrange tanto *Docker* quanto *Docker-Compose*, ou seja, basta insta-la.

1. Acesse https://docs.docker.com/docker-for-windows/install/, realize o download da ferramenta, execute-a e ela instala-rá todas as dependências necessárias.

2. Com a ferramenta instalada, realize um clique duplo sobre o icone gerado e o mesmo será inicializado.

## Clonando repositório
```bash
git clone
```

## Executando
Realize o build do projeto
```bash
docker-compose build
```

Inicialize a aplicação
```bash
docker-compose up -d
```
Crie um superusuário (admin)
```bash
docker-compose exec web python manage.py createseruser
```
Acesse a aplicação através do IP localhost `127.0.0.1:8000/` ou `0.0.0.0:8000/`

Para encerrar a aplicação, utilize
```bash
docker-compose down
```