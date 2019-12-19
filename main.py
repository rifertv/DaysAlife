from datetime import datetime

birthdate = input("Введите дату рождения(день_месяц_год): ")
convert = datetime.strptime(birthdate, "%d_%m_%Y")
today = datetime.now()
days = today - convert

print("Вы живете " + str(days.days) + " дней.")

