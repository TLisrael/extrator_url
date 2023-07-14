class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL está vazia")

    def get_url(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[indice_interrogacao+1:]
        return url_base
    
    def get_valor_parametros(self, parametro_busca):
        indice_parametro = self.get_url().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url()[indice_valor:]
            print(valor)
        else:
            valor = self.get_url()[indice_valor:indice_e_comercial]
        print(valor)
        return valor


url = ExtratorURL('bytebank.com/cambio?moedaOrigem=Dolar&moedaDestino=Real&quantidade=100')
valor_quantidade = url.get_valor_parametros('quantidade')

