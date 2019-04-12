class Client:
    __id = None
    __nome = None

    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome

    def getClientId(self):
        return self.__id

    def getClientNome(self):
        return self.__nome

    def getClientName(self, id):
        retorno = ""
        if(self.__id == id):
            retorno = self.__nome
        else:
            retorno = "Cliente não encontrado!!"
        return(retorno)