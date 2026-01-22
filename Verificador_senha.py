import time

print("Vamos verificar se você tem uma senha boa...")
senha = input("Digite a sua senha:")

print("Analisando...")
#time.sleep() faz uma pausa.
time.sleep(2)

simbolos ="!@#$%^&*()-_=+[{]};:'\",<.>/?|\\"

# o any() verifica se ao menos uma condição pedida foi encontrada
tem_simbolo = any(letra in simbolos for letra in senha)
tem_maiuscula = any(letra.isupper() for letra in senha)
tem_minuscula = any(letra.islower() for letra in senha)
tem_numero = any(letra.isdigit() for letra in senha)



'''
len() -> ele conta a quantia de caracteres
if -> verifica se a condição esta sendo atendida
and -> adiciona mais "filtros" ao if.
else -> se o if falho o else assume. 
 '''


if len(senha) >= 8 and tem_simbolo and tem_maiuscula and tem_minuscula and tem_numero:
    print("Parabéns sua senha é forte")
else:
    print("Melhor criar outra senha...")        
