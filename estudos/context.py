class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome): # utilizado para voce poder executar como se fosse uma função
         print(f"{nome} ligando para {self.phone}")


c1 = CallMe("319835945906")

c1("Gabriel")