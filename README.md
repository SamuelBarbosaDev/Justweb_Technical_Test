# Justweb Technical Test
Esse é um teste técnico para a vaga de Desenvolvedor Python Pleno.


## Questão 1 (Arquitetura de Soluções e Software):

Você recebe a tarefa de realizar a integração
entre dois sistemas diferentes. Um desses sistemas é uma plataforma de CRM e o outro um
sistema ERP. O sistema de CRM fornece APIs passivas e webhooks como ferramentas de
integração enquanto o sistema ERP fornece apenas APIs passivas. O sistema CRM é hospedado
em nuvem e você não possui acesso à infra dele, enquanto que o sistema ERP é hospedado on-
premises em um banco de dados relacional e você possui acesso direto a essa infra. Não existe
integração nativa entre os dois sistemas. Não existem impedimentos de infraestrutura que
impeçam ou limitem essa integração. Suponha que você possua quaisquer tecnologias ou
ferramentas disponíveis para concluir a tarefa. Baseado nesse cenário, responda as questões a
seguir:

### a) Como você começaria esse projeto?

**Resposta:**
Em Branco

### b) Quais tecnologias você usaria? Por quê?

**Resposta:**
Em Branco

### c) Faça um esboço da arquitetura dessa solução.

**Resposta:**
Em Branco

### d) Você conseguiria estimar quanto tempo levaria essa implementação? Considere uma jornada de trabalho padrão, de 40 horas semanais, de segunda a sexta.

**Resposta:**
Em Branco


## Questão 2 (Python):
Você possui dois dataframes, o dataframe A possui 1000 linhas e B possui
860 linhas. A seguir o mapa de colunas de cada dataframe:
```python
Columns_A = [‘id’, ‘id_cliente’, ‘data_contratacao’, ‘id_contrato’, ‘valor_contrato’]
Columns_B = [‘id’, ‘id_cliente’, ‘data_cancelamento’, ‘id_contrato’, ‘valor_contrato’]
```

### a) Escreva um código em Python que te permita encontrar uma lista de id_clientes dentro do dataframe A.

**Resposta:**
```python
lista_clientes_1 = df_a['id_cliente'].unique()
display(lista_clientes_1)
```

### b) Existe uma forma mais eficiente de se resolver o item a)? Justifique sua resposta.

**Resposta:**
```python
lista_clientes_2 = set(df_a['id_cliente'])
display(lista_clientes_2)
```

Set é um tipo de dado do python, uma coleção desordenada onde não pode haver números repetidos, então basicamente ao transformar uma lista de 'id_cliente' e um set ele elimina automaticamente as duplicatas, isso é mais eficiente em termos de memória, aqui está a definição de set segundo a documentação do **python**: 

"5.4. Conjuntos

Python também inclui um tipo de dados para conjuntos, chamado set. Um conjunto é uma coleção desordenada de elementos, sem elementos repetidos. Usos comuns para conjuntos incluem a verificação eficiente da existência de objetos e a eliminação de itens duplicados. Conjuntos também suportam operações matemáticas como união, interseção, diferença e diferença simétrica.

Chaves ou a função set() podem ser usados para criar conjuntos."

### c) Como obter a data_cancelamento (campo do dataframe B) vinculado aos registros do dataframe A?

**Resposta:**
```python
df_a_mais_b = df_a.merge(
    right=df_b[['id_cliente', 'data_cancelamento']],
    how='inner',
    on='id_cliente'
)
display(df_a_mais_b)
```

### d) Encontre quantos clientes temos por data de contratacao no dataframe A.

**Resposta:**
```python
qtd_clientes_contratacao = (
    df_a
    .groupby(['data_contratacao'])
    .agg({'id_cliente': 'count'})
    .rename(columns={'id_cliente': 'clientes'})
    .reset_index()
)
display(qtd_clientes_contratacao)
```

### e) Encontre quantos clientes temos por data de cancelamento no dataframe B.

**Resposta:**
```python
qtd_clientes_cancelamento = (
    df_b
    .groupby(['data_cancelamento'])
    .agg({'id_cliente': 'count'})
    .rename(columns={'id_cliente': 'clientes'})
    .reset_index()
)
display(qtd_clientes_cancelamento)
```


## Questão 3 (Django):
Você precisa desenvolver o back-end de um determinado sistema e a
linguagem escolhida para resolver esse problema é Python, utilizando o framework Django. O
sistema em questão é para agendamento de clientes que será utilizado por uma clínica
odontológica. Junto dessa demanda, você também recebe a documentação funcional descrita a
seguir:


- Endpoint para cadastrar novos agendamentos.
- Endpoint para editar ou cancelar um agendamento.
- Endpoint para listar todos os agendamentos.
- Endpoint para listar um agendamento específico.
- Validação para não permitir agendar dois clientes no mesmo horário.
- Cálculo de vagas disponíveis por data.


Baseando-se nessas considerações sobre o sistema, responda as questões que se seguem.

### a) Como você começaria a trabalhar nesse projeto?

**Resposta:**
Em Branco

### b) Escreva um esboço de código para os 4 endpoints solicitados.

**Resposta:**
Em Branco

### c) Como você implementaria a validação de não permitir agendar dois clientes no mesmo horário?

**Resposta:**
Em Branco

### d) Como você poderia processar requisições que tentam agendar dois clientes no mesmo horário?

**Resposta:**
Em Branco

### e) Apresente uma implementação do cálculo de vagas de agendamento. Suponha que cada atendimento demora 30 minutos para ser concluído e a clínica só funcione das 08:00 às 18:00, inclusive no horário do almoço. Desconsidere sábados e domingos.

**Resposta:**
Em Branco


## Questão 4 (SQL):
Uma pessoa do time financeiro encomenda para você um conjunto de relatórios financeiros que ela não consegue extrair a partir de bases de dados padrão do sistema utilizado na empresa. Você decide ir direto ao banco de dados para gerar esses relatórios e atender essa demanda. A tabela recuperada a partir do arquivo CSV que lhe foi entregue possui uma documentação incompleta, mostrada a seguir:


- **Id:** primary key
- **Valor:** valor original do título
- **Status:** status do título
- **Baixa_data:** data que o título foi baixado
- **Id_renegociacao:** codigo que vincula com o campo id_renegociacao_novo para renegociar um título
- **Id_renegociacao_novo:** codigo usado para gerar o título renegociado



Os demais campos não possuem qualquer documentação. A partir desta tabela responda às
seguintes questões que foram trazidas pela pessoa do financeiro:

### a) Qual é o valor total de títulos emitidos no mês de junho de 2020? Qual é o valor total de títulos com vencimento no mesmo período? Por que esses números são diferentes?

**Resposta:**
Em Branco

### b) Gerar um relatório com todos os clientes que tiveram títulos pagos em julho de 2020.

**Resposta:**
Em Branco

### c) Encontre quantos boletos foram renegociados no mês de julho de 2020.

**Resposta:**
Em Branco

### d) Encontre o valor pago de juros de todos os boletos pagos em junho de 2020.

**Resposta:**
Em Branco

### e) Encontre o id dos boletos que foram usados para gerar uma renegociação em junho de 2020.

**Resposta:**
Em Branco
