import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from database import Base, DP, Municipio, Ocorrencia

metadata = Base.metadata

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

print('  # | Municipio' + ' '*41 + ' |  qtde')
print('-'*65)
for i, (dp, c) in enumerate(result.fetchall(), start=1):
    print(f'{i:3} | {dp:50} | {c:6}')
