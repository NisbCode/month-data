import csv
import os.path
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import calendar
from pandas.tseries.holiday import *
from pandas.tseries.offsets import CustomBusinessDay

pd.set_option('display.max_columns', None)    # <-- Mostrar todas as colunas 

# Valores fantasia
ACRESCIMO_VR_FIXO = 700
ACRESCIMO_SALARIO_FIXO_1 = 1000
ACRESCIMO_SALARIO_FIXO_2 = 1142.80
TOTAL_VR_INICIO = 930
TOTAL_SALARIO_INICIO = 2385.54
TOTAL_SALARIO_FINAL = TOTAL_SALARIO_INICIO
TOTAL_VR_FINAL = TOTAL_VR_INICIO

#MONTH = datetime.now().month
TODAY = datetime.today()
MONTH = 5                           
YEAR = datetime.now().year
FILE_CSV_BACKUP = './dados_salario_mensal_de_' + str(MONTH) + '-' + str(YEAR) + '.csv'
FILE_CSV_BACKUP_AUX = './dados_salario_mensal_de_' + str(MONTH) + '-' + str(YEAR) + 'AUX.csv'




def printSum(tittle, description):
    print(description,"%.2f" % df[tittle].sum())


"""
..######.....###....##..........###....########..####..#######........###....##.....##.########..#######..##.....##....
.##....##...##.##...##.........##.##...##.....##..##..##.....##......##.##...##.....##....##....##.....##.###...###....
.##........##...##..##........##...##..##.....##..##..##.....##.....##...##..##.....##....##....##.....##.####.####....
..######..##.....##.##.......##.....##.########...##..##.....##....##.....##.##.....##....##....##.....##.##.###.##....
.......##.#########.##.......#########.##...##....##..##.....##....#########.##.....##....##....##.....##.##.....##....
.##....##.##.....##.##.......##.....##.##....##...##..##.....##....##.....##.##.....##....##....##.....##.##.....##.###
..######..##.....##.########.##.....##.##.....##.####..#######.....##.....##..#######.....##.....#######..##.....##.###
"""

def monthSalary():
    middle_of_month = "15/"+ str(MONTH) +"/" + str(YEAR)
    #print(middle_of_month)

    res = calendar.monthrange(YEAR, MONTH)[1]
    #print("Last date of month : " + str(res))
    end_of_month = str(res) + "/"+ str(MONTH) +"/" + str(YEAR)
    #print(end_of_month)
    total = whichDay(middle_of_month)
    total += whichDay(end_of_month)
    return total


def whichDay(dia):
    date_time_obj = datetime.strptime(dia, '%d/%m/%Y')
    date_time_obj_aux = datetime.strptime(dia, '%d/%m/%Y')
    holidays = open("./holidays.txt", "r")
    readfile = holidays.read()
    valid = True

    while(valid):
        if(dia in readfile):
            #print("Não úteis")
            date_time_obj = date_time_obj - timedelta(1)
            dia = date_time_obj.strftime("%d/%m/%Y")
        elif (date_time_obj.weekday() == 6) or (date_time_obj.weekday() == 5):
            #print("Não úteis")
            date_time_obj = date_time_obj - timedelta(1)
        else:
            #print("Útil")
            print("Dia que o salário pode cair neste mês:", date_time_obj)
            valid = False
            if(date_time_obj > datetime.today()):
                #print("Dia não passou")
                return 0
            else:
                #print("Dia passou")
                #print(dia)
                if(date_time_obj == date_time_obj_aux or date_time_obj < date_time_obj_aux):
                    print(ACRESCIMO_SALARIO_FIXO_1)
                    return ACRESCIMO_SALARIO_FIXO_1
                else:
                    return ACRESCIMO_SALARIO_FIXO_2
        holidays.close() 
    
    
    

"""
.##.....##....###....##........#######..########..########..######.....########.####.##.....##..#######...######.
.##.....##...##.##...##.......##.....##.##.....##.##.......##....##....##........##...##...##..##.....##.##....##
.##.....##..##...##..##.......##.....##.##.....##.##.......##..........##........##....##.##...##.....##.##......
.##.....##.##.....##.##.......##.....##.########..######....######.....######....##.....###....##.....##..######.
..##...##..#########.##.......##.....##.##...##...##.............##....##........##....##.##...##.....##.......##
...##.##...##.....##.##.......##.....##.##....##..##.......##....##....##........##...##...##..##.....##.##....##
....###....##.....##.########..#######..##.....##.########..######.....##.......####.##.....##..#######...######.
"""

