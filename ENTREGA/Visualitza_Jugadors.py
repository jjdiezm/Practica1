# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 19:26:21 2019

@author: Grup pràctiques:  Quim Dalmases / Juanjo Díez
"""

import pickle
import matplotlib.pyplot as plt

with open('fotos.pickle', 'rb') as image_file:
    img_objects = pickle.load(image_file)
# tam = len(img_objects.keys())
# Full teams list
full_team_list = ['Alavés', 'Athletic', 'Atlético', 'Barça', 'Betis', 'Celta', 'Eibar', 'Espanyol',
                  'Getafe', 'Girona', 'Huesca', 'Leganés', 'Levante', 'Rayo', 'Real Madrid', 'Real Sociedad',
                  'Sevilla FC', 'Valencia', 'Valladolid', 'Villarreal']


def team_photos(team_list):
    """ Function to show the fotos of a team list one by one

    :param team_list: List of teams
    :return: nothing
    """
    for team in team_list:
        num = 0
        for key in img_objects.keys():
            if team in key:
                num += 1
                plt.imshow(img_objects[key])
                plt.title(key.replace("_", "\n"), fontsize=18)
                plt.show()
        plt.show()
        print("Team {} has {} players registered.".format(str(team), str(num)))
    return


def team_facebook(team_list, cols=5):
    """ Function to show the fotos of a team list as facebook

    :param team_list: List of teams
    :param cols: number of cols to plot, 5 predefined value if not passed
    :return: nothing:
    """

    # For each team in list passed:
    for team in team_list:
        # Lists to store team players and names
        player_list = list()
        player_names = list()
        for key in img_objects.keys():
            if team in key:
                # store image
                player_list.append(img_objects[key])
                # store player name without team name and underscores
                title = key.replace(team, "")
                player_names.append(title.replace("_", " "))
        if len(player_list) > 0:
            # calculated row number based on number of players and cols set
            rows = len(player_list)//cols
            if len(player_list) % cols > 0:
                rows += 1
            # array of subplots
            figure, axes_array = plt.subplots(rows, cols, figsize=(10, 10))
            # fill array with images
            for num in range(len(player_list)):
                i = num//cols
                j = num % cols
                axes_array[i, j].imshow(player_list[num])
                axes_array[i, j].set_title(player_names[num], fontsize=10)
                axes_array[i, j].axis("off")
            # Avoid painting axis of void images
            if len(player_list) % cols > 0:
                for void_cell in range(cols - (len(player_list) % cols)):
                    j = cols - void_cell - 1
                    i = rows - 1
                    axes_array[i, j].axis("off")
            # Configure plot by spacing images and adding a title
            figure.subplots_adjust(hspace=0.3)
            figure.suptitle(team, fontsize=12, fontweight='bold')
            plt.show()
        else:
            print("No players registered on team: ".format(str(team)))
    return


# Example picking some teams:
team_facebook(full_team_list[i] for i in [2, 3, 14, 16, 17])
# Other Example
# team_photos(full_team_list[18:])
