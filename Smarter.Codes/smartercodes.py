import json


def do_recursion(c, count):
    for sub_child in c:
        if sub_child["selected"] == 1:
            if count/2 == 0:
                count = (count*2)+1
            else:
                count *= 2
            print("-" * (count+1) + ">" + sub_child["name"])
            do_recursion(sub_child["children"], count)
        else:
            continue


d = json.load(open('foodyo_output.json'))
root = d["body"]["Recommendations"]
for i in root:
    print(i["RestaurantName"])
    for menu in i['menu']:
        if menu["type"] == 'sectionheader':
            for child in menu["children"]:
                if child["type"] == 'item' and child["selected"] == 1:
                    print("-->"+child["name"])
                    do_recursion(child["children"], 2)
                else:
                    continue
        else:
            continue

