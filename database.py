import sqlalchemy as sa
from sqlalchemy.orm import declarative_base


engine = sa.create_engine('sqlite:///ocorrencias.db')

Base = declarative_base()


class DP(Base):
    __tablename__ = 'tbDP'

    codDP = sa.Column(
        'codDP',
        sa.INTEGER,
        primary_key=True,
        nullable=False,
        index=True
    )
    nome = sa.Column('nome', sa.VARCHAR(100), nullable=False)
    endereco = sa.Column('endereco', sa.VARCHAR(255), nullable=False)


class ResponsavelDP(Base):
    __tablename__ = 'tbResponsavelDP'

    codDP = sa.Column(
        'codDP',
        sa.ForeignKey(
            DP.codDP,
            ondelete='NO ACTION',
            onupdate='CASCADE'
        ),
        primary_key=True,
        nullable=False,
        index=True
    )
    delegado = sa.Column('delegado', sa.VARCHAR(100), nullable=False)


class Municipio(Base):
    __tablename__ = 'tbMunicipio'

    codIBGE = sa.Column(
        'codIBGE',
        sa.INTEGER,
        primary_key=True,
        nullable=False,
        index=True
    )
    municipio = sa.Column('municipio', sa.VARCHAR(100), nullable=False)
    regiao = sa.Column('regiao', sa.VARCHAR(25), nullable=False)


class Ocorrencia(Base):
    __tablename__ = 'tbOcorrencia'

    idRegistro = sa.Column(
        'idRegistro',
        sa.INTEGER,
        primary_key=True,
        nullable=False,
        index=True
    )
    codDP = sa.Column(
        'codDP',
        sa.ForeignKey(
            DP.codDP,
            ondelete='NO ACTION',
            onupdate='CASCADE'
        ),
        nullable=False,
        index=True
    )
    codIBGE = sa.Column(
        'codIBGE',
        sa.ForeignKey(
            Municipio.codIBGE,
            ondelete='NO ACTION',
            onupdate='CASCADE'
        ),
        nullable=False,
        index=True
    )
    ano = sa.Column('ano', sa.CHAR(4), nullable=False)
    mes = sa.Column('mes', sa.CHAR(2), nullable=False)
    ocorrencia = sa.Column('ocorrencia', sa.VARCHAR(2), nullable=False)
    qtde = sa.Column('qtde', sa.INTEGER, nullable=False)


if __name__ == '__main__':
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print(e)
    else:
        print('Tabela criadas com sucesso!')
