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
