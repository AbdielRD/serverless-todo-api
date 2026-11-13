# Serverless To-Do List API 🚀

API RESTful sin servidor (*Serverless*) construida con Python y servicios nativos de AWS, diseñada para gestionar una lista de tareas de forma escalable y eficiente.

## 🏗️ Arquitectura del Sistema
El proyecto implementa una arquitectura orientada a eventos y completamente administrada, eliminando la necesidad de aprovisionar o gestionar servidores físicos o virtuales:

1. **API Gateway (HTTP API):** Actúa como el punto de entrada público, recibiendo las peticiones HTTP desde internet y enrutándolas.
2. **AWS Lambda:** Función computacional escrita en **Python** encargada de procesar la lógica de negocio (validaciones y control de métodos HTTP).
3. **Amazon DynamoDB:** Base de datos NoSQL altamente disponible para el almacenamiento persistente de las tareas.

---

## 🛠️ Tecnologías y Stack
* **Lenguaje:** Python 3.x (`boto3`)
* **Cloud Provider:** Amazon Web Services (AWS)
* **Servicios AWS:** Lambda, API Gateway, DynamoDB, IAM
* **Control de versiones:** Git / GitHub

---

## 🔌 Endpoints de la API

* **`GET /`**
  * **Descripción:** Consulta y recupera todas las tareas registradas en la base de datos.
  * **Respuesta exitosa (`200 OK`):** Retorna un objeto JSON con la lista de tareas.

* **`POST /`**
  * **Descripción:** Crea una nueva tarea en el sistema.
  * **Cuerpo de la petición (JSON):**
    ```json
    {
      "title": "Aprender Serverless en AWS"
    }
    ```
  * **Respuesta exitosa (`201 Created`):** Retorna el ID único generado (`taskId`), el título y el estado inicial.

---

## 🚀 Despliegue y Pruebas
La función procesa eventos HTTP de manera segura mediante roles de IAM configurados con políticas de acceso least-privilege hacia DynamoDB (`AmazonDynamoDBFullAccess`), utilizando variables de entorno (`TABLE_NAME`) para desacoplar la configuración de la infraestructura.
