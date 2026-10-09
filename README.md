```
Usage:

python soX.py -u <url> -l <userlist> -p <passlist> [-x <proxylist>]

Arguments:

-u, --url: Specifies the target URL of the login form where the POST request will be sent.
-l, --userlist: Path to the text file containing the list of usernames to be tested.
-p, --passlist: Path to the text file containing the list of passwords to be tested.
-x, --proxylist: (Optional) Path to a text file containing a list of proxies. Proxies are rotated during the attack to bypass rate limiting.
Requirements:

Python 3.x
requests library installed via pip
```
