import calendar

from datetime import date

from datetime import datetime


dia = date.today().day
mes = date.today().month
ano = date.today().year

print(f'Data: {dia}/{mes}/{ano}')

#for mes in range(12):
 #   print(calendar.month(date.today().year, mes +1))
    
print(calendar.month(1972, 5))

print(date.today().day)
print(date.today().month)
print(date.today().year)
print(date.today())

# Obtendo a data atual
data_atual = datetime.now()

# Formatando a data no formato brasileiro
data_formatada = data_atual.strftime("%d/%m/%Y")

print("Data formatada:", data_formatada)
print("Data atual: ", data_atual)



