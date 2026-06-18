scores = [2, 45, 102, 4, 9, 12, 45, 90, 1, 0, 1]
s = 0
for i in scores:
    s = i + s
print(f"Total Score is : {s}")

s = sum(scores)
print(f"Total Score is : {s}")

m = 0
for i in scores :
    if i > m :
        m = i
print(f"Highest Score is : {m}") 

print(max(scores))



l = scores[0]
for i in scores :
    if i < l :
        l = i
print(f"lowest Score is : {l}") 

print(min(scores))    

