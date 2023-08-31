import openpyxl


# para consultar as formulas em excel, visite: https://exceljet.net/formulas


workbook = openpyxl.Workbook() # criado planilha
workbook.create_sheet('demo funções') # criado uma folha
sheet_funcoes = workbook['demo funções'] # Ativando a folha

sheet_funcoes['A1'].value = '=SUM(5,5)'  # 5 mais 5
sheet_funcoes['A2'].value = '=SUM(5,10)'  
sheet_funcoes['A3'].value = '=SUM(5,5)'  
sheet_funcoes['A4'].value = '=AVERAGE(10, 50)'  # MEDIA
sheet_funcoes['A5'].value = '=MIN(A1,A3)'  #  VALOR MINIMO ENTRE AS CELULAS SELECIONADAS
sheet_funcoes['A6'].value = '=SUM(5,5)'  #
sheet_funcoes['A7'].value = '=SUM(5,5)'  #

workbook.save('formulas.xlsx')