import matplotlib.pyplot as plt
import pandas as pd

pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', 30)

pd.set_option('display.width', 1000)
google_play = pd.read_csv('googleplaystore.csv', encoding='latin-1')


bar_graph_plot = plt.figure(figsize=(15, 8))
bar_graph = bar_graph_plot.add_subplot()
bar_graph.set_xlabel('название приложения')
bar_graph.set_ylabel('рейтинг')
bar_graph.set_title('топ приложения google play')
best_rating = google_play.sort_values('Rating', ascending=False).sort_values('Installs', ascending=False).head(7)
labels = list(best_rating['App'])[1:]
labels_rating = list(best_rating['Rating'])[1:]
bar_graph.bar(labels, labels_rating)
print('Первый график показывает, что самым популярным приложением в google play является', labels[0])

pie_graph_plot = plt.figure(figsize=(15, 8))
pie_graph = pie_graph_plot.add_subplot()
pie_graph.set_title('самые популярные категории приложений')
popular_categories = dict(google_play.value_counts('Category').head(8))
pie_graph.pie(list(popular_categories.values()), labels=list(popular_categories.keys()), autopct='%1.1f%%')
print('Второй график показывает, что самыми популярными категориями являются Family, Game и Tools')


pie_graph_content_rating_plot = plt.figure(figsize=(15, 8))
pie_graph_content_rating = pie_graph_content_rating_plot.add_subplot()
pie_graph_content_rating.set_title('самые популярные возрастные ограничения приложений')
popular_categories = dict(google_play.value_counts('Content Rating').head(4))
pie_graph_content_rating.pie(list(popular_categories.values()), labels=list(popular_categories.keys()),
                             autopct='%1.1f%%')
print('Третий график показывает, что самыми популярными возрастными ограничениями являются Everyone и Teen')



barh_graph_plot = plt.figure(figsize=(15, 8))
barh_graph = barh_graph_plot.add_subplot()
barh_graph.set_xlabel('количество приложений')
barh_graph.set_ylabel('тип приложения(бесплатное/платное)')
barh_graph.set_title('количество платных и бесплатных популярных приложений в google play')
free_paid = dict(google_play.value_counts('Type'))
barh_graph.barh(list(free_paid.keys())[:-1], list(free_paid.values())[:-1])

print('Четверный график показывает, что популярных бесплатных приложений гораздо больше, чем популярных платных')

plt.show()
