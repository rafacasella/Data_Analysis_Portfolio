# 📉 Análise de Cohort e Retenção Bancária

## 📌 Sobre o Projeto
Este projeto realiza uma análise estatística e comportamental aprofundada sobre a retenção e o engajamento de correntistas utilizando dados históricos de uma instituição financeira. O objetivo principal é mapear a jornada dos clientes ao longo do tempo através de uma matriz clássica de Cohort, permitindo identificar os períodos críticos de evasão precoce e fornecer insumos estratégicos para que a equipe de negócios aumente o LTV (*Lifetime Value*).

O projeto foi estruturado a partir de um tratamento e modelagem de dados robustos diretamente em ambiente SQL (PostgreSQL), sendo posteriormente integrado ao Power BI para uma visualização dinâmica e interativa das curvas de decaimento de clientes.

## 🛠️ Tecnologias e Ferramentas
* **Banco de Dados:** PostgreSQL (Armazenamento, validação e modelagem da matriz de cohort).
* **Interface de Queries:** pgAdmin 4 (Escrita de scripts, funções de auditoria e otimização).
* **Visualização de Dados:** Power BI Desktop (Modelagem de dados, conexão nativa e painel interativo).
* **Linguagem:** SQL (Extração, tratamento de dados nulos e cálculo de índices de intervalo).

## 🔍 Engenharia de Dados e Consultas SQL
Para otimizar a performance do Power BI, toda a transformação pesada dos dados foi realizada diretamente na fonte através do PostgreSQL. A lógica implementada nos scripts estruturados segue as seguintes etapas:

1. **Auditoria de Qualidade:** Criação de uma função customizada para checar valores vazios no dataset e posterior tratamento de *missing values*.
2. **Definição do Cohort:** Identificação da data da primeira compra/movimentação absoluta de cada `CustomerID`, estabelecendo o grupo fixo do cliente.
3. **Cálculo de Intervalo de Tempo:** Cálculo da distância em meses entre a venda atual e o cohort inicial (Mês 0: primeira interação; Mês 1: primeiro mês subsequente, etc.).
4. **Agregação e Métrica:** Consolidação final com a contagem de clientes únicos ativos por período para gerar o percentual exato de retenção.

## 📊 Como Visualizar o Projeto
1. O arquivo do relatório do Power BI está disponível na pasta `/dashboard`.
2. Para que o painel funcione perfeitamente na sua máquina, é necessário abrir o arquivo e alterar as credenciais da fonte de dados para apontar para o seu próprio servidor PostgreSQL.
3. *(Opcional)* Você também pode visualizar o comportamento do painel através dos arquivos `dashboard_final.png` ou do arquivo animado `.gif` contidos na pasta de apresentação.

## 🗄️ Carga do Banco de Dados
1. Restaure a estrutura e os dados retail utilizando o arquivo localizado em `data/banco_de_dados.sql` no seu PostgreSQL.
2. Execute os scripts analíticos da pasta `sql` através do pgAdmin 4 para processar e estruturar a visão final do cohort.

***
📌 Este projeto faz parte do meu Portfólio de Análise e Engenharia de Dados.
