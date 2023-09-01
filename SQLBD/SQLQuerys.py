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
    cur.execute("Insert into Articulos values({cod},\"{nom}\",{pre},{cant})".format(cod = Codigo, nom = Nombre, pre = Precio, cant = Cantidad))
    conexion.commit()
    conexion.close()

def SeleccionarTablaArticulos():
     conexion = iniciar_conexionBD()
     cur = conexion.cursor()
     cur.execute("Select * from Articulos")
     resultado = cur.fetchall()
     conexion.close()
     return resultado

def GuardarArticuloBodega(Bodega, Codigo, Nombre, Precio, Cantidad):
     conexion = iniciar_conexionBD()
     cur = conexion.cursor()
     cur.execute("Insert into Bodega{Num} values({cod},\"{nom}\",{pre},{cant})".format(Num = Bodega, cod = Codigo, nom = Nombre, pre = Precio, cant = Cantidad))
     conexion.commit()
     cur.execute("Delete from Articulos where Codigo={cod} and Nombre = \"{nom}\" and Precio = {pre} and cantidad = {cant}".format(cod = Codigo, nom = Nombre, pre = Precio, cant = Cantidad))
     conexion.commit()
     conexion.close()

def ObtenerDistrubidores():
    conexion = iniciar_conexionBD()
    cur = conexion.cursor()
    cur.execute("Select * from Distribuidores")
    resultado = cur.fetchall()
    conexion.close()
    return resultado

def ObtenerDistrubidoresCombobox():
    conexion = iniciar_conexionBD()
    cur = conexion.cursor()
    cur.execute("Select Nombre from Distribuidores")
    resultado = cur.fetchall()
    conexion.close()
    return resultado

def RegistrarDistribuidor(Codigo, Nombre):
     conexion = iniciar_conexionBD()
     cur = conexion.cursor()
     cur.execute("Insert into Distribuidores values({cod},\"{nom}\")".format(cod = Codigo, nom = Nombre))
     conexion.commit()
     conexion.close()

def ModificarCantidad(Codigo,Nombre,Precio,CantidadTabla,Resultado, Bodega):
     conexion = iniciar_conexionBD()
     cur = conexion.cursor()
     cur.execute("Update {Bod} set Cantidad = {Res} where ID = {cod} and Nombre = \"{Nom}\" and Precio = {Pre} and Cantidad = {Cant}".format(Bod = Bodega, Res = Resultado, cod = Codigo, Nom = Nombre, Pre = Precio, Cant = CantidadTabla))
     conexion.commit()
     conexion.close()

def EliminarArticulo(Codigo,Nombre,Precio,CantidadTabla,Bodega):
    conexion = iniciar_conexionBD()
    cur = conexion.cursor()
    cur.execute("Delete from {Bod} where ID={cod} and Nombre = \"{nom}\" and Precio = {pre} and cantidad = {cant}".format(Bod = Bodega, cod = Codigo, nom = Nombre, pre = Precio, cant = CantidadTabla))
    conexion.commit()
    conexion.close()