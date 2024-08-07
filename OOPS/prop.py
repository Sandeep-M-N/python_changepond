class Arithmatic:
    def __init__(self,value):
        self._value=value #protected attribute
    @property
    def Value1(self):
        print("to retrive the value of \'_value\'")
        return self._value
    @Value1.setter
    def setValue(self,value):
        print("setting value to ",value) #new value/updated
        self._value=value
    @Value1.deleter
    def delvalue(self):
        print("deleting the value")
        del self._value

    # value=property(getValue,setValue,delvalue)

A1=Arithmatic()
print(A1.setValue(12))

# A1.value=13
# print(A1.value)