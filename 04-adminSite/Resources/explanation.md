# Bug Report - admin site with public password

##  Bug description

The system exposes a `.htpasswd` file in a public directory, which allows an attacker to obtain administrator credentials. This file contains a password hash that can be easily decrypted using online tools, compromising the security of the administration site.

## How did I find it?

Returning to the robots.txt file, we had seen another directory not to index, /whatever/ if we do a curl (curl https://target.com/whatever/.htpasswd) we see that there is a link to a file called htpasswd. Doing a simple search we see that it is a file that together with another (htaccess) is used in Apache servers to protect with passwords directories on a website.
It includes username and password, <user:password>.
We visit any encryptor, md5 hash decryptor ("https://md5decrypt.net/en/") and we put this password of the file htpasswd that is => root:437394baff5aa33daa618be47b75cb49
and we obtain, root=qwerty123@
we go to which we deduce that is the link of admin login, we put user and password and.... capum! we have flag!

## Steps to replicate

1. curl http://127.0.0.1:3000/whatever/htpasswd
2. Decrypt the hash
3. Go to http://127.0.0.1:3000/admin
4. Login with this credentials
