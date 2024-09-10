import os, config
from colorama import Fore, Back

def cls():

    os.system('clear')

def white(text):

    print(Fore.BLACK + Back.WHITE + text + Fore.RESET + Back.RESET)

cls()

main = True
debug = False
shell = True

while main:

    while shell:

        a = input(Fore.LIGHTRED_EX + config.name + Fore.WHITE + '@fluffterm % ' + Fore.LIGHTGREEN_EX)

        b = a.split()

        if a == 'exit' or a == 'quit':

            cls()
            exit()

        elif a == 'clear' or a == 'cls':

            cls()

        elif a == 'ls' or a == 'dir':

            print(Fore.RESET + '\n'.join(config.files))

        elif b[0] == 'cat' or b[0] == 'type' and len(b) == 2:

            if b[1] in config.files:

                print(Fore.RESET + config.cont[config.files.index(b[1])])

        elif b[0] == 'vim' and len(b) == 2:

            cls()

            if b[1] in config.files:

               a = input(Fore.RESET + config.cont[config.files.index(b[1])])
               config.cont[config.files.index(b[1])] += a

            else:

                config.files.append(b[1])
                config.cont.append('')

                a = input()
                config.cont[config.files.index(b[1])] += a

            cls()

        elif b[0] == 'touch' and len(b) == 2 and not b[1] in config.files:

            config.files.append(b[1])
            config.cont.append('')

        elif b[0] == 'rm' and len(b) == 2 and b[1] in config.files:

            config.cont.pop(config.files.index(b[1]))
            config.files.pop(config.files.index(b[1]))

        elif a == 'debug':

            a = input(Fore.YELLOW + 'You are about to enter the debug shell, are you sure you want to continue?[Y/N]: ' + Fore.RESET)
            if a.lower() == 'y':

                shell = False
                debug = True
                cls()
                print(Fore.YELLOW + 'fluffTerm Debug Shell v1.0.0\n' + Fore.RESET)

    while debug:

        a = input(Fore.YELLOW + 'debug> ' + Fore.RESET)

        if a == 'exit':

            cls()
            exit()

        elif a == 'filedump':

            print(config.files)

        elif a == 'contdump':

            print(config.cont)
