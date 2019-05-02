from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy import text, select, ForeignKey

db = create_engine("postgresql+psycopg2://postgres:24029722@localhost/asa")

metadados = MetaData()

alunos = Table('alunos',metadados, Column('id',Integer,primary_key=True),Column('nome',String(60)))


endereco = Table('endereco',metadados, Column('id',Integer,primary_key=True),Column('aluno_id', Integer, ForeignKey('alunos.id')), Column('descricao', String(60)))
metadados.create_all(db)

conn = db.connect()

conn.execute(alunos.insert(),[
    {'nome' : 'Joao'},
    {'nome' : 'Pedro'},
    {'nome' : 'Claudio'},
    {'nome' : 'Afonso'}, 
])

conn.execute(endereco.insert(),[
    {'aluno_id': 1,'descricao': 'Rua teste1 , 1234'},
    {'aluno_id': 2,'descricao': 'Rua teste2 , 1234'},
    {'aluno_id': 3,'descricao': 'Rua teste3 , 1234'},
    {'aluno_id': 4,'descricao': 'Rua teste4 , 1234'},
])
select_command = select([alunos, endereco]).where(alunos.c.id == endereco.c.aluno_id)
result = conn.execute(select_command)
print(select_command)

for row in result:
    print(row)

conn.close()

# insert_command = alunos.insert().values(nome = 'Teste5',endereco = 'teste')
# print(insert_command)
# result = conn.execute(insert_command)


# result = conn.execute(alunos.insert(),[
#     {'nome': 'joao', 'endereco': 'Rua 1, 123'},
#     {'nome': 'joao1', 'endereco': 'Rua 2, 123'},
#     {'nome': 'joao2', 'endereco': 'Rua 3, 123'},
#     {'nome': 'joao3', 'endereco': 'Rua 4, 123'},
# ])
# print(result.inserted_primary_key)

# select_command = alunos.select()
# select_command = text("SELECT alunos.nome, alunos.endereco FROM alunos WHERE alunos.id = :x")

# select_command = select([alunos])
# select_command = select([alunos]).where(alunos.c.id == 1)
# update_command = alunos.update().where(alunos.c.id == 1).values(nome='Joaozinho')
# result = conn.execute(update_command)
# print(update_command)

# delete_command = alunos.delete().where(alunos.c.id == 1)
# result = conn.execute(delete_command)
# print(delete_command)

# conn = db.connect()
# result = conn.execute(select_command).fetchall()
# print(select_command)

# for row in result:
#     # print(row)
#     print('nome:' +row['nome'] + 'endereco:' +row['endereco'])

