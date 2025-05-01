# Bug Report - Referer & User-Agent Header Check (Bypass via Header Injection)

##  Bug description

The application reveals a hidden flag only when two specific HTTP headers are present:  
- `Referer: https://www.nsa.gov/`  
- `User-Agent: ft_bornToSec`  

By crafting a request with these headers (e.g., using `curl`), the flag is displayed.  
This is a logic flaw, as it relies on client-controlled headers for access control, which can be easily spoofed.


## How did I find it?

In the main page, scroll down and click on the BornToSec copyright.
Redirects you to http://127.0.0.1:3000/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
In this page, in the source code, you can extract two ideas: 
	<!--
		You must come from : "https://www.nsa.gov/".
	-->
and,
	<!--
		You must come from : "https://www.nsa.gov/".
	-->

Using a curl you can obtain the flag.

## Steps to replicate

1. Two things: Referer: https:www.nsa.gov || User-agent(browser): ft_bornToSec
2. Open terminal and type the following command:
	curl -A ft_bornToSec -e https://www.nsa.gov/ http://localhost:3000/index.php\?page\=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f | grep flag

Tip: -A == User-Agent && -e == --referer
