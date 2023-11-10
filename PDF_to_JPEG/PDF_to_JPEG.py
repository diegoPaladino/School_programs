import os
from pdf2image import convert_from_path



# PROVISORIO : APENAS ENQUANTO SE CONFECCIONA O CÓDIGO
print('########################################################################################################################################################################')


def convert_pdf_to_jpeg(pdf_folder, output_folder):
    # Contador para limitar a quantidade de arquivos convertidos
    count = 0

    for root, dirs, files in os.walk(pdf_folder):
        for file in files:
            if file.endswith(".pdf"):
                # Limita a conversão aos primeiros 2 arquivos PDF encontrados
                if count < 2:
                    pdf_path = os.path.join(root, file)
                    images = convert_from_path(pdf_path)
                    
                    for i, image in enumerate(images):
                        image_name = os.path.splitext(file)[0] + f'_page_{i + 1}.jpeg'
                        image_path = os.path.join(output_folder, image_name)
                        image.save(image_path, 'JPEG')
                    
                    count += 1
                else:
                    break

# Caminho da pasta que contém os PDFs
pdf_folder = r'\\LAB\Users\Public\FOLHA DE PONTO\2023\VESPERTINO\10 - OUTURBO - NOVEMBRO\ATESTADO\VESPERTINO\ACLENIA NEIDE DE SOUZA'

# Caminho da pasta onde você deseja salvar as imagens JPEG
output_folder = r'\\LAB\Users\Public\FOLHA DE PONTO\2023\VESPERTINO\10 - OUTURBO - NOVEMBRO\ATESTADO\VESPERTINO\ACLENIA NEIDE DE SOUZA\JPEGs'

convert_pdf_to_jpeg(pdf_folder, output_folder)
