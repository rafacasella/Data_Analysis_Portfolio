-- Etapa 4: Identificar o mês de início (Cohort) de cada cliente
-- Descobrir a data da primeira compra absoluta de cada customerid,
-- esse será o grupo (cohort) ao qual o cliente pertencerá

CREATE OR REPLACE VIEW v_cohort_clientes AS
SELECT 
    customerid, 
    MIN(DATE_TRUNC('month', invoicedate)) AS mes_cohort
FROM retail
GROUP BY customerid;