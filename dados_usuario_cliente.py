import openpyxl

workbook = openpyxl.Workbook() # criado planilha

workbook.create_sheet('funcionários') # criando uma pagina

sheet_funcionarios = workbook['funcionários'] # ativando uma folha

sheet_funcionarios.append(['nome', 'cargo', 'salario']) # fazendo as colunas

continuar = 's'
while continuar == 's':
    nome = input('Nome: ')
    cargo = input('Cargo: ')
    salario = input('Salario: ')
    sheet_funcionarios.append([nome, cargo, salario])
    continuar = input('Adicionar mais um funcionário? (s/n)')

workbook.save('Funcionários.xlsx')


