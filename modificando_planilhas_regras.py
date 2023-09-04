import openpyxl

workbook = openpyxl.load_workbook('hockey-players.xlsx')
sheet_player_data = workbook['PlayerData']

for linha in sheet_player_data.iter_rows(min_row=2): # ou seja, a partir da linha 2
    if linha[2].value == 'Canada':
        linha[2].value == 'CANADA'  # ou seja, vai pegar a palavra canada e transformar em CANADA
    if linha[5].value >= 150: # vai pegar o itém peso na planilha e, caso seja > ou = que 150, vai escrever 'Divisãa A'
        linha[5].value = 'Divisão A'    

workbook.save('hockey_players_novo.xlsx')
        