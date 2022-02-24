# При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"

class Volunteer:
    def __init__(self, name, city):
        self.name = name
        self.city = city


class InvitedPersons(Volunteer):
    def __init__(self, name, city, status):
        super().__init__(name, city)
        self.status = status

    def __str__(self):
        return f'{self.name}, г.{self.city}, статус: {self.status}'


n1 = InvitedPersons('Иванов Иван Иванович', 'Москва', 'Наставник')
n2 = InvitedPersons('Степанов Игорь Викторович', 'Луга', 'Стажёр')
n3 = InvitedPersons('Светлая Василиса Петровна', 'Воронеж', 'Волонтёр')

print(n1)
print(n2)
print(n3)