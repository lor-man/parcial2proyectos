import psycopg2 as ps
import datetime
salir = False

print("Boletos aerolinea")

def postgres_insert(nombre,vuelo,clss1,clss2,clss3,subTotal,descuento,total):
    conexion=None
    try:
        conexion=ps.connect(database="Parcial2",user="postgres",password="123456",host="172.31.64.1",port="5432")
        cursor=conexion.cursor()
        cursor.execute("""INSERT INTO public."boletosAerolinea"("ID", nombre, "claseVuelo", "cantClase1", "cantClase2", "cantClase3", subtotal, descuento, total) 
        VALUES (nextval('pk_boletosAerolinea'), %(nm)s, %(clssV)s, %(cntClss1)s, %(cntClss2)s, %(cntClss3)s,%(sub)s,%(des)s,%(total)s); """,
        {'nm':nombre,'clssV':vuelo ,'cntClss1':clss1 ,'cntClss2':clss2 ,'cntClss3':clss3,'sub':subTotal,'des':descuento,'total':total})
        conexion.commit()
        cursor.close()
    except (Exception, ps.Error) as error:
        print("Error al obtener datos ", error)
    finally:
        if conexion is not None:
            conexion.close()

def postgres_select():
    conexion=None
    try:
        conexion=ps.connect(database="Parcial2",user="postgres",password="123456",host="172.31.64.1",port="5432")
        cursor=conexion.cursor()
        cursor.execute("""SELECT * FROM public."boletosAerolinea" ORDER BY "ID" ASC""")
        datos=cursor.fetchall()
        print("-------------------------------Registro-----------------------------")
        for fila in datos:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("ID:                          ",fila[0])
            print("Nombre:                      ",fila[1])
            print("Clase de vuelo:              ",fila[2])
            print("Cant. servicios 1era clase:  ",fila[3])
            print("Cant. servicios 1era clase:  ",fila[4])
            print("Cant. servicios 1era clase:  ",fila[5])
            print("Subtotal:                    ",fila[6])
            print("Descuento:                   ",fila[7])
            print("Total:                       ",fila[8])
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        cursor.close()
        print("--------------------------------------------------------------------")
    except (Exception, ps.Error) as error:
        print("Error al obtener datos ", error)
    finally:
        if(conexion is not None):
            conexion.close()

def postgres_delet(id):
    conexion=None
    try:
        conexion=ps.connect(database="Parcial2",user="postgres",password="123456",host="172.31.64.1",port="5432")
        cursor=conexion.cursor()
        cursor.execute("""DELETE FROM public."boletosAerolinea" WHERE "ID"=%(id)s;""",{'id':id})
        conexion.commit()
        cursor.close()
    except (Exception, ps.Error) as error:
        print("Error al obtener datos ", error)
    finally:
        if conexion is not None:
            conexion.close()

