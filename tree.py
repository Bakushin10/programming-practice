from treelib import Node, Tree
tree = Tree()
dates = [
    "2018/11/12 9:21:05",
    "2018/11/12 9:22:05",
    "2018/11/12 9:23:05",
    "2018/11/12 10:21:05",
    "2018/11/12 11:65:05",
    "2018/11/12 11:45:05",
    "2018/11/13 10:21:05",
    "2018/11/13 11:65:05",
    "2018/11/13 11:45:05",
    ]

for d in range(len(dates)):
    date = dates[d][0:10]
    print(date)

tree.create_node("Harry", "harry")  # root node
tree.create_node("Jane", "jane", parent="harry")
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")
tree.show()