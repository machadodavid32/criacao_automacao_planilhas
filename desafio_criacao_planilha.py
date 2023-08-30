import openpyxl

workbook = openpyxl.Workbook()
del workbook['Sheet']
workbook.create_sheet('produtos')

# Como selecionar um sheet para trabalhar nele
sheet_produtos = workbook['produtos']

# sempre colocar cabeçalho(nome da coluna) se não existir ainda
sheet_produtos.append(['computador', 'ano', 'preco'])

# criando
workbook.save('Computadores.xlsx')


# Adicionando dados em uma planilha
sheet_produtos.append(['Computador 1', '2001', '500'])
sheet_produtos.append(['Computador 2', '2002', '1500'])
sheet_produtos.append(['Computador 3', '2003', '133'])
sheet_produtos.append(['Computador 4', '2005', '1242'])


workbook.save('Computadores.xlsx')