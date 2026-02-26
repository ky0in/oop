class logger:

    _log_file= None

    def __new__(cls,fillername):
        if not cls._log_file:
            cls._log_file = super().__new__(cls)
            cls._log_file = open(fillername, 'a')
            return cls._log_file
        
    def __init__(self,filename):
        self.fp = open(filename,"a")
    
    def add(self, message):
        self._log_file.write(message + '\n')
        

if __name__ == "__main__":
    log1 = logger('log1.txt')
    log2 = logger('log2.txt')
    log3 = logger('log3.txt')

    log1.add('zapis1')
    log2.add('zapis2')
    log3.add('zapis3')