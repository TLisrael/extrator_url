# url = 'bytebank.com/cambio?moedaOrigem=Dolar&moedaDestino=Real&quantidade=100'


url = " "

# Sanitização de URL 
url = url.strip() # Remove espaços no início e no fim da string

# Validação de URL
if url == "":
    raise ValueError("A URL está vazia")

# Extrai a parte da URL que contém o protocolo e o host
url_base = url[0:19]
print(url_base)

# Encontra o índice do caractere '?' na URL
indice_interrogacao = url.find('?')

# Extrai a parte da URL após o '?', que contém os parâmetros
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Define o parâmetro que queremos buscar na URL
parametro_busca = 'moedaOrigem'

# Encontra o índice do início do parâmetro na URL
indice_parametro = url_parametros.find(parametro_busca)

# Calcula o índice do início do valor do parâmetro
indice_valor = indice_parametro + len(parametro_busca) + 1

# Encontra o índice do caractere '&' que marca o próximo parâmetro
indice_e_comercial = url_parametros.find('&', indice_valor)

# Verifica se o caractere '&' foi encontrado e extrai o valor do parâmetro
if indice_e_comercial == -1:
    # Se não encontrar, extrai até o final
    valor = url_parametros[indice_valor:]
    print(valor)
else:
    # Se encontrar, extrai até o caractere '&'
    valor = url_parametros[indice_valor:indice_e_comercial]
    print(valor)


# O find quando nao encontrar um valor, ele retorna -1
