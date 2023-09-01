import openpyxl

workbook = openpyxl.Workbook() # criado planilha
del workbook['Sheet']
workbook.create_sheet('Vagas') # criando uma pagina

sheet_vagas = workbook['Vagas'] # ativando uma folha

sheet_vagas.append(['Empresa', 'Vaga', 'Data da Aplicação', 'Retorno']) # fazendo as colunas

continuar = 's'
while continuar == 's':
    nome = input('empresa: ')
    vaga = input('vaga: ')
    data = input('data da aplicação: ')
    retorno = input('retorno: ')
    sheet_vagas.append([nome, vaga, data, retorno])
    continuar = input('Adicionar mais uma vaga? (s/n)')

workbook.save('vagas python.xlsx')
