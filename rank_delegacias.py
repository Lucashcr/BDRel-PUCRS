import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from database import Base, DP, Municipio, Ocorrencia

metadata = Base.metadata

engine = sa.create_engine('sqlite:///ocorrencias.db')
session = sessionmaker(engine)()

query = select(
    DP.nome.label('DP'),
    sa.func.sum(Ocorrencia.qtde).label('Total')
).join(
    Ocorrencia,
    Ocorrencia.codDP == DP.codDP
).join(
    Municipio,
    Ocorrencia.codIBGE == Municipio.codIBGE
).where(
    Municipio.regiao == 'Capital'
).group_by(
    DP.nome
).order_by(
    sa.func.sum(Ocorrencia.qtde).label('Total').desc()
)

result = session.execute(query)

print('  # | DP' + ' '*48 + ' |  qtde')
print('-'*65)
for i, (dp, c) in enumerate(result.fetchall(), start=1):
    print(f'{i:3} | {dp:50} | {c:6}')
