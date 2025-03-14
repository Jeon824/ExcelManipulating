#-*-coding:utf-8-*-
import pandas as pd
import openpyxl as op

def get_excel(dir):
    load_wb = op.load_workbook(dir)
    return load_wb

#def extract_name(dir):
#지자체명 추출
def df_to_ws(df,ws):
    for r in dataframe_to_rows(df, index = True, header = True):
        ws.append(r)

#def save_to_excel(df, name):
    #name에서 지역 이름 추출해서 파일 이름으로 변경