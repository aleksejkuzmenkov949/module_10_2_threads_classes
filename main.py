import threading
import time

class Knight(threading.Thread):
    enemies = 100  # количество врагов, общая для всех рыцарей

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while Knight.enemies > 0:
            time.sleep(1)  # задержка в 1 секунду
            Knight.enemies -= self.power
            self.days += 1
            if Knight.enemies < 0:  # если врагов меньше 0, устанавливаем в 0
                Knight.enemies = 0
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {Knight.enemies} воинов.")


# Создание и запуск потоков
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
