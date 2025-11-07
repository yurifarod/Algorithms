/*Consultar dados sobre sessao*/
select pid as id,
		usename,
		application_name,
		client_addr,
		now() - query_start as tempo_execucao,
		state
from pg_stat_activity
where pid <> pg_backend_pid()
		and datname = 'nome_database';

/*Matar sessao*/
select pg_terminate_backend(pid) 
from pg_stat_activity 
WHERE pid <> pg_backend_pid() --nao matar minha propria sessao
		AND datname = 'nome_database';


/*Dez maiores taelas*/
WITH table_stats AS (
	select schemaname,
			tablename,
			pg_relation_size(schemaname || '.'|| tablename) as table_size,
			(pg_total_relation_size(schemaname || '.'|| tablename) - pg_relation_size(schemaname || '.'|| tablename)) as index_size,
			pg_total_relation_size(schemaname || '.'|| tablename) as total_size
	from pg_tables
)
select table_stats.schemaname,
		table_stats.tablename,
		pg_size_pretty(table_stats.table_size) as table_size,
		pg_size_pretty(table_stats.index_size) as index_size,
		pg_size_pretty(table_stats.total_size) as total_size
from table_stats
where table_stats.schemaname = 'public'
order by table_stats.total_size desc,
		table_stats.index_size desc,
		table_stats.table_size desc
limit 10;
