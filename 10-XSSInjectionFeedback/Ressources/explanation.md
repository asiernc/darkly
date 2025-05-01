# Bug Report - XSS Feedback input

##  Bug description

The comment input interprets HTML syntax. What does this mean?
It is not protected against HTML elements. For example, if I enter <b>asier</b> in the name field and submit it, the name appears in bold.


## How did I find it?

After many attempts to get the flag, I tried using curl, but I realized it was simpler to test directly in the web form.

First, I tried injecting an image tag to trigger an error with an onerror handler, like this: <img src=x onerror=alert('XSS')>. However, I noticed that this tag was completely stripped from the comment.

Then, I simply entered the word script, and surprisingly, that alone was enough to reveal the flag — no full script tag needed!

## Steps to replicate

1. Scroll down on the homepage and click on "Go to Leave a Feedback".
2. In the name or comment field, enter the word script.
3. Submit the form — the flag will be revealed.
