time_1 = input("Введите первый временной промежуток в формате HH:MM : ")
time_2 = input("Введите второй временной промежуток в формате HH:MM : ")

time_1 = time_1.split(":")
time_2 = time_2.split(":")
try:
    time_1_in_min = int(time_1[0])*60 + int(time_1[1])
    time_2_in_min = int(time_2[0])*60 + int(time_2[1])
except:
    print("Ошибка")
else:
    if time_1_in_min < time_2_in_min:   
        print("Временной промежуток в минутах =" +str(time_2_in_min - time_1_in_min))
    else:
        print("Временной промежуток в минутах =" + str(time_1_in_min - time_2_in_min))
