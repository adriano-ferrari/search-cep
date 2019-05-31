from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
post_fields = {'relaxation': '02989095', 'tipoCEP': 'ALL', 'semelhante': 'N'}

request = Request(url, urlencode(post_fields).encode())
result = urlopen(request).read()
result = str(result)

print(result)