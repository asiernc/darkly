# Bug Report - XSS Feedback input

##  Bug description

A Reflected XSS Injection is when the script is activated through a link, which sends a request to a website with a vulnerability that enables execution of malicious scripts.


## How did I find it?

We saw that when going into the media page there was the src parameter which was free to input.

First we tried to put the link as: "http://localhost:3000/index.php?page=media&src=<script>alert(1)</script>" but the script didn't execute as we wanted so we started looking into how to bypass the XSS Filters.

The way that worked for us is a link that redirects to a script that sets into the html encrypted in base64 to pass the filters.

## Steps to replicate

1. Go to:
	- http://localhost:3000/index.php?page=media&src=nsa

2. Instead of the src=nsa image we are going to put the script encoded as we sayed before:
	- http://localhost:3000/index.php?page=media&src=<a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">42</a>
