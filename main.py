from empresa.DAO.DAOpersona import DAOPersona

def main():

#CRUD - CREATE, READ, UPDATE, DELETE
#CLAE - CREAR, LEER, ACTUALIZAR, ELIMINAR   

# Crear una persona en la base de datos
    CrearPersona = DAOPersona()
    CrearPersona.crear_persona_db("Samir", "Goede", "samir.goede@ejemplo.com", "6543232")

#aca se demuestra la herencia de la clase usuario
    
if __name__ == '__main__':
    main()
