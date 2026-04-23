SELECT motivo_contato, COUNT(*) 
FROM atendimentos 
GROUP BY motivo_contato;
