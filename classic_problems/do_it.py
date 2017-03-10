# Implement a function DoIt( o,a ) such that the following code:
# Object o = SomeClass()
# O.first = 'fizz'
# O.second = 'buzz'
#
# print DoIt( o, 'first)
# print DoIt(o, 'second')

class SomeClass():
    def __init__(self):
        self.first = ""
        self.second = ""

def DoIt(obj, string):
    if string == "first":
        return obj.first
    elif string == "second":
        return obj.second

o = SomeClass()
o.first= "fizz"
o.second = "buzz"

print DoIt(o, 'first')
print DoIt(o, 'second')
