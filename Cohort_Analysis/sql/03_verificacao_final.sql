-- ==============================================================================
-- ETAPA 3: Quality Assurance (Validação Final de Qualidade de Dados)
-- Reexecutar a auditoria automatizada para comprovar que a base 
-- 	de dados está 100% limpa e pronta para a análise.
-- ==============================================================================

SELECT * FROM public.analisar_valores_vazios('retail');