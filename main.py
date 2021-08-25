from time import sleep
import botCommands
import colorama
from colorama import Fore, Style
from banner import banner as bn
from platform import system
import os
import sys
import time
import re
# {slowprint:
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.5 / 100)
# }

# { Clear Function:
def clear():
    if system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
# }

def main():
    help_commands = ["-h", "--h", "-H", "--HELP", "-help", "-HELP", "--help", "help", "HELP", "/", "/?", "?", "-", ""]
    
    try:
        if sys.argv[1] in help_commands:
            clear()

            print(bn)
            print(f"""\n\t{Fore.RED}[{Fore.LIGHTGREEN_EX}FaQ{Fore.WHITE}~{Fore.WHITE}@SalmanAlwan{Fore.WHITE}]\n\n\t{Fore.RED}[{Fore.LIGHTGREEN_EX}Help{Fore.WHITE}~{Fore.WHITE}@Command{Fore.WHITE}]
            \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}-u {Fore.WHITE}[USERNAME] 
            \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}-p {Fore.WHITE}[PASSWORD] 
            \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}-h {Fore.WHITE}Help Menu 
            
            \t{Fore.RED}>> {Fore.LIGHTGREEN_EX}EXAMPLE:{Fore.WHITE} {Fore.WHITE} 
            \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-u {Fore.WHITE}user1234 {Fore.BLUE}-p {Fore.WHITE}password1234\n""")
            quit()
        if sys.argv[1] == "-u" and sys.argv[3] == "-p":
            pat_usr = re.compile("[A-Za-z0-9]+")
            pat_psw = re.compile("[A-Za-z0-9]+")

            
            

            if pat_usr.fullmatch(sys.argv[2]) is not None and pat_psw.fullmatch(sys.argv[4]) is not None:
                pass
            else:
                clear()

                print(bn)
                print(f"""\n\t{Fore.RED}[{Fore.LIGHTGREEN_EX}FaQ{Fore.WHITE}~{Fore.WHITE}@SalmanAlwan{Fore.WHITE}]\n\n\t{Fore.RED}[{Fore.LIGHTGREEN_EX}Help{Fore.WHITE}~{Fore.WHITE}@Command{Fore.WHITE}]
                \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-u {Fore.WHITE}[USERNAME] 
                \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-p {Fore.WHITE}[PASSWORD] 
                \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-h {Fore.WHITE}Help Menu 
                
                \t{Fore.RED}>> {Fore.LIGHTGREEN_EX}EXAMPLE:{Fore.WHITE} {Fore.WHITE} 
                \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-u {Fore.WHITE}user1234 {Fore.BLUE}-p {Fore.WHITE}password1234\n""")
                quit()
        else:
            clear()

            print(bn)
            print(f"""\n\t{Fore.RED}[{Fore.LIGHTGREEN_EX}FaQ{Fore.WHITE}~{Fore.WHITE}@SalmanAlwan{Fore.WHITE}]\n\n\t{Fore.RED}[{Fore.LIGHTGREEN_EX}Help{Fore.WHITE}~{Fore.WHITE}@Command{Fore.WHITE}]
            \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-u {Fore.WHITE}[USERNAME] 
            \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-p {Fore.WHITE}[PASSWORD] 
            \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-h {Fore.WHITE}Help Menu 
            
            \t{Fore.RED}>> {Fore.LIGHTGREEN_EX}EXAMPLE:{Fore.WHITE} {Fore.WHITE} 
            \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-u {Fore.WHITE}user1234 {Fore.BLUE}-p {Fore.WHITE}password1234\n""")
            quit()
    except IndexError:
        clear()

        print(bn)
        
        print(f"""\n\t{Fore.RED}[{Fore.LIGHTGREEN_EX}FaQ{Fore.WHITE}~{Fore.WHITE}@SalmanAlwan{Fore.WHITE}]\n\n\t{Fore.RED}[{Fore.LIGHTGREEN_EX}Help{Fore.WHITE}~{Fore.WHITE}@Command{Fore.WHITE}]
        \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-u {Fore.WHITE}[USERNAME] 
        \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-p {Fore.WHITE}[PASSWORD] 
        \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-h {Fore.WHITE}Help Menu 
        
        \t{Fore.RED}>> {Fore.LIGHTGREEN_EX}EXAMPLE:{Fore.WHITE} {Fore.WHITE} 
        \t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}-u {Fore.WHITE}user1234 {Fore.BLUE}-p {Fore.WHITE}password1234\n""")
        quit()
    clear()
    print(bn)
    
    print('\n\n', '\t')
    slowprint (Fore.RED+"                       ["+Fore.LIGHTGREEN_EX+"welcome"+Fore.BLUE+"~"+Fore.WHITE+"@User"+Fore.RED+']')
    slowprint (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"igSuck"+Fore.BLUE+"~"+Fore.WHITE+"@SalmanAlwan"+Fore.RED+']')

    print(Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"fetching"+Fore.BLUE+"~"+Fore.WHITE+f"@Username | Password"+Fore.RED+']')
    pw = sys.argv[4]
    usr = sys.argv[2]
    bot = botCommands.InstaBot(usr, pw)
    sleep(0.5)

    # TODO: ADD MORE COMMANDS
    
    print(f"""\n\t{Fore.RED}[{Fore.LIGHTGREEN_EX}Enter{Fore.BLUE}~{Fore.WHITE}@Home{Fore.RED}]
          \t{Fore.RED}[{Fore.LIGHTGREEN_EX}1{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}get your followers 
          \t{Fore.RED}[{Fore.LIGHTGREEN_EX}2{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}follow followers of @xyz 
          \t{Fore.RED}[{Fore.LIGHTGREEN_EX}3{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}follow users followed by @xyz 
          \t{Fore.RED}[{Fore.LIGHTGREEN_EX}4{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}get @username's followers
          \t{Fore.RED}[{Fore.LIGHTGREEN_EX}5{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}queue tasks
          
          \t\t {Fore.RED}[{Fore.LIGHTGREEN_EX}OR{Fore.RED}] 
          \t {Fore.RED}[{Fore.LIGHTGREEN_EX}00{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}terminate Bot""")

    while True:
        ip = input (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+f"{usr}"+Fore.BLUE+"~"+Fore.WHITE+f"@Choice"+Fore.RED+f']{Fore.WHITE} ')
        if(ip == '1'):
            bot.get_followers_of()

        elif(ip == '2'):
            #print(f"{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}Username {Fore.WHITE}of @account to be scrapped: ")
            user = input(f"\t{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}Username {Fore.WHITE}of @account to be scrapped: ")
            bot.follow_followers_of(user)

        elif(ip == '3'):
            sleep(1)
            user = input(f"\t{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}Username {Fore.WHITE}of @account to be scrapped: ")
            bot.follow_users_followed_by(user)

        elif(ip == '4'):
            sleep(1)
            #user = input("Username of account to be scrapped: ")
            user = input(f"\t{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}Username {Fore.WHITE}of @account to be scrapped: ")
            bot.get_followers_of(user)

        elif ip == '5':
            print(f"""\n\t{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}Queue {Fore.WHITE}task by entering @index of the task
                        \t\t\t{Fore.RED}[{Fore.LIGHTGREEN_EX}python{Fore.RED}] {Fore.WHITE}main.py {Fore.BLUE}get your followers 
                        \t\t\t{Fore.RED}[{Fore.LIGHTGREEN_EX}2{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}follow followers of @xyz 
                        \t\t\t{Fore.RED}[{Fore.LIGHTGREEN_EX}3{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}get @username's followers
                        \t\t\t{Fore.RED}[{Fore.LIGHTGREEN_EX}99{Fore.RED}] {Fore.BLUE}to {Fore.WHITE}stop @queueing""")
            queue = []
            while True:
                
                choice = input(f"\t\t{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}Enter {Fore.WHITE}task: ")
                if choice == '99' or choice == 99:
                    break
                if(choice == '1'):
                    queue.append((1, 0))

                elif(choice == '2'):
                    user = input(f"\t{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}Username {Fore.WHITE}of @account to be scrapped: ")
                    
                    target = input(f"\t{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}Enter {Fore.WHITE}Max @people to follow: ")
                    queue.append((2, user, target))

                elif(choice == '3'):
                    user = input(f"\t{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}Username {Fore.WHITE}of @account to be scrapped: ")

                    queue.append((3, user))

            for task in queue:
                if task[0] == 1:
                    bot.get_followers_of()
                if task[0] == 2:
                    bot.follow_followers_of(task[1], task[2])
                elif task[0] == 3:
                    bot.get_followers_of(task[1])
            print(f'\t{Fore.RED}[{Fore.LIGHTGREEN_EX}Queue{Fore.BLUE}~{Fore.WHITE}@Completed{Fore.RED}]')

        elif ip == '00':
            break

        else:
            print(f"\t{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}Wrong {Fore.WHITE}Choice!")
            sleep(3)
            continue

        print(f"\t{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}Task {Fore.WHITE}finished!")         
    print(Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"Bot"+Fore.BLUE+"~"+Fore.WHITE+f"@terminated"+Fore.RED+']')



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\t{Fore.RED}[{Fore.LIGHTGREEN_EX}~{Fore.RED}] {Fore.BLUE}You {Fore.WHITE}terminated the @operation Manually!")
