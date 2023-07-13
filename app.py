
# Uma URL pode ser dividida em diversas partes:
# protocolo: http
# host: bytebank.com
# caminho: /cambio
# Query String: ?moedaOrigem=real&moedaDestino=dolar&quantidade=100

url = 'bytebank.com/cambio?moedaOrigem=real'
url_base = url[0:19]
print(url_base)

url_parametros = url[20:36]
print(url_parametros)

# A função find() retorna a posição do caractere passado como parâmetro
# Se o caractere não for encontrado, a função retorna -1
indice_interrogacao = url.find('?')
print(indice_interrogacao)

url_base = url[0:indice_interrogacao]
print(url_base)

# A função split() divide uma string em uma lista de strings
# O parâmetro passado é o caractere que será usado como separador
url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)

# A função replace() substitui um caractere por outro
url = 'bytebank.com/cambio?moedaOrigem=real'
url = url.replace('?', '&')
print(url)

# A função split() divide uma string em uma lista de strings
# O parâmetro passado é o caractere que será usado como separador
url_parametros = url.split('&')
print(url_parametros)

