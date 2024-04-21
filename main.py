from classes import *

# TODO: Main functions that creates UI, accounts, etc

desired_skills = [{'name': 'Python', 'level': 1, 'exp': 0},
                  {'name': 'Guitar', 'level': 1, 'exp': 0}]

player = Player('Jeff', desired_skills)



def main():
    player.add_new_skill(input('What is your new skill? '))
    print(player.skills)


if __name__ == "__main__":
    main()