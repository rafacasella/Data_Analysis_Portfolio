-- Etapa 7: Calcular o percentual (%) de retenção por Cohort

WITH cohort_base AS (
    -- Reutiliza a lógica de agrupamento para trazer os números absolutos
    SELECT 
        TO_CHAR(mes_cohort, 'YYYY-MM') AS cohort,
        indice_mes,
        COUNT(DISTINCT customerid) AS clientes_ativos
    FROM v_atividades_cohort
    GROUP BY mes_cohort, indice_mes
),
cohort_com_total_inicial AS (
    -- Usa a função FIRST_VALUE para encontrar a quantidade de clientes no Índice 0 (Mês Inicial)
    SELECT 
        cohort,
        indice_mes,
        clientes_ativos,
        FIRST_VALUE(clientes_ativos) OVER(
            PARTITION BY cohort 
            ORDER BY indice_mes
        ) AS total_clientes_inicial
    FROM cohort_base
)
-- Calcula o percentual arredondado com duas casas decimais
SELECT 
    cohort,
    indice_mes,
    clientes_ativos,
    total_clientes_inicial,
    ROUND((clientes_ativos::numeric / total_clientes_inicial::numeric) * 100, 2) AS percentual_retencao
FROM cohort_com_total_inicial
ORDER BY cohort, indice_mes;