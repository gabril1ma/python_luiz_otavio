class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None

    def set_user(self, user):
        self.user = user

    
    @classmethod
    def create_user(cls,user):
        connection = cls()
        connection.user = user
        return connection
    

c1 = Connection("malado")
print(c1.host)

c2 = Connection.create_user("gabriel")
print(c2.host)

c3 = Connection()
c3.set_user("dinossauro rei")
print(c3.user)


class Camisa:
    def __init__(self, cor):
        self.cor_camisa = cor


    @property
    def cor(self):
        print("property")
        return self.cor_camisa
    
    @property
    def tamanho(self):
        return "o tamanho tu que escolhe irmão mas não no meu programa m"
    
    @cor.setter # usado para definir o valor para a property podendo colocar condições para os valores
    def cor(self, value):
        if value == "rosa":
            raise ValueError("rosa é coisa de viado")
        print("setter")
        print("agora vim pro setter olha só que maravilha", value)
        self.cor_camisa = value



camisa = Camisa("vermelha")

camisa.cor = "azul"  #chamando dessa maneira vai passar pelo setter e pela property

print(camisa.cor)  # estou chamando pelo getter
print(camisa.tamanho)



class publico_privado_protected:
    def __init__(self):
        # python NÂO TEM ESSE SISTEMA depende do programador seguir 
        self.publico = "publico" # se define somente com o nome 
        # pode ser usado em qualquer lugar
        self._protected = "protected" # se define com um _ na frente
        # pode ser usado em qualquer classe que herde da classe que foi criado
        self.__privado = "privado" # se define com dois _ na frente
        # deve ser usado apenas na classe que foi criado
    def get_privado(self):
        return self.__privado

    def set_privado(self, value):
        self.__privado = value

    def __metodo_privado(self):
        print("metodo privado")

    def metodo_publico(self):
        print("metodo publico")
        self.__metodo_privado()



