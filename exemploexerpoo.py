from time import sleep
 
 
class Tamagotchi:
    def __init__(self, nome_tamagotchi, idade=1, fome='', dias=0):
        self.nome = nome_tamagotchi
        self.__idade = idade
        self.__fome = fome
        self.__intensidade_fome = ['pouca', 'muita', 'passando']
        self.__dias_sem_comer = dias
 
    @property
    def fome(self):
        return self.__fome
 
    @property
    def idade(self):
        return self.__idade
 
    @staticmethod
    def opcoes_mostrar():
        print(f'O que deseja mostrar:',
              f'\t[ 1 ]\tNome',
              f'\t[ 2 ]\tIdade',
              f'\t[ 3 ]\tFome', sep='\n')
        while True:
            opc = input('O que deseja alterar [1 - 3]: ')
            try:
                opc = int(opc)
                if 1 <= opc <= 3:
                    return opc
                else:
                    print('Opção inválida')
            except ValueError:
                print('Opção inválida')
 
    def mostrar(self):
        mostrar = self.opcoes_mostrar()
        if mostrar == 1:
            print(f'O nome do seu tamagotchi é {self.nome}')
        elif mostrar == 2:
            print(f'Seu tamagotchi tem {self.idade} dia de vida' if self.idade == 1
                  else f'Seu tamagotchi tem {self.idade} dias de vida')
        else:
            if not self.fome:
                print(f'Seu tamagotchi não está com fome')
                return
            print(f'Seu tamagotchi está {self.fome} fome.' if self.__fome == 'passando'
                  else f'Seu tamagotchi está com {self.fome} fome')
 
    def mudar_nome(self, novo_nome):
        if self.nome == novo_nome:
            print('Seu tamagotchi já possui esse nome')
            return
        self.nome = novo_nome
        print('O nome do seu tamagotchi foi alterado com sucesso!')
 
    def alimentar(self):
        print('Seu tamagotchi foi alimentado')
        self.__fome = ''
        self.__dias_sem_comer = 0
 
    @staticmethod
    def valida_opcao():
        while True:
            opc = input('Digite uma opção [0 - 4]: ')
            try:
                opc = int(opc)
                if 0 <= opc <= 4:
                    return opc
                else:
                    print('Opção inválida')
            except ValueError:
                print('Opção inválida')
 
    def opcoes(self):
        print('-'*40, f'O que deseja fazer:', '\t[ 0 ]\tSair do programa',
              '\t[ 1 ]\tMostrar atributos do seu tamagotchi',
              '\t[ 2 ]\tMudar o nome do seu tamagotchi',
              '\t[ 3 ]\tAlimentar seu tamagotchi',
              '\t[ 4 ]\tFazer ele dormir', '-'*40, sep='\n')
        opc = self.valida_opcao()
        print('-' * 40)
        if opc == 1:
            self.mostrar()
        elif opc == 2:
            novo_nome = input('Digite o novo nome do seu tamagotchi: ')
            self.mudar_nome(novo_nome)
        elif opc == 3:
            if not self.fome:
                print('Seu tamagotchi não está com fome.')
                return
            self.alimentar()
        elif opc == 4:
            self.__dias_sem_comer += 1
            if self.__dias_sem_comer <= 3:
                self.__fome = self.__intensidade_fome[self.__dias_sem_comer - 1]
            else:
                print('Seu tamagoshi morreu de fome!')
                try:
                    arquivo = open('tamagotchi.txt', 'w+')
                    arquivo.close()
                except FileNotFoundError:
                    pass
                return True
            print('Seu tamagotchi foi dormir por 1 dia.')
            self.__idade += 1
            sleep(1)
            print('Seu tamagotchi acordou.')
            sleep(1)
 
        else:
            with open('tamagotchi.txt', 'w+') as arquivo:
                arquivo.write(f'{self.nome}\n')
                arquivo.write(f'{self.idade}\n')
                arquivo.write(f'{self.fome}\n')
                arquivo.write(f'{self.__dias_sem_comer}\n')
            return True
 
 
# Main Program
try:
    with open('tamagotchi.txt', 'r') as file:
        if len(file.readlines()) != 0:
            file.seek(0)
            print('Carregando seu tamagoshi...')
            sleep(1)
            nome_carregado = file.readline().replace('\n', '')
            idade_carregado = int(file.readline().replace('\n', ''))
            fome_carregado = file.readline().replace('\n', '')
            dias_carregado = int(file.readline().replace('\n', ''))
            tamagotchi = Tamagotchi(nome_carregado, idade_carregado, fome_carregado, dias_carregado)
            print(f'Tamagtcshi {tamagotchi.nome} carregado com sucesso!')
        else:
            print('Criando seu tamagotchi...')
            sleep(1)
            nome_carregado = input('Qual será o nome do seu tamagotchi: ')
            tamagotchi = Tamagotchi(nome_carregado)
            print('Seu tamagotchi foi criado com sucesso.')
except FileNotFoundError:
    print('Criando seu tamagotchi...')
    sleep(1)
    nome_carregado = input('Qual será o nome do seu tamagotchi: ')
    tamagotchi = Tamagotchi(nome_carregado)
    print('Seu tamagotchi foi criado com sucesso.')
sleep(1)
while True:
    opcao = tamagotchi.opcoes()
    if opcao:
        break
print('Encerrando programa...')
sleep(1)
print('-'*40, 'Programa encerrado!', sep='\n')