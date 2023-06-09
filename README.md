# PUCPR - Projeto Completo - Manipulação de Dataset - Python
---------------------------------------------------------------------------
## Alunos:
* Alex Marzani Motta
* Gabriel Delphino Doring

## Instrutor:
* Maicris Fernandes

## Curso:
* Pós-Graduação em Engenharia de Redes e Telecomunicações - Turma U - POLS 275528

## Objetivo:
* Fazer Download do CSV contendo as informações sobre os acidentes automotivos da Austrália do período de 1989 até 2021;
    * LINK: https://www.kaggle.com/datasets/deepcontractor/australian-fatal-car-accident-data-19892021
* Gerar a série histórica do número de acidentes por ano na Austrália;
* Gerar a série histórica do número de acidentes por meses na Austrália, efetuando comparativos entre meses subsequentes de cada ano expressos em porcentagens;
* Calcular a média mensal de acidentes cumulativa de todos os anos;
* Calcular o número de acidentes ocorridos em finais de semana e meios de semana, cumulativos de todos os anos, efetuando comparativo dos dados expresso em porcentagens;

## Descrição das etapas do Trabalho:
1. Após realizar o download do arquivo, este foi editado para reduzir para apenas as informações pertinentes ao trabalho e alterar o as Colunas para nomes que não sejam parecidos com nomes reservados das linguagens utilizadas. Este arquivo se encontra no repositório com o nome de **car_accident_AUS.db**.

2. Criado o arquivo **csvManipulation.py** para manipular as informações diretamente do arquivo CSV para dentro do código.

3. Criado o arquivo **databaseInitiator.py** para iniciar a base de dados **CarAccidentAUS.db** em SQLite3.

4. Criado o arquivo **queriesSQL.py** para todas a funções e Queries necessárias para manipulação dos dados dentro da base de dados.

5. Criado o arquivo **main.py** para executar todas as funções dentro de **queriesSQL.py** e expor os resultados no terminal.

6. Ao executar o arquivo **main.py**, todos os resultados serão exibidos no terminal, cumprindo todas as requisições do trabalho.

## Github
* https://github.com/axlbear/pucpr_python_dataset.git
## Agradecemos ao Professor Maicris pelo curso ministrado.
