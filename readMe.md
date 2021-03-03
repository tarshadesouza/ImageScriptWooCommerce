# Whats this for?
This script was made to change 'imagen' columns that have invalid image urls to valid ones.

## Invalid url example:
www.testimage.jpg - this will not be seen as a valid url in woocommerce importer it must be in valid format.

## Valid url example:
http://www.testimage.jpg - this will be seen as valid

# Running this script
- First open in vscode make sure venv has pandas installed
- From Root level (cd ImageScriptWooCommerce) run 'source bin/activate' to activate venv
- Run in terminal with 'python imageScript.py' 
- If script is run succesfully it should create a new file with the nomenclature 'cleanedData' + time and date creation 