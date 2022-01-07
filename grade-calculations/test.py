import pandas as pd
import numpy as np

midterm = 0.15
lab = 0.3
final = 0.3
attendance = 0.1


def adjust_cols(df):
    df.drop('LETTER GRADE', axis=1, inplace=True)


def fillna(df):
    df2 = df.fillna(value=0, axis=0)
    return df2


def gradenum_to_letter(grade):
    if grade <= 100 and grade >= 90:
        return 'AA'
    elif grade <= 89 and grade >= 85:
        return 'BA'
    elif grade <= 84 and grade >= 80:
        return 'BB'
    elif grade <= 79 and grade >= 75:
        return 'CB'
    elif grade <= 74 and grade >= 70:
        return 'CC'
    elif grade <= 69 and grade >= 65:
        return 'DC'
    elif grade <= 64 and grade >= 60:
        return 'DD'
    elif grade <= 59 and grade >= 50:
        return 'FD'
    else:
        return 'FF'


def evalute_total_grade(df_row_sliced):
    total = 0
    if df_row_sliced['ATTENDANCE'] < 0.7:
        return 'NA'

    else:
        # Midterms   
        total += df_row_sliced['MIDTERM 1'] * midterm
        total += df_row_sliced['MIDTERM 2'] * midterm

        # Final
        total += df_row_sliced['FINAL'] * final
        
        # Lab
        total += df_row_sliced['LAB'] * lab

        # Attendance
        # TODO: Figure a way to map attendance scores
