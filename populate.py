import pandas as pd
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from database import Base, DP, Municipio, Ocorrencia, ResponsavelDP

engine = sa.create_engine('sqlite:///ocorrencias.db')
session = sessionmaker(engine)()

dados_dp = pd.read_csv('./dados/DP.csv', sep=',')
dados_resp = pd.read_excel('./dados/ResponsavelDP.xlsx')
dados_munic = pd.read_csv('./dados/Municipio.csv', sep=',')
dados_ocorr = pd.read_excel('./dados/ocorrencias.xlsx')

metadata = Base.metadata

session.execute(
    sa.Table(DP.__tablename__, metadata).insert(),
    dados_dp.to_dict('records')
)

session.execute(
    sa.Table(Municipio.__tablename__, metadata).insert(),
    dados_munic.to_dict('records')
)

session.execute(
    sa.Table(Ocorrencia.__tablename__, metadata).insert(),
    dados_ocorr.to_dict('records')
)

session.execute(
    sa.Table(ResponsavelDP.__tablename__, metadata).insert(),
    dados_resp.to_dict('records')
)

session.commit()
session.close()
