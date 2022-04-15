# Examen-POO

El link de este repositorio es : https://github.com/carlospuigserver/Examen-POO.git

Para realizar el examen propuesto, me he guiado por la solución habilitada en el campus virtual.


### Main

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-



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
import csv
import copy

from weapon_type import WeaponType
from pokemon import Pokemon


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
      Null .
    Example
    -------
      >>> get_data_from_user("file.csv")
    """
    set_of_pokemons = []

    if not isinstance(name_file, str):
        raise TypeError("The paramenter name_file is not a String.")

    name_file_s = name_file

    try:
        with open(name_file_s, newline='') as csv_file:
            reader = csv.reader(csv_file)
            data_from_file = list(reader)

        for temp_pokemon_csv in data_from_file:
            coach_pokemon = Pokemon(int(temp_pokemon_csv[0]),
                                    temp_pokemon_csv[1],
                                    WeaponType.from_str(temp_pokemon_csv[2]),
                                    int(temp_pokemon_csv[3]),
                                    int(temp_pokemon_csv[4]),
                                    int(temp_pokemon_csv[5]))

            set_of_pokemons.append(coach_pokemon)

    except SyntaxError:
        print("Oops! The Pokemons of the coach were not introduced correctly." +
                " Try again...")

    return set_of_pokemons


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
       Null .
    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """
    if isinstance(list_of_pokemons,list):

        for temp_pokemon in list_of_pokemons:
            if not isinstance(temp_pokemon, Pokemon):
                raise TypeError("All pokemons should be Pokemon Type")
        print("Please Coach " + str(coach_to_ask) + " introduce the ID of the Pokemon: " + "\n")

        while True:
            print("List of Pokemons: " + "\n")
            
            for i in list_of_pokemons:
                print(i)
            
            string_introduced = input(":~>")
            try:
                int_introduced= int(string_introduced)
            except ValueError:
                print("Please, introduce an ID present in the list:")
            for temp_pokemon in list_of_pokemons:
                if int_introduced == temp_pokemon.get_id():
                    return temp_pokemon
            print("Please, introduce a number present in the list: ")
    else:
        raise TypeError("list_pokemons should be a list")


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
       Null .
    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """

    if isinstance(list_of_pokemons, list):
        for temp_pokemon in list_of_pokemons:
            if not isinstance(temp_pokemon, Pokemon):
                raise TypeError("All pokemons should be pokemon Type")

    defeated = True

    for temp_pokemon in list_of_pokemons:
        if temp_pokemon.is_alive():
            defeated = False

    return not defeated


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
    print("For Game User 1: \n")
    game_user_1 = get_data_from_user("coach_1_pokemons.csv")

    # Get configuration for Game User 2.
    print("For Game User 2: \n")
    game_user_2 = get_data_from_user("coach_2_pokemons.csv")

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    temp_list_pokemons_from_coach_1 = game_user_1
    list_pokemons_alive_coach_1 = copy.copy(temp_list_pokemons_from_coach_1)

    temp_list_pokemons_from_coach_2 = game_user_2
    list_pokemons_alive_coach_2 = copy.copy(temp_list_pokemons_from_coach_2)

    # Choose first pokemons
    print("Coach 1 choose your first pokemon")
    temp_pokemon_coach_1 = get_pokemon_in_a_list_of_pokemons("Please coach 1 introduce the id of the pokemon:", list_pokemons_alive_coach_1)
    print("Coach 2 choose your first pokemon")
    temp_pokemon_coach_2 = get_pokemon_in_a_list_of_pokemons("Please coach 2 introduce the id of the pokemon:",list_pokemons_alive_coach_2)

    while(coach_is_undefeated(temp_list_pokemons_from_coach_1) and coach_is_undefeated(temp_list_pokemons_from_coach_2)):

        if not temp_pokemon_coach_1.is_alive():
            # Select a new pokemon
            print("Coach 1 your pokemon: " + str(temp_pokemon_coach_1) + " has been defeated. Please select the new pokemon to fight ")
            list_pokemons_alive_coach_1.remove(temp_pokemon_coach_1)
            temp_pokemon_coach_1 = get_pokemon_in_a_list_of_pokemons("Please coach 1 introduce the id of the pokemon", list_pokemons_alive_coach_1)
        if not temp_pokemon_coach_2.is_alive():
            # Select a new pokemon
            print("Coach 2 your pokemon: " + str(temp_pokemon_coach_2) + " has been defeated. Please select the new pokemon to fight ")
            list_pokemons_alive_coach_2.remove(temp_pokemon_coach_2)
            temp_pokemon_coach_2 = get_pokemon_in_a_list_of_pokemons("Please coach 2 introduce the id of the pokemon", list_pokemons_alive_coach_2)

        print("pokemon from Game User 1 attacks.")
        temp_pokemon_coach_1.fight_attack(temp_pokemon_coach_2)
        print("pokemon from Game User 2 attacks.")
        temp_pokemon_coach_2.fight_attack(temp_pokemon_coach_1)


    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")
    if (coach_is_undefeated(temp_list_pokemons_from_coach_1)and not coach_is_undefeated(temp_list_pokemons_from_coach_2)):
        print("The WINNER is Game User 1.")
    elif (not coach_is_undefeated(temp_list_pokemons_from_coach_1) and coach_is_undefeated(temp_list_pokemons_from_coach_2)):
        print("The WINNER is Game User 2.")
    else:
        print("Both Game Users have been defeated. There is a DRAW.")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")
    for temp_pokemon in temp_list_pokemons_from_coach_1:
        print(temp_pokemon)

    print("Game User 2:")
    for temp_pokemon in temp_list_pokemons_from_coach_2:
        print(temp_pokemon)


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()



```
### POKEMON

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.
@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
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
from weapon_type import WeaponType


class Pokemon():
    """Python class to implement a basic version of a Pokemon of the game.
    This Python class implements the basic version of a Pokemon of the game.
    Syntax
    ------
      obj = Pokemon(id, pokemon_name, weapon_type, health_points,
                   attack_rating, defense_rating)
    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.
    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.
    Attributes
    ----------
    Example
    -------
      >>> from pokemon import Pokemon
      >>> from weapon_type import WeaponType
      >>> obj_Pokemon = Pokemon(1, "Bulbasaur", WeaponType.PUNCH, 100, 7, 10)
    """

    # Global variable to store the list of IDs.
    __list_ids = []


    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        """Constructor of the class.
        This special method is executed when an object of this class is
        created.
        Syntax
        ------
          [ ] = __init__(self, id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] pokemon_id ID of Pokemon.
          [in] pokemon_name Name of the Pokemon.
          [in] weapon_type Type of weapon that carries out the Pokemon.
          [in] health_points Points of health that the Pokemon has.
          [in] attack_rating Attack rating of the Pokemon.
          [in] defense_rating Defense rating of the Pokemon.
        Returns
        -------
          obj Python object output parameter that represents an instance
              of the class Pokemon.
        Exceptions
        ----------
          TypeError:
            If the parameter id is NOT a int.
            If the parameter pokemon_name is NOT a String.
            If the parameter weapon_type is NOT a enum WeaponType.
            If the parameter health_points is NOT be an int.
            If the parameter attack_rating is NOT be a int.
            If the parameter defense_rating is NOT be a int.
          ValueError:
            If the parameter id is already found in other Pokemon.
            If the parameter health_points is NOT > 0 and <= 100.
            If the parameter attack_rating is NOT > 0 and <= 10.
            If the parameter defense_rating is NOT > 0 and <= 10.
        Example
        -------
          >>> from pokemon import Pokemon
          >>> from weapon_type import WeaponType
          >>> obj_Pokemon = Pokemon(1, "Bulbasaur", WeaponType.PUNCH, 100, 7, 10)
        """

        if isinstance(pokemon_id, int):
            if pokemon_id not in Pokemon.__list_ids:
                self._pokemon_id = pokemon_id
                Pokemon.__list_ids.append(self._pokemon_id)
            else:
                raise ValueError("The parameter pokemon_id should be a new id not taken by other Pokemon.")
        else:
            raise TypeError("The parameter id should be a int.")

        if isinstance(pokemon_name, str):
            self._pokemon_name = pokemon_name
        else:
            raise TypeError("The parameter pokemon_name should be a String.")

        if isinstance(weapon_type, WeaponType):
            self._weapon_type = weapon_type
        else:
            raise TypeError("The parameter weapon_type should be a WeaponType.")

        if isinstance(health_points, int):
            if 1 <= health_points <= 100:
                self._health_points = health_points
            else:
                raise ValueError("The parameter health_points should be > 0 and <= 100.")
        else:
            raise TypeError("The parameter health_points should be a int.")

        if isinstance(attack_rating, int):
            if 1 <= attack_rating <= 10:
                self._attack_rating = attack_rating
            else:
                raise ValueError("The parameter attack_rating should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter attack_rating should be a int.")

        if isinstance(defense_rating, int):
            if 1 <= defense_rating <= 10:
                self._defense_rating = defense_rating
            else:
                raise ValueError("The parameter defense_rating should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter defense_rating should be a int.")


    def __del__(self):
        """Deconstructor of the class.
        This special method is executed when an object of this class is
        created.
        Syntax
        ------
          [ ] = __del__(self)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
        Exceptions
        ----------
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.__del__( )
        """
        Pokemon.__list_ids.remove(self._pokemon_id)


    def __str__(self):
        """Method to present a human-readable format of the object.
        Method to present a human-readable format of the object that is formed
        in this class. This method is useful for logging or displaying some
        information about the object.
        Syntax
        ------
          [ ] = __str__( )
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
        Returns
        -------
          String Human-readable format of the object.
        Exceptions
        ----------
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.__str__( )
        """
        human_readable_string = ("Pokemon ID " + str(self._pokemon_id) +
                                 " with name " + self._pokemon_name +
                                 " has as weapon " + self._weapon_type.name +
                                 " and health " + str(self._health_points))

        return human_readable_string


    def get_id(self):
        """Method to get the attribute id of the object.
        Syntax
        ------
          [ ] = obj_Pokemon.get_id( )
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
        Returns
        -------
          String The value of the specific attribute.
        Exceptions
        ----------
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.get_id( )
        """
        return self._pokemon_id


    def get_pokemon_name(self):
        """Method to get the attribute pokemon_name of the object.
        Syntax
        ------
        [ ] = obj_Pokemon.get_pokemon_name( )
        Parameters
        ----------
        [in] self Python object that represents an instance of the
                class Pokemon.
        Returns
        -------
        String The value of the specific attribute.
        Exceptions
        ----------
        Example
        -------
        >>> from Pokemon import Pokemon
        >>> obj_Pokemon = Pokemon()
        >>> obj_Pokemon.get_pokemon_name( )
        """
        return self._pokemon_name


    def get_weapon_type(self):
        """Method to get the attribute weapon_type of the object.
        Method to get the attribute weapon_type in a human-readable format of
        the object that is formed in this class.
        Syntax
        ------
          [ ] = obj_Pokemon.get_weapon_type( )
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
        Returns
        -------
          String The value of the specific attribute.
        Exceptions
        ----------
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.get_weapon_type()
        """
        return self._weapon_type


    def get_health_points(self):
        """Method to get the attribute health_points of the object.
        Method to get the attribute health_points in a human-readable format of
        the object that is formed in this class.
        Syntax
        ------
          [ ] = obj_Pokemon.get_health_points( )
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
        Returns
        -------
          int The value of the specific attribute.
        Exceptions
        ----------
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.get_health_points( )
        """
        return self._health_points


    def get_attack_rating(self):
        """Method to get the attribute attack_rating of the object.
        Method to get the attribute attack_rating in a human-readable format of
        the object that is formed in this class.
        Syntax
        ------
          [ ] = obj_Pokemon.get_attack_rating( )
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
        Returns
        -------
          int The value of the specific attribute.
        Exceptions
        ----------
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.get_attack_rating( )
        """
        return self._attack_rating


    def get_defense_rating(self):
        """Method to get the attribute defense_rating of the object.
        Method to get the attribute defense_rating in a human-readable format of
        the object that is formed in this class.
        Syntax
        ------
          [ ] = obj_Pokemon.get_defense_rating( )
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
        Returns
        -------
          int The value of the specific attribute.
        Exceptions
        ----------
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.get_defense_rating( )
        """
        return self._defense_rating


    def set_pokemon_name(self, pokemon_name_to_be_set):
        """Method to set the attribute pokemon_name of the object.
        Method to set the attribute pokemon_name based on a human-readable
        format of the object that is formed in this class.
        Syntax
        ------
          [ ] = obj_Pokemon.set_pokemon_name(pokemon_name_to_be_set)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] pokemon_name_to_be_set String that contains the name to assign
                                      to the Pokemon.
        Returns
        -------
        Exceptions
        ----------
          TypeError If the parameter weapon_type_to_be_set is NOT a String.
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.set_pokemon_name("Pikachu")
        """
        if isinstance(pokemon_name_to_be_set, str):
            self._pokemon_name = pokemon_name_to_be_set
        else:
            raise TypeError("The parameter pokemon_name_to_be_set should be a String.")


    def set_weapon_type(self, weapon_type_to_be_set):
        """Method to set the attribute weapon_type of the object.
        Method to set the attribute weapon_type based on a human-readable
        format of the object that is formed in this class.
        Syntax
        ------
          [ ] = obj_Pokemon.set_weapon_type(weapon_type_to_be_set)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] weapon_type_to_be_set String that contains the weapon to assign
                                     to the Pokemon.
        Returns
        -------
        Exceptions
        ----------
          TypeError If the parameter weapon_type_to_be_set is NOT a String.
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.set_weapon_type("Sword")
        """
        if isinstance(weapon_type_to_be_set, WeaponType):
            self._weapon_type = weapon_type_to_be_set
        else:
            raise TypeError("The parameter weapon_type should be a WeaponType.")


    def set_attack_rating(self, attack_rating_to_be_set):
        """Method to set the attribute attack_rating of the object.
        Method to set the attribute attack_rating based on a human-readable
        format of the object that is formed in this class.
        Syntax
        ------
          [ ] = obj_Pokemon.set_attack_rating( )
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] attack_rating_to_be_set String that contains the attack rating
                                       to assign to the Pokemon.
        Returns
        -------
        Exceptions
        ----------
          TypeError If the parameter attack_rating_to_be_set is NOT a int.
          ValueError If the parameter attack_rating_to_be_set is NOT > 0 and <= 10.
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.set_attack_rating(8)
        """
        if isinstance(attack_rating_to_be_set, int):
            if 1 <= attack_rating_to_be_set <= 10:
                self._attack_rating = attack_rating_to_be_set
            else:
                raise ValueError("The parameter attack_rating_to_be_set should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter attack_rating_to_be_set should be a int.")


    def set_defense_rating(self, defense_rating_to_be_set):
        """Method to set the attribute defense_rating of the object.
        Method to set the attribute defense_rating based on a human-readable
        format of the object that is formed in this class.
        Syntax
        ------
          [ ] = obj_Pokemon.set_defense_rating( )
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] defense_rating_to_be_set String that contains the defense rating
                                        to assign to the Pokemon.
        Returns
        -------
        Exceptions
        ----------
          TypeError If the parameter defense_rating_to_be_set is NOT a int.
          ValueError If the parameter defense_rating_to_be_set is NOT > 0 and <= 10.
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.set_attack_rating(8)
        """
        if isinstance(defense_rating_to_be_set, int):
            if 1 <= defense_rating_to_be_set <= 10:
                self._defense_rating = defense_rating_to_be_set
            else:
                raise ValueError("The parameter defense_rating_to_be_set should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter defense_rating_to_be_set should be a int.")


    def is_alive(self):
        """Method to know if the Pokemon is alive.
        Method to know if a Pokemon is still alive based on the value of the
        attribute health_points.
        Syntax
        ------
          [ ] = obj_Pokemon.is_alive( )
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
        Returns
        -------
          Boolean True if the Pokemon is alive. False otherwise.
        Exceptions
        ----------
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.is_alive( )
        """
        return not bool(self._health_points == 0)



    def fight_attack(self, pokemon_to_attack):
        """Method to attack using a hit to other Pokemon.
        Method that implements the attack of the Pokemon using a hit over other
        Pokemon.
        Syntax
        ------
          [ ] = obj_Pokemon.fight_attack(pokemon_to_attack)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] Pokemon pokemon_to_attack Pokemon to hit to.
        Returns
        -------
        Exceptions
        ----------
        TypeError If the parameter pokemon_to_attack is NOT a Pokemon.
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.fight_attack(pokemon_enemy)
        """
        points_of_damage = self._attack_rating

        print("The Pokemon " + self._pokemon_name +
              " hits the Pokemon " + pokemon_to_attack.get_pokemon_name() +
              " with " + str(points_of_damage) + " points of damage!")

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit


    def fight_defense(self, points_of_damage):
        """Method to defense from a hit of other Pokemon.
        Method that implements the defense of the Pokemon from a hit of other
        Pokemon.
        Syntax
        ------
          [ ] = obj_Pokemon.fight_defense(points_of_damage)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] int Points that represent the hit from another Pokemon.
        Returns
        -------
        Exceptions
        ----------
        TypeError If the parameter points_of_damage is NOT an int.
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.fight_defense(13)
        """
        if not isinstance(points_of_damage, int):
            raise TypeError("The parameter points_of_damage should be an int.")

        print("The Pokemon " + self._pokemon_name +
              " has received an attack of " +
              str(points_of_damage) + " points of damage.")

        if points_of_damage > self._defense_rating:
            self._health_points = (self._health_points -
                                   (points_of_damage - self._defense_rating))
            pokemon_was_hit = True
        else:
            print("No damage received.")
            pokemon_was_hit = False

        # Normalizing the defeat of the Pokemon.
        if self._health_points < 1:
            self._health_points = 0

        return pokemon_was_hit


def main():
    """Function main of the module.
    The function main of this module is used to test the Class that is described
    in this module.
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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF

