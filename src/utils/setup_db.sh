#This will not run as a script im just saving commands

sudo -i -u postgres

createdb "penguin" #pw=peng
createuser --interactive --pwprompt "peng-dev"

psql
ALTER USER "peng-dev" CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE "penguin" TO "peng-dev";


psql -h localhost -d penguin -U peng-dev

\dn
SET search_path TO public;
select * from users;