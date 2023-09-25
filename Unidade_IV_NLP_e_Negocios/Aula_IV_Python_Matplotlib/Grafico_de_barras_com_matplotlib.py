import matplotlib.pyplot

meses = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
         ]
consumo = [800, 600, 650, 650, 700, 1000, 1400, 900, 950, 1200, 800, 1300]
matplotlib.pyplot.bar(meses, consumo)
matplotlib.pyplot.title('Consumo de chocolate no último ano')
matplotlib.pyplot.xlabel('Meses')
matplotlib.pyplot.ylabel('Consumo')
matplotlib.pyplot.show()
