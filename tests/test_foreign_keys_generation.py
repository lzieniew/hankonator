from base import Entity, Attribute, Types, Erd, Relationship, add_foreign_keys


def get_erd():
    erd = Erd()

    e1 = Entity('Arkusz', 'Arkusze', [Attribute('IdA', Types.INT, True,
                                                'Unikalny identyfikator Arkusza nadawany automatycznie przez system, np. 1. '),
                                      Attribute('Ocena', Types.INT_POSITIVE, False,
                                                'Ilość punktów zdobyta przez uczestnika konkursu wprowadzana przez sprawdzającego, np. 30.')])
    e2 = Entity('Pytanie', 'Pytania', [Attribute('IdP', Types.INT, True,
                                                 ' Unikalny identyfikator Pytania nadawany automatycznie przez system, np. 4. '),
                                       Attribute('Pytanie', Types.STRING, False,
                                                 'Treść pytania, np. Co oznacza skrót FIFO?'),
                                       Attribute('Odpowiedź', Types.STRING, False,
                                                 '(ang. First in, First out) żądania są przetwarzane sekwencyjnie wg kolejki.')])
    e3 = Entity('Uczestnik', 'Uczestnicy', [Attribute('NrAlbumu', Types.INT, True,
                                                      'Unikalny identyfikator Uczestnika nadawany automatycznie przez system, np. 3. '),
                                            Attribute('Nazwisko', Types.STRING, False,
                                                      'Nazwisko uczestnika, np. Kowalski. '),
                                            Attribute('Imię', Types.STRING, False, 'Imię uczestnika, np. Adam. ')])
    e4 = Entity('Konkurs', 'Konkursy', [Attribute('IdK', Types.INT, True,
                                                  'Unikalny identyfikator Konkursu nadawany automatycznie przez system, np. 2. '),
                                        Attribute('Nazwa', Types.STRING, False, 'Nazwa konkursu, np.  Electron.'),
                                        Attribute('Data', Types.DATE, False,
                                                  'Data realizacji konkursu, np. 14/05/2018.')])
    e5 = Entity('Organizator', 'Organizatorzy', [Attribute('IdO', Types.INT, True,
                                                           'Unikalny identyfikator Organizatora nadawany automatycznie przez system, np. 6. '),
                                                 Attribute('Nazwisko', Types.STRING, False,
                                                           'Nazwisko organizatora, np. Szymański.'),
                                                 Attribute('Imię', Types.STRING, False,
                                                           'Imię organizatora, np. Dawid.')])
    e6 = Entity('Sprawdzający', 'Sprawdzający', [Attribute('IdS', Types.INT, True,
                                                           'Unikalny identyfikator Sprawdzającego nadawany automatycznie przez system, np. 5.'),
                                                 Attribute('Nazwisko', Types.STRING, False,
                                                           'Nazwisko sprawdzającego, np. Nowak.'),
                                                 Attribute('Imię', Types.STRING, False,
                                                           'Imię sprawdzającego, np. Mateusz')])
    e7 = Entity('PytanieNaArkuszu', 'PytaniaNaArkuszu',
                [Attribute('IdPnA', Types.INT, True, 'Unikalny identyfikator PytaniaNaArkuszu, np. 70.')],
                is_strong=True)

    erd.entities = [e1, e2, e3, e4, e5, e6, e7]

    r1 = Relationship('NależyDo', left_entity='Konkurs', left_quantity='1,1', right_entity='Arkusz',
                      right_quantity='0,N')
    r2 = Relationship('Zawiera', left_entity='Arkusz', left_quantity='1,1', right_entity='PytanieNaArkuszu',
                      right_quantity='0,N')
    r3 = Relationship('Uczestniczy', left_entity='Konkurs', left_quantity='1,1', right_entity='Uczestnik',
                      right_quantity='0,N')
    r4 = Relationship('Wypełnia', left_entity='Arkusz', left_quantity='0,N', right_entity='Uczestnik',
                      right_quantity='0,1')
    r5 = Relationship('Jest', left_entity='Pytanie', left_quantity='1,1', right_entity='PytanieNaArkuszu',
                      right_quantity='0,N')
    r6 = Relationship('Tworzy', left_entity='Arkusz', left_quantity='0,N', right_entity='Organizator',
                      right_quantity='1,1')
    r7 = Relationship('Sprawdza', left_entity='Sprawdzający', left_quantity='0,1', right_entity='Arkusz',
                      right_quantity='0,N')

    erd.relationships = [r1, r2, r3, r4, r5, r6, r7]

    return erd


def test_creation():
    erd = get_erd()
    assert erd is not None
    assert erd.entities
    assert erd.relationships

def test_add_foreign_keys():
    erd = get_erd()
    add_foreign_keys(erd)
    assert erd.entities[0].foreign_keys

def test_foreign_keys_values():
    erd = get_erd()
    add_foreign_keys(erd)

