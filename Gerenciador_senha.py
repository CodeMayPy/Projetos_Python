#1- Receber ums string e usar hashlib pra transformar em sha-256

#1.1: chamando a hashlib
import hashlib
hash_object = hashlib.sha256()

#1.2: convertendo dados
senha =input("Digite sua senha:")
hash_object.update(senha.encode('utf-8')) #converte em bytes

hash_final = hash_object.hexdigest() #hash segura

print(hash_final)

#3- salvar essa hash em .txt

gerenciando_senhas = 'minha_hash.txt'
with open(gerenciando_senhas, 'a') as file_object:  # 'a'(append) adiciona o texto sem apagar ou 'w' (write) apagaria o q estiver no arquivo
    file_object.write(hash_final + '\n')    #\n mostra as hash com quebra de linha

print(f"Hash salva com sucesso em {gerenciando_senhas}!")