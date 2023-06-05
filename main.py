import sys
import functions

print('*' * 70)
print('q, uznai weather, if hochesh exit to Enter!')
print('*' * 70)

while True:
    q = input('Введите название города ')
    if not q:
        sys.exit('До свидания!')
        break
    else:
        weather = functions.get_weather(q)
        functions.print_weather(weather)
        functions.save_excel(weather)




