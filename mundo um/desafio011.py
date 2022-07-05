largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

areaDaParede = largura * altura
# 1 litro de tinta pinta 2 metros quadrado
tintaNecessaria = areaDaParede * 2

print('Você vai preciar de {:.2f} litros de tinta para pintar uma area de {:.2f} metros quadrado'.format(tintaNecessaria, areaDaParede))
