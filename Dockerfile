# Usa Python 3.13 slim
FROM python:3.13-slim

ENV DB_SERVER=host.docker.internal,1433
ENV DB_NAME=master
ENV DB_USER=jose
ENV DB_PASSWORD=apple951

# Instala Java (requisito de allure)
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    openjdk-17-jre \
    && rm -rf /var/lib/apt/lists/*

# Instala allure CLI
RUN curl -o allure.zip -L https://github.com/allure-framework/allure2/releases/download/2.14.0/allure-2.14.0.zip \
    && unzip allure.zip -d /opt/ \
    && mv /opt/allure-2.14.0 /opt/allure \
    && ln -s /opt/allure/bin/allure /usr/bin/allure \
    && rm allure.zip

RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unixodbc \
    unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia todos los archivos del proyecto al contenedor
COPY . .

# Instala dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["bash", "-c"]
CMD ["pytest tests --alluredir=allure-results && allure serve allure-results"]
