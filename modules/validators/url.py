import re
from .utils import validator

ip_middle_octet = u"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5]))"
ip_last_octet = u"(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))"

regex = re.compile(
    u"^"
    u"(?:(?:https?|ftp)://)"
    u"(?:\S+(?::\S*)?@)?"
    u"(?:"
    u"(?P<private_ip>"
    u"(?:(?:10|127)" + ip_middle_octet + u"{2}" + ip_last_octet + u")|"
    u"(?:(?:169\.254|192\.168)" + ip_middle_octet + ip_last_octet + u")|"
    u"(?:172\.(?:1[6-9]|2\d|3[0-1])" + ip_middle_octet + ip_last_octet + u"))"
    u"|"
    u"(?P<public_ip>"
    u"(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])"
    u"" + ip_middle_octet + u"{2}"
    u"" + ip_last_octet + u")"
    u"|"
    u"(?:(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)"
    u"(?:\.(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)*"
    u"(?:\.(?:[a-z\u00a1-\uffff]{2,}))"
    u")"
    u"(?::\d{2,5})?"
    u"(?:/\S*)?"
    u"$", re.UNICODE
)

pattern = re.compile(regex)

@validator
def url(value, public=False):
    if not public: return pattern.match(value)
    match_result = pattern.match(value)
    if match_result.groupdict()['private_ip']: return False
    return match_result

