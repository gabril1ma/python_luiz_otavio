from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"

class Log:
    def _log(self, msg):
        raise NotImplementedError("Implemente o metodo log")
    
    def log_error(self, msg):
        return self._log(f"ERROR: {msg}")
    
    def log_succes(self, msg):
        return self._log(f"Succes: {msg}")
    

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f"{msg} {self.__class__.__name__}"
        print(f"salvando no log {msg_formatada}")
        with open(LOG_FILE, "a") as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write("\n")
        print(msg)



class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} {self.__class__.__name__}")



if __name__ == "__main__":
    lp = LogPrintMixin()
    lp.log_error("taligaad erro")
    lp.log_succes("lallalaa sucesso")
    lp._log("TESTEEEE")
    lf = LogFileMixin()
    lf.log_error("taligaad erro")
    lf.log_succes("lallalaa sucesso")



    
