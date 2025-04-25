/*Consulta que retorna as tabelas com o maior volume de dados (em MB) para Oracle*/

select lower(SEGMENT_NAME) as "Nome da Tabela",
		BYTES/1024/1024 as "Tamanho em MB",
		tablespace_name as "Nome da Tablespace"
from dba_segments
where segment_type = 'TABLE'
order by BYTES desc