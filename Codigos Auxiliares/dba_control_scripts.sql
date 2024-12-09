/*
 * Consultas de auxilio para controle e gestão dos recursos em Banco de Dados Oracle
*/

select a.spid as pid,
       b.sid as sid,
       b.serial# as serial#,
       b.machine as machine_name,
       b.username as  username,
       b.osuser as os_user,
       b.SQL_EXEC_START as start_time,
       b.program as program,
       s.sql_fulltext
from v$session b,
	 v$process a,
	 v$sqlarea s
where b.paddr = a.addr
	and type = 'USER'
	and b.status = 'ACTIVE'
	and b.sql_id = s.sql_id
order by to_number(spid);

select 'ALTER SYSTEM KILL SESSION ''' || b.sid || ', ' || b.serial# || ''' IMMEDIATE;' as kill_comand
from v$session b,
	 v$process a
where b.paddr = a.addr
	and b.status = 'ACTIVE'
	and b.osuser='user_name';

/*
 * O script para matar a seção é gerado automaticamente pela Query acima
 * */

ALTER SYSTEM KILL SESSION '52, 1367' IMMEDIATE;

/*
 * LOCKED TABLES QUERY
 * 
 * */
SELECT B.Owner,
		B.Object_Name,
		A.Oracle_Username,
		A.OS_User_Name,
		a.*
FROM V$Locked_Object A, All_Objects B
WHERE A.Object_ID = B.Object_ID;