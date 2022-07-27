import os

from dotenv import load_dotenv


def configs():
    try :
        print("cargando environment")
        load_dotenv()
    except Exception:
        print("ocurrio un error cargando las variables de entorno")



def main():
    print("programa para usar de ejemplo para la utilizacion del archivo .env")

    configs()
    print("se termino de cargar las configuraciones")
    print ("obteniendo valores")
    dbHost = os.getenv("DB_HOST")
    print("db Host %s"% dbHost)

    
if __name__ == "__main__":
    main()