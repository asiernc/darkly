# Bug Report -  Open redirect

##  Bug description

The web application has a link that redirects the user based on a URL parameter (site=instagram). However, that parameter is not validated correctly. By changing the site value in the URL manually (e.g. to google or to an internal value like flag), you can make the web redirect wherever you want, or even access hidden internal pages like flag.
This is an Open Redirect, a vulnerability that can be used for phishing (redirecting to malicious sites) or, in this case, to move around the web without authorization.

## How did I find it?

When you are inspecting these 3 redirects to social websites, I notice that instead of putting the value already directly in the href, such as:
<a href="https://www.google.es"/>, is serving the redirects from index.php (server), and reviewing the field (href="index.php? page=redirect&site=instagram"), I notice that the instagram link is not there, so it is defined in page=redirect inside index.php, then investigating we see that the redirect is being served by the backend, trusting that the link will be defined in the backend, but the request is already entering the server, so we expose ourselves to be able to move through the server without restrictions.


## Steps to replicate

1. Go down in index page to the instagram icon or facebook.
2. Inspect element and see the <a> tag, change the last value (example: instagram => my-site.com).
3. Press the icon.
