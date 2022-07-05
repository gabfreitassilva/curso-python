preco = float(input('Digite o preço do produto: R$ '))

# desconto de 5%
novoPreco = preco - (preco * 0.05)

print('O preço agora é de R$ {:.2f} já adcionado 5% de desconto'.format(novoPreco))
