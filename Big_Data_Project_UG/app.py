from WebScrapping import WebScrapper
from AppSettings import AppSettings
from DataAnalyzer import DataAnalyzer
from Utils import Utils
from MongoDbContext import DBContext
import _thread
import matplotlib.pyplot as plot


drones = 'Drone'
gopros = 'GoPro'

# 0 clear db
DBContext().drop_collection(drones)
DBContext().drop_collection(gopros)

# 1 WEB SKRAPUJEMY
drone_scrapper = WebScrapper()
gopro_scrapper = WebScrapper()
drone_values = drone_scrapper.read_product_info(drones, 10)
gopro_values = gopro_scrapper.read_product_info(gopros, 10)

# 2 ZAPISUJEMY DO BAZY + Zczytujemy bo wymagane :=D :=D
cena = 'cena produktu'
ilosc_transakcji = 'ilość zamówień'


drones_jsons = Utils.convert_to_json_pair_values(drone_values, cena, ilosc_transakcji)
gopros_jsons = Utils.convert_to_json_pair_values(gopro_values, cena, ilosc_transakcji)

db_context = DBContext()
db_context.add_rows(drones_jsons, collection_name=drones)
drones_from_db = db_context.get_all(collection_name=drones)

db_context2 = DBContext()
db_context2.add_rows(gopros_jsons, collection_name=gopros)
gopros_from_db = db_context2.get_all(collection_name=gopros)


# 4 Uzywamy na wykresiku
drones_list = Utils.convert_jsons_to_tuples(drones_from_db, cena, ilosc_transakcji)
gopros_list = Utils.convert_jsons_to_tuples(gopros_from_db, cena, ilosc_transakcji)
DataAnalyzer.analyze_data(drones_list, cena, ilosc_transakcji, drones)
DataAnalyzer.analyze_data(gopros_list, cena, ilosc_transakcji, gopros)
DataAnalyzer.run_analyzed_data_charts()