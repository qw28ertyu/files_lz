import matplotlib.pyplot as plt  # для вывода графика статистики
import docx  # для работы с документом
from collections import Counter  # для автоматического подсчета элементов

lion = docx.Document('lion.docx')  # чтение документа
doc = docx.Document()  # файл для вывода таблицы

# Все элементы (строчные буквы) для фильтрации (включая 'ё')
letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
           'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']

table = doc.add_table(rows=1, cols=3)  # создание таблицы с одной строкой и тремя колонками
table.style = 'Table Grid'  # стиль таблицы

hdr_cells = table.rows[0].cells  # заголовки таблицы
hdr_cells[0].text = 'Слово' 
hdr_cells[1].text = 'Частота встречи, раз'
hdr_cells[2].text = 'Частота встречи, %'

text = '\n'.join([paragraph.text for paragraph in lion.paragraphs])  # извлекаем и объединяем текст из абзацев
text_lower = text.lower()  # приводим к нижнему регистру
words = text_lower.split()  # разбиваем на отдельные слова

filtered_words = [
    word.strip(" ,.!?()[]{}'\"-_@")  # очищаем от знаков препинания
    for word in words 
    if len(word) > 0 and all(char in letters for char in word.strip(" ,.!?()[]{}'\"-_@"))  # фильтруем по списку букв
]

word_counts = Counter(filtered_words)  # считаем частоту уникальных слов
total_words = len(filtered_words)  # создаем переменную с количеством слов

for word, count in word_counts.items(): 
    procent = (count / total_words) * 100 if total_words > 0 else 0  # считаем частоту в процентах
    
    new_row = table.add_row()  # создаем новую строчку
    new_row.cells[0].text = word  # заполняем первую ячейку
    new_row.cells[1].text = str(count)  # вторую ячейку
    new_row.cells[2].text = f"{procent:.2f}"  # третью ячейку с округлением

doc.save('table.docx')  # сохраняем файл с таблицей

filtered_text = ''.join([char for char in text.lower() if char in letters])  # фильтруем текст по списку букв
letter_counts = Counter(filtered_text)  # считаем количество каждой буквы

sorted_letters = sorted(letter_counts.keys())  # сортируем буквы по алфавиту
sorted_counts = [letter_counts[letter] for letter in sorted_letters]  # получаем их частоты

plt.figure(figsize=(12, 6))  # задаем размер гистограммы
plt.bar(sorted_letters, sorted_counts, color='skyblue')  # строим столбчатую гистограмму

plt.xlabel('Буквы')  # подпись оси x
plt.ylabel('Количество')  # подпись оси y
plt.title('Количество строчных русских букв в тексте')  # заголовок графика
plt.grid(axis='y')  # сетка для удобства чтения

plt.tight_layout()  # автоподгонка макета
plt.show()  # отображаем график