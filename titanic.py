import matplotlib.pyplot as plt  # для создания графика
import pandas as pd  # для работы с таблицами

df = pd.read_parquet('titanic.parquet')  # читаем данные
df.to_csv('titanic.csv', index=False)  # переделываем код в csv
df = pd.read_csv('titanic.csv')  # читаем csv файл

a = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)  # переделываем данные в таблицу

a.plot(kind='bar', stacked=True)  # строим гистограмму с объединенными столбцами

plt.title('Выживаемость пассажиров Титаника')  # заголовок
plt.xlabel('Класс билета')  # подпись оси x
plt.ylabel('Количество пассажиров')  # подпись оси y
plt.xticks(rotation=0)  # подписи классов горизонтальными
plt.legend(['Не выжил', 'Выжил'])  # цвета на гистограмме
plt.tight_layout()  # чтобы все поместилось
plt.show()  # вывод графика