class Product:
    __id = None
    __nome = None
    __price = None

    def __init__(self, id, nome, price):
        self.__id = id
        self.__nome = nome
        self.__price = price

    def getProductId(self):
        return self.__id

    def getProductNome(self):
        return self.__nome

    def getProductPrice(self):
        return self.__price

    def getProductName(self, id):
        retorno = ""
        if(self.__id == id):
            retorno = self.__nome
        else:
            retorno = "Produto não encontrado!!"
        return(retorno)