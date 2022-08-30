# Mini-Projeto - Introdução à Programação
## Introdução à Ciência de Dados


### Requisitos do projeto: 

- Crie a classe ExtratorDeProbabilidades que contém ao menos os seguintes atributos
(i) referência a um arquivo csv, e (ii) uma estrutura de lista com tuplas e dicionários
para armazenar os dados da base.

- Crie um método carregar_colunas(lista_colunas, quantidade) que recebe uma lista
de strings (representando o nome das colunas da base) e um número inteiro
(representando uma quantidade de registros), e carrega uma amostra dos registros
de tamanho quantidade com apenas as colunas em lista_colunas. Atenção: os
dados carregados deverão ser codificados na estrutura de lista que é atributo da
classe.

- Crie o método descarregar() que reinicializa a estrutura de lista como vazia.

- Crie o método probabilidade_apriori((característica, valor)) que calcula - para os
dados carregados em memória - a probabilidade da coluna característica possuir o
valor valor.

- Crie o método probabilidade_apriori_intervalo((característica, (inicio,fim))) que
permite o calculo - para os dados carregados em memória - da probabilidade apriori
considerando intervalos numéricos.

- Crie o método probabilidade_condicional(((característica_1,
valor_1),(característica_2, valor)2))) que calcula - para os dados carregados em
memória - a probabilidade condicional da coluna característica_1 possuir o valor
valor_1 dado que característica_2 possui o valor valor_2.

- Crie o método probabilidade_apriori_intervalo((característica, valor), (característica,
(inicio, fim))) ou probabilidade_apriori_intervalo((característica, (início, fim)),
(característica, valor)) ou probabilidade_apriori_intervalo((característica, (início, fim)), 
(característica, (início, fim))) que permite o calculo - para os dados carregados em
memória - da probabilidade condicional considerando intervalos numéricos.

- Integre todas as funcionalidades em um Menu a partir do qual é possível carregar e
descarregar bases de dados, consultar todas as probabilidades apriori e
condicionais.
