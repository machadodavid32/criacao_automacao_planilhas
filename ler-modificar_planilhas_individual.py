import openpyxl

workbook = openpyxl.load_workbook('hockey-players.xlsx') # caso este arquivo tivesse em algum outro lugar do computador, passar caminho completo
sheet_player_data = workbook['PlayerData'] # planilha PlayerData
print(sheet_player_data['D3'].value) # vai imprimir a informação na celula escolhida
sheet_player_data['D3'].value = 'Amanda'  # vai substituir a informação na celula e colocar esta nova.

