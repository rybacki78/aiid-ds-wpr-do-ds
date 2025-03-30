# klasa i obiekt
# definicja pustej klasy
class Player:
    pass

p1 = Player()


print(type(p1))
# czy klasa Player jest klasą potomną klasy object
print(issubclass(Player, (object)))
# jest też jednocześnie instancją klasy Player oraz object
print(isinstance(p1, (object, Player)))