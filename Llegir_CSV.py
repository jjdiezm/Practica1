# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:15:34 2019
Descripció:
    Pràctica nº1 : Tipología i cicle de vida de les dades.
    Implementació pràctica de web-scraping en diari esportiu per generar
    un dataset d'analisi sobre el funcionament de la lliga 2018-2019.

@author: Quim Dalmases / Juanjo Díez
"""

import pandas as pd

file_players = "jugadors.csv"
file_stats = "estadistiques_jugadors.csv"
file_pichichi = "pichichi_stats.csv"
file_zamora = "zamora_stats.csv"
file_munoz = "miguel-munoz_stats.csv"


def print_csv(csv_file):
    """ Function to print a CSV preview as a table using pandas

    :param csv_file: csv file to import, needs to be on the same directory as this .py file
    :return: Nothing
    """
    data_frame = pd.read_csv(csv_file)
    print(data_frame)


def print_filtered_csv(csv_file, filter_column):
    """ Function to print a CSV as a table using pandas and filtering by a column

    :param csv_file: csv file to import, needs to be on the same directory as this .py file
    :param filter_column: column to filter the dataframe
    :return: Nothing
    """

    data_frame = pd.read_csv(csv_file)
    filter_df = data_frame[filter_column].unique()
    for row in filter_df:
        data_team = data_frame.loc[data_frame[filter_column] == row]
        data_team = data_team.drop(columns=filter_column)
        print("\nEquip: {}".format(row))
        print(data_team)
    return


# Usage examples:
# print_csv(file_zamora)
# print_csv(file_munoz)
# print_filtered_csv(file_stats, 'nomEquip')
# print_filtered_csv(file_players, 'Equip')
print_filtered_csv(file_pichichi, 'nomEquip')