```
### pokemon_air
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.
@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
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

from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonAir(Pokemon):
    """Python class to implement a basic version of a Pokemon of the game.
    This Python class implements the basic version of a Pokemon of the game.
    Syntax
    ------
      obj = PokemonAir(id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)
    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.
    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.
    Attributes
    ----------
    Example
    -------
      >>> from pokemon import Pokemon
      >>> from weapon_type import WeaponType
      >>> obj_Pokemon = PokemonEarth(1, "Pidgey", WeaponType.PUNCH, 100, 7, 10)
    """


    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        """Constructor of the class.
        This special method is executed when an object of this class is
        created.
        Syntax
        ------
          [ ] = __init__(self, id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] pokemon_id ID of Pokemon.
          [in] pokemon_name Name of the Pokemon.
          [in] weapon_type Type of weapon that carries out the Pokemon.
          [in] health_points Points of health that the Pokemon has.
          [in] attack_rating Attack rating of the Pokemon.
          [in] defense_rating Defense rating of the Pokemon.
        Returns
        -------
          obj Python object output parameter that represents an instance
              of the class Pokemon.
        Exceptions
        ----------
          TypeError:
            If the parameter id is NOT a int.
            If the parameter pokemon_name is NOT a String.
            If the parameter weapon_type is NOT a enum WeaponType.
            If the parameter health_points is NOT be an int.
            If the parameter attack_rating is NOT be a int.
            If the parameter defense_rating is NOT be a int.
          ValueError:
            If the parameter id is already found in other Pokemon.
            If the parameter health_points is NOT > 0 and <= 100.
            If the parameter attack_rating is NOT > 0 and <= 10.
            If the parameter defense_rating is NOT > 0 and <= 10.
        Example
        -------
          >>> from pokemon import Pokemon
          >>> from weapon_type import WeaponType
          >>> obj_Pokemon = PokemonEarth(1, "Pidgey", WeaponType.PUNCH, 100, 7, 10)
        """

        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)


    def fight_defense(self, points_of_damage):
        """Method to defense from a hit of other Pokemon.
        Method that implements the defense of the Pokemon from a hit of other
        Pokemon.
        Syntax
        ------
          [ ] = obj_Pokemon.fight_defense(points_of_damage)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] int Points that represent the hit from another Pokemon.
        Returns
        -------
        Exceptions
        ----------
        TypeError If the parameter points_of_damage is NOT an int.
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.fight_defense(13)
        """
        if not isinstance(points_of_damage, int):
            raise TypeError("The parameter points_of_damage should be an int.")

        print("The Pokemon " + self._pokemon_name +
              " has received an attack of " +
              str(points_of_damage) + " points of damage.")

        failure_probability = random.randrange(0, 2)

        if failure_probability == 0:  # Normal defense applied.
            if points_of_damage > self._defense_rating:
                self._health_points = (self._health_points -
                                       (points_of_damage - self._defense_rating))
                pokemon_was_hit = True
            else:
                print("No damage received.")
                pokemon_was_hit = False
        else:
            print("No damage received.")
            pokemon_was_hit = False

        # Normalizing the defeat of the Pokemon.
        if self._health_points < 1:
            self._health_points = 0

        return pokemon_was_hit


def main():
    """Function main of the module.
    The function main of this module is used to test the Class that is described
    in this module.
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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonAir(1, "Pidgey", WeaponType.HEADBUTT, 100, 8, 7)

    if pokemon_1.get_pokemon_name() == "Pidgey":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 7:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonAir(7, "Pidgey", WeaponType.HEADBUTT, 100, 7, 6)

    if str(pokemon_2) == "Pokemon ID 7 with name Pidgey has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonAir(3, "Pidgey", WeaponType.KICK, 97, 8, 7)

    if pokemon_3.is_alive():
        pokemon_was_hit = pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if pokemon_was_hit:
            if not pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
        else:
            if pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
            
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonAir(4, "Pidgey", WeaponType.ELBOW, 93, 9, 5)

    pokemon_was_hit = pokemon_4.fight_defense(70)

    if pokemon_was_hit:
        if pokemon_4.get_health_points() == 28:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")
    else:
        if pokemon_4.get_health_points() == 93:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonAir(5, "Pidgey", WeaponType.PUNCH, 99, 10, 8)
    pokemon_6 = PokemonAir(6, "Pidgey", WeaponType.PUNCH, 99, 9, 6)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 95:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
```
### pokemon_water
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.
@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
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
from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonWater(Pokemon):
    """Python class to implement a basic version of a Pokemon of the game.
    This Python class implements the basic version of a Pokemon of the game.
    Syntax
    ------
      obj = PokemonWater(id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)
    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.
    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.
    Attributes
    ----------
    Example
    -------
      >>> from pokemon import Pokemon
      >>> from weapon_type import WeaponType
      >>> obj_Pokemon = PokemonWater(1, "Squirtle", WeaponType.PUNCH, 100, 7, 10)
    """


    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        """Constructor of the class.
        This special method is executed when an object of this class is
        created.
        Syntax
        ------
          [ ] = __init__(self, id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] pokemon_id ID of Pokemon.
          [in] pokemon_name Name of the Pokemon.
          [in] weapon_type Type of weapon that carries out the Pokemon.
          [in] health_points Points of health that the Pokemon has.
          [in] attack_rating Attack rating of the Pokemon.
          [in] defense_rating Defense rating of the Pokemon.
        Returns
        -------
          obj Python object output parameter that represents an instance
              of the class Pokemon.
        Exceptions
        ----------
          TypeError:
            If the parameter id is NOT a int.
            If the parameter pokemon_name is NOT a String.
            If the parameter weapon_type is NOT a enum WeaponType.
            If the parameter health_points is NOT be an int.
            If the parameter attack_rating is NOT be a int.
            If the parameter defense_rating is NOT be a int.
          ValueError:
            If the parameter id is already found in other Pokemon.
            If the parameter health_points is NOT > 0 and <= 100.
            If the parameter attack_rating is NOT > 0 and <= 10.
            If the parameter defense_rating is NOT > 0 and <= 10.
        Example
        -------
          >>> from pokemon import Pokemon
          >>> from weapon_type import WeaponType
          >>> obj_Pokemon = PokemonWater(1, "Squirtle", WeaponType.PUNCH, 100, 7, 10)
        """

        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         10, defense_rating)

        if isinstance(attack_rating, int):
            if 11 <= attack_rating <= 20:
                self._attack_rating = attack_rating
            else:
                raise ValueError("The parameter attack_rating should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter attack_rating should be a int.")


    def set_attack_rating(self, attack_rating_to_be_set):
        """Method to set the attribute attack_rating of the object.
        Method to set the attribute attack_rating based on a human-readable
        format of the object that is formed in this class.
        Syntax
        ------
          [ ] = obj_Pokemon.set_attack_rating( )
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] defense_rating_to_be_set String that contains the defense rating
                                        to assign to the Pokemon.
        Returns
        -------
        Exceptions
        ----------
          TypeError If the parameter defense_rating_to_be_set is NOT a int.
          ValueError If the parameter defense_rating_to_be_set is NOT > 0 and <= 10.
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.set_attack_rating(8)
        """
        if isinstance(attack_rating_to_be_set, int):
            if 11 <= attack_rating_to_be_set <= 20:
                self._attack_rating = attack_rating_to_be_set
            else:
                raise ValueError("The parameter attack_rating_to_be_set should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter attack_rating_to_be_set should be a int.")


