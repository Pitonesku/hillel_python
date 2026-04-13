# ДЗ 13.1. Очистити текст від html-тегів
# Ваше завдання написати функцію, яка прочитає заданий файл, очистить текст від html-тегів і запише цей текст в інший файл.
# html-тег завжди починається з "<" і закінчується на ">" тобто. потрібно видалити ці символи та все, що між ними.
# Функція отримує на вхід два параметри – ім'я файлу, який потрібно очистити, та ім'я файлу, куди потрібно записати очищений текст. Ім'я файлу, куди потрібно писати, можна задати за замовчуванням.
# Приклади файлів у вкладенні – файл який потрібно очистити (draft.html) та приклад файлу, який може вийти на виході з очищеним текстом (cleaned.txt). Файл draft.html необхідно скачати і покласти поряд з файлом, де буде вирішення цієї домашки.
# Додаткове завдання для тих, хто захоче ускладнити рішення - спробуйте прибрати рядки, в яких немає інформації.

import re
import os

DIR_PATH = os.path.dirname(__file__)
INPUT_FILE_PATH = os.path.join(DIR_PATH, "draft.html")
OUTPUT_FILE_PATH = os.path.join(DIR_PATH, "cleaned.txt")

patern = r"<.*?>"

def clean_html(input_file, output_file = "cleaned.txt",  patern = r"<.*?>"):
    with open(input_file, "r", encoding = "utf-8") as file, \
        open (output_file, "w", encoding = "utf-8") as cleaned_file:
        cleaned_text = re.sub(patern,"",file.read(), flags = re.DOTALL)
        return cleaned_file.write(cleaned_text)

clean_html(INPUT_FILE_PATH, "Lesson 13/cleaned.txt")





 