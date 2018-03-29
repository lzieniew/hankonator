

class Domain():

    def __init__(self, name, short_name):
        self.name = name
        self.short_name = short_name

class StringDomain(Domain):

    def __init(self, domain, length):
        super(StringDomain, self).__init__(domain.name, domain.short_name)
        self.length = length


class Domains(object):

    INT = Domain('Liczba naturalna', 'Int')
    INT_POSITIVE = Domain('Liczba naturalna dodatnia', 'Int+')
    INT_NEGATIVE = Domain('Liczba naturalna ujemna', 'Int-')
    DATE = Domain('Data', 'Date')

    @staticmethod
    def STRING(length):
        return StringDomain(Domain(u'Łańcuch znaków', 'String[' + repr(length) + ']'), length)