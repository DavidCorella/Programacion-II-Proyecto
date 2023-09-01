import mariadb

def iniciar_conexionBD():
        try:
            con = mariadb.connect(
                user="David",
                password="123456",
                host="10.147.18.2",
                port=3306,
                database="Inventario"
            )
        except mariadb.Error as e:
            print("Error al conectar al servidor: {e}")
        return con


def crearBodega(numero):
    conexion = iniciar_conexionBD()
    cur = conexion.cursor()
    cur.execute("CREATE TABLE Bodega{num}(ID int, NOMBRE varchar(50), PRECIO double, Cantidad int)".format(num = numero))
    conexion.commit()
    conexion.close()
    
def obtenerTablas():
    conexion = iniciar_conexionBD()
    cur = conexion.cursor()
    cur.execute("SHOW TABLES")
    resultado = cur.fetchall()
    conexion.close()
    return resultado

def eliminarBodega(numero):
    conexion = iniciar_conexionBD()
    cur = conexion.cursor()
    cur.execute("DROP TABLE Bodega{num}".format(num = numero))
    conexion.commit()
    conexion.close()

def seleccionarTabla(numero):
    conexion = iniciar_conexionBD()
    cur = conexion.cursor()
    cur.execute("Select * from Bodega{num}".format(num = numero))
    resultado = cur.fetchall()
    conexion.close()
    return resultado

def registrarArticulo(Codigo,Nombre,Precio,Cantidad):
    conexion = iniciar_conexionBD()
    cur = conexion.cursor()
    cur.execute("Insert into Articulos values({cod},{nom},{pre},{cant})".format(cod = Codigo, nom = Nombre, pre = Precio, cant = Cantidad))
    cur.commit()
    conexion.close()