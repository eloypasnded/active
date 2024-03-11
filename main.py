import requests
import time

def main():
    while True:
        try:
            start_time = time.time()
            response1 = requests.get("https://spadl.onrender.com/")
            response2 = requests.get("https://spadl2.onrender.com/")
            end_time = time.time()

            print(f"Tiempo de respuesta para https://spadl.onrender.com/: {end_time - start_time:.2f} segundos")
            print(f"Tiempo de respuesta para https://spadl2.onrender.com/: {end_time - start_time:.2f} segundos")

            # Esperar 10 minutos antes de volver a hacer la solicitud
            time.sleep(600)

        except KeyboardInterrupt:
            print("El script ha sido detenido manualmente.")
            break

if __name__ == "__main__":
    main()
