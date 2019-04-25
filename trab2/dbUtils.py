import psycopg2
from sqlalchemy import create_engine
from psycopg2 import Error
class DbUtils:
    db_string = "postgresql+psycopg2://postgres:4011@localhost/Asao"
    db_query = " "

    
    
    def insertVendedores(self, cpf, nome, carteiratrabalho, telefone, dataadmissao, fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO projeto2.tb_vendedores (cpf, nome, carteiratrabalho, telefone, dataadmissao,fg_ativo) VALUES (%s, %s, %s, %s, %s, %s);" 
        values = (cpf, nome, carteiratrabalho, telefone, dataadmissao, fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True
        except (Exception, psycopg2.Error) as error :
            print(error)
            print("Problemas para inserir vendedor\n")
            res = False
        return res

    def getVendedores(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from projeto2.tb_vendedores"
        vendedores = db.execute(self.select_query)
        return vendedores

    def insertCategorias(self, titulo_categoria, descricao_categoria, fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO projeto2.tb_categorias (titulo_categoria, descricao_categoria, fg_ativo) VALUES (%s, %s, %s);" 
        values = (titulo_categoria,descricao_categoria, fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True
        except (Exception, psycopg2.Error) as error :
            print(error)
            print("Problemas para inserir categoria\n")
            res = False
        return res

    def getCategorias(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from projeto2.tb_categorias"
        categorias = db.execute(self.select_query)
        return categorias

    def insertFornecedores(self, cnpj,razaosocial,telefone,endereco,contato,fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO projeto2.tb_fornecedores (cnpj, razaosocial, telefone, endereco, contato, fg_ativo) VALUES (%s,%s,%s, %s, %s,%s);" 
        values = (cnpj, razaosocial, telefone, endereco, contato, fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True
        except (Exception, psycopg2.Error) as error :
            print(error)
            print("Problemas para inserir fornecedor\n")
            res = False
        return res

    def getFornecedores(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from projeto2.tb_fornecedores"
        fornecedores = db.execute(self.select_query)
        return fornecedores

    def insertProdutos(self, id_fornecedor, id_categoria, nomeproduto, descricaoproduto, valor_unitario, quantidade, quantidademinima,fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO projeto2.tb_produtos (id_fornecedor, id_categoria, nomeproduto, descricaoproduto, valor_unitario, quantidade, quantidademinima,fg_ativo) VALUES (%s,%s,%s, %s, %s,%s,%s,%s);" 
        values = (id_fornecedor, id_categoria, nomeproduto, descricaoproduto, valor_unitario, quantidade, quantidademinima,fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True
        except (Exception, psycopg2.Error) as error :
            print(error)
            print("Problemas para inserir produto\n")
            res = False
        return res

    def getProdutos(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from projeto2.tb_produtos"
        produtos = db.execute(self.select_query)
        return produtos

    def insertCompras(self, id_fornecedor,id_produto,id_categoria,datacompra,valortotal,quantidade, fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO projeto2.tb_compras (id_fornecedor,id_produto,id_categoria,datacompra,valortotal,quantidade, fg_ativo) VALUES (%s,%s,%s, %s, %s,%s,%s);" 
        values = (id_fornecedor,id_produto,id_categoria,datacompra,valortotal,quantidade, fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True
        except (Exception, psycopg2.Error) as error :
            print(error)
            print("Problemas para inserir compra\n")
            res = False
        return res

    def getCompras(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from projeto2.tb_compras"
        compras = db.execute(self.select_query)
        return compras

    def insertVendas(self, id_vendedor,id_categoria,id_produto,datavenda,valortotal,quantidade, fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO projeto2.tb_vendas (id_vendedor,id_categoria,id_produto,datavenda,valortotal,quantidade, fg_ativo) VALUES (%s,%s,%s, %s, %s,%s,%s);" 
        values = (id_vendedor,id_categoria,id_produto,datavenda,valortotal,quantidade, fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True
        except (Exception, psycopg2.Error) as error :
            print(error)
            print("Problemas para inserir venda\n")
            res = False
        return res

    def getVendas(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from projeto2.tb_vendas"
        vendas = db.execute(self.select_query)
        return vendas