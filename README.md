# Old Wave backend en FastApi
Para correr la aplicación se deben seguir los siguientes pasos
## 1. Clonar el repositorio
1. git clone https://github.com/SotalvaroO/oldwave-fastapi-backend.git
2. acceder a la carpeta raiz del proyecto mediante cd ${ruta_del_proyecto}
## 2. Crear el entorno virtual de python dentro del directorio raiz del proyecto
### Para Windows
python -m venv venv
### Para Linux
python3 -m venv venv
## 3. Activar el entorno virtual
### Para Windows
venv\Scripts\activate
### Para Linux
source venv/bin/activate
## 4. Reinstalar las dependencias que existen en el archivo requirements.txt
pip install -r requirements.txt
## 5. Levantar el servidor Uvicorn y agregarle actualización en tiempo real
uvicorn main:app --reload