# Valores fantasia
food_hortifruti_category =          np.array([25.58])
food_packedlunch_category =         np.array([0])
food_fastfood_category =            np.array([86.50])
food_supermarket_category =         np.array([13.16])
food_uffbandejao_category =         np.array([5])
uber =                              np.array([12.97, 8.31, 12.20, 9.11, 8.93, 9.99, 14.92, 8.99, 9.9])
uber_others =                       np.array([31.95, 39.91])
drinks =                            np.array([78.56, 14])
bus_usage =                         np.array([0])
home_objects =                      np.array([10.98, 330])
computer_objects =                  np.array([0])
school_ordrawing_supplies =         np.array([0])                       #0
clothes =                           np.array([169.70])
rent =                              np.array([350])
medicine =                          np.array([30.47, 30.88])
internet =                          np.array([100])
money_given_to_friends =            np.array([26.98])
money_received_from_friends =       np.array([40, 66.66])
other =                             np.array([39.89, 102])
date_of_backup =                    np.array([TODAY.strftime("%d/%m/%Y")])






TOTAL_SALARIO_FINAL += monthSalary()
print("Valor com salário: " +str(TOTAL_SALARIO_FINAL))









list = {
    'C_Sacolão':                            food_hortifruti_category,
    'C_Marmita':                            food_packedlunch_category,
    'C_FastFood':                           food_fastfood_category,
    'C_Mercado':                            food_supermarket_category,
    'C_Bandejão_UFF':                       food_uffbandejao_category,
    'Uber':                                 uber,
    'Uber_Outros':                          uber_others,
    'Bebidas':                              drinks,
    'Transporte':                           bus_usage,
    'Coisas_Casa':                          home_objects,
    'Coisas_PC':                            computer_objects,
    'Material_escola_desenho':              school_ordrawing_supplies,
    'Roupas':                               clothes,
    'Aluguel':                              rent,
    'Remédios':                             medicine,
    'Internet':                             internet,
    'Amigos':                               money_given_to_friends,
    'Outro':                                other,
    'Historico_Backup':                     date_of_backup,
}


"""
....###....########...#######.........########.....###.....######..##....##.##.....##.########.
...##.##...##.....##.##.....##........##.....##...##.##...##....##.##...##..##.....##.##.....##
..##...##..##.....##.##.....##........##.....##..##...##..##.......##..##...##.....##.##.....##
.##.....##.########..##.....##........########..##.....##.##.......#####....##.....##.########.
.#########.##...##...##..##.##........##.....##.#########.##.......##..##...##.....##.##.......
.##.....##.##....##..##....##..###....##.....##.##.....##.##....##.##...##..##.....##.##.......
.##.....##.##.....##..#####.##.###....########..##.....##..######..##....##..#######..##.......
"""


if os.path.isfile(FILE_CSV_BACKUP):
    print("??????????????????")
    a_df = pd.read_csv(FILE_CSV_BACKUP)
    df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in list.items()]))
    a_df = pd.concat([a_df, df])
    a_df.to_csv(FILE_CSV_BACKUP_AUX, index=False)

    print(a_df)
else:
    df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in list.items()]))
    df.to_csv(FILE_CSV_BACKUP, index=False)
    df = pd.read_csv(FILE_CSV_BACKUP)


print("========================================================================")
print("SOFC - Sistema de Organização Financeira em Categorias")
print("Cálculos do período entre os dias 26/04/2022 - 28/05/2022")
print("Valor baseado nos gastos referentes ao Salário")
print("-----------------Salário ANTES do período-----------------")
print("-=-=-=-=-=-=-=-=-= 2385.54 =-=-=-=-=-=-=-=-=-")
print("========================================================================")

print(df)           #<-- Mostra todos as colunas e seus valores

printSum("C_Sacolão",                   "Gastos com Sacolão:")
printSum("C_Marmita",                   "Gastos com Marmita:")
printSum("C_FastFood",                  "Gastos com FastFood:")
printSum("C_Mercado",                   "Gastos com Mercado:")
printSum("C_Bandejão_UFF",              "Gastos com Bandejão_UFF:")
printSum("Uber",                        "Gastos com Uber:")
printSum("Uber_Outros",                 "Gastos com Uber para Outras pessoas:")
printSum("Bebidas",                     "Gastos com Bebidas:")
printSum("Transporte",                  "Gastos com Passagem usando vale transporte:")
printSum("Coisas_Casa",                 "Objetos para casa:")
printSum("Coisas_PC",                   "Objetos para PC:")
printSum("Material_escola_desenho",     "Materiais escolares ou de desenho:")
printSum("Roupas",                      "Gastos com Roupas:")
printSum("Aluguel",                     "Gastos com Aluguel:")
printSum("Remédios",                    "Gastos com Remédios:")
printSum("Internet",                    "Gastos com Internet:")
printSum("Amigos",                      "Dinheiro dado para amigos")
printSum("Outro",                       "Gastos com outro não listado:")


