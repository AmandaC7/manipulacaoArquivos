
print ('Olá, qual o seu nome?')
name=input()
print('Olá,', name, 'em que ano você nasceu?')
ano_escolhido = input()
ano_atual = 2020
idade = int(ano_atual) - int(ano_escolhido)
print(name, 'você tem', idade, 'anos de idade')

if idade <= 12:
    print("Você é uma criança")
elif idade <18 :
        print("Você é um adolescente")
elif idade <24:
                  print("Você é um jovem adulto")
elif idade<60:
                      print("Você é um adulto")
elif idade> 60:
                          print("Você está velho(a)")

