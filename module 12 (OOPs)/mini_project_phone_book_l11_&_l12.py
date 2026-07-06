class Contact :
    ph_directory = []
    
    def __init__(self, name, ph_no):
        self.name = name
        self.ph_no = ph_no
        Contact.ph_directory.append(self)
        
        
    def show_contact(self):
        return f"Name : {self.name}, Contact no : {self.ph_no}"
    
    @classmethod
    def show_all_contact(cls) :
        if len(cls.ph_directory) == 0 :
            print("No contacts found in the directory!")
        else :
            for contact in cls.ph_directory:
                print("All contact from the directory")
                #print(contact) # it will give the object not name and no
                print(contact.show_contact())
    
    @classmethod
    def search_contact(cls, search_nm) :
        for contact in cls.ph_directory :
            if contact.name.lower() == search_nm.lower() :
                return contact.name
        return f"No contact found for {search_nm}"
    @staticmethod
    def validation_ph_no(no):
        if len(no) >= 8 and no.isdigit():
            return True
        else:
            return False        
        
'''
c1 = Contact("vivek", 1111111111)
c2 = Contact("akash", 2222222222)

"""
print(Contact.ph_directory) # [<__main__.Contact object at 0x00000120DAD94980>, <__main__.Contact object at 0x00000120DAD847D0>]
# above we created the 2 obj and print it
print("\n---------------------------")

print(c1.show_contact())

print("\nCalling using the objnm ---------------------------")

c1.show_all_contact()

print("\nCalling using the class_nm---------------------------")

Contact.show_all_contact()

"""

c3 = Contact("Rohit", 6666666666)

print(c3.search_contact("rohit"))
print(Contact.search_contact("Vivek"))
print(Contact.search_contact("vishal"))

'''

n_contacts = int(input("Hoe many contacts do you want to add? : "))

for i in range(n_contacts):
    name = input("Enter the name of the contact: ")
    ph_no =  input("Enter the Ph_no: ")
    if Contact.validation_ph_no(ph_no):
        Contact(name, ph_no)
    else:
        print(f"Invalid ph_no for {name}, ph_no shoulde be at least 8 digits and it only contain number")
        
        
Contact.show_all_contact()