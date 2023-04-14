import datetime, random, numpy
position = 0
field = []
score = 0

health_potion = "health_potion"
enemy = "enemy"
empty = "empty"
health = 10
print("Введите размер игрового поля")
start = int(input())
items = [health_potion, enemy, empty]
command = ''
while start <= 4:
    print("Список шибко коротний")
    start = int(input())
def gen_field():
    global field
    field.clear()
    for i in range(start):
        rand_val = numpy.random.choice(items, p=[0.25, 0.2, 0.55])
        field.append(rand_val)
gen_field()
print(field)

print("Введите свою команду")

while command != "конец":
    a = input()
    parsed_data = a.split()
    command = parsed_data[0]
    args = parsed_data[1:]
    
    if command == "пошути":
        print('Когда узнал, что твою машину угнали стало спокойнее, ведь труп в багажнике больше не твоя проблема')
    elif command == 'погода':
        print('Оч жарко, аж +361 градус по фаренгейту')
    elif command == 'время':
        print('сейчас', datetime.datetime.now())

        
    elif command == "список":
        print(field)
    elif command == "игрок":
        print(str(health) + " очков здоровья", str(score) + " очков","позиция " + str(position), sep = '\n')

    elif command == 'походить':
        if int(args[0]) > 0:
            position += int(args[0])
            if position >= len(field):
                position %= len(field)
                gen_field()
        else:
            print("Кажется ты не понял, Идти можно только вперед")
        
        if field[position] == health_potion:
            health += random.randint(2, 4)
        elif field[position] == enemy:
            health += random.randint(-10, -5)
            score += random.randint(3, 6)
        elif field[position] == empty:
            pass
        print(position)
        print(field)
        if health <= 0:
            print('You Died', 'Результат забега', score)
            break

    else:
        print('Я пока слишком глупенький, чтобы понимать чтото больше заданных команд, задонатьте разрабу и быть может эта ленивая жопа чтото сделает')
