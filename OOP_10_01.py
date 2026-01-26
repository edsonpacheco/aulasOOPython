import requests
import zipfile
import io

# Endereço da base de dados de consumo da UCI
url = "https://archive.ics.uci.edu/static/public/235/individual+household+electric+power+consumption.zip"

def baixar_dados(url_fonte):
    print("Iniciando download...")
    resposta = requests.get(url_fonte)  
    # O objeto 'resposta' contem o binario do arquivo
    com_zip = zipfile.ZipFile(io.BytesIO(resposta.content))
    com_zip.extractall("./dados_smart_grid")
    print("Dados extraídos com sucesso!")
# Execução

if __name__ == "__main__":
    baixar_dados(url)
