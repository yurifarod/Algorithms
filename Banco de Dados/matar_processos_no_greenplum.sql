select pg_terminate_backend(pid) 
from pg_stat_activity 
WHERE pid <> pg_backend_pid() --nao matar minha propria sessao
		AND datname = 'nome_database';