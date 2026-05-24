-- Etapa 5: Calcular o índice de meses transcorridos desde a primeira compra
-- Calcular a distância em meses entre a data da venda atual e a data do cohort (primeira compra)

CREATE OR REPLACE VIEW v_atividades_cohort AS
SELECT 
    v.customerid,
    c.mes_cohort,
    DATE_TRUNC('month', v.invoicedate) AS mes_venda,
    -- Calcula a diferença em meses entre o mês da venda e o mês do cohort
    (EXTRACT(YEAR FROM age(DATE_TRUNC('month', v.invoicedate), c.mes_cohort)) * 12 + 
     EXTRACT(MONTH FROM age(DATE_TRUNC('month', v.invoicedate), c.mes_cohort)))::int AS indice_mes
FROM retail v
JOIN v_cohort_clientes c ON v.customerid = c.customerid;