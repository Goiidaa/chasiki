"""
# temperature.py - Copyright (c) 2025 Arthur Dantas
# This file is part of ClockTemp, licensed under the GNU General Public License v3.
# See <https://www.gnu.org/licenses/> for details.
"""
# temperature.py - Copyright (c) 2025 Arthur Dantas
# This file is part of ClockTemp, licensed under the GNU General Public License v3.
# See <https://www.gnu.org/licenses/> for details.

import requests
from bs4 import BeautifulSoup as BS

url = 'https://rp5.ru/Погода_в_Казани,_Татарстан'
class_ = 'ArchiveTemp'
class_feels = 'ArchiveTempFeeling'


# Get weather data from Open-Meteo
def get_weather(lat=0, lon=0):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Проверяем наличие ошибок в запросе

        # Парсим HTML-код страницы
        html = BS(r.text, 'html.parser')

        # Находим элемент с классом ArchiveTemp
        archive_temp = html.find(class_=class_)
        archive_temp1 = html.find(class_=class_feels)

        # Извлекаем температуры
        temperatures = archive_temp.find_all(class_='t_0')
        temp_values = []

        for temp in temperatures:
            temp_values.append(int(temp.get_text(strip=True)))  # Извлекаем текст и добавляем в список

        return temp_values  # Возвращаем список температур

    except requests.RequestException as e:
        print(f"Ошибка при получении данных: {e}")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


# Пример использования
if __name__ == "__main__":
    temperatures = get_weather()
    print("Температуры:", temperatures)
