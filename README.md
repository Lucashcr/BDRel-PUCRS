# Banco de Dados Relacional - PUCRS

Exercícios referentes à disciplina de Banco de Dados Relacional ministrada durante o curso de Desenvolvimento Full Stack, ministrada pelo professor Claudio Bonel.

## Criando ambiente virtual:

_OBS: Estou utilizando a versão 3.11 do Python, o código não foi testado em versões anteriores._

### Windows

```ps
python -m venv venv
```
```ps
.\venv\Scripts\activate
```
```ps
pip install -r requirements.txt
```

### Linux/MacOS

```sh
python3 -m venv venv
```
```sh
source venv/bin/activate
```
```sh
pip install -r requirements.txt
```

## Criando banco de dados:

```sh
python database.py
```

## Populando banco de dados:

```sh
python populate.py
```

## Calculando rank de delegacias por município:

> Suponha que o Secretário de Estado de Polícia Civil te solicitou para apresentar um
ranqueamento de todas as Delegacias de Polícia, localizadas na Capital, através da
quantidade de ocorrências

```sh
python rank_delegacias.py
```