-- ==============================================================================
-- ETAPA 1: Automação de Data Quality:
-- Função dinâmica para identificar dados nulos ou vazios
-- em qualquer coluna de uma tabela selecionada.
-- ==============================================================================

CREATE OR REPLACE FUNCTION public.analisar_valores_vazios(nome_tabela TEXT)
RETURNS TABLE (
    nome_da_coluna TEXT,
    total_linhas_vazias BIGINT
) AS $$
DECLARE
    reg_coluna RECORD;
    query_contagem TEXT;
BEGIN
    -- Cria uma tabela temporária para consolidar o relatório
    CREATE TEMP TABLE IF NOT EXISTS resultado_analise (
        coluna TEXT,
        total_vazios BIGINT
    ) ON COMMIT DROP;
    
    TRUNCATE resultado_analise;

    -- Loop dinâmico que percorre todas as colunas da tabela
    FOR reg_coluna IN 
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name = nome_tabela AND table_schema = 'public'
    LOOP
        -- Query dinâmica com tratamento correto de aspas
        query_contagem := 'INSERT INTO resultado_analise SELECT ' || quote_literal(reg_coluna.column_name) || 
                          ', COUNT(*) FROM ' || quote_ident(nome_tabela) || 
                          ' WHERE ' || quote_ident(reg_coluna.column_name) || ' IS NULL OR ' || quote_ident(reg_coluna.column_name) || '::text = ''''';
        
        EXECUTE query_contagem;
    END LOOP;

    -- Retorna apenas as colunas que possuem dados vazios
    RETURN QUERY 
    SELECT coluna, total_vazios 
    FROM resultado_analise 
    WHERE total_vazios > 0;

END;
$$ LANGUAGE plpgsql;

-- ==============================================================================
-- Chamada da função:
-- ==============================================================================
SELECT * FROM public.analisar_valores_vazios('retail');
