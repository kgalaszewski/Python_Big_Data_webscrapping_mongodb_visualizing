import numpy
import pandas
import matplotlib.pyplot as plot
from typing import List

class DataAnalyzer:
    @classmethod
    def analyze_data(cls, values_collection: List[tuple], x_axis_name: str, y_axis_name: str, title: str):
        if not values_collection:
            print('Collection can not be empty')
            return
        x_axis_collection = []
        y_axis_collection = []

        for record in values_collection:
            x_axis_collection.append(record[0])
            y_axis_collection.append(record[1])

        cls.__generate_plot(x_axis_collection, y_axis_collection, x_name=x_axis_name, y_name=y_axis_name, title=title)


    @classmethod
    def __generate_plot(cls, x_collection: list, y_collection: list, x_name: str, y_name: str, title: str):
        if not x_collection or not y_collection:
            print('Not enough data to analyze')
            return
        multiple_series = {
            x_name: pandas.Series(x_collection, index=[i for i in range(len(x_collection))]),
            y_name: pandas.Series(y_collection, index=[i for i in range(len(y_collection))])
        }
        data_frame = pandas.DataFrame(multiple_series)
        data_frame.plot(x=x_name, y=y_name, kind='bar', title=title)
        plot.show()
