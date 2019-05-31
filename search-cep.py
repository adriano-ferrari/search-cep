from urllib.parse import urlencode
from urllib.request import Request, urlopen


def unescapeXml(s):
    s = s.replace('&lt;', '<')
    s = s.replace('&gt;', '>')
    s = s.replace('&amp;', '&')
    s = s.replace('&nbsp;', ' ')
    return s


def unescapeString(s):
    s = s.replace('\\r', '')
    s = s.replace('\\t', '')
    s = s.replace('\\n', '')
    return s


url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
post_fields = {'relaxation': '02989095', 'tipoCEP': 'ALL', 'semelhante': 'N'}

request = Request(url, urlencode(post_fields).encode())
result = urlopen(request).read()
result = str(result)

result = unescapeString(result)
result = bytes(result, "iso=8859-1").decode("unicode_escape")
result = unescapeXml(result)
print(result)