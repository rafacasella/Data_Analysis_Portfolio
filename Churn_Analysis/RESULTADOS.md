## 📈 Análise do Modelo de Regressão Logística

### 📊 Resumo de Qualidade do Modelo
* **Ajuste Sólido:** O **Pseudo R-squ. (0.4321)** indica que o modelo explica cerca de 43,2% da variabilidade do Churn. Para dados de comportamento humano e retenção, este é um valor considerado muito bom.
* **Significância Geral:** O **LLR p-value (0.000)** mostra que o modelo como um todo é altamente confiável e estocasticamente superior a um modelo sem variáveis.

---

### 🔥 Principais Alavancas do Churn (Fatores de Risco)
Estas variáveis aumentam a chance de o cliente cancelar o serviço (coeficientes positivos com $P > |z|$ menor que 0.05):

* **Ligações para o Suporte (`suportcalls` = +0.3313):** É um dos maiores preditores de atrito. Cada ligação adicional para o suporte eleva consideravelmente o risco de cancelamento. Isso indica problemas na experiência do produto ou fricção no atendimento.
* **Contrato Mensal (`contractlength_Monthly` = +0.3209):** Clientes com planos mensais têm uma propensão drasticamente maior ao Churn em comparação com a categoria de referência (Anual). A falta de um compromisso de longo prazo facilita a saída.
* **Atrasos de Pagamento (`paymentdelays` = +0.2132):** Cada dia adicional de atraso no pagamento aumenta de forma muito clara o risco de Churn. Inadimplência ou problemas financeiros do cliente são fortes sinais de abandono iminente.
* **Tempo de Casa (`tenure` = +0.0354) & Idade (`age` = +0.0195):** Curiosamente, o risco de Churn aumenta levemente à medida que o cliente fica mais velho e acumula mais tempo de contrato.

---

### 🛡️ Fatores de Retenção (Fatores de Proteção)
Estas variáveis diminuem a chance de o cliente cancelar o serviço (coeficientes negativos com $P > |z|$ menor que 0.05):

* **Gênero Masculino (`gender_Male` = -1.1363):** É o coeficiente negativo mais forte. Os homens neste dataset têm uma chance significativamente menor de Churn em comparação às mulheres.
* **Frequência de Uso (`usagesfrequency` = -0.0592):** Quanto mais vezes o cliente utiliza a plataforma/serviço, menor é o risco de cancelamento. Engajamento retém clientes.
* **Contrato Trimestral (`contractlength_Quarterly` = -0.1741):** Comparado ao plano Anual, o plano Trimestral apresenta um menor risco de Churn neste modelo.
* **Planos Premium e Standard:** Ambos reduzem o Churn em comparação ao plano *Basic*. O plano `Premium` (-0.0949) protege um pouco mais o cliente do que o plano `Standard` (-0.0576).
* **Gasto Total (`totalspend` = -0.0010):** Clientes que investiram mais dinheiro historicamente têm uma propensão ligeiramente menor a cancelar (efeito sutil devido à escala do valor, mas estatisticamente relevante).

---

### ⚠️ Variáveis Sem Relevância Estatística
* **Última Interação (`lastinteraction` = -0.0010):** O valor de $P > |z|$ é 0.452 (muito maior que o limite padrão de 0.05). Isso significa que essa variável **não tem relevância estatística** para explicar o Churn neste modelo. O número de dias desde o último contato não faz diferença para o cancelamento aqui.

---

### 💡 Recomendações de Negócio Baseadas nos Dados
* **Ações de Suporte:** Criar alertas automáticos acionados a partir da 3ª ou 4ª ligação do cliente ao suporte para a equipe de *Customer Success* intervir ativamente.
* **Migração de Contratos:** Criar campanhas e descontos para migrar clientes do plano Mensal para o Trimestral ou Anual.
* **Régua de Cobrança:** Desenvolver lembretes amigáveis automáticos de pagamento antes da data de vencimento para conter a inadimplência antes que ela vire Churn.
