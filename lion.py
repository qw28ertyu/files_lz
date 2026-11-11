import matplotlib.pyplot as plt  # для вывода графика статистики
import docx  # для работы с документом
from collections import Counter  # для автоматического подсчета элементов

doc_source = docx.Document('lion.docx')  # чтение документа
table_doc = docx.Document()  # файл для вывода таблицы

# Все элементы (строчные буквы) для фильтрации (включая 'ё')
alphabet_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                    'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']

result_table = table_doc.add_table(rows=1, cols=3)  # создание таблицы с одной строкой и тремя колонками
result_table.style = 'Table Grid'  # стиль таблицы

headers = result_table.rows[0].cells  # заголовки таблицы
headers[0].text = 'Слово' 
headers[1].text = 'Частота встречи, раз'
headers[2].text = 'Частота встречи, %'

full_text = '\n'.join([p.text for p in doc_source.paragraphs])  # извлекаем и объединяем текст из абзацев
text_lower = full_text.lower()  # приводим к нижнему регистру
raw_words = text_lower.split()  # разбиваем на отдельные слова

clean_words = [
    w.strip(" ,.!?()[]{}'\"-_@")  # очищаем от знаков препинания
    for w in raw_words 
    if len(w) > 0 and all(char in alphabet_letters for char in w.strip(" ,.!?()[]{}'\"-_@"))  # фильтруем по списку букв
]

word_freq = Counter(clean_words)  # считаем частоту уникальных слов
total_word_count = len(clean_words)  # создаем переменную с количеством слов

for word, freq in word_freq.items(): 
    percentage = (freq / total_word_count) * 100 if total_word_count > 0 else 0  # считаем частоту в процентах
    
    row = result_table.add_row()  # создаем новую строчку
    row.cells[0].text = word  # заполняем первую ячейку
    row.cells[1].text = str(freq)  # вторую ячейку
    row.cells[2].text = f"{percentage:.2f}"  # третью ячейку с округлением

table_doc.save('table.docx')  # сохраняем файл с таблицей

filtered_chars = ''.join([char for char in full_text.lower() if char in alphabet_letters])  # фильтруем текст по списку букв
char_freq = Counter(filtered_chars)  # считаем количество каждой буквы

sorted_chars = sorted(char_freq.keys())  # сортируем буквы по алфавиту
char_counts = [char_freq[char] for char in sorted_chars]  # получаем их частоты

plt.figure(figsize=(12, 6))  # задаем размер гистограммы
plt.bar(sorted_chars, char_counts, color='skyblue')  # строим столбчатую гистограмму

plt.xlabel('Буквы')  # подпись оси x
plt.ylabel('Количество')  # подпись оси y
plt.title('Количество строчных русских букв в тексте')  # заголовок графика
plt.grid(axis='y')  # сетка для удобства чтения

plt.tight_layout()  # автоподгонка макета
plt.show()  # отображаем график
