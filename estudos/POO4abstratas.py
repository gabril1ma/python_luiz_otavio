from abc import ABC, abstractmethod

class Log(ABC):   # abstrato utilizado para não ser implementado diretamente

    @abstractmethod
    def _log(self, msg):
        ...
    
    def log_error(self, msg):
        return self._log(f"ERROR: {msg}")
    
    def log_succes(self, msg):
        return self._log(f"Succes: {msg}")
    

class LogPrintMixin(Log):  # deve ser herdado e definido dentro da sub classe
    def _log(self, msg):
        print(f"{msg} {self.__class__.__name__}")

l = LogPrintMixin()

l.log_error("taligaad erro")


# aula 232


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f"enviando email {self.mensagem}")
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f"enviando sms {self.mensagem}")
        return True

#n = Notificao("teste (não funciona)") # não pode ser instanciado pois é abstrato

n = NotificacaoSMS("teste agora funcionando")
n.enviar()


def notificar(notificacao: Notificacao):

    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("notificação enviada com sucesso")
    else: 
        print("falha ao enviar notificação")


notificar(NotificacaoSMS("teste sms"))

notificacao_email = NotificacaoEmail("teste email")

notificar(notificacao_email)




# aula  234

class MyError(Exception):
    ...

class AnotherError(Exception):
    ...

def levantar():
    raise MyError("deu erro no teu cerebro ai tenta dnv mais bem feito")


#levantar()

try:
    levantar()

except MyError as error:

    print(error.__class__.__name__, ":", error)
    exception_ = AnotherError("outro erro meu fi nu ze")
#    raise
    raise exception_ from error


class Numbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self): #usado para mostrar o formato dos dados dentro da classe
        return f"Numbers({self.x!r}, {self.y!r})"
    

n1 = Numbers(3,6)

print(n1)