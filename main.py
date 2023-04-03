#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.
import random
import csv
from pokemon import Pokemon
from weapon_type import WeaponType
def get_data_from_user(name_file):
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      list_pokemons List of Pokemons obtained from CSV .

    Example
    -------
      >>> list_pokemons = get_data_from_user("file.csv")
    """
    list_pokemons = []
    with open(name_file, "r") as file:
      reader = csv.reader(file)
      for line in reader:
        if line[2]=="headbutt":
          list = Pokemon(int(line[0]), str(line[1]), WeaponType.HEADBUTT, int(line[3]), int(line[4]), int(line[5]))
        elif line[2]=="punch":
          list = Pokemon(int(line[0]), str(line[1]), WeaponType.PUNCH, int(line[3]), int(line[4]), int(line[5]))
        elif line[2]=="kick":
          list = Pokemon(int(line[0]), str(line[1]), WeaponType.KICK, int(line[3]), int(line[4]), int(line[5]))
        elif line[2]=="elbow":
          list = Pokemon(int(line[0]), str(line[1]), WeaponType.ELBOW, int(line[3]), int(line[4]), int(line[5]))
        
        list_pokemons.append(list)
    return list_pokemons
            

    



def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       List List of the Pokemons associaated to the coach that are undefeated.

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """
    if len(list_of_pokemons) == 3:
      print("1:", list_of_pokemons[0].pokemon_name,"2:", list_of_pokemons[1].pokemon_name,"3:", list_of_pokemons[2].pokemon_name)
    elif len(list_of_pokemons) == 2:
      print("1:", list_of_pokemons[0].pokemon_name,"2:", list_of_pokemons[1].pokemon_name)
    else:
      print("Solo le queda, 1:", list_of_pokemons[0].pokemon_name)
    pokemon_a_eleir = input("Coach " + str(coach_to_ask) + " select a Pokemon: ")
    pokemon_a_eleir = int(pokemon_a_eleir)
    if pokemon_a_eleir == 1:
      pokemon_a_eleir = list_of_pokemons[0]
    elif pokemon_a_eleir == 2:  
      pokemon_a_eleir = list_of_pokemons[1]
    elif pokemon_a_eleir == 3:
      pokemon_a_eleir = list_of_pokemons[2]
    return pokemon_a_eleir
    

    


def coach_is_undefeated(list_of_pokemons):
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Boolean True if the coach has all her/his Pokemons defeated.
               False if the coach has any Pokemon that is undefeated.

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """
    if len(list_of_pokemons)==0:
      return False
    else:
      return True


def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """



    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.
    coach1 = get_data_from_user("coach_1_pokemons.csv")
    for i in coach1:
      print(i)
    
    
    


    # Get configuration for Game User 2.
    coach2 = get_data_from_user("coach_2_pokemons.csv")
    for i in coach2:
      print(i)
    dañoRecibido1 = 0
    dañoRecibido2 = 0
    dañoRealizado1 = 0
    dañoRealizado2 = 0
    
    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    pokemons= [coach1, coach2]
    
    

    # Choose first pokemons
    pokemons1 = get_pokemon_in_a_list_of_pokemons("coach1", coach1)
    pokemons2 = get_pokemon_in_a_list_of_pokemons("coach2", coach2)
    # Main loop.
    
      
      

    while coach_is_undefeated(coach1) and coach_is_undefeated(coach2):
      numeroAleatorio = random.randint(1, 2)
      print(numeroAleatorio)
      if numeroAleatorio == 1:
        print("Empieza el jugador uno")
        print("El jugador uno selecciona {}".format(pokemons1.pokemon_name))
        print("El jugador dos selecciona {}".format(pokemons2.pokemon_name))
        while True:

          print("El jugador uno ataca")
          pokemons1.fight_attack(pokemons2)
          dañoRealizado1 += pokemons1.attack_rating - pokemons2.defense_rating
          dañoRecibido2 += pokemons1.attack_rating - pokemons2.defense_rating

          print("El jugador dos ataca")
          pokemons2.fight_attack(pokemons1)
          dañoRealizado2 += pokemons2.attack_rating - pokemons1.defense_rating
          dañoRecibido1 += pokemons2.attack_rating - pokemons1.defense_rating

          if pokemons1.health_points <= 0: #si el pokemon 1 no le queda vida, se elimina y se escoge otro
            coach1.remove(pokemons1)
            if coach_is_undefeated(coach1) == False or coach_is_undefeated(coach2) == False:#en caso de no queda pookemons, se acaba el juego
              break
            else:
              pokemons1 = get_pokemon_in_a_list_of_pokemons("coach1", coach1)# en caso de si quedar pokemons vivos, se escoge otro
          elif pokemons2.health_points <= 0:
            coach2.remove(pokemons2)
            if coach_is_undefeated(coach1) == False or coach_is_undefeated(coach2) == False:
             break
            else:
              pokemons2 = get_pokemon_in_a_list_of_pokemons("coach2", coach2)
          else:
           continue
          

        

      else:
        print("Empieza el jugador dos")
        print("El jugador dos selecciona {}".format(pokemons2.pokemon_name))  
        print("El jugador uno selecciona {}".format(pokemons1.pokemon_name))
        while True:

          print("El jugador dos ataca")
          pokemons2.fight_attack(pokemons1)
          dañoRealizado2 += pokemons2.attack_rating - pokemons1.defense_rating
          dañoRecibido1 += pokemons2.attack_rating - pokemons1.defense_rating

          print("El jugador uno ataca")
          pokemons1.fight_attack(pokemons2)
          dañoRealizado1 += pokemons1.attack_rating - pokemons2.defense_rating
          dañoRecibido2 += pokemons1.attack_rating - pokemons2.defense_rating

          if pokemons1.health_points <= 0:#si el pokemon 1 no le queda vida, se elimina y se escoge otro
            coach1.remove(pokemons1)
            if coach_is_undefeated(coach1) == False or coach_is_undefeated(coach2) == False:#en caso de no queda pokemons, se acaba el juego
              break
            else:
              pokemons1 = get_pokemon_in_a_list_of_pokemons("coach1", coach1)# en caso de si quedar pokemones vivos, se escoge otro
          elif pokemons2.health_points <= 0:
            coach2.remove(pokemons2)
            if coach_is_undefeated(coach1) == False or coach_is_undefeated(coach2) == False:
             break
            else:
              pokemons2 = get_pokemon_in_a_list_of_pokemons("coach2", coach2)
          else: 
            continue
            
          




        # Turno del usuario del Juego 2.
      if len(coach1)==0:#si el jugador 1 no le queda pokemons, se acaba el juego
        print("------------------------------------------------------------------")
        print("Ha ganado el jugador dos")
        print("------------------------------------------------------------------")
        # Turno del usuario del Juego 1.
      elif len(coach2)==0:#si el jugador 2 no le queda pokemons se acaba el juego
        print("------------------------------------------------------------------")
        print("Ha ganado el jugador uno")
        print("------------------------------------------------------------------")




    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")
    print("El jugador uno ha realizado", dañoRealizado1, "de daño")
    print("El jugador uno ha recibido", dañoRecibido1, "de daño")
    print("------------------------------------------------------------------")
    print("Game User 2:")
    print("El jugador dos ha realizado", dañoRealizado2, "de daño")
    print("El jugador dos ha recibido", dañoRecibido2, "de daño")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
