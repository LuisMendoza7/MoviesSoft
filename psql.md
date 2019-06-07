### PostgreSQL Installation
##### 1. Installation

First, we need to install postgresql to start.
```
$ sudo apt-get update
$ sudo apt-get install postgresql
```

##### 2. Postgres User

Once the installation have finished, we can start the configuration.

By default, PostgreSQL create an user called **postgres**, and that user is associated by default. To access to that user we type:
```
$ sudo -i -u postgres
```
Then we can access to PostgreSQL Shell with:
```
$ psql
```
And our shell will change to PostgreSQL shell:
```
postgres=#
postgres=# \q             #exit
```
An easy way to enter to PostgresSQL is:
```
$ psql postgres
postgres=#
```
##### 3. Create a new Role
Right now we have the **postgres** role, but we need to create our own role to interact with PostgreSQL:

If we have started our session with **postgres**, we can create our role.
```
postgres@server createuser --interactive
```
After that, the shell will ask us some information:
```
Output:
Enter name of role to add: rolname
Shall the new role be a superuser? (y/n) y
```


##### 4. Create a database
We login with the postgres user, then, to create a database we type:
```
postgres@server createdb dbname
```
Another way to create it is:
```
$ sudo -u postgres createdb dbname
```
##### 5. Access to the database
Once we have created the database, we can access to it, we login with the user and then, start the sqlshell:
```
postgres=#
```
If we want to know if we are property connected, we can use:
```
postgres=# \conninfo
You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
```
To connect to the database, we type:
```
postgres=# \c dbname
You are now connected to database "dbname" as user "rolname".
```

##### 6. Create and delete tables
If we are connected in a database, we can create and delete tables. PostgreSQL use SQL syntax to any modification to a database.

For example:
```
CREATE TABLE name (col1 coltype (length), col2 coltype (length));
```
Never forget to close a SQL code with **;**

To check our tables in a database we can type:
```
postgres=# \dt
```
And a simplified view of our database will be shown
```
Output
List of relations
Schema |    Name    | Type  | Owner
--------+------------+-------+-------
public |    name    | table | rolname
(1 row)
```


### PostgreSQL Migration
##### 1. Postgres password
By defaul the postgres user does not have a password, and this may cause some conflicts in the connection or other actions.

Inside `psql` sheel we can update or modify our password:
```
postgres=# ALTER USER postgres PASSWORD 'password';
ALTER ROLE            #Message of successful modify
```
##### 2. Migration File
If we want to migrate a database model to PostgreSQL, first, we need to create our database(with the same name) in PostgreSQL and then, modify our migrations file.

First of all, we need to start our migration, the migration init must have the initial database.
```
$ python migrate.py db init
```
Then after we have started the migration, we have to modify our file, adding our paths and configuration of PostgreSQL:
```python
POSTGRES = {
'user': 'postgres',
'pw': 'password',
'db': 'dbname',
'host': 'localhost',
'port': '5432'
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
```
**Do not forget to comment or delete the path of the other database.**

After modifying our migration file, we can continue:
```
$ python migrate.py db migrate
$ python migrate.py db upgrade
```
After finishing with the migration, we can access to our database in PostgreSQL
