from datetime import datetime
import os
import threading
import traceback
from colorama import Fore, Style, init

class Log:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(Log, cls).__new__(cls)
        return cls._instance

    def __init__(self, debug=False):
        self.debug = debug
        if not hasattr(self, 'initialized'):  # Isso evita a reinitialização
            self.initialized = True
            if not self.debug:
                self._filename = None
                self._create_log_folder()
                self._create_log_file()

    def _create_log_folder(self):
        if not os.path.exists('log'):
            os.mkdir('log')

    def _create_log_file(self):
        # timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        # self._filename = os.path.join('log', f"log_{timestamp}.txt")
        self._filename = os.path.join('log', "log.txt")

    def _write_log(self, message):
        if self.debug:
            return
        with open(self._filename, 'a', encoding='utf-8') as file:
            file.write(message + "\n")

    def info(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        flag = Fore.GREEN + '[INFO]' + Style.RESET_ALL
        log_message = f"{timestamp}    {flag} - {message}"
        print(log_message, flush=True)
        
        default_log_message = f"{timestamp}    [INFO] - {message}"
        self._write_log(default_log_message)

    def warning(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        flag = Fore.YELLOW + '[WARNING]' + Style.RESET_ALL
        log_message = f"{timestamp} {flag} - {message}"
        print(log_message, flush=True)
        
        default_log_message = f"{timestamp} [WARNING] - {message}"
        self._write_log(default_log_message)

    def error(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        error = traceback.format_exc()
        flag = Fore.RED + '[ERROR]' + Style.RESET_ALL
        log_message = f"{timestamp}   {flag} - {message} - {error}"
        print(log_message, flush=True)
        
        default_log_message = f"{timestamp}   [ERROR] - {message} - {error}"
        self._write_log(default_log_message)

    def robot(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        flag = Fore.BLUE + '[ROBOT]' + Style.RESET_ALL
        log_message = f"{timestamp}   {flag} - {message}"
        print(log_message, flush=True)
        
        default_log_message = f"{timestamp}   [ROBOT] - {message}"
        self._write_log(default_log_message)
