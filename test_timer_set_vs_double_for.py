from time import perf_counter

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


file_list1 = file_json1["data"]
file_list2 = file_json2["data"]

def equals_element_massive(a, b):
    for element in b:
      if element['id'] == a:
        return True
    return False
start1 = perf_counter()
for element in file_list1:
    print(equals_element_massive(element['id'], file_list2))
end1 = perf_counter()
print(end1 - start1)

def set_genius(a, b):
    a1 = set()
    b1 = set()
    for num in range(len(a)):

      a1.add(a[num]['id'])
      b1.add(b[num]['id'])
    if len(a1) == len(a1.union(b1)):
      return True
    return False
start2 = perf_counter()
set_genius(file_list1, file_list2)
end2 = perf_counter()
print(end2 - start2)

print((end1 - start1) / (end2 - start2))
