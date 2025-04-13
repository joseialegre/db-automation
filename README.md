> **Nota:** Este proyecto da por hecho que tienes una base de datos SQL Server configurada y accesible, así como Docker instalado en tu computadora.

# 🧪 DB Automation Project
---

## 📦 Requisitos

### 1. Guardar requirements
```bash
pip freeze > requirements.txt
```

### 2. Instalar requirements
```bash
pip install -r requirements.txt
```

---

## ⚙️ Modos de Ejecución

### ✅ En Local

```bash
rm -r -fo allure-results
pytest tests --alluredir=allure-results
```

### 🐳 Ejecutar Allure con Docker (si no lo tenés instalado)

```bash
docker run --rm -p 5050:5050 \
  -v "${PWD}/allure-results:/app/allure-results" \
  -v "${PWD}/allure-report:/app/allure-report" \
  frankescobar/allure-docker-service
```

### 🌐 Ver el Reporte

[http://localhost:5050/static/projects/default/reports/latest/index.html](http://localhost:5050/static/projects/default/reports/latest/index.html)


## 🐳 En Docker (Contenedor del Proyecto)

### 1. Build de la imagen
```bash
docker build -t db-automation .
```

### 2. Ejecutar el contenedor
```bash
docker run --rm -p 5252:5252 -p 8000:8000 db-automation
```
