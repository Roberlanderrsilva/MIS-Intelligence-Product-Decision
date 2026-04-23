# 📖 Dicionário de Dados & Regras de Negócio

Este documento descreve a estrutura dos dados utilizados e as premissas legais de privacidade (LGPD).

| Coluna | Tipo | Descrição | Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `ID_Chamado` | UUID | Identificador único | Chave primária para rastreio de ticket. |
| `Data_Hora` | Datetime | Timestamp da chamada | Usado para cálculo de Nível de Serviço. |
| `ID_Agente` | String | Hash/ID do Colaborador | Anonimizado conforme diretrizes da LGPD. |
| `Motivo_Contato` | String | Categoria do problema | Input primário para o Time de Produto. |
| `Plataforma` | String | OS do Usuário | Filtro para análise de bugs sistêmicos. |

**Nota sobre LGPD:** Todos os dados de identificação pessoal (PII) de clientes foram removidos deste dataset simulado, utilizando apenas IDs transacionais.
