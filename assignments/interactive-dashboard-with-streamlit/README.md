# 📘 Assignment: Interactive Dashboard with Streamlit

## 🎯 Objective

Construa um dashboard web interativo em Python com Streamlit para explorar dados agregados de participação em clubes escolares. Você praticará leitura de CSV, filtros, métricas e visualizações conectadas aos dados selecionados.

## 📝 Tasks

### 🛠️ Load and Explore the Dataset

#### Descrição
Use o arquivo `data.csv` fornecido para carregar os dados no scaffold `starter-code.py` e conhecer suas colunas. Antes de executar o app pela primeira vez, instale as dependências e inicie o Streamlit no terminal.

```bash
python -m pip install streamlit pandas
python -m streamlit run starter-code.py
```

#### Requisitos
O dashboard deve:

- Carregar `data.csv` a partir da pasta da assignment.
- Mostrar uma prévia dos dados e explicar o significado das colunas `month`, `club`, `category`, `attendance` e `sessions`.
- Usar os dados agregados fornecidos; não inserir informações pessoais de alunos.


### 🛠️ Add Interactive Filters

#### Descrição
Adicione controles na barra lateral para selecionar uma categoria de clube e um clube. Inclua uma opção para mostrar todos os valores em cada filtro e aplique as seleções aos dados antes de apresentar os resultados.

#### Requisitos
O dashboard deve:

- Permitir filtrar por categoria e por clube.
- Atualizar a tabela e os resultados quando qualquer filtro mudar.
- Continuar funcionando quando a combinação de filtros não retornar linhas, exibindo uma mensagem clara.


### 🛠️ Present Metrics and Charts

#### Descrição
Resuma os dados filtrados para que alguém da escola consiga comparar a participação nos clubes e acompanhar sua variação ao longo dos meses.

#### Requisitos
O dashboard deve:

- Exibir o total de participações registradas, o número de clubes no recorte e o total de encontros realizados.
- Mostrar um gráfico de barras que compare as participações por clube.
- Mostrar um gráfico de linha com as participações agregadas por mês.
- Atualizar métricas e gráficos de acordo com os filtros selecionados.