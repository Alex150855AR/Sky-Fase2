SKY Platform - Fase 2 (DevOps & Microservicios)

Este repositorio contiene la Fase 2 del proyecto de modernización tecnológica para la empresa SKY. El objetivo principal es la implementación de la arquitectura de microservicios diseñada en la Fase 1, aplicando fundamentos y prácticas de DevOps como Integración Continua (CI), Pruebas Automatizadas y Despliegue en la nube (AWS).

Arquitectura y Tecnologías

El proyecto implementa el servicio principal de gestión de clientes (client-service) utilizando tecnologías modernas y escalables:

Framework: FastAPI (Python) para alto rendimiento y autogeneración de documentación OpenAPI.

Validación de Datos: Pydantic (Validación estricta de RFC y formatos de Email).

Persistencia: Almacenamiento ágil basado en archivos JSON (data/clientes.json) para esta fase inicial.

Testing: Pytest para pruebas unitarias y de integración.

Integración Continua (CI): GitHub Actions (Linting con Flake8 y Testing automatizado).

Despliegue (CD/Infraestructura): Amazon Web Services (Instancia EC2 Ubuntu Linux).

Containerización: Docker (Dockerfile preparado para fases futuras).

Estructura del Proyecto

sky-fase2/
├── .github/workflows/
│   └── ci.yml               # Pipeline de Integración Continua (GitHub Actions)
├── app/
│   ├── __init__.py
│   ├── main.py              # Punto de entrada de la aplicación FastAPI
│   ├── models.py            # Modelos de datos y validaciones (Pydantic)
│   ├── routes.py            # Controladores y Endpoints CRUD
│   └── validators.py        # Lógica de validación de negocio (RFC, Email)
├── data/
│   └── clientes.json        # Base de datos en formato JSON
├── docs/
│   └── infraestructura.md   # Evidencias fotográficas del despliegue en AWS y CI
├── tests/
│   ├── __init__.py
│   └── test_app.py          # Suite de pruebas unitarias automatizadas
├── Dockerfile               # Receta de construcción de la imagen Docker
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Documentación principal


API Endpoints (Referencia)

La API provee un CRUD completo para la gestión de clientes. Puedes probar estos endpoints interactivamente accediendo a la ruta /docs (Swagger UI) una vez que el servidor esté corriendo.

1. GET /health
Descripción: Health Check del servidor.
Respuestas: 200 OK

2. GET /api/clientes
Descripción: Lista todos los clientes registrados.
Respuestas: 200 OK

3. POST /api/clientes
Descripción: Crea un nuevo cliente validando RFC y Email.
Respuestas: 201 Created, 422 Unprocessable

4. GET /api/clientes/{id}
Descripción: Obtiene los detalles de un cliente específico por ID.
Respuestas: 200 OK, 404 Not Found

5. DELETE /api/clientes/{id}
Descripción: Elimina un cliente del sistema por ID.
Respuestas: 200 OK, 404 Not Found

Instalación y Ejecución Local

Para ejecutar este proyecto en un entorno de desarrollo local (Windows/Linux/Mac), sigue estos pasos:

1. Clonar el repositorio

git clone [https://github.com/Alex150855AR/Sky-Fase2.git](https://github.com/Alex150855AR/Sky-Fase2.git)
cd Sky-Fase2

2. Crear y activar el entorno virtual

En Windows:

python -m venv venv
.\venv\Scripts\activate

En Linux / Mac:

python3 -m venv venv
source venv/bin/activate

3. Instalar dependencias

pip install --upgrade pip
pip install -r requirements.txt

4. Ejecutar el servidor de desarrollo

uvicorn app.main:app --reload --port 5000

La aplicación estará disponible en: http://127.0.0.1:5000
La documentación interactiva (Swagger) está en: https://www.google.com/search?q=http://127.0.0.1:5000/docs

Pruebas Unitarias y Calidad de Código

El proyecto incluye una suite de pruebas para garantizar la fiabilidad del código. Para ejecutarlas localmente:

# Ejecutar análisis estático de código (Linting)
flake8 app tests

# Ejecutar pruebas unitarias
pytest tests/

Integración Continua (CI Pipeline)

Este proyecto utiliza GitHub Actions. En cada push o pull_request a la rama main, se dispara automáticamente un workflow definido en .github/workflows/ci.yml que:

Configura un entorno limpio con Python (Matriz de pruebas en 3.10 y 3.11).

Instala las dependencias.

Ejecuta Flake8 para asegurar estándares de calidad de código (PEP-8).

Ejecuta Pytest para verificar que ninguna funcionalidad se haya roto.

Si el pipeline falla, el despliegue es bloqueado, asegurando prácticas DevOps de alta calidad.

Despliegue en AWS EC2 (Producción)

La aplicación está diseñada para ser desplegada en una instancia Amazon EC2 (t3.micro) con Ubuntu Server.

Pasos de despliegue manual (Ejecutados en la Fase 2):

Levantar instancia EC2 en AWS.

Configurar Security Group permitiendo tráfico TCP en los puertos 22 (SSH) y 5000 (FastAPI).

Conexión vía SSH al servidor:

ssh -i "sky-key.pem" ubuntu@<IP_PUBLICA_AWS>

Actualización del sistema e instalación de dependencias nativas (python3-pip, python3-venv).

Clonado del repositorio, creación de entorno virtual e instalación de dependencias (ver sección de Ejecución Local).

Ejecución del servidor expuesto al internet público:

uvicorn app.main:app --host 0.0.0.0 --port 5000

(Nota: Las evidencias fotográficas de este proceso, incluyendo la consola de AWS, Security Groups y el check verde de GitHub Actions, se encuentran documentadas en docs/infraestructura.md).

Autor: Alex Aparicio

Proyecto: Reto / Fase 2 - Fundamentos DevOps