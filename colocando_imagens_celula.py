import openpyxl
from openpyxl.drawing.image import Image
workbook = openpyxl.Workbook()


workbook.create_sheet('produtos') # criando página
sheet_produtos = workbook['produtos']
sheet_produtos.append(['item', 'imagem', 'preço']) # criando colunas

sheet_produtos['A2'].value = 'Celular' # adicionando informação a celula A2
sheet_produtos['C2'].value = '2500' # adicionando informação a celula C2


img = Image('image.jpg')

sheet_produtos.add_image(img, 'B2')

workbook.save('Produtos1.xlsx')

