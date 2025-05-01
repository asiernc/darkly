# Bug Report - Unrestricted File Upload

##  Bug description

Occurs when a web application allows users to upload files without proper validations, which can allow an attacker to upload malicious files, such as PHP scripts, instead of just images or text files.

## How did I find it?

While exploring the web page, I noticed that there was a form that allowed users to upload files through an image upload field. The form appeared to be intended for uploading images, but I didn't see any clear validation or restrictions on what types of files could be uploaded.

I decided to investigate the form further and tried changing the file being uploaded, replacing an image with a PHP file containing a simple script.

## Steps to replicate

1. curl -F "uploaded=@script.php;type=image/jpeg" -F "Upload=Upload" http://127.0.0.1:3000/index.php?page=upload

-F "uploaded=@script.php;type=image/jpeg" ==> simula el envio de un multi-part/form-data, subimos el archivo script.ph (@ indica que es desde el sistema local), y forzamos el mime type a imagen/jpeg para enganar al servidor por si solo valida la extension del archivo.

-F "Upload=Upload" ==> simulamos el mismo formulario de la web victima, con mismo nombre y mismo valor.

http://127.0.0.1:3000/index.php?page=upload ==> web victima


https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload