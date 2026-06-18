'''
modules :- It is nothing but python files that hav some python code written in it
            we can create our own modules by writing some programs, saving them as .py files and using
            them in another file
            
python has inbuild modules we use print(), id(), etc all these functions are part of the module which is
pre-impiorted
we can import module using the import keyword

'''
import random

# random() :- It returns random float between (included)0.0 - 1.0(excluded)
print(random.random())
print(random.random())

# randint(a, b) ==> It returns random int between a and b (both included)
print(random.randint(7, 100))
print(random.randint(1, 120000))

# choice(sequence) ==> It returns a random Item from the sequence
num = [10, 4, 1 ,8, 4, 3]
print(random.choice(num))

friuts = ["Apple", "Mango", "Orange"]
print(random.choice(friuts))

# shuffle(sequence) ==> It returns the elements shuffled in random order
num = [10, 4, 1 ,8, 4, 3]
print(random.shuffle(num)) # random.shuffle does not print anything it return none
print(num) # List is shuffled

friuts = ["Apple", "Mango", "Orange"] 
print(random.shuffle(friuts)) # random.shuffle does not print anything it return none
print(friuts) # List is shuffled
