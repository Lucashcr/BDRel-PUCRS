import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from database import Municipio, Ocorrencia

engine = sa.create_engine('sqlite:///ocorrencias.db')
session = sessionmaker(engine)()

query = sa.select(
    Municipio.municipio.label('Municipio'),
    sa.func.sum(Ocorrencia.qtde).label('Total')
).join(
    Ocorrencia,
    Ocorrencia.codIBGE == Municipio.codIBGE
).where(
    Ocorrencia.ocorrencia == 'roubo_veiculo'
).group_by(
    Municipio.municipio
).order_by(
    sa.func.sum(Ocorrencia.qtde).desc()
)

result = session.execute(query)

print('  # | Municipio' + ' '*41 + ' |  Total')
print('-'*66)
for i, (dp, c) in enumerate(result.fetchall(), start=1):
    print(f'{i:3} | {dp:50} | {c:6}')
