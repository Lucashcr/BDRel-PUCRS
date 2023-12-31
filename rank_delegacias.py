import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from database import DP, Municipio, Ocorrencia

engine = sa.create_engine('sqlite:///ocorrencias.db')
session = sessionmaker(engine)()

query = sa.select(
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

print('  # | DP' + ' '*48 + ' |  Total')
print('-'*66)
for i, (dp, c) in enumerate(result.fetchall(), start=1):
    print(f'{i:3} | {dp:50} | {c:6}')
