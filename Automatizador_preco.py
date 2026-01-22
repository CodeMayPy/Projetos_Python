
import time
from selenium import webdriver
from selenium.webdriver.common.by import By #localiza elementos


# Receber uma informação
acao = input('Qual acão você quer acompanhar?')

#exibir resultado a partir da resposta
link = "https://investidor10.com.br/fiis/" + acao

navegador = webdriver.Chrome()
navegador.get(link)

#espera o site carregar
time.sleep(5)

# pega e mostra o preço atual na tela
preco_texto = navegador.find_element(By.CLASS_NAME, "value").text
print(f'O preço da ação {acao} é de: {preco_texto}.')

#perguntar se quer um alerta de preço
comando = input("Gostaria de receber alerta de preço?")

if comando.lower() != "s":
    print('Resposta errada.Tente novamente.')
else:
    print("Muito bem, vamos lá.")



#sim, enviar por email 