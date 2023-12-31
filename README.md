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
*Essa é de fato, uma tarefa desafiadora.*
1. Definiria os principais objetivos.
2. Estudaria o comportamento da API.
3. Escolheria as ferramentas mais adequadas para a tarefa.
4. Planejaria a forma de comunicação entre os dois sistemas.
5. Começaria a desenvolver a solução.
6. Realizaria testes na solução criada.
7. Se tudo estivesse funcionando corretamente, implementaria a solução.
8. Pensaria em uma forma de monitorar continuamente a solução criada.

### b) Quais tecnologias você usaria? Por quê?

**Resposta:**
Python, PostgreSQL, Redis, Celery, Pytest.

**Python:** Acredito que o Python seja uma boa escolha devido à familiaridade não apenas minha, mas também de todo o time com a tecnologia.

**PostgreSQL:** É um banco de dados sólido e confiável.

**Redis:** Acredito que um message broker seria útil nesse desafio.

**Celery:** Temos muito a ganhar ao usar o Celery neste projeto.

**Pytest:** É de suma importância testar nossa solução.

### c) Faça um esboço da arquitetura dessa solução.

**Resposta:**
CRM <-- Nossa Solução <-- ERP

### d) Você conseguiria estimar quanto tempo levaria essa implementação? Considere uma jornada de trabalho padrão, de 40 horas semanais, de segunda a sexta.

**Resposta:**
Como mencionei anteriormente, é uma tarefa muito desafiadora e depende muito do contexto do negócio, além do nível de experiência da equipe. Portanto, fazer uma estimativa precisa sem ter o contexto adequado seria incorreto.


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
```output
array([101, 102, 103, 104, 105])
```


### b) Existe uma forma mais eficiente de se resolver o item a)? Justifique sua resposta.

**Resposta:**
```python
lista_clientes_2 = set(df_a['id_cliente'])
display(lista_clientes_2)
```
```output
{101, 102, 103, 104, 105}
```
*Set é um tipo de dado do python, uma coleção desordenada onde não pode haver números repetidos, então basicamente ao transformar uma lista de **'id_cliente'** e um set ele elimina automaticamente as duplicatas, isso é mais eficiente em termos de memória, aqui está a definição de set segundo a documentação do **python**:*

*"5.4. Conjuntos*

*Python também inclui um tipo de dados para conjuntos, chamado set. Um conjunto é uma coleção desordenada de elementos, sem elementos repetidos. Usos comuns para conjuntos incluem a verificação eficiente da existência de objetos e a eliminação de itens duplicados. Conjuntos também suportam operações matemáticas como união, interseção,diferença e diferença simétrica.*

*Chaves ou a função set() podem ser usados para criar conjuntos." - [Documentação do python](https://docs.python.org/pt-br/3/tutorial/datastructures.html)* 


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
```output
id	id_cliente	data_contratacao	id_contrato	valor_contrato	data_cancelamento
0	1	101	2023-01-15	201	1000.00	2023-05-15
1	2	102	2023-02-20	202	1500.50	2023-06-20
2	3	103	2023-03-10	203	800.25	2023-07-10
3	4	104	2023-04-05	204	1200.75	2023-08-05
4	5	105	2023-05-12	205	2000.50	2023-09-12
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
```output
data_contratacao	clientes
0	2023-01-15	1
1	2023-02-20	1
2	2023-03-10	1
3	2023-04-05	1
4	2023-05-12	1
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
```output
data_cancelamento	clientes
0	2023-05-15	1
1	2023-06-20	1
2	2023-07-10	1
3	2023-08-05	1
4	2023-09-12	1
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
1. Criaria o repositório do projeto.
2. Clonaria o repositório para a minha máquina.
3. Criaria um ambiente virtual.
4. Instalaria as dependências necessárias.
5. Criaria o projeto.
```shell
django-admin startproject core .
```
6. Criaria o app.
```shell
python manage.py startapp agendamentos
```
7. Adicionaria os apps **agendamentos** e **rest_framework** ao **INSTALLED_APPS** em **core/settings.py**.
8. Criaria as migrações.
```shell
python manage.py makemigrations
```
9. Em seguida, aplicaria as migrações.
```shell
python manage.py migrate
```
10. Criaria os meus models.
11. Criaria os serializers.
12. Criaria as views.
13. Definiria as rotas.

### b) Escreva um esboço de código para os 4 endpoints solicitados.

**Resposta:**
```python
from rest_framework import status
from rest_framework import generics
from django.http import JsonResponse
from rest_framework import permissions
from agendamentos.models import Agendamentos
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from agendamentos.serializers import AgendamentosSerializer
from rest_framework.decorators import (
    api_view,
    permission_classes
)


class CadastrarAgendamento(generics.CreateAPIView):
    queryset = Agendamentos.objects.all()
    serializer_class = AgendamentosSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(http_method_names=['PATCH', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def cancelar_e_editar(request, pk):
    obj = get_object_or_404(klass=Agendamentos, id=pk)

    if request.method == 'PATCH':
        serializer = AgendamentosSerializer(
            instance=obj,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return JsonResponse(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'DELETE':
        obj.cancelamento = True
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListarAgendamentos(generics.ListCreateAPIView):
    queryset = Agendamentos.objects.all()
    serializer_class = AgendamentosSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AgendamentoEspecifico(generics.RetrieveAPIView):
    queryset = Agendamentos.objects.all()
    serializer_class = AgendamentosSerializer
    permission_classes = [permissions.IsAuthenticated]

```

### c) Como você implementaria a validação de não permitir agendar dois clientes no mesmo horário?

**Resposta:**
```python
def validate_data(self, value):
    if value < timezone.now():
        raise serializers.ValidationError(
            detail='O agendamento não pode ser feito no passado.',
            code=status.HTTP_400_BAD_REQUEST
        )

    if value not in get_horario_disponiveis(value.date()):
        raise serializers.ValidationError(
            'Esse horário não está disponível.'
        )

    return value
```

### d) Como você poderia processar requisições que tentam agendar dois clientes no mesmo horário?

**Resposta:**
*Você mencionou 'requisições', o que implica em mais de uma solicitação. Isso significa que uma delas será processada antes da outra. Assim que a primeira requisição tiver o seu agendamento registrado no banco de dados, a validação acima não permitirá outro agendamento no mesmo horário.*

### e) Apresente uma implementação do cálculo de vagas de agendamento. Suponha que cada atendimento demora 30 minutos para ser concluído e a clínica só funcione das 08:00 às 18:00, inclusive no horário do almoço. Desconsidere sábados e domingos.

**Resposta:**
```python
from typing import Iterable
from agendamentos.models import Agendamentos
from datetime import (
    date,
    datetime,
    timedelta,
    timezone
)


def get_horario_disponiveis(data: date) -> Iterable[datetime]:
    """
    Retorna uma lista com objetos do tipo datetime cujas datas são o mesmo dia
    passado (data) e os horários são os horário disponíveis para aquele dia,
    conforme outros agendamentos existem.
    """

    start = datetime(
        year=data.year,
        month=data.month,
        day=data.day,
        hour=8,
        minute=0,
        tzinfo=timezone.utc
    )
    end = datetime(
        year=data.year,
        month=data.month,
        day=data.day,
        hour=18,
        minute=0,
        tzinfo=timezone.utc
    )
    delta = timedelta(minutes=30)
    horario_disponiveis = set()

    while start < end:
        if not Agendamentos.objects.filter(data=start).exists():
            horario_disponiveis.add(start)
        start = start + delta

    return horario_disponiveis
```


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

Valor total de títulos emitidos em junho (mês 6) de 2020:
```sql
select
    sum(valor)
from base_de_dados

where (
    year(data_emissao) = 2020
    and month(data_emissao) = 6
)
```
```output
+-----------------+
|       sum(valor)|
+-----------------+
|540360.0000000052|
+-----------------+
```


Valor total de títulos vencimentos em junho (mês 6) de 2020:
```sql
select
    sum(valor)
from base_de_dados

where (
    year(data_vencimento) = 2020
    and month(data_vencimento) = 6
)
```
```output
+-----------------+
|       sum(valor)|
+-----------------+
|3076802.819998371|
+-----------------+
```


Quantidade de títulos emitidos em junho (mês 6) de 2020:
```sql
select
    count(data_emissao)
from base_de_dados

where (
    year(data_emissao) = 2020
    and month(data_emissao) = 6
)
```
```output
+-------------------+
|count(data_emissao)|
+-------------------+
|               5423|
+-------------------+
```


Quantidade de títulos vencimento em junho (mês 6) de 2020:
```sql
select
    count(data_vencimento)
from base_de_dados

where (
    year(data_vencimento) = 2020
    and month(data_vencimento) = 6
)
```
```output
+----------------------+
|count(data_vencimento)|
+----------------------+
|                 32082|
+----------------------+
```

*O motivo é que havia mais vencimentos agendados para junho (mês 6) de 2020 do que a emissão de boletos em junho (mês 6) de 2020.*

### b) Gerar um relatório com todos os clientes que tiveram títulos pagos em julho de 2020.

**Resposta:**
```sql
select
    id,
    data_emissao,
    data_vencimento,
    valor,
    status,
    pagamento_data,
    baixa_data,
    pagamento_valor
from base_de_dados

where (
    year(pagamento_data) = 2020
    and month(pagamento_data) = 7
)
```
```output
+------+-------------------+-------------------+-----+------+-------------------+-------------------+---------------+
|    id|       data_emissao|    data_vencimento|valor|status|     pagamento_data|         baixa_data|pagamento_valor|
+------+-------------------+-------------------+-----+------+-------------------+-------------------+---------------+
|110562|2019-06-05 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-22 00:00:00|2020-07-23 09:02:14|         110.06|
|112238|2019-06-06 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-31 00:00:00|2020-07-31 16:10:50|           99.9|
|119472|2019-06-11 00:00:00|2020-06-01 00:00:00| 79.9|     R|2020-07-31 00:00:00|2020-07-31 11:37:50|           79.9|
|120832|2019-06-12 00:00:00|2020-06-01 00:00:00| 79.9|     R|2020-07-01 00:00:00|2020-07-02 08:19:44|           82.1|
|131361|2019-06-24 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-02 00:00:00|2020-07-03 08:25:46|         102.52|
|131867|2019-06-24 00:00:00|2020-06-01 00:00:00| 79.9|     R|2020-07-03 00:00:00|2020-07-06 08:30:09|          82.12|
|136426|2019-06-26 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-20 00:00:00|2020-07-21 08:10:25|         102.88|
|137384|2019-06-26 00:00:00|2020-06-01 00:00:00| 79.9|     R|2020-07-03 00:00:00|2020-07-03 11:24:09|          81.55|
|151412|2019-07-08 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-06 00:00:00|2020-07-07 08:24:31|          102.6|
|153162|2019-07-09 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-09 00:00:00|2020-07-10 08:26:20|         102.66|
|161626|2019-07-16 00:00:00|2020-06-01 00:00:00| 79.9|     R|2020-07-06 00:00:00|2020-07-07 08:24:32|           82.2|
|163660|2019-07-19 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-31 00:00:00|2020-08-01 08:17:15|          111.5|
|171636|2019-07-25 00:00:00|2020-06-01 00:00:00| 79.9|     R|2020-07-16 00:00:00|2020-07-17 11:09:17|          87.34|
|173326|2019-07-29 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-01 00:00:00|2020-07-02 09:27:49|          106.7|
|175784|2019-07-30 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-08 00:00:00|2020-07-09 08:54:06|         107.82|
|176303|2019-07-30 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-03 00:00:00|2020-07-06 15:30:38|         107.02|
|183009|2019-08-06 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-23 00:00:00|2020-07-24 08:39:14|          110.2|
|183710|2019-08-06 00:00:00|2020-06-01 00:00:00| 69.9|     R|2020-07-10 00:00:00|2020-07-13 09:14:10|          75.58|
|188279|2019-08-09 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-01 00:00:00|2020-07-02 09:28:02|          106.7|
|190243|2019-08-12 00:00:00|2020-06-01 00:00:00| 99.9|     R|2020-07-03 00:00:00|2020-07-06 15:30:51|         107.02|
+------+-------------------+-------------------+-----+------+-------------------+-------------------+---------------+
```

### c) Encontre quantos boletos foram renegociados no mês de julho de 2020.

**Resposta:**
```sql
select
    count(id)
from base_de_dados

where (
    year(data_vencimento) = 2020
    and month(data_vencimento) = 7
    and (
        id_renegociacao is not null
        or id_renegociacao_novo is not null
    )
)
```
```output
+---------+
|count(id)|
+---------+
|        1|
+---------+
```

### d) Encontre o valor pago de juros de todos os boletos pagos em junho de 2020.

**Resposta:**

Valor total de juros pagos por boletos em junho de 2020:
```sql
select
    sum(valor) - sum(pagamento_valor) as juros_total
from base_de_dados

where (
    year(data_vencimento) = 2020
    and month(data_emissao) = 6
    and status = 'R'
)
```
```output
+------------------+
|       juros_total|
+------------------+
|-7964.829999999201|
+------------------+
```

Juros pagos por boletos em junho de 2020:
```sql
select
    valor - pagamento_valor as juros_total
from base_de_dados

where (
    year(data_emissao) = 2020
    and month(data_emissao) = 6
    and status = 'R'
)
```
```output
+--------------------+
|         juros_total|
+--------------------+
|                 0.0|
|-0.09999999999999432|
|                 0.0|
|  -4.409999999999997|
| -3.2299999999999898|
|                 0.0|
|                 0.0|
|                 0.0|
|                 0.0|
| -2.9099999999999966|
|               -4.25|
|  -7.429999999999993|
|                 0.0|
|                 0.0|
|                 0.0|
| -3.1499999999999915|
|                 0.0|
|                 0.0|
|  -4.709999999999994|
|                 0.0|
+--------------------+
```

### e) Encontre o id dos boletos que foram usados para gerar uma renegociação em junho de 2020.

**Resposta:**
```sql
select
    id,
    id_renegociacao,
    id_renegociacao_novo
from base_de_dados

where (
    year(data_emissao) = 2020
    and month(data_emissao) = 6
    and (
        id_renegociacao is not null
        or id_renegociacao_novo is not null
    )
)
```

```output
+------+---------------+--------------------+
|    id|id_renegociacao|id_renegociacao_novo|
+------+---------------+--------------------+
|400729|           null|               541.0|
|407525|           null|               542.0|
|407525|           null|               542.0|
+------+---------------+--------------------+
```
