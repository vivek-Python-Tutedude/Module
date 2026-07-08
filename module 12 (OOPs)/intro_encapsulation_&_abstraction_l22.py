'''
Data Hiding / Encapsulation
Encapsulation is a core OOP principle that involves bundling data (attributes) and the
methods that operate on that data within a single unit (a class). It also implies data hiding,
which restricts direct access to some of an object's components.

# Concept of Encapsulation

 Bundling: Combining attributes and methods into a single class. This is achieved
naturally by defining attributes in __init__ and methods within the class.

 Data Hiding (Information Hiding): The idea of protecting the internal state of an
object from direct external access. This prevents accidental corruption of data and
ensures that the object's internal logic is consistent.

o Instead of direct access (object.attribute = value), data should ideally be
accessed or modified through public methods (often called getters and setters).

o This provides a controlled interface to the object's data, allowing for
validation, logging, or other logic to be executed when data is accessed or changed.

8.2 Data Hiding in Python (by Convention)

Unlike languages like Java or C++ that have keywords like private or protected, Python
does not have strict access modifiers. Instead, it relies on conventions and a mechanism
called "name mangling."

'''

'''
1. Public Attributes (No Underscore):
 Attributes without any leading underscores are considered public. They can be
accessed and modified directly from anywhere.

 This is the default and most common in Python.
example as shown below
'''
class PublicExample:
    def __init__(self, value):
        self.public_attribute = value
        
        
obj = PublicExample(10)
print(obj.public_attribute) # Accessible

obj.public_attribute = 20 # Modifiable
print(obj.public_attribute)

'''
2. "Protected" Attributes (Single Underscore _name):
 Attributes prefixed with a single underscore (e.g., _protected_attribute) are a
convention to indicate that they are "protected" or "internal use only."

 Python does not prevent direct access or modification of these attributes. It's a hint to
other developers: "Don't touch this directly unless you know what you're doing."
example as shown below
'''
class ProtectedExample:
    def __init__(self, value):
        self._protected_attribute = value # Convention for "protected"
        
        
obj = ProtectedExample(10)
print(obj._protected_attribute) # Still accessible, but convention says don't

obj._protected_attribute = 20 # Still modifiable
print(obj._protected_attribute)

'''
3. "Private" Attributes (Double Underscore __name - Name Mangling):
 Attributes prefixed with two leading underscores (e.g., __private_attribute)
trigger name mangling.

 Python internally renames these attributes to _ClassName__private_attribute.
This makes them harder, but not impossible, to access directly from outside the class.
It's a way to avoid naming conflicts in inheritance.

 They are still technically accessible by their mangled name, but it's strongly
discouraged.
example as shown below
'''

class PrivateExample:
    def __init__(self, value):
        self.__private_attribute = value # Triggers name mangling
        
    def get_private(self):
        return self.__private_attribute
    
obj = PrivateExample(10)
# print(obj.__private_attribute) # This will cause an AttributeError
print(obj.get_private()) # Accessible via method
# Output: 10
# Accessing via mangled name (not recommended)
print(obj._PrivateExample__private_attribute)
# Output: 10
obj._PrivateExample__private_attribute = 20
print(obj.get_private())
# Output: 20

'''
Summary on Data Hiding in Python: Python's philosophy is "we're all consenting adults."
It provides mechanisms to indicate intent (like _ and __), but ultimately trusts developers to
respect conventions.
'''
