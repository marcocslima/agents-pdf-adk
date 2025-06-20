# Use uma imagem base Python oficial
FROM python:3.10-slim

# Define diretório de trabalho
WORKDIR /app

# Copia requirements e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código para o container
COPY . .

# Expõe a porta padrão do FastAPI/ADK Web
EXPOSE 8000

# Comando para rodar o servidor ADK Web
CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8000"]