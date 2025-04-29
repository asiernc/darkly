# Bug Report - Parameter Tampering

##  Bug description



## How did I find it?

With the same logic that we used in the recovery Password (hidden components), there is a section in the web of surveys, we enter.
We see a very simple order form, range values from 1-10 and we don't find a submit, when we change a value the form auto-sends. ??
We proceed to devtools and open source code. We see that in fact it is not a single form, they are 5, each one with a post with an onchange, so automatically when we select
a value the request will be sent to the server. And wanting to test if the form values are not only checked in the frontend, but also in the backend, to reject or not the request, and check that the value sent is within the range provided. To our surprise, we modify the value of the 2 to '42', we select the 2 in the form, and as this the onChange event, automatically we get the flag.

## Steps to replicate

1. Go to surveys and open devTools
2. Search the first input range element, change de value in the html source code, and select this value.
3. Automatic sends the flag.
