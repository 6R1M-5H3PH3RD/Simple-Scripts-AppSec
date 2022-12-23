#Server-side template injection (SSTI) is a type of vulnerability that occurs when an application processes user-supplied input as a template, allowing an attacker to inject arbitrary code into the template and execute it on the server.
#This code checks for common template tags and payloads that may indicate an SSTI vulnerability. 
#It uses regular expressions to search for the template tags and simple string comparisons to check for the payloads.
#Keep in mind that this is a very basic SSTI detector and may not detect all possible SSTI vulnerabilities. 
#It is important to thoroughly test and validate user input to prevent SSTI vulnerabilities in your application.

import re

def detect_ssti(input_string):
    # Check for Jinja2 template tags
    if "{{" in input_string or "}}" in input_string:
        return True

    # Check for Django template tags
    if "{%" in input_string or "%}" in input_string:
        return True

    # Check for Twig template tags
    if "{{" in input_string or "}}" in input_string:
        return True

    # Check for PHP template tags
    if "<?=" in input_string or "?>" in input_string:
        return True

    # Check for common SSTI payloads
    payloads = [
        "{{ 7*7 }}",
        "{% if True %}True{% endif %}",
        "{{ ''.__class__.__mro__[2].__subclasses__() }}",
        "<?=system('id')?>"
    ]
    for payload in payloads:
        if payload in input_string:
            return True

    # No SSTI detected
    return False
