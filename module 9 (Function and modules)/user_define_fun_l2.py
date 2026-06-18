def greeting() :
    print("Hello. good morning!")
    print("It's beautiful day")

greeting()  # calling function
greeting()
greeting()



def greeting(name) : # passing the argument
    print(f"Hello {name}, good morning!")
    print("It's beautiful day")

greeting("vivek")  # calling function
greeting("akash")
greeting("aana")


def even_odd(no) :
    if no % 2 == 0 :
        print(f"{no} is even no.")
    else :
        print(f"{no} is odd no.")
even_odd(4)
even_odd(7)

def add(a,b) :
    print(f"additon of {a} and {b} is: ",a+b)

add(5,-9)
add(1000,1760)