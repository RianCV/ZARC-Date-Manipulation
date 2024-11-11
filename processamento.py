import pandas as pd
from datetime import datetime

#colocando os numeros decendiais em suas respectivas datas
periodos_inicio = {} 
periodos_inicio[0] = "-"
periodos_inicio[1] = datetime.strptime("01/01", "%d/%m").date().strftime("%d-%b")
periodos_inicio[2] = datetime.strptime("11/01", "%d/%m").date().strftime("%d-%b")
periodos_inicio[3] = datetime.strptime("21/01", "%d/%m").date().strftime("%d-%b")
periodos_inicio[4] = datetime.strptime("01/02", "%d/%m").date().strftime("%d-%b")
periodos_inicio[5] = datetime.strptime("11/02", "%d/%m").date().strftime("%d-%b")
periodos_inicio[6] = datetime.strptime("21/02", "%d/%m").date().strftime("%d-%b")
periodos_inicio[7] = datetime.strptime("01/03", "%d/%m").date().strftime("%d-%b")
periodos_inicio[8] = datetime.strptime("11/03", "%d/%m").date().strftime("%d-%b")
periodos_inicio[9] = datetime.strptime("21/03", "%d/%m").date().strftime("%d-%b")
periodos_inicio[10] = datetime.strptime("01/04", "%d/%m").date().strftime("%d-%b")
periodos_inicio[11] = datetime.strptime("11/04", "%d/%m").date().strftime("%d-%b")
periodos_inicio[12] = datetime.strptime("21/04", "%d/%m").date().strftime("%d-%b")
periodos_inicio[13] = datetime.strptime("01/05", "%d/%m").date().strftime("%d-%b")
periodos_inicio[14] = datetime.strptime("11/05", "%d/%m").date().strftime("%d-%b")
periodos_inicio[15] = datetime.strptime("21/05", "%d/%m").date().strftime("%d-%b")
periodos_inicio[16] = datetime.strptime("01/06", "%d/%m").date().strftime("%d-%b")
periodos_inicio[17] = datetime.strptime("11/06", "%d/%m").date().strftime("%d-%b")
periodos_inicio[18] = datetime.strptime("21/06", "%d/%m").date().strftime("%d-%b")
periodos_inicio[19] = datetime.strptime("01/07", "%d/%m").date().strftime("%d-%b")
periodos_inicio[20] = datetime.strptime("11/07", "%d/%m").date().strftime("%d-%b")
periodos_inicio[21] = datetime.strptime("21/07", "%d/%m").date().strftime("%d-%b")
periodos_inicio[22] = datetime.strptime("01/08", "%d/%m").date().strftime("%d-%b")
periodos_inicio[23] = datetime.strptime("11/08", "%d/%m").date().strftime("%d-%b")
periodos_inicio[24] = datetime.strptime("21/08", "%d/%m").date().strftime("%d-%b")
periodos_inicio[25] = datetime.strptime("01/09", "%d/%m").date().strftime("%d-%b")
periodos_inicio[26] = datetime.strptime("11/09", "%d/%m").date().strftime("%d-%b")
periodos_inicio[27] = datetime.strptime("21/09", "%d/%m").date().strftime("%d-%b")
periodos_inicio[28] = datetime.strptime("01/10", "%d/%m").date().strftime("%d-%b")
periodos_inicio[29] = datetime.strptime("11/10", "%d/%m").date().strftime("%d-%b")
periodos_inicio[30] = datetime.strptime("21/10", "%d/%m").date().strftime("%d-%b")
periodos_inicio[31] = datetime.strptime("01/11", "%d/%m").date().strftime("%d-%b")
periodos_inicio[32] = datetime.strptime("11/11", "%d/%m").date().strftime("%d-%b")
periodos_inicio[33] = datetime.strptime("21/11", "%d/%m").date().strftime("%d-%b")
periodos_inicio[34] = datetime.strptime("01/12", "%d/%m").date().strftime("%d-%b")
periodos_inicio[35] = datetime.strptime("11/12", "%d/%m").date().strftime("%d-%b")
periodos_inicio[36] = datetime.strptime("21/12", "%d/%m").date().strftime("%d-%b")

periodos_final = {}
periodos_final[0] = "-"
periodos_final[1] = datetime.strptime("10/01", "%d/%m").date().strftime("%d-%b")
periodos_final[2] = datetime.strptime("20/01", "%d/%m").date().strftime("%d-%b")
periodos_final[3] = datetime.strptime("31/01", "%d/%m").date().strftime("%d-%b")
periodos_final[4] = datetime.strptime("10/02", "%d/%m").date().strftime("%d-%b")
periodos_final[5] = datetime.strptime("20/02", "%d/%m").date().strftime("%d-%b")
periodos_final[6] = datetime.strptime("28/02", "%d/%m").date().strftime("%d-%b")
periodos_final[7] = datetime.strptime("10/03", "%d/%m").date().strftime("%d-%b")
periodos_final[8] = datetime.strptime("20/03", "%d/%m").date().strftime("%d-%b")
periodos_final[9] = datetime.strptime("31/03", "%d/%m").date().strftime("%d-%b")
periodos_final[10] = datetime.strptime("10/04", "%d/%m").date().strftime("%d-%b")
periodos_final[11] = datetime.strptime("20/04", "%d/%m").date().strftime("%d-%b")
periodos_final[12] = datetime.strptime("30/04", "%d/%m").date().strftime("%d-%b")
periodos_final[13] = datetime.strptime("10/05", "%d/%m").date().strftime("%d-%b")
periodos_final[14] = datetime.strptime("20/05", "%d/%m").date().strftime("%d-%b")
periodos_final[15] = datetime.strptime("31/05", "%d/%m").date().strftime("%d-%b")
periodos_final[16] = datetime.strptime("10/06", "%d/%m").date().strftime("%d-%b")
periodos_final[17] = datetime.strptime("20/06", "%d/%m").date().strftime("%d-%b")
periodos_final[18] = datetime.strptime("30/06", "%d/%m").date().strftime("%d-%b")
periodos_final[19] = datetime.strptime("10/07", "%d/%m").date().strftime("%d-%b")
periodos_final[20] = datetime.strptime("20/07", "%d/%m").date().strftime("%d-%b")
periodos_final[21] = datetime.strptime("31/07", "%d/%m").date().strftime("%d-%b")
periodos_final[22] = datetime.strptime("10/08", "%d/%m").date().strftime("%d-%b")
periodos_final[23] = datetime.strptime("20/08", "%d/%m").date().strftime("%d-%b")
periodos_final[24] = datetime.strptime("31/08", "%d/%m").date().strftime("%d-%b")
periodos_final[25] = datetime.strptime("10/09", "%d/%m").date().strftime("%d-%b")
periodos_final[26] = datetime.strptime("20/09", "%d/%m").date().strftime("%d-%b")
periodos_final[27] = datetime.strptime("30/09", "%d/%m").date().strftime("%d-%b")
periodos_final[28] = datetime.strptime("10/10", "%d/%m").date().strftime("%d-%b")
periodos_final[29] = datetime.strptime("20/10", "%d/%m").date().strftime("%d-%b")
periodos_final[30] = datetime.strptime("31/10", "%d/%m").date().strftime("%d-%b")
periodos_final[31] = datetime.strptime("10/11", "%d/%m").date().strftime("%d-%b")
periodos_final[32] = datetime.strptime("20/11", "%d/%m").date().strftime("%d-%b")
periodos_final[33] = datetime.strptime("30/11", "%d/%m").date().strftime("%d-%b")
periodos_final[34] = datetime.strptime("10/12", "%d/%m").date().strftime("%d-%b")
periodos_final[35] = datetime.strptime("20/12", "%d/%m").date().strftime("%d-%b")
periodos_final[36] = datetime.strptime("31/12", "%d/%m").date().strftime("%d-%b")

def removeSolo(data, tipo): #removing soils that are not clay or AD6
    if(tipo == "Argiloso"):
        new_data = data[data["Solo"] == "Argiloso"]
    elif(tipo == "AD6"):
        new_data = data[data["Solo"] == "AD6"]
    return new_data

def removeColumns(data, colunas_list): #removing columns that don't need to be included
    new_array = data.drop(columns=colunas_list)
    return new_array


def find_window_date(data): #salvar a janela de plantio em duas novas colunas (inicio e termino)
    new_data = data
    new_data["Inicio"] = 0
    new_data["Termino"] = 0
    for j in range(0,new_data.shape[0]): #percorre todas as linhas
        first = 0
        last = 0
        janela_excecao = False #caso a janela ultrapasse de um ano para outro (exemplo de outubro ate fevereiro)
        for i in range(1,37): #percorre todas as colunas de data
            if(new_data.loc[j, str(i)] != 0 and first == 0): #1. acha a primeira ocorrencia nao nula
                if((i == 1 and new_data.loc[j, str(36)] != 0) or janela_excecao): #2. caso comece o ano no meio de uma janela
                    if(i == 36):
                        first = i
                        break
                    janela_excecao = True
                    if(new_data.loc[j, str(i+1)] == 0 and last == 0): #2.1 termino da janela
                        last = i
                        continue
                    if(new_data.loc[j, str(i)] != 0 and last != 0): #2.2 inicio da janela
                        first = i
                        break
                    continue
                first = i #1.1 inicio da janela
                continue
            if(new_data.loc[j, str(i)] != 0): #1.2 termino da janela
                last = i
        if(last == 0): #caso exista apenas um numero
            last = first
        new_data.loc[j,"Inicio"] = first
        new_data.loc[j,"Termino"] = last
    return new_data

def turn_to_date(data): #modifies the window string
    new_array = data
    new_array["Inicio"] = new_array["Inicio"].replace(periodos_inicio)
    new_array["Termino"] = new_array["Termino"].replace(periodos_final)
    return new_array

def REALLY_turn_to_date(data): #format the date
    new_data = data
    new_data['Inicio'] = pd.to_datetime(new_data['Inicio'], format='%d-%b', errors='coerce')
    new_data['Termino'] = pd.to_datetime(new_data['Termino'], format='%d-%b', errors='coerce')
    return new_data

def remove_number_columns(data): #remove columns of numbers
    new_array = data
    new_array = new_array.drop(columns=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'])
    return new_array

def remove_groups(data): #removes the groups (I)
    new_data = data[data["Grupo"] == "Grupo I"]
    return new_data



#Here I execute the code, changing manually the seed to for security reasons

data = pd.read_csv("./milho/milho_TOTAL.csv")
data = find_window_date(data)
data = turn_to_date(data)
data = remove_number_columns(data)

#data = removeSolo(data, "Argiloso")
data = remove_groups(data)
data = removeColumns(data, ["Outros manejos", "Clima", "Safra","Grupo"])
data = REALLY_turn_to_date(data)
data.to_csv("./arquivos_finais/milho_FINAL.csv", index=False)