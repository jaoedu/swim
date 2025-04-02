# Usa a imagem oficial do Python
FROM python

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

COPY requirements.txt /app

# Instala as dependências do projeto
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expõe a porta 8000 para o Django
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["python", "project/manage.py", "runserver", "0.0.0.0:8000"]