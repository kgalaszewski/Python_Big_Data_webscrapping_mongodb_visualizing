from typing import List

class Utils:
    @classmethod
    def convert_to_json_pair_values(cls, values: List[tuple], first_name: str, second_name: str) -> List[object]:
        if not values:
            print('Can not convert empty list')
            return

        json_result = []

        for row in values:
            json = {
                first_name : row[0],
                second_name : row[1]
            }
            json_result.append(json)

        return json_result


    @classmethod
    def convert_jsons_to_tuples(cls, values: List[object], xx: str, yy: str) -> List[tuple]:
        if values:
            return list(map(lambda x: (float(x[xx].replace(' ','').replace(',','.')), int(x[yy])), values))

