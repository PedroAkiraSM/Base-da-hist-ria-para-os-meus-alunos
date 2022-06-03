import time
time.sleep

print("\t Olá, seja muito bem vindo ao nosso primeiro jogo em Python")
time.sleep(2.4)
input("\t Pressione ENTER para continuar")
print(
    '\t"Locutor: Em um belo dia de sol, o nosso amigo estava andando pelo parque..."'
)
time.sleep(2.7)
print(
    '\t"Quando derrepente uma bola de basquete cai em sua cabeça... e ele desmaia"'
)
time.sleep(3)
print(
    '\t"Locutor: Por sorte uma pessoa estava passando na hora e o vê caido no chão"'
)
time.sleep(3)
print('\t"Pessoa: ACORDE!!"')
time.sleep(1.5)
print('\t"Pessoa: ACORDE!!"')
time.sleep(1.5)

print('\t"Você consegue me dizer seu nome?"')
usuario = input('\t"Me-meu nome é: ')
print(f"Olá {usuario}, como esta se sentindo?")
time.sleep(2)

#Escolhas
print("[1] Estou bem, foi apenas o impacto...")
print("[2] Ah minha cabeça ainda dói bastante...")
time.sleep(1.7)

escolha1 = input("O que você diz: ")
time.sleep(1.7)
if escolha1 == '1':
	print(
	    f'{usuario}:"Estou bem, foi apenas o impacto da bola, ainda mais com este calor que esta fazendo."'
	)
elif escolha1 == '2':
	print(
	    f'{usuario}:"Ah minha cabeça ainda dói bastante... poderia me levar até um médico mais próximo"'
	)
time.sleep(2)

#Continua a história
print("Continua...")