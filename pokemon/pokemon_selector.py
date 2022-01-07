import random


def select_pokemon(pokemons):
    print('Pokemon list')
    print(pokemons)
    print('----------------------------')

    pokemon = ' '
    selected_pokemon = []
    selected_pokemon_name = ''

    while (selected_pokemon_name.lower() != pokemon):
        pokemon = str.lower(input('Enter a valid pokemon name: '))

        for i in range(len(pokemons)):
            if str.lower(pokemons[i][0][0]) == pokemon:
                selected_pokemon = pokemons[i]
                selected_pokemon_name = selected_pokemon[0][0]
    return selected_pokemon


def select_random_pokemon(pokemons):
    random_selected_pokemon = random.choice(pokemons)
    return random_selected_pokemon


def main():
    pokemon_list = [ [('Bulbasaur', 30, 90), 45],  [('Ivysaur', 42, 70), 60],  [('Venusaur', 35, 85), 82],  [('Charizard', 30, 65), 84],
    [('Squirtle', 30, 35), 48], [('Blastoise', 35, 45), 83], [('Caterpie', 25, 50), 30], [('Rattata', 30, 95), 56],
    [('Fearow', 25, 100), 90], [('Pikachu', 30, 80), 55], [('Primeape', 40, 90), 105],[('Arcanine', 40, 70), 110],
    [('Machop', 25, 55), 80], [('Machamp', 30, 80), 130], [('Geodude', 20, 45), 80], [('Graveler', 40, 90), 95], [('Golem', 45, 65), 120]]

    rand_number = random.randint(1,2)

    print('Player 1 is you')
    print('Player 2 is computer')
    print('')
    print("Player " + str(rand_number) + ' Chooses first')
    print('----------------------------')

    if rand_number == 1:
        user_pokemon = select_pokemon(pokemon_list)
        print('You chose ' + str(user_pokemon[0][0]) + '!')
        random_pokemon = select_random_pokemon(pokemon_list)
        print('Computer chose ' + random_pokemon[0][0] + '!')
    elif rand_number == 2:
        random_pokemon = select_random_pokemon(pokemon_list)
        print('Computer chose ' + random_pokemon[0][0] + '!')
        user_pokemon = select_pokemon(pokemon_list)
        print('You chose ' + str(user_pokemon[0][0]) + '!')
    else:
        print('rand_number error')
        print('rand_number=', rand_number)

if __name__ == '__main__':
    main()
