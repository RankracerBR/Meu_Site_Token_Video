#Define a imagem base como Python 3
FROM python:3

#Configuração para evitar o buffer
ENV PYTHONBUFFERED=1

#Define o diretório
WORKDIR /code

#Copiar as dependências
COPY requirements.txt /code/

#Instalar as dependências
RUN pip install -r requirements.txt

#Copiar todos os arquivos do diretório local para a image
COPY . /code/