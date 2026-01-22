import time

print("Vamos verificar se você tem uma senha boa...")
senha = input("Digite a sua senha:")

print("Analisando...")
time.sleep(2)

simbolos ="!@#$%^&*()-_=+[{]};:'\",<.>/?|\\"

tem_simbolo = any(letra in simbolos for letra in senha)
tem_maiuscula = any(letra.isupper() for letra in senha)
tem_minuscula = any(letra.islower() for letra in senha)
tem_numero = any(letra.isdigit() for letra in senha)




if len(senha) >= 8 and tem_simbolo and tem_maiuscula and tem_minuscula and tem_numero:
    print("Parabéns sua senha é forte")
else:
    print("Melhor criar outra senha...")        