def main():
    """Function main of the module.
    The function main of this module is used to test the Class that is described
    in this module.
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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonWater(1, "Squirtle", WeaponType.HEADBUTT, 100, 12, 8)

    if pokemon_1.get_pokemon_name() == "Squirtle":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 12:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 8:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonWater(7, "Squirtle", WeaponType.HEADBUTT, 100,15, 7)

    if str(pokemon_2) == "Pokemon ID 7 with name Squirtle has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonWater(3, "Squirtle", WeaponType.KICK, 97, 15, 8)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonWater(4, "Squirtle", WeaponType.ELBOW, 93, 11, 9)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 32:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonWater(5, "Squirtle", WeaponType.PUNCH, 99, 20, 10)
    pokemon_6 = PokemonWater(6, "Squirtle", WeaponType.PUNCH, 99, 18, 9)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 88:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
```
### pokemon_electricity
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.
@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
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

from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonElectricity(Pokemon):
    """Python class to implement a basic version of a Pokemon of the game.
    This Python class implements the basic version of a Pokemon of the game.
    Syntax
    ------
      obj = PokemonElectricity(id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)
    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.
    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.
    Attributes
    ----------
    Example
    -------
      >>> from pokemon import Pokemon
      >>> from weapon_type import WeaponType
      >>> obj_Pokemon = PokemonEarth(1, "Pikachu", WeaponType.PUNCH, 100, 7, 10)
    """


    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        """Constructor of the class.
        This special method is executed when an object of this class is
        created.
        Syntax
        ------
          [ ] = __init__(self, id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] pokemon_id ID of Pokemon.
          [in] pokemon_name Name of the Pokemon.
          [in] weapon_type Type of weapon that carries out the Pokemon.
          [in] health_points Points of health that the Pokemon has.
          [in] attack_rating Attack rating of the Pokemon.
          [in] defense_rating Defense rating of the Pokemon.
        Returns
        -------
          obj Python object output parameter that represents an instance
              of the class Pokemon.
        Exceptions
        ----------
          TypeError:
            If the parameter id is NOT a int.
            If the parameter pokemon_name is NOT a String.
            If the parameter weapon_type is NOT a enum WeaponType.
            If the parameter health_points is NOT be an int.
            If the parameter attack_rating is NOT be a int.
            If the parameter defense_rating is NOT be a int.
          ValueError:
            If the parameter id is already found in other Pokemon.
            If the parameter health_points is NOT > 0 and <= 100.
            If the parameter attack_rating is NOT > 0 and <= 10.
            If the parameter defense_rating is NOT > 0 and <= 10.
        Example
        -------
          >>> from pokemon import Pokemon
          >>> from weapon_type import WeaponType
          >>> obj_Pokemon = PokemonEarth(1, "Pikachu", WeaponType.PUNCH, 100, 7, 10)
        """

        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)


    def fight_attack(self, pokemon_to_attack):
        """Method to attack using a hit to other Pokemon.
        Method that implements the attack of the Pokemon using a hit over other
        Pokemon.
        Syntax
        ------
          [ ] = obj_Pokemon.fight_attack(pokemon_to_attack)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] Pokemon pokemon_to_attack Pokemon to hit to.
        Returns
        -------
        Exceptions
        ----------
        TypeError If the parameter pokemon_to_attack is NOT a Pokemon.
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.fight_attack(Pokemon_enemy)
        """

        points_of_damage = self._attack_rating

        print("The Pokemon " + self._pokemon_name +
              " hits the Pokemon " + pokemon_to_attack.get_pokemon_name() +
              " with " + str(points_of_damage) + " points of damage!")

        hit_probability = random.randrange(0, 2)

        if hit_probability == 0:  # Normal attack applied.
            points_of_damage = self._attack_rating
        else:  # Special attack applied.
            points_of_damage = 2 * self._attack_rating

        pokemon_was_hit = pokemon_to_attack.fight_defense(points_of_damage)

        return pokemon_was_hit


def main():
    """Function main of the module.
    The function main of this module is used to test the Class that is described
    in this module.
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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonElectricity(1, "Pikachu", WeaponType.HEADBUTT, 100, 8, 7)

    if pokemon_1.get_pokemon_name() == "Pikachu":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 7:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonElectricity(7, "Pikachu", WeaponType.HEADBUTT, 100, 7, 6)

    if str(pokemon_2) == "Pokemon ID 7 with name Pikachu has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonElectricity(3, "Pikachu", WeaponType.KICK, 97, 8, 7)

    if pokemon_3.is_alive():
        pokemon_was_hit = pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if pokemon_was_hit:
            if not pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
        else:
            if pokemon_3.is_alive():
                print("Test PASS. The method is_alive() has been implemented correctly.")
            else:
                print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonElectricity(4, "Pikachu", WeaponType.ELBOW, 93, 9, 5)

    pokemon_was_hit = pokemon_4.fight_defense(70)

    if pokemon_was_hit:
        if pokemon_4.get_health_points() == 28:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")
    else:
        if pokemon_4.get_health_points() == 93:
            print("Test PASS. The method fight_defense() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonElectricity(5, "Pikachu", WeaponType.PUNCH, 99, 10, 8)
    pokemon_6 = PokemonElectricity(6, "Pikachu", WeaponType.PUNCH, 99, 9, 6)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if (pokemon_6.get_health_points() == 95) or (pokemon_6.get_health_points() == 85):
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
```
### pokemon_earth
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.
@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
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
from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonEarth(Pokemon):
    """Python class to implement a basic version of a Pokemon of the game.
    This Python class implements the basic version of a Pokemon of the game.
    Syntax
    ------
      obj = PokemonEarth(id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)
    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.
    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.
    Attributes
    ----------
    Example
    -------
      >>> from pokemon import Pokemon
      >>> from weapon_type import WeaponType
      >>> obj_Pokemon = PokemonEarth(1, "Diglett", WeaponType.PUNCH, 100, 7, 10)
    """


    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        """Constructor of the class.
        This special method is executed when an object of this class is
        created.
        Syntax
        ------
          [ ] = __init__(self, id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] pokemon_id ID of Pokemon.
          [in] pokemon_name Name of the Pokemon.
          [in] weapon_type Type of weapon that carries out the Pokemon.
          [in] health_points Points of health that the Pokemon has.
          [in] attack_rating Attack rating of the Pokemon.
          [in] defense_rating Defense rating of the Pokemon.
        Returns
        -------
          obj Python object output parameter that represents an instance
              of the class Pokemon.
        Exceptions
        ----------
          TypeError:
            If the parameter id is NOT a int.
            If the parameter pokemon_name is NOT a String.
            If the parameter weapon_type is NOT a enum WeaponType.
            If the parameter health_points is NOT be an int.
            If the parameter attack_rating is NOT be a int.
            If the parameter defense_rating is NOT be a int.
          ValueError:
            If the parameter id is already found in other Pokemon.
            If the parameter health_points is NOT > 0 and <= 100.
            If the parameter attack_rating is NOT > 0 and <= 10.
            If the parameter defense_rating is NOT > 0 and <= 10.
        Example
        -------
          >>> from pokemon import Pokemon
          >>> from weapon_type import WeaponType
          >>> obj_Pokemon = PokemonEarth(1, "Diglett", WeaponType.PUNCH, 100, 7, 10)
        """

        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         attack_rating, 10)

        if isinstance(defense_rating, int):
            if 11 <= defense_rating <= 20:
                self._defense_rating = defense_rating
            else:
                raise ValueError("The parameter defense_rating should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter defense_rating should be a int.")


    def set_defense_rating(self, defense_rating_to_be_set):
        """Method to set the attribute defense_rating of the object.
        Method to set the attribute defense_rating based on a human-readable
        format of the object that is formed in this class.
        Syntax
        ------
          [ ] = obj_Pokemon.set_defense_rating( )
        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] defense_rating_to_be_set String that contains the defense rating
                                        to assign to the Pokemon.
        Returns
        -------
        Exceptions
        ----------
          TypeError If the parameter defense_rating_to_be_set is NOT a int.
          ValueError If the parameter defense_rating_to_be_set is NOT > 0 and <= 10.
        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.set_attack_rating(8)
        """
        if isinstance(defense_rating_to_be_set, int):
            if 11 <= defense_rating_to_be_set <= 20:
                self._defense_rating = defense_rating_to_be_set
            else:
                raise ValueError("The parameter defense_rating_to_be_set should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter defense_rating_to_be_set should be a int.")


def main():
    """Function main of the module.
    The function main of this module is used to test the Class that is described
    in this module.
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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = PokemonEarth(1, "Diglett", WeaponType.HEADBUTT, 100, 8, 15)

    if pokemon_1.get_pokemon_name() == "Diglett":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 15:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonEarth(7, "Diglett", WeaponType.HEADBUTT, 100, 7, 12)

    if str(pokemon_2) == "Pokemon ID 7 with name Diglett has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonEarth(3, "Diglett", WeaponType.KICK, 97, 8, 15)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = PokemonEarth(4, "Diglett", WeaponType.ELBOW, 93, 9, 11)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 34:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonEarth(5, "Diglett", WeaponType.PUNCH, 99, 10, 20)
    pokemon_6 = PokemonEarth(6, "Diglett", WeaponType.PUNCH, 99, 9, 18)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
```
### weapon_type
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the Enum WeaponType, but also the test of
this Python class.
@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  weapon_type.py
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
from enum import Enum


class WeaponType(Enum):
    """Python class to implement an enumeration for the attribute Weapon Type.
    This Python class implements an enumeration for the attribute Weapon Type.
    Syntax
    ------
      obj = WeaponType.Enum
    Parameters
    ----------
    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class WeaponType.
    Attributes
    ----------
    Example
    -------
      >>> from weapon_type import WeaponType
      >>> obj_WeaponType = WeaponType.Boxer
    """
    PUNCH = 2
    KICK = 4
    ELBOW = 6
    HEADBUTT = 10

    def __str__(self):
        return self.name

    @staticmethod
    def from_str(str_weapon_type):
        """Method to obtain a Enum from a String.
        This method is used to generate a Enum based on a String.
        Syntax
        ------
          [ ] = from_str(str_weapon_type)
        Parameters
        ----------
          str_weapon_type String String that represents a Weapon Type.
        Returns
        -------
          Null .
        Example
        -------
          >>> weapon_type.from_str("punch")
        """
        str_weapon_type = str_weapon_type.lower()
        if str_weapon_type == 'punch':
            return WeaponType.PUNCH
        elif str_weapon_type == 'kick':
            return WeaponType.KICK
        elif str_weapon_type == 'elbow':
            return WeaponType.ELBOW
        elif str_weapon_type == 'headbutt':
            return WeaponType.HEADBUTT
        else:
            raise TypeError("The str " + str_weapon_type + " does not correspond with a warrior Type")


def main():
    """Function main of the module.
    The function main of this module is used to test the Class WeaponType.
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

    print("=================================================================.")
    print("Test Case 1: Check Class WeaponType - Name.")
    print("=================================================================.")

    if isinstance(WeaponType.PUNCH, WeaponType):
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.KICK, WeaponType):
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.ELBOW, WeaponType):
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WeaponType.HEADBUTT, WeaponType):
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Check Class WeaponType - Value.")
    print("=================================================================.")

    if WeaponType.PUNCH.value == 2:
        print("Test PASS. The enum for Punch has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.KICK.value == 4:
        print("Test PASS. The enum for Kick has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.ELBOW.value == 6:
        print("Test PASS. The enum for Elbow has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if WeaponType.HEADBUTT.value == 10:
        print("Test PASS. The enum for Head Butt has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
```
