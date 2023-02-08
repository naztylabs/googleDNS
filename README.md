# Update Google DNS using Python
A simple python script that will accept multiple domains to update with current external IPs. 

## Some things to note...
- The script is currently set up to use the requests library. Please ensure that it is installed prior to running (pip install requests)
- Currently only one domain is set up, more can be added by uncommenting the included elif statement.

## How to use
- Extract the folder somewhere safe on your server/computer (i.e. C:\googleDNS)
- Once extracted, open updateGoogleDNS.py in your favorite text editor.
- Fill in the domain1 variable, the username variable, and the password variable with information from your Google Dynamic DNS
- Run the python file or use one of the included shell/batch files to kick start it
- Verify the file is running correctly by checking the response.log file (may take 2 runs for file to generate)