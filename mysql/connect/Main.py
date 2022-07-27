from tkinter import EXCEPTION
import mysql.connector

import os
from dotenv import load_dotenv


def configs():
    try :
        print("cargando environment")
        load_dotenv()
    except Exception:
        print("ocurrio un error cargando las variables de entorno")
def conectarDB():
    try:

        mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USERNAME"),
            password =os.getenv("DB_PASSWORD")
        )
        return mydb 
        
    except Exception:
      print("ocurrio un error conectandose a la db")


def main():
    print("este programa se conecta a la base de datos")
    print("cargando onfiguraciones")
    configs()
    print("configuraciones cargadas")
    print("conectando db")
    mydb = conectarDB()
  
    print("se logro conectar a la db")
    print(mydb)


if __name__ == "__main__":
    main()  