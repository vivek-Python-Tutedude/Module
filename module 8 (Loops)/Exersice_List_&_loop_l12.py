# count all countries which are starting with "I"
# print all these contries
countries = ["India", "United states", "Australia", "Ireland", "Sri lanka", "Iceland", "Cube", "Iran", "Poland"]

counter = 0
output = []
for i in countries :
    if i[0] == 'I'  :
        counter = counter + 1
        output.append(i)
print(f"The no of country are strating with I is: {counter}")
print(f"Lists of coutries is : {output}")


'''
# 2nd method
for i in countries :
    if i.startswith('I') :
        counter = counter + 1
        print(i)
print(f"The no of country are strating with I is: {counter}")
print(f"Lists of coutries is : {output}")
'''