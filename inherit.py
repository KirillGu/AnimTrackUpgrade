class Animals:
    def __init__(self, name, weight, sound):
        self.name = name
        self.weight = weight
        self.sound = sound


class Milk:
    milk = 10

class Eggs:
    eggs = 10

class Cow(Animals, Milk):
    type_animal = 'Корова'





class Ducks(Animals, Eggs):
    type_animal = 'Утка'





class Geese(Animals, Eggs):
    type_animal = 'Гусь'





class Goats(Animals, Milk):
    type_animal = 'Коза'





class Hens(Animals, Eggs):
    type_animal = 'Курица'





class Sheep(Animals):
    type_animal = 'Баран'
    wool = 10




class Far:
    def __init__(self, farm):
        self.farm = farm

    def get_heavy(self):
        heavy = ''
        max_weight = 0

        for item in self.farm:
            if item.weight > max_weight:
                max_weight = item.weight
                heavy = f"{item.type_animal} {item.name}"

        return f"Самый большой вес {max_weight} кг имеет {heavy}"

    def give_milk(self):
        for item in self.farm:
            item.milk -= 1
        return f'{item.milk} литров у - {item.name} , {horns.milk} литров у - {horns.name} , {manka.milk} литров у - {manka.name}'

    def eat(self):
        for item in self.farm:
            item.weight += 1
        return f'Вы покормили животных'


horns = Goats('Рога', 88 , "беее")
hooves = Goats('Копыта', 89, "беее")
manka = Cow('Манька', 260, "мууу")
koko = Hens('Ко-ко', 1, "кококо")
kukareku = Hens('Кукареку', 3, "кококо")
mallard = Ducks('Кряква', 6, "кря")
baa_lamb = Sheep('Барашек', 90, "меее")
curly = Sheep('Кудрявый', 101, "меее")
gray = Geese('Серый', 4, "гага")
white = Geese('Белый', 7, "гага")

my_farm = {horns, baa_lamb, koko, hooves, mallard, curly, kukareku, manka, gray, white}

all_sound = {horns.sound, baa_lamb.sound, koko.sound, hooves.sound, mallard.sound, curly.sound, kukareku.sound, manka.sound, gray.sound}

milk_giv = {horns, hooves, manka}


mil_far = Far(milk_giv)
finish_farmer = Far(my_farm)
print(finish_farmer.get_heavy())
print(all_sound)
print(mil_far.give_milk())
print(finish_farmer.eat())
print(f'{gray.name} стал весить:{gray.weight}кг и он доволен')
