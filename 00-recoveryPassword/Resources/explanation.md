# Bug Report - Hidden input with sensitive data exposure 

##  Bug description

The vulnerability is that the web page has a hidden input field in the password recovery form. This field contains a hardcoded value (the administrator's email). By inspecting the source code (with tools such as “Inspect element” in the browser), any user can see this email and use it to initiate the password recovery process without prior knowledge. This is considered a Sensitive Information Exposure, because critical data (such as an administrator email) should never be visible or accessible from the client side, not even in hidden fields.

Also, if the “password recovery” process does not validate the user's identity well, it could fall into the category of Broken Authentication.

## How did I find it?

Although we do not have any login, we access the home page and see how there is a button to retrieve password, once inside is strange because we do not see any input to put our email, so we inspect element, and not only see that this hidden div, but also has the value hardcoded, not as a placeholder, but as a value, so we assume that this is the admin email. we press the submit button and magically, that was the admin email. We gained access.

## Steps to replicate

1. Press the signin button and press 'I forgot my password'.
2. Go to inspect in this page and see how the input for the recovery email is hidden.
3. Only needs 'change' the hardcoded email value.
4. Press submit button
