# Nested list => List inside another  list

l1 = [7, 1.6, "Python", True, None, [1, 2, 3], 10]
print("len of list: ", len(l1))
print(l1[-2][0])
print(l1[-2])


# list inside the list
l2 = [[1, 2], [3, 4], [5, 6, [7, 8]]]
print(len(l2))
print(f"when we have to fetch 8 :{l2[-1][2][1]}")