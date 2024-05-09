from time import sleep
class Tamagotchi:
    def __init__(self):
        self.fome = 8
        self.saude = 7
        self.diversao = 5
        self.banho = 4
        self.idade = 0

    def Alimentar(self):
        self.fome += 5
        self.saude -= 5
        self.idade += 1
        if self.fome == 10:
            print('Já estou cheio!')
        elif self.fome > 10:
            self.fome = 10
        if self.saude < 0:
            self.saude = 0

    def Cuidar(self):
        self.saude += 5
        self.diversao -= 5
        self.idade += 1
        if self.saude == 10:
            print('Estou bem por enquanto!')
        elif self.saude > 10:
            self.saude = 10
        if self.diversao < 0:
            self.diversao = 0

    def Brincar(self):
        self.diversao += 5
        self.banho -= 5
        self.idade += 1
        if self.diversao == 10:
            print(' Brinquei bastante, estou com preguiça agora!')
        elif self.diversao >= 10:
            self.diversao = 10
        if self.banho < 0:
            self.banho = 0

    def Limpar(self):
        self.banho += 5
        self.fome -= 5
        self.idade += 1
        if self.banho == 10:
            print('Já estou limpo!')
        elif self.banho > 10:
            self.banho = 10
        if self.fome < 0:
            self.fome = 0

    def Status(self):
        print(f'Fome: {self.fome}\nSaúde: {self.saude}\nDiversão: {self.diversao}\nBanho: {self.banho}\nIdade: {self.idade}')

tamagotchi = Tamagotchi()

print('Olá seja bem vindo ao seu amigo virtual, onde você poderá cuidar de um bichinho e deixa-lo feliz o máximo que puder.')
sleep(3)
print('Vamos começar?')
sleep(3)
print("""
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---
""")
sleep(1)

while True:
    escolha = int(input("""O que gostaria de fazer agora?
[1] Status
[2] Alimentar
[3] Cuidar
[4] Brincar
[5] Limpar
"""))
    if escolha == 1:
        tamagotchi.Status()
    elif escolha == 2:
        tamagotchi.Alimentar()
    elif escolha == 3:
        tamagotchi.Cuidar()
    elif escolha == 4:
        tamagotchi.Brincar()
    elif escolha == 5:
        tamagotchi.Limpar()
    else:
        print('Escolha inválida!')

    if tamagotchi.idade == 18:
        print('Seu bichinho ficou mais velho e aproveitou a sua vida, porém chegou sua hora!')
        sleep(1)
        print("""
/  \.-" "-./  \.
\    -   -    /
 |   X   X   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---
""")
        sleep(1)
        print('Obrigado por cuidar dele!')
        break
