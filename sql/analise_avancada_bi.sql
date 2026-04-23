-- Relatório Gerencial para Tableau e Power BI
WITH Performance_Agentes AS (
    SELECT 
        agente,
        COUNT(*) as total_chamados,
        AVG(tempo_atendimento) as tma,
        SUM(CASE WHEN satisfacao >= 4 THEN 1 ELSE 0 END) as promotores
    FROM tb_geral_mis
    GROUP BY agente
)
SELECT 
    agente,
    total_chamados,
    tma,
    (promotores * 100.0 / total_chamados) as percentual_csat
FROM Performance_Agentes
WHERE total_chamados > 10
ORDER BY percentual_csat DESC;
