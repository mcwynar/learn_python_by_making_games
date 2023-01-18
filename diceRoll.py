import random
from time import sleep, time


while True:
    number_of_meshes = []
    for i in range(5):
        number_of_meshes.append(random.randint(1, 6))
        print(number_of_meshes[i])
    start_time = time()
    inputValue = input()
    end_time = time()
    print(round(end_time-start_time, 1))
    if inputValue.isalpha():
        # print(type(inputValue))
        break
    else:
        if int(inputValue) == sum(number_of_meshes):
            print("To jest poprawna odpowiedz")
        else:
            print(f"Zla odpowiedz. Poprawna to {sum(number_of_meshes)}")
    sleep(1)



# print(number_of_meshes)
print("7".isalpha())
