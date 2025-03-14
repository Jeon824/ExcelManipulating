#-*-coding:utf-8-*-
import border as bd
import openpyxl
import manipulate_excel as me
import pandas as pd
#get excel data
def compare(file_list):

    saved_file_list = []

    for dir in file_list:
        loaded_wb = bd.get_excel(dir)

        original_sheet = loaded_wb.active

        table_start_point = 0

        table_max_row = original_sheet.max_row
        pin = -1
        index_of_in_cash = -1
        index_of_out_cash = -1

        df = pd.DataFrame(original_sheet.values)

        for i in range(0,table_max_row):#find starting point of table
            if(df.iloc[i,0] == 1):
                pin = i

        df_columns = df.iloc[pin-1, 1:]

        df_index = df.iloc[pin:,0]
        df = df.iloc[pin:,1:]
        df.columns = df_columns
        df.index = df_index
        df.index.name = None
        df.columns.name = None


        seek_column = "거래내용"

        seek_column_index = -1

        group_list = ["PC우리은행","가상계좌","실시간이체","기타"]


        for i in range(0,len(df_columns)-1):
            if (seek_column == df.columns[i]):
                seek_column_index = i

        row_index_dict = {}                                 #dictionary that shows number of row 

        for kward in group_list:
            row_index_dict[kward] = []

        df = df.sort_values(by = ['거래내용', '기록사항'])

        start_pos = 0
        etc_index = 0

        sep_df = {}

        for sep_kward in group_list:
            sep_df[sep_kward] = pd.DataFrame(columns = df_columns)

        if(seek_column_index != -1):
            for kward in group_list:                   #TODO:기타 부분 해결 loc[kward]로 확인하여 keyword가 존재하지 않으면 기타의 index로 추가한다.
                if kward == "기타":
                    break
                print(kward)
                j = start_pos
                
                for i in range(j,df.index.max()):
                    if(df.iloc[i][seek_column_index] == kward):
                        row_index_dict[kward].append(i)
                    elif(df.iloc[i][seek_column_index] != kward  and (df.iloc[i][seek_column_index] in group_list)):
                        start_pos = i
                        print(f'{i}th compare with ({kward},{df.iloc[i][seek_column_index]})')
                        break
                    else:
                        sep_df["기타"].loc[etc_index] = df.iloc[i]
                        etc_index += 1
                        start_pos = i + 1


        for sep_kward in group_list:
            print(row_index_dict[sep_kward])

        for sep_kward in group_list:    #Just combine with Line71
            sep_df_index = 0
            if row_index_dict[sep_kward] is not None: # true
                for index in row_index_dict[sep_kward]:
                    sep_df[sep_kward].loc[sep_df_index] = df.iloc[index]
                    sep_df_index += 1
        single_none_list = [None]

        depoist_column_index = -1            #index that indicates amount of deposit

        withdraw_column_index = -1           #index that indicates amount of withdraw

        for i in range(1,len(df_columns)+1):
            print(df_columns[i]) 

        for i in range(1,len(df_columns)+1):#find column indexes that corresponds with deposit and withdraw
            if df_columns[i].find('금') > -1:
                if df_columns[i].find('입') > -1 or df_columns[i].find('맡') > -1:
                    depoist_column_index = i
                elif df_columns[i].find('출') > -1 or df_columns[i].find('찾') > -1:
                    withdraw_column_index = i
        
        print("@@Deposit-Column-index",depoist_column_index)
        print("@@Withdraw-Column-index",withdraw_column_index)
                 



        for sep_kward in group_list:#add row that indicates amount of deposit and withdraw
            sum_row = pd.Series(single_none_list * len(df_columns))
            
        for i in range(0,len(df_columns)-1):
            if (seek_column == df.columns[i]):
                seek_column_index = i
