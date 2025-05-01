# Bug Report - Directory Traversal Attack

##  Bug description

This is a type of vulnerability that allows an attacker to access files and directories located outside the main directory of the web application, meaning they can navigate through the file structure of a web server.

## How did I find it?

Knowing the type of attack, I attempted to navigate through directories. Noticing that all the website pages are served via the page key, I tried to see if directory traversal was possible by going up two levels. At first, a "wrong ??" alert appeared — a clue. Then, I continued adding '../' until I reached the root of the server's filesystem.


## Steps to replicate

1. put in the url path, a value for page, "?page=../../../../../../../etc/passwd"

## How to prevent the attack?

Use specific filesystem functions that correctly handle absolute and relative paths.
