import sys,os
from filter import Type,Filter
from colorama import Fore
class Debug:
    Logs = {}
    Orderes = []
    @staticmethod
    def Log(logs:str|list,log_type:str = Type.Info) -> None:
        avaible_logs = [Type.Info,Type.Warn,Type.Error,Type.Error_Info]
        if log_type in avaible_logs:
            if not isinstance(logs,dict):
                if log_type not in Debug.Logs:
                    Debug.Logs[log_type] = []
                Debug.Logs[f"{log_type}"].append(logs)
                Debug.Orderes.append((log_type,logs))
            else:
                for log in logs:
                    log_type = log
                    abs_log = logs[log]
                    if log_type not in Debug.Logs:
                        Debug.Logs[log_type] = []
                    Debug.Logs[f"{log_type}"].append(abs_log)
                    Debug.Orderes.append((log_type,abs_log))
        else:
            raise TypeException(log_type)
    @staticmethod
    def Write(log:str|list,log_type:str = Type.Info) -> None:
        Debug.Log(log,log_type)
        print({log_type:log})
    @staticmethod
    def Delete(log:str) -> None:
        try:
            Debug.Logs.remove(log)
        except Exception:
            print(f"can't find '{log}' in debug logs")
    @staticmethod
    def Array(deb_arr:list | None = None) -> list:
        if deb_arr is None:
            deb_arr = Debug.Orderes
        return deb_arr
    @staticmethod
    def Show(log_type:str|list = Filter.All) -> None:
        if log_type != Filter.All:
            if log_type in Debug.Logs:
                print("============DEBUG LOGS=========")
                for l_type,log in Debug.Orderes:
                    print(f"[{l_type}]:{log}"if l_type == log_type else "")
                print("===============================")
            else:
                print("There is no Debug logs")
        if log_type == "All":
            print("============DEBUG LOGS=========")
            for l_type,log in Debug.Orderes:
                print(f"[{l_type}]:{log}")     
            print("===============================")
    @staticmethod
    def Break() -> None:
        sys.exit()
    @staticmethod
    def Warning(warn_log:str) -> None:
        print(Fore.RED)
        print(warn_log)
        print(Fore.RESET)
        Debug.Log(f"[WARN]:{warn_log}")
    @staticmethod
    def BreakWCode(exit_code:int) -> None:
        sys.exit(exit_code)
    @staticmethod
    def BreakWWarn(warn:str) -> None:
        Debug.Log(f"WARN:{warn}")
        print(Fore.RED)
        print(warn)
        sys.exit()
    @staticmethod
    def Save_Log() -> None:
        user = os.path.expanduser("~")
        folder = os.path.join(user,"Debug Logs")
        os.makedirs(folder,exist_ok=True)
        logs = [f for f in os.listdir(folder) if f.startswith("log") and f.endswith(".txt")]
        executions = []
        for log in logs:
            log = log.replace("log","").replace(".txt","")
            try:
                log = int(log)
            except:
                log = 0
            executions.append(log)
        biggest = Debug.__find_biggest__(executions) + 1
        change = os.path.join(folder,f"log{biggest}.txt")
        with open(change,"a",encoding="utf-8") as file:
            for change_log,log_type in Debug.Orderes:
                file.write(f"[{change_log}]:{log_type}\n")
    @staticmethod   
    def __find_biggest__(numbers:int|list) -> int:
        biggest = 0
        for number in numbers:
            if int(number) > biggest:
                biggest = int(number)
            else:
                continue
        return biggest
class TypeException(Exception):
    def __init__(self,lo_type):
        self.lo_type = lo_type
        super().__init__(f"Level Type '{self.lo_type}' is not defined")
def __execute_stuff(ex_type,ex_value,ex_traceback):
    if issubclass(ex_type,TypeException):
        print(ex_value)
    else:
        sys.__excepthook__(ex_type, ex_value, ex_traceback)
sys.excepthook = __execute_stuff