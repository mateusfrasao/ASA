create schema projeto2



CREATE TABLE projeto2.tb_categorias(
	id_categoria SERIAL PRIMARY KEY,
	titulo_categoria VARCHAR(40),
	descricao_categoria VARCHAR(100),
	fg_ativo INTEGER
);




CREATE TABLE projeto2.tb_fornecedores(
	id_fornecedor SERIAL PRIMARY KEY,
	cnpj VARCHAR(20),
	razaosocial VARCHAR(50),
	telefone VARCHAR(12),
	endereco VARCHAR(60),
	contato VARCHAR(30),
	fg_ativo INTEGER
);






CREATE TABLE projeto2.tb_produtos(
	id_produtos SERIAL PRIMARY KEY,
	id_fornecedor INTEGER,
	id_categoria INTEGER,
	nomeproduto VARCHAR(40),
	descricaoproduto VARCHAR(100),
	valor_unitario NUMERIC(10,2),
	quantidade INTEGER,
	quantidademinima INTEGER,
	fg_ativo INTEGER,

	CONSTRAINT produtos_fk FOREIGN KEY(id_fornecedor)
	REFERENCES projeto2.tb_fornecedores(id_fornecedor),

	CONSTRAINT produtos_fk2 FOREIGN KEY(id_categoria)
	REFERENCES projeto2.tb_categorias(id_categoria)
	
);






CREATE TABLE projeto2.tb_vendedores(
	id_venda SERIAL PRIMARY KEY,
	cpf VARCHAR(14),
	nome VARCHAR(40),
	carteiratrabalho VARCHAR(6),
	telefone VARCHAR(50),
	dataadmissao DATE,
	fg_ativo INTEGER
);






CREATE TABLE projeto2.tb_compras(
	id_compra SERIAL PRIMARY KEY,
	id_fornecedor INTEGER,
	id_produto INTEGER,
	id_categoria INTEGER,
	datacompra DATE,
	valortotal NUMERIC(15,2),
	quantidade INTEGER,
	fg_ativo INTEGER,
	CONSTRAINT compras_fk1 FOREIGN KEY(id_fornecedor)
	REFERENCES projeto2.tb_fornecedores(id_fornecedor),
	
	CONSTRAINT compras_fk2 FOREIGN KEY(id_produto)
	REFERENCES projeto2.tb_produtos(id_produtos),
	
	CONSTRAINT compras_fk3 FOREIGN KEY(id_categoria)
	REFERENCES projeto2.tb_categorias(id_categoria)
	
);



CREATE TABLE projeto2.tb_vendas(
	id_venda SERIAL PRIMARY KEY,
	id_vendedor INTEGER,
	id_categoria INTEGER,
	id_produto INTEGER,
	datavenda DATE,
	valortotal NUMERIC(15,2),
	quantidade INTEGER,
	fg_ativo INTEGER,

	CONSTRAINT vendas_fk1 FOREIGN KEY(id_vendedor)
	REFERENCES projeto2.tb_vendedores(id_venda),
	
	CONSTRAINT vendas_fk2 FOREIGN KEY(id_categoria)
	REFERENCES projeto2.tb_categorias(id_categoria),
	
	CONSTRAINT vendas_fk3 FOREIGN KEY(id_produto)
	REFERENCES projeto2.tb_produtos(id_produtos)

	
);



