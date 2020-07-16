# Напишите функцию который будет определять введенный год, 
# високосный или нет.

god = int(input())
if (god % 4 == 0 and god % 100 != 0):
    print(" Vysokosnyi")
else:
    print("Obychnyi")