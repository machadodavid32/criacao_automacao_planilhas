import openpyxl

workbook = openpyxl.Workbook()
del workbook['Sheet']
workbook.create_sheet('instrumentos')

# Como selecionar um sheet para trabalhar nele
sheet_instrumentos = workbook['instrumentos']

# sempre colocar cabeçalho(nome da coluna) se não existir ainda
sheet_instrumentos.append(['instrumento', 'marca', 'preco'])

# criando
workbook.save('Intrumentos.xlsx')


# Adicionando dados em uma planilha
sheet_instrumentos.append(['Instrumento 1', 'marca 1', '1200'])
sheet_instrumentos.append(['Instrumento 2', 'marca 2', '1300'])
sheet_instrumentos.append(['Instrumento 3', 'marca 3', '800'])
sheet_instrumentos.append(['Instrumento 4', 'marca 4', '2500'])

# Como passar dados por endereço da celula
sheet_instrumentos['A6'].value = 'Instrumento 5'
sheet_instrumentos['B6'].value = 'marca 5'
sheet_instrumentos['C6'].value = '4000'


workbook.save('Intrumentos.xlsx')