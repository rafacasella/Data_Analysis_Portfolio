-- ==============================================================================
-- ETAPA 2: Data Processing (Tratamento dos Dados)
-- Tratar valores nulos e vazios sem perder informações.
-- ==============================================================================

-- Tratar a coluna 'description':
-- Como é um campo de texto, substituíremos vazios por um rótulo padrão.
UPDATE public.retail
SET description = 'Sem Descricao'
WHERE description IS NULL OR description = '';

-- Tratar a coluna 'customerid':
-- Imputar um ID padrão (zero: 0) que represente "Cliente Não Identificado".
UPDATE public.retail
SET customerid = 0
WHERE customerid IS NULL;