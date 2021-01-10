# dslr
проект школы 21 - посвящен анализу данных и построению логистической регрессии

## Суть проекта
Нужно сделать цифровой аналог распределительной шляпы из вселенной Гарри Поттера. Сам проект разбит на 3 части

### Часть 1
Сделать аналог функции describe из pandas - высчитывать перцентили, мат. ожидание, дисперсию и т.д.

### Часть 2
Поработать с визуализацией данных:  
- построить гистограмму фичей с гомогенным распределением (перед этим нужно отнормировать данные: можно через z-оценку, можно min-max нормализацию)
- определить одинаковые фичи (там будет видна прямая зависимость)
- вывести scatter_plot_matrix для определения признаков, по которым можно классификацию выстроить 

### Часть 3
Построение логистической регрессии по типу "один против всех" и будет состоять из 2 программ:
- программа для построения весов на тренировочном датасете. Работает всё на градиентном спуске. Из специфики: в тренировочном датасете есть пропуски - их пропускаем (дропаем). После работы вписывает веса отдельный файл.
- программа для прогнозирования факультетов на тестовом датасете. Данные вписываются в отдельный файл. При проверке с помощью скрипта и датасета с реальными факультетами будут смотреть точность: должна быть от 98%.

### Часть 4
Это бонус. Программа, которая по ответам пользователя предсказывает факультет, который подошёл бы ему. Перед этим файл с весами должен уже быть создан. 
## изображения факультетов используются в некоммерческих целях

