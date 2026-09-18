class Logger:
    __instance=None
    
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
            cls.__instance.count = 0
        return cls.__instance

    def log(self,msg):
        print(f"Logging {msg}")
        self.count+=1

    def getCount(self):
        return self.count

log1 = Logger()
log2 = Logger()
log3 = Logger()

log1.log("Hello")
log2.log("22Hello")
log3.log("22323Hello")
print(log1.getCount())
print(log2.getCount())