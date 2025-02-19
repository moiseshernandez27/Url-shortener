URL Shortener API

Este proyecto es un acortador de URLs desarrollado con FastAPI, Redis para almacenamiento en caché y PostgreSQL como base de datos.

🚀 Características

Acorta URLs largas en enlaces más cortos.

Recupera la URL original a partir de un enlace corto.

Almacena temporalmente las URLs en Redis para mejorar el rendimiento.

Usa PostgreSQL para almacenamiento persistente.

Dockerizado para fácil despliegue.

📦 Tecnologías Usadas

FastAPI - Framework web en Python

Redis - Caché en memoria

PostgreSQL - Base de datos relacional

SQLAlchemy - ORM para manejar la base de datos

Docker - Contenedores para facilitar la ejecución

🔧 Instalación y Uso

1️⃣ Clonar el repositorio

 git clone https://github.com/moiseshernandez27/url_shortener.git
 cd url_shortener

2️⃣ Configurar las variables de entorno

Crea un archivo .env con las siguientes variables:

DATABASE_URL=postgresql://user:password@db:5432/url_shortener
REDIS_HOST=redis
REDIS_PORT=6379

3️⃣ Construir y ejecutar los contenedores con Docker

docker-compose up --build

Esto iniciará la API en http://localhost:8000

📌 Endpoints

1️⃣ Acortar una URL

POST /shorten

{
  "original_url": "https://example.com"
}

Respuesta:

{
  "short_url": "abc123",
  "original_url": "https://example.com"
}

2️⃣ Recuperar la URL original

GET /{short_url}

curl -X GET "http://localhost:8000/abc123"

Respuesta:

{
  "original_url": "https://example.com"
}

📜 Licencia

Este proyecto está bajo la licencia MIT.
