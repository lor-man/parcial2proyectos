import psycopg2 as ps
import datetime
salir = False

print("Control de citas")

def postgres_insert(nombre,edad,peso,altura,fecha,hora):
    conexion=None
    try:
        conexion=ps.connect(database="Parcial2",user="postgres",password="123456",host="172.31.64.1",port="5432")
        #cursor=conexion.cursor("""INSERT INTO public."controlCitas"("ID", nombre, edad, peso, altura, fecha, hora)VALUES (nextval('pk_controlCitas'), %s, %s, %s, %s, %s,%s); """,(nombre,edad,peso,altura,fecha,hora))
        cursor=conexion.cursor()
        cursor.execute("""INSERT INTO public."controlCitas"("ID", nombre, edad, peso, altura, fecha, hora)VALUES (nextval('pk_controlCitas'), %(nm)s, %(ed)s, %(pes)s, %(alt)s, %(date)s,%(h)s); """,{'nm':nombre,'ed':edad ,'pes':peso ,'alt':altura ,'date':fecha ,'h':hora})
        conexion.commit()
        cursor.close()
    except (Exception, ps.Error) as error:
        print("Error al obtener datos ", error)
    finally:
        if conexion is not None:
            conexion.close()

def postgres_select(fecha):
    #selectquery=""" SELECT "ID",nombre,hora FROM public."controlCitas" where fecha = '2021-04-22'; """
    conexion=None
    try:
        conexion=ps.connect(database="Parcial2",user="postgres",password="123456",host="172.31.64.1",port="5432")
        cursor=conexion.cursor()
        cursor.execute(""" SELECT "ID",nombre,hora FROM public."controlCitas" where fecha = %(fecha)s; """,{'fecha':fecha})
        datos=cursor.fetchall()
        print("Registro de datos del programa:")
        for fila in datos:
            print("ID: ",fila[0])
            print("Nombre:   ",fila[1])
            print("Hora:  ",fila[2])
            print("Fecha:  ",fecha)
            print("\n")
        cursor.close()
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
        cursor.execute("""DELETE FROM public."controlCitas" WHERE "ID"=%(id)s;""",{'id':id})
        conexion.commit()
        cursor.close()
    except (Exception, ps.Error) as error:
        print("Error al obtener datos ", error)
    finally:
        if conexion is not None:
            conexion.close()

def in_datos():
    try:
        nombre=str(input("Ingrese el nombre del paciente: "))
        edad=int(input("Ingrese la edad del paciente: "))
        peso=float(input("Ingrese el peso del paciente: ")) 
        altura=float(input("Ingrese la altura del paciente: "))
        print("Formato de fecha YY-MM-DD")
        dia=int(input("Ingrese el dia de la cita: "))
        mes=int(input("Ingrese el mes de la cita: "))
        year=int(input("Ingrese el año de la cita: "))
        print("Formato de hora 24hrs. HH:MM")
        hora=str(int(input("Ingrese la hora: ")))
        minutos=str(int(input("Ingrese los minutos: ")))
        date=datetime.date(year,mes,dia)
        #hr="""'"""+hora+':'+minutos+"""'"""
        #date=year+'-'+mes+'-'+dia
        hr=hora+':'+minutos
        if(edad>=0 and peso>=0 and altura>=0):
            return nombre, edad,peso,altura,date,hr
        else:
            return -1,-1,-1,-1,-1,-1
    except:
        print("Se ha ingresado mal un dato, por favor intentalo de nuevo")

while(salir!=True):
    try:
        print("Menú: \n 1) Ingresar cita \n 2) Mostrar citas \n 3) Eliminar cita \n 4)Salir")
        opc=int(input("Ingrese la opción:\n-->"))
        if(opc==1):
            nombre,edad,peso,altura,date,hr=in_datos()
            if(nombre!=-1):
                postgres_insert(nombre,edad,peso,altura,date,hr)
            else:
                print("Se ingreso un mal dato")
        elif(opc==2):
            print("Formato de fecha YY-MM-DD")
            dia=int(input("Ingrese el dia de la cita: "))
            mes=int(input("Ingrese el mes de la cita: "))
            year=int(input("Ingrese el año de la cita: "))
            print("")
            if(dia>0 and mes>0 and year>0):
                date=datetime.date(year,mes,dia)
                postgres_select(date)
            else:
                print("Se ingreso un dato erroneo, intentelo de nuevo...")
        elif(opc==3):
            opc=int(input(("Ingrese el ID de la cita a eliminar(El proceso es irreversible)\n->")))
            if(opc>=0):
                postgres_delet(opc)
            else:
                print("Se ingreso mal el ID o no existe el registro")
        elif(opc==4):
            salir=True  
        else:
            print("Opcion invalida elige otra!!!")
    except Exception as exc:
        print(str(exc)+"\n Algo va mal")