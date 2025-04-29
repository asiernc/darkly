# Bug Report - Insecure Cookie-Based Authentication  Broken Access Control

##  Bug description

By manually modifying the hidden value attached to a form, it is possible to access restricted functions due to lack of server validation.

## How did I find it?

Looking at the cookies that sets the web in our browser, we see one with a strange name, which seems more a boolean than a cookie, called 'i_am_admin'????
with a value of b326b5062b2f0e69046810717534cb09, we try and pass it through an md5 decryptor, and we get 'false'. 
That's it, we encrypt true in md5 => b326b506262b2f0e69046810717534cb09 and try to update the web. 
We became admin overnight.

## Steps to replicate

1. Open devTools and go to 'Application' => cookies
2. Change the value for true in md5 (b326b506262b2f0e69046810717534cb09)
3. Refresh the page
