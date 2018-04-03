

class Type():

    def __init__(self, name, short_name, length=0):
        self.name = name
        self.short_name = short_name
        self.length = length

        if length is not 0:
            self.short_name += '[' + str(length) + ']'

    def __repr__(self):
        return self.name

class StringType(Type):

    def __init(self, domain, length):
        super(StringType, self).__init__(domain.name, domain.short_name)
        self.length = length


class Types(object):

    INT = Type('Liczba naturalna', 'Int')
    INT_POSITIVE = Type('Liczba naturalna dodatnia', 'Int+')
    INT_NEGATIVE = Type('Liczba naturalna ujemna', 'Int-')
    DATE = Type('Data', 'Date')
    STRING = Type('Łańcuch znaków', 'String', length=1024)
    BOOL = Type('Wartość logiczna', 'Bool')
