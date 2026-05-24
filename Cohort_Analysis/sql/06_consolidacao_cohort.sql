-- Etapa 6: Agrupamento final e contagem de clientes únicos retidos
-- Contar quantos clientes únicos realiazaram compras naquele período

SELECT 
    TO_CHAR(mes_cohort, 'YYYY-MM') AS cohort,
    indice_mes,
    COUNT(DISTINCT customerid) AS clientes_ativos
FROM v_atividades_cohort
GROUP BY mes_cohort, indice_mes
ORDER BY mes_cohort, indice_mes;