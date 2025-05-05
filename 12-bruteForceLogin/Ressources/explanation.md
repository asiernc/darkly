# Bug Report - Brute Force Login

##  Bug description

The authentication system allows unlimited login attempts without applying security measures such as account lockout, delays between attempts or captchas. This allows an attacker to perform a brute force attack to guess passwords.

## How did I find it?

I discovered the bug while performing security tests on the login form. I used an automated script to submit multiple username/password combinations, and the system did not block the attempts or show any mitigation measures.

## Steps to replicate

1. Access the login form at the URL: `http://127.0.0.1:3000/index.php?page=signin`.
2. Use a brute-force script (e.g. with Python and the `requests` library) to submit multiple username/password combinations.
3. Note that the system allows unlimited attempts without locking the account or applying delays.
4. If a list of common passwords is used, it is possible to guess the correct password in a reasonable time.

