def select_pokemon(pokemons):
    # Get the pokemon name from user
    # Think of a way to find that pokemon from "pokemons" list
    # return that pokemon (return <pokemon>)


def select_random_pokemon(pokemons):
    # Use the random.choice() in random module
    # random.choice(<array or list or etc>) = randomly chosen element
    # Return the pokemons


def move_pokemon(pokemon, pokemons, player):
    # remove the pokemon from pokemons list
    # append the pokemon to player list (player.append(pokemon) if player is an existing container like a list)
    # Return the modified pokemons list

def print_players(player1, player2):
    # Print player1's pokemons (basically print player1's player list)
    # Print player2's pokemons



def make_attack(pokemon1, pokemon2):
    # Get pokemon1's AP, pokemon2's HP
    # Decrease pokemon2's HP by pokemon1's AP
    # Return the pokemons


def fight_pokemons(pokemon1, pokemon2, player1, player2):
    # In a loop, let the pokemons attack each other
        # Decrease pokemon2's HP by pokemon1's AP
        # Check if pokemon2 is dead (HP < 0)
            # If dead, then pokemon1 wins
                # Remove the dead pokemon from player's list
            # If not, then pokemon1 attacks pokemon2

        # Be careful with break statements or you'll get stuck in infinite loop
    # return pokemons

def main():
    pokemons = <list here>
    print(pokemons)

    player1_pokemon = select_pokemon(pokemons)
    player2_pokemon = select_random_pokemon(pokemons)
    pokemons = move_pokemon(...)
    pokemons = move_pokemon(...)
    # Print chosen pokemons
    # Print the pokemon list
    # fight
