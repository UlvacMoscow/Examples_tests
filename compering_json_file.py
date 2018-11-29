from deepdiff import DeepDiff
import pprint

""" Я себе облегчил задачу что не стал создавать два файла.json,
    Так надо было бы до них задавать пути и потом делать десериализации json.load(os.path.dirname(os.path.abspath(__file__)), file)
    И я понимаю что у нас схема json идентична, и нужно выявить только различия значений в одинаковых ключах"""


file_json1= {
          "data": [
            {
              "id": 1.0255789
            },
            {
              "id": 2.0008779
            },
            {
              "id": 2.5008789
            }
          ]
        }



file_json2= {
          "data": [
            {
              "id": 1.0255789
            },
            {
              "id": 2.0008779
            },
            {
              "id": 2.5008899
            }
          ]
        }



def values_json(file_json):
    temp = []
    for value in file_json['data']:
        temp.append(value['id'])
    return temp


def deepJson (json1, json2):
    a = values_json(json1)
    b = values_json(json2)
    return print(DeepDiff(a, b, significant_digits=5))


deepJson(file_json1, file_json2)
