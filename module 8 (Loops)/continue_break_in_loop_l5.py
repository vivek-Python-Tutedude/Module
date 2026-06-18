'''
continue & break are use to control the loop

coontinue :-  It skips the statements which are present after the continue statement inside the loop
                and proceeds with the next loop or next iteration
                
break :-  It basically makes the control flow go out of the loop when it trigger the break statement
        (It termineats or exit the loop)
'''

for num in range(10) :
    if num % 3 == 0 :
        continue
    print(num)

for num in range(1, 10) :
    if num % 3 == 0 :
        break
    print(num)