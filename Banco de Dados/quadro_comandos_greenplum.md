# Quadro de Resumo: Recuperação de Segmentos no Greenplum

| Prioridade | Comando | Função / O que faz | Indicação / Quando deve ser usado |
| :---: | :--- | :--- | :--- |
| **1** | `gprecoverseg -a` | **Recuperação Incremental** | **Primeira ação** após a queda de um segmento. Sincroniza apenas o delta (dados perdidos enquanto esteve fora) de forma rápida. |
| **2** | `gprecoverseg -ra` | **Rebalanceamento do Cluster** | **Após o sucesso do comando anterior (`-a` ou `-F`)**. Retorna os segmentos recuperados aos seus papéis originais (Primário/Mirror). |
| **3** | `gprecoverseg -F` | **Recuperação Total (Forçada)** | Quando a recuperação incremental (`-a`) falhar ou se o disco do segmento foi substituído/corrompido. Reconstrói o segmento do zero. |
| **4** | `gpstop -r -f` | **Reinício Rápido e Forçado** | **Cenário de emergência extrema**. Quando o cluster travar por completo (deadlock/exaustão de recursos) e não responder a outros comandos. |

*Nota: Monitore sempre o status e o progresso utilizando `gpstate -m` e `gprecoverseg -p`.*
