#média simples
Lista = [11, 12, 13, 15, 16, 17]
from statistics import mean as Media
#print(f'Media: { Media(Lista) }')
#print(f'Media: { (11+12+13+15+16+17) / len(Lista) } ')

# Periodo da média móvel
n = 5
for Intervalo in range(3):
  print(f'{Intervalo}ª Dia: { sum(Lista[Intervalo:n]) / 5 }')
#formula média movel
    #MMA = Soma dos preços de fechamento ÷ Número de dias