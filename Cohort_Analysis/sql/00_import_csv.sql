-- ==============================================================================
-- ETAPA 0: Inicialização do Ambiente:
-- Criar a estrutura da tabela 'retail' e importar a base bruta CSV.
-- ==============================================================================

-- Criação da tabela estruturada
CREATE TABLE IF NOT EXISTS public.retail (
    invoiceno TEXT,
    stockcode VARCHAR(30),
    description VARCHAR(50),
    quantity INTEGER,
    invoicedate TIMESTAMP WITHOUT TIME ZONE,
    unitprice NUMERIC(10,2),
    customerid INTEGER,
    country VARCHAR(30)
);

-- Importação do CSV (Utilizado em servidor local)
COPY public.retail 
FROM 'C:/downloads/online_retail.csv' 
WITH (
    FORMAT CSV, 
    HEADER true, 
    DELIMITER ',', 
    ENCODING 'UTF8'
);