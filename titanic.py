import matplotlib.pyplot as plt  # для создания графика
import pandas as pd  # для работы с таблицами

titanic_df = pd.read_parquet('titanic.parquet')  # читаем данные
titanic_df.to_csv('titanic.csv', index=False)  # переделываем код в csv
titanic_df = pd.read_csv('titanic.csv')  # читаем csv файл

survival_table = titanic_df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)  # переделываем данные в таблицу

survival_table.plot(kind='bar', stacked=True)  # строим гистограмму с объединенными столбцами

plt.title('Выживаемость пассажиров Титаника')  # заголовок
plt.xlabel('Класс билета')  # подпись оси x
plt.ylabel('Количество пассажиров')  # подпись оси y
plt.xticks(rotation=0)  # подписи классов горизонтальными
plt.legend(['Не выжил', 'Выжил'])  # цвета на гистограмме
plt.tight_layout()  # чтобы все поместилось
plt.show()  # вывод графика
