
dict_list =[{"a":123,"b":34},{"a":123,"b":334},{"a":12,"b":334},{"a":128,"b":334},{"a":133,"b":334}]

#for l in len:
i=0
final_dict_list = list()
new_list = list()
while i<len(dict_list):
  new_dict = dict()
  new_dict["a"] = dict_list[i]["a"]
  new_dict["b"] = dict_list[i]["b"]
  new_dict["items"] = list()
  item_dic = dict()
  item_dic["z"] = dict_list[i]["b"]
  new_dict["items"].append(item_dic)
  new_list.append(new_dict)
  i = i+1


print(new_list)
index = 0
jindex = index +1
while index<len(new_list):
  while jindex < len(new_list):
    if new_list[index]["a"] == new_list[jindex]["a"]:
      new_list[index]["items"].append(new_list[jindex]["items"][0])
      jindex = jindex+1








