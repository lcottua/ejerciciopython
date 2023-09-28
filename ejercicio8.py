precio = input("Introduce el precio con dos decimales: ")
print(precio[:precio.find('.')], "pesos y ", precio[precio.find('.')+1:], 'céntimos')
