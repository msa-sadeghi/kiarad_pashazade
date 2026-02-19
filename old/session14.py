# string = "hello"

# count_dict = {}
# for ch in string:
#     if ch not in count_dict:
#         count_dict[ch] = 1
#     else:
#         count_dict[ch] += 1

# print(count_dict)

# def تابع(شروع, پایان):
#     لیست = []
#     for عدد in range(شروع, پایان + 1):
#         لیست.append(عدد)

#     return لیست

# print(تابع(2,10))

class Character:
    def __init__(self, name,  health, ammo):
        self.name = name
        self.health = health
        self.ammo = ammo

    def move(self):
        print(f"{self.name} is moving")

    def shoot(self):
        print(f"{self.name} is shooting bullet")

class Player(Character):
    def __init__(self, name, health, ammo, bomb):
        super().__init__(name,  health, ammo)
        self.bomb = bomb

    def jump(self):
        print(f"{self.name} is jumping")

class Enemy(Character):
    def __init__(self, name, health, ammo, damage):
        super().__init__(name, health, ammo)
        self.damage = damage

    def find_player(self):
        print(f"{self.name} is going to find the player")
    



p1 = Player("mario", 5, 10, 5)
p1.move()
p1.shoot()
p1.jump()


e1 = Enemy("enemy1", 2, 4, 1)
e1.move()
e1.shoot()
e1.find_player()


