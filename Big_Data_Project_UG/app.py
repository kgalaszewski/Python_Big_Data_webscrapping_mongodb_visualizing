from WebScrapping import WebScrapper
from AppSettings import AppSettings
from DataAnalyzer import DataAnalyzer
from Utils import Utils
from MongoDbContext import DBContext
import _thread
import matplotlib.pyplot as plot


def execute_program(product1: str, product2: str, sample_size: int):
    # 0 clear db
    DBContext().drop_collection(product1)
    DBContext().drop_collection(product2)

    # 1 WEB SKRAPUJEMY
    drone_scrapper = WebScrapper()
    gopro_scrapper = WebScrapper()
    drone_values = drone_scrapper.read_product_info(product1, sample_size)
    gopro_values = gopro_scrapper.read_product_info(product2, sample_size)

    # 2 ZAPISUJEMY DO BAZY + Zczytujemy bo wymagane :=D :=D
    cena = 'cena produktu'
    ilosc_transakcji = 'ilość zamówień'


    drones_jsons = Utils.convert_to_json_pair_values(drone_values, cena, ilosc_transakcji)
    gopros_jsons = Utils.convert_to_json_pair_values(gopro_values, cena, ilosc_transakcji)

    db_context = DBContext()
    db_context.add_rows(drones_jsons, collection_name=product1)
    drones_from_db = db_context.get_all(collection_name=product1)

    db_context2 = DBContext()
    db_context2.add_rows(gopros_jsons, collection_name=product2)
    gopros_from_db = db_context2.get_all(collection_name=product2)


    # 4 Uzywamy na wykresiku
    drones_list = Utils.convert_jsons_to_tuples(drones_from_db, cena, ilosc_transakcji)
    gopros_list = Utils.convert_jsons_to_tuples(gopros_from_db, cena, ilosc_transakcji)
    DataAnalyzer.analyze_data(drones_list, cena, ilosc_transakcji, product1)
    DataAnalyzer.analyze_data(gopros_list, cena, ilosc_transakcji, product2)
    DataAnalyzer.run_analyzed_data_charts()


# Run the program :
product1_name = 'Drone'
product2_name = 'GoPro'
data_sample_size = 10

execute_program(product1_name, product2_name, data_sample_size)
