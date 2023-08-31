import openpyxl

workbook = openpyxl.Workbook()
del workbook['Sheet']
workbook.create_sheet('instrumentos')

# Como selecionar um sheet para trabalhar nele
sheet_instrumentos = workbook['instrumentos']

# sempre colocar cabeçalho(nome da coluna) se não existir ainda
sheet_instrumentos.append(['instrumento', 'marca', 'preco'])

# criando
workbook.save('Intrumentos1.xlsx')


# Adicionando dados em uma planilha
sheet_instrumentos.append(['Instrumento 1', 'marca 1', '1200'])
sheet_instrumentos.append(['Instrumento 2', 'marca 2', '1300'])
sheet_instrumentos.append(['Instrumento 3', 'marca 3', '800'])
sheet_instrumentos.append(['Instrumento 4', 'marca 4', '2500'])

workbook.save('Intrumentos1.xlsx')
'''
sheet_instrumentos.delete_rows(3) # deletando a linha 3

workbook.save('Intrumentos1.xlsx')

sheet_instrumentos.delete_rows(2, 4) # deletando desde a linha 2 até a 4

sheet_instrumentos.delete_cols(1) # Deletando coluna 1 - pode ser varias colunas

'''

# Apagando apenas uma celula

del workbook['instrumentos']['B2']  # excluindo a celula B2
workbook.save('Intrumentos1.xlsx')