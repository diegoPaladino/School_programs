import pdf2image
import os



print('########################################################################################################################################################################')
print(TimeoutError)

# Obtém o caminho da pasta
pasta = "//LAB/Users/Public/FOLHA DE PONTO/2023/VESPERTINO/10 - OUTURBO - NOVEMBRO/ATESTADO/VESPERTINO/ACLENIA NEIDE DE SOUZA"

# Obtém os nomes dos arquivos PDF
arquivos_pdf = os.listdir(pasta)

# Filtra os arquivos PDF
arquivos_pdf = [arquivo for arquivo in arquivos_pdf if arquivo.endswith(".pdf")]

# Converte os arquivos PDF para JPEG
for arquivo_pdf in arquivos_pdf:
    pdf = pdf2image.convert_from_path(os.path.join(pasta, arquivo_pdf))

    # Obtém o nome do arquivo JPEG
    nome_arquivo_jpeg = arquivo_pdf.replace(".pdf", ".jpeg")

    # Salva o arquivo JPEG
    pdf[0].save(os.path.join(pasta, nome_arquivo_jpeg))

# Converte os 2 primeiros arquivos PDF da pasta
for i in range(0, 2):
    pdf = pdf2image.convert_from_path(os.path.join(pasta, arquivos_pdf[i]))

    # Obtém o nome do arquivo JPEG
    nome_arquivo_jpeg = arquivos_pdf[i].replace(".pdf", ".jpeg")

    # Salva o arquivo JPEG
    pdf[0].save(os.path.join(pasta, nome_arquivo_jpeg))