# Sistema de Gestión de Empleados

Este es un sistema de gestión de empleados desarrollado en Python que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los registros de empleados en una base de datos MySQL.

## Características

- Gestión completa de empleados (CRUD)
- Interfaz de línea de comandos intuitiva
- Conexión segura a base de datos MySQL
- Validación de datos
- Estructura MVC (Modelo-Vista-Controlador)

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

1. Python 3.x
2. MySQL Server
3. pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar el repositorio

```bash
git clone [URL_DEL_REPOSITORIO]
cd sistemagestionempleados-main
```

### 2. Instalar dependencias

```bash
pip install pymysql
```

### 3. Configurar la base de datos

1. Abre MySQL Workbench o tu cliente MySQL preferido
2. Crea una nueva base de datos:
```sql
CREATE DATABASE gestion_empleados;
```

3. Crea las tablas necesarias ejecutando el script SQL que se encuentra en el archivo `database.sql`

### 4. Configurar la conexión a la base de datos

Edita el archivo `empresa/conexion_db.py` y actualiza los siguientes parámetros con tus credenciales:

```python
host = "localhost"  # o la dirección de tu servidor MySQL
user = "tu_usuario"
password = "tu_contraseña"
db = "gestion_empleados"
```

## Estructura del Proyecto

```
sistemagestionempleados-main/
├── empresa/
│   ├── DAO/
│   │   ├── DAOpersona.py
│   │   └── __init__.py
│   ├── DTO/
│   │   ├── DTOpersona.py
│   │   ├── DTOempleado.py
│   │   ├── DTOdepartamento.py
│   │   └── __init__.py
│   └── conexion_db.py
├── main.py
└── README.md
```

## Uso del Sistema

1. Ejecuta el programa principal:
```bash
python main.py
```

2. En el menú principal, podrás:
   - (C) Crear nuevos registros
   - (R) Mostrar registros existentes
   - (U) Actualizar registros
   - (D) Eliminar registros
   - (E) Salir del programa

## Funcionalidades

### Crear Registro
- Permite ingresar nuevos empleados con sus datos personales
- Valida la información ingresada
- Almacena los datos en la base de datos

### Mostrar Registros
- Muestra todos los registros existentes
- Permite buscar registros específicos por ID
- Muestra la información en formato tabular

### Actualizar Registros
- Permite modificar los datos de un empleado existente
- Muestra los datos actuales antes de la modificación
- Valida los nuevos datos ingresados

### Eliminar Registros
- Permite eliminar registros por ID
- Solicita confirmación antes de eliminar
- Muestra mensaje de éxito o error

## Solución de Problemas

Si encuentras algún error:

1. Verifica que la base de datos esté correctamente configurada
2. Comprueba que las credenciales de MySQL sean correctas
3. Asegúrate de que todas las dependencias estén instaladas
4. Verifica que el servidor MySQL esté en ejecución

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

```
├── empresa/
│   ├── __init__.py             # Indica que es un paquete Python
│   ├── DAO/                    # Clases (Data Acces Object)
│   │   ├── __init__.py         # Importación de módulos
│   │   ├── DAOpersona.py       # Clase Data Acces Object Persona
│   ├── DTO/                    # Lógica de negocio - Data transfer Object
│   │   ├── __init__.py         # Importación de módulos
│   │   ├── DTOdepartamento.py  # Clase Departamento
│   │   ├── DTOempleado.py      # Clase Empleados
│   │   ├── DTOpersona.py       # Clase Persona
│   │   └── DTOusuario.py       # Clase Usuario
├── conexion_db.py              # Configuraciones generales del proyecto (ej. variables de entorno)
├── main.py                     # Punto de entrada principal para ejecutar el programa
└── README.md                   # Descripción del proyecto y cómo ejecutarlo


> [!TIP]
> Construido modularmente con paradigma OOB Python.

> [!IMPORTANT]  
> No esta terminado aun, falta base de datos

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Este proyecto tiene la siguiente estructura de directorios:


```
├── empresa/
│   ├── __init__.py             # Indica que es un paquete Python
│   ├── DAO/                    # Clases (Data Acces Object)
│   │   ├── __init__.py         # Importación de módulos
│   │   ├── DAOpersona.py       # Clase Data Acces Object Persona
│   ├── DTO/                    # Lógica de negocio - Data transfer Object
│   │   ├── __init__.py         # Importación de módulos
│   │   ├── DTOdepartamento.py  # Clase Departamento
│   │   ├── DTOempleado.py      # Clase Empleados
│   │   ├── DTOpersona.py       # Clase Persona
│   │   └── DTOusuario.py       # Clase Usuario
├── conexion_db.py              # Configuraciones generales del proyecto (ej. variables de entorno)
├── main.py                     # Punto de entrada principal para ejecutar el programa
└── README.md                   # Descripción del proyecto y cómo ejecutarlo

Creado por Samir Goede
