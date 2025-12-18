"""
Write a function which detects if entered string is http/https domain name with optional slash at the and
Restriction: use re module
Note that address may have several domain levels
    >>>is_http_domain('http://wikipedia.org')
    True
    >>>is_http_domain('https://ru.wikipedia.org/')
    True
    >>>is_http_domain('griddynamics.com')
    False
"""
import re


def is_http_domain(domain: str) -> bool:
    """Function which checks if string is http/https domain name"""

    # Match the domain labels to be between 1 and 63 characters
    regex_pattern = r'https?://([1-9|a-z]){1,63}(\.([1-9|a-z]){1,63})+/?'
    if re.fullmatch(regex_pattern, domain.lower()):
        return True

    return False
