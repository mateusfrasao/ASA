from flask import Flask, url_for, request, json, jsonify, abort
from json import dumps
from dbUtils import DbUtils
#from bottle import response

app = Flask(__name__)
myUser = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!!'

@app.route('/hello')
def api_hello(): #http://127.0.0.1:5000/hello?name=Luis
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'





if __name__ == '__main__':
    app.run()



@app.route('/addvendedor', methods = ['POST'])
def api_addvendedordb():
    
    if not request.json:
        abort(400)
    req_data = request.get_json()

    cpf = req_data['cpf']
    nome = req_data['nome']
    carteiratrabalho = req_data['carteiratrabalho']
    telefone = req_data['telefone']
    dataadmissao = req_data['dataadmissao']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()

    if(dbutils.insertVendedores(cpf, nome, carteiratrabalho,telefone,dataadmissao,fg_ativo)):
        result = {"result": "Vendedor inserido com sucesso"}
    else:
        result = {"result": "Problemas para inserir o vendedor"}
    return jsonify(result)

@app.route('/getvendedores')
def api_getvendedor():
    vendedores = []
    dbUtils = DbUtils()
    vendedorData = dbUtils.getVendedores()
    for i in vendedorData:
        x = {"id": i[0], "cpf": i[1], "nome": i[2], "carteira_de_trabalho": i[3],
        "telefone": i[4], "data_de_admissao": i[5], "fg_ativo": i[6]}
        vendedores.append(x)
    return jsonify(vendedores)

@app.route('/addcategoria', methods = ['POST'])
def api_addcategoriadb():
    
    if not request.json:
        abort(400)
    req_data = request.get_json()

    titulo_categoria = req_data['titulo_categoria']
    descricao_categoria = req_data['descricao_categoria']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()

    if(dbutils.insertCategorias( titulo_categoria,descricao_categoria, fg_ativo)):
        result = {"result": "Categoria inserida com sucesso"}
    else:
        result = {"result": "Problemas para inserir a categoria"}
    return jsonify(result)

@app.route('/getcategorias')
def api_getcategoria():
    categorias = []
    dbUtils = DbUtils()
    categoriaData = dbUtils.getCategorias()
    for i in categoriaData:
        x = {"id": i[0], "titulo_da_categoria": i[1], "descricao_da_categoria": i[2],"fg_ativo": i[3]}
        categorias.append(x)
    return jsonify(categorias)


@app.route('/addfornecedor', methods = ['POST'])
def api_addfornecedordb():
    
    if not request.json:
        abort(400)
    req_data = request.get_json()

    cnpj = req_data['cnpj']
    razaosocial = req_data['razaosocial']
    telefone = req_data['telefone']
    endereco = req_data['endereco']
    contato = req_data['contato']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()

    if(dbutils.insertFornecedores(cnpj,razaosocial,telefone,endereco,contato, fg_ativo)):
        result = {"result": "Fornecedor inserido com sucesso"}
    else:
        result = {"result": "Problemas para inserir fornecedor"}
    return jsonify(result)

@app.route('/getfornecedores')
def api_getfornecedor():
    fornecedores = []
    dbUtils = DbUtils()
    fornecedorData = dbUtils.getFornecedores()
    for i in fornecedorData:
        x = {"id": i[0], "cnpj": i[1], "razaosocial": i[2], "telefone":i[3],"endereco":i[4], "contato":i[5], "fg_ativo":i[6]}
        fornecedores.append(x)
    return jsonify(fornecedores)

@app.route('/addproduto', methods = ['POST'])
def api_addprodutodb():
    
    if not request.json:
        abort(400)
    req_data = request.get_json()

    id_fornecedor = req_data['id_fornecedor']
    id_categoria = req_data['id_categoria']
    nomeproduto = req_data['nomeproduto']
    descricaoproduto = req_data['descricaoproduto']
    valor_unitario = req_data['valor_unitario']
    quantidade = req_data['quantidade']
    quantidademinima = req_data['quantidademinima']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()

    if(dbutils.insertProdutos(id_fornecedor,id_categoria,nomeproduto,descricaoproduto,valor_unitario,quantidade,quantidademinima, fg_ativo)):
        result = {"result": "Produto inserido com sucesso"}
    else:
        result = {"result": "Problemas para inserir produto"}
    return jsonify(result)

@app.route('/getprodutos')
def api_getproduto():
    produtos = []
    dbUtils = DbUtils()
    produtoData = dbUtils.getProdutos()
    for i in produtoData:
        x = {"id_produto": i[0], "id_fornecedor": i[1], "id_categoria": i[2], "nomeproduto":i[3],"descricaoproduto":i[4], "valor_unitario":str(i[5]), "quantidade":i[6], "quantidademinima":i[7], "fg_ativo":i[8]}
        produtos.append(x)
    return jsonify(produtos)

@app.route('/addcompra', methods = ['POST'])
def api_addcompradb():
    
    if not request.json:
        abort(400)
    req_data = request.get_json()

    id_fornecedor = req_data['id_fornecedor']
    id_produto = req_data['id_produto']
    id_categoria = req_data['id_categoria']
    datacompra = req_data['datacompra']
    valortotal = req_data['valortotal']
    quantidade = req_data['quantidade']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()

    if(dbutils.insertCompras(id_fornecedor,id_produto,id_categoria,datacompra,valortotal,quantidade, fg_ativo)):
        result = {"result": "Compra inserida com sucesso"}
    else:
        result = {"result": "Problemas para inserir compra"}
    return jsonify(result)

@app.route('/getcompras')
def api_getcompra():
    compras = []
    dbUtils = DbUtils()
    compraData = dbUtils.getCompras()
    for i in compraData:
        x = {"id_compra":i[0],"id_fornecedor":i[1], "id_produto": i[2], "id_categoria": i[3], "datacompra":i[4],"valortotal":str(i[5]), "quantidade":i[6], "fg_ativo":i[7]}
        compras.append(x)
    return jsonify(compras)

@app.route('/addvenda', methods = ['POST'])
def api_addvendadb():
    
    if not request.json:
        abort(400)
    req_data = request.get_json()

    id_vendedor = req_data['id_vendedor']    
    id_categoria = req_data['id_categoria']
    id_produto = req_data['id_produto']
    datavenda = req_data['datavenda']
    valortotal = req_data['valortotal']
    quantidade = req_data['quantidade']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()

    if(dbutils.insertVendas(id_vendedor,id_categoria,id_produto,datavenda,valortotal,quantidade, fg_ativo)):
        result = {"result": "Venda inserida com sucesso"}
    else:
        result = {"result": "Problemassssss para inserir venda"}
    return jsonify(result)

@app.route('/getvendas')
def api_getvenda():
    vendas = []
    dbUtils = DbUtils()
    vendaData = dbUtils.getVendas()
    for i in vendaData:
        x = {"id_venda":i[0],"id_vendedor":i[1], "id_categoria": i[2],"id_produto": i[3], "datavenda":i[4],"valortotal":str(i[5]), "quantidade":i[6], "fg_ativo":i[7]}
        vendas.append(x)
    return jsonify(vendas)




    



