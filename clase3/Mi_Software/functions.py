import pandas as pd
from bs4 import BeautifulSoup
import requests

def temp_max():
    url = "https://www.meteoblue.com/es/tiempo/semana/madrid_españa_3117735"  # Cambia esta URL por una válida
    try:
        r = requests.get(url)
        r.raise_for_status()  # Esto lanza una excepción si la respuesta no es exitosa
        print(r)  # Response [200] -> Funciona

        soup = BeautifulSoup(r.text, "html5lib")  # Si la página funciona, extrae el texto en formato html
        temperatura = soup.find_all(class_="tab-temp-max")
        temp = []
        for temp_i in temperatura:
            temp_text = temp_i.get_text(strip=True).replace("\xa0°C", "").replace("°", "").strip()
            try:
                temp_value = int(temp_text)
                temp.append(temp_value)
                print(f"Temperatura extraída: {temp_value}°C")
                if temp_value >= 40:
                    print("Temperatura desértica")
                elif temp_value >= 33:
                    print("Temperatura Alta")
                elif temp_value > 3:
                    print("Temperatura Confortable")
                else:
                    print("Temperatura muy fría")
                
            except ValueError:   
                print(f"No se pudo convertir la temperatura: {temp_text}")
                
    except requests.RequestException as e:
        print(f"Error al acceder a la página: {e}")
    return temp