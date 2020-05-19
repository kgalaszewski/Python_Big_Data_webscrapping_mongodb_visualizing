from WebScrapping import WebScrapper
from AppSettings import AppSettings
from DataAnalyzer import DataAnalyzer
from Utils import Utils
from MongoDbContext import DBContext
import _thread
import matplotlib.pyplot as plot


# drones = 'Drony'
# gopros = 'GoPros'

# # 0 clear db
# DBContext().drop_collection(drones)
# DBContext().drop_collection(gopros)

# # 1 WEB SKRAPUJEMY
# scrapper = WebScrapper()
# drone_values = scrapper.read_product_info('Drone', 10)
# gopro_values = scrapper.read_product_info('GoPro', 10)

# # 2 ZAPISUJEMY DO BAZY + Zczytujemy bo wymagane :=D :=D
# cena = 'cena'
# ilosc_transakcji = 'ilosc_transakcji'


# drones_jsons = Utils.convert_to_json_pair_values(drone_values, cena, ilosc_transakcji)
# gopros_jsons = Utils.convert_to_json_pair_values(gopro_values, cena, ilosc_transakcji)

# db_context = DBContext()
# db_context.add_rows(drones_jsons, collection_name=drones)
# drones_from_db = db_context.get_all(collection_name=drones)

# db_context2 = DBContext()
# db_context2.add_rows(gopros_jsons, collection_name=gopros)
# gopros_from_db = db_context2.get_all(collection_name=gopros)


# # 4 Uzywamy na wykresiku
# drones_list = Utils.convert_jsons_to_tuples(drones_from_db, cena, ilosc_transakcji)
# gopros_list = Utils.convert_jsons_to_tuples(gopros_from_db, cena, ilosc_transakcji)
# DataAnalyzer.analyze_data(drones_list, cena, ilosc_transakcji, drones)
# DataAnalyzer.analyze_data(gopros_list, cena, ilosc_transakcji, gopros)


import pandas
multiple_series = {
    'x_name': pandas.Series([1, 3], index=['a', 'b']),
    'y_name': pandas.Series([2, 4], index=['a', 'b'])
}
multiple_series2 = {
    'x_name': pandas.Series([3, 2], index=['a', 'b']),
    'y_name': pandas.Series([1, 2], index=['a', 'b'])
}
data_frame = pandas.DataFrame(multiple_series)
data_frame2 = pandas.DataFrame(multiple_series2)
data_frame.plot(x='x_name', y='y_name', kind='bar', title='title', subplots=True)
data_frame2.plot(x='x_name', y='y_name', kind='bar', title='title', subplots=True)
plot.show()