clssVuelo=0
clssBebida=[0,0,0]
clssComida=[0,0,0]
clssPelicula=[0,0,0]
x=None
name=str(input("Ingrese su nombre:"))
while(salir!=True):
    try:        
        print("Menú: \n 1) Ingresar servicios \n 2) Eliminar servicios \n 3) Calcular \n 4) Mostrar registros \n 5) Eliminar registro \n 6) Salir")
        opc=int(input("Ingrese la opción:\n-->"))
        if(opc==1):
            print("Escoga el tipo de vuelo: 1)Primera clase, 2)Segunda clase, 3)Tercera clase")
            x=int(input("-> "))
            if(x== 1):
                clssVuelo=1
            elif(x==2):
                clssVuelo=2
            elif(x==3):
                clssVuelo=3
            else:
                clssVuelo=3
            print("Ingrese la cantidad de camida por el tipo de clase ")
            clss1Comida=int(input("Cantidad de comida de 1ra clase= "))
            clss2Comida=int(input("Cantidad de comida de 2ra clase= "))
            clss3Comida=int(input("Cantidad de comida de 3ra clase= "))

            clss1Bebida=int(input("Cantidad de bebida de 1ra clase= "))
            clss2Bebida=int(input("Cantidad de bebida de 2ra clase= "))
            clss3Bebida=int(input("Cantidad de bebida de 3ra clase= "))

            clss1Pelicula=int(input("Cantidad de pelicula de 1ra clase= "))
            clss2Pelicula=int(input("Cantidad de pelicula de 2ra clase= "))
            clss3Pelicula=int(input("Cantidad de pelicula de 3ra clase= "))
            if(clss1Comida>=0 and clss1Bebida>=0 and clss1Pelicula>=0 and clss2Comida>=0 and clss2Bebida>=0 and clss2Pelicula>=0 and clss3Comida>=0 and clss3Bebida>=0 and clss3Pelicula>=0):
                clssComida[0]=clssComida[0]+clss1Comida
                clssComida[1]=clssComida[1]+clss2Comida
                clssComida[2]=clssComida[2]+clss3Comida
                clssBebida[0]=clssBebida[0]+clss1Bebida
                clssBebida[1]=clssBebida[1]+clss2Bebida
                clssBebida[2]=clssBebida[2]+clss3Bebida
                clssPelicula[0]=clssPelicula[0]+clss1Pelicula
                clssPelicula[1]=clssPelicula[1]+clss2Pelicula
                clssPelicula[2]=clssPelicula[2]+clss3Pelicula
            else:
                print("Se a ingresado un dato erroneo por favor intentelo de nuevo")
        elif(opc==2):
            name=str(input("Ingrese su nombre:"))
            clssVuelo=0
            clssBebida=[0,0,0]
            clssComida=[0,0,0]
            clssPelicula=[0,0,0]
        elif(opc==3):
            Descuento=0
            cntServicios=0
            for cnt in clssBebida:
                cntServicios=cntServicios+cnt
            for cnt in clssComida:
                cntServicios=cntServicios+cnt
            for cnt in clssPelicula:
                cntServicios=cntServicios+cnt
            subtotal=50*clssComida[0]+40*clssComida[1]+25*clssComida[2]+35*clssBebida[0]+25*clssBebida[1]+10*clssBebida[2]+70*clssPelicula[0]+55*clssPelicula[1]+25*clssPelicula[2]
            if(cntServicios>=10):
                Descuento= 0.1*subtotal
            elif(clssVuelo==1 and clssBebida[1]==clssBebida[2]==clssComida[1]==clssComida[2]==clssPelicula[1]==clssPelicula[2]==0 and clssBebida[0]>=1 and clssComida[0]>=1 and clssPelicula[0]>=1):
                Descuento= 0.05*subtotal
            elif(cntServicios>=10 and clssBebida[0]>=1 and clssComida[0]>=1 and clssPelicula[0]>=1 ):
                    Descuento = 0.15*subtotal
            else:
                Descuento=0
            cntServicios1=clssBebida[0]+clssComida[0]+clssPelicula[0]
            cntServicios2=clssBebida[1]+clssComida[1]+clssPelicula[1]
            cntServicios3=clssBebida[2]+clssComida[2]+clssPelicula[2]
            Total=subtotal-Descuento
            print("-----------------------------------------CALCULANDO----------------------------------------------")
            print("Subtotal=  "+str(subtotal))
            print("Descuento= "+str(Descuento))
            print("Total=     "+str(Total))
            print("-------------------------------------------------------------------------------------------------")
            postgres_insert(name,clssVuelo,cntServicios1,cntServicios2,cntServicios3,subtotal,Descuento,Total)
        elif(opc==4):
            postgres_select()
        elif(opc==5):
            id_delete=int(input("Ingrese el ID del registro que desea eliminar(ver registro primero)\n-->"))
            postgres_delet(id_delete)
        elif(opc==6):
            salir=True
        else:
            print("Opcion invalida elige otra!!!")
    except Exception as exc:
        print(str(exc)+"\n Algo va mal")