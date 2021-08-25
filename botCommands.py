# {Modules:
from selenium import webdriver
from time import sleep
import os
import time
from platform import system
import sys
import colorama
from colorama import Fore, Style
# }

# {Classes:
class InstaBot:
    task = 0
    count = 0
    
    def __init__(self, username, pw):
        log = open("log.txt", 'a')
        log.write("__Session Start__\n\t")
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.maximize_window()
        self.username = username
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        sleep(0.5)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        sleep(0.5)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(5)

        # { Clear Function:
        def clear():
            if system() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')
        # }

        # {slowprint:
        def slowprint(s):
            for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(2.5 / 100)
        # }

        # {GUI:
        sys.path.insert(1, 'E:\\~Salman\\programming\\python\\igSuck-New\\banner.py')
        from banner import banner as bn
        clear()
        print(bn)
        slowprint (Fore.RED+"                       ["+Fore.LIGHTGREEN_EX+"login"+Fore.BLUE+"~"+Fore.WHITE+"@Successful"+Fore.RED+']')
        slowprint (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"bot"+Fore.BLUE+"~"+Fore.WHITE+"@Alive"+Fore.RED+']')

        str = time.asctime(time.localtime(time.time())) + ' ->  Login Successful ('+username+'):'
        log.write(str)
        log.close()
        
    def scroll_followers_list(self, target):
        print(Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"scrolling"+Fore.BLUE+"~"+Fore.WHITE+f"@{target}"+Fore.RED+']✘'+Fore.WHITE+' users.'+Fore.RED+' Dont'+Fore.WHITE+' close the window'+Fore.RED+'.'+Fore.WHITE)
        sleep(5)
        scroll_element = self.driver.find_element_by_xpath(
            "//div[@class='isgrP']")
        length = 0
        sleep(3)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView();", scroll_element)

        while length < target-1:

            sleep(1)
            elements = scroll_element.find_elements_by_tag_name('button')[-10:]
            for element in elements:
                try:
                    self.driver.execute_script(
                        "return arguments[0].scrollIntoView();", element)
                    sleep(0.15)
                except:
                    continue
            while len(scroll_element.find_elements_by_xpath("//div[@class='By4nA']")) > 0:
                print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"bot"+Fore.BLUE+"~"+Fore.WHITE+"@Sleeping"+Fore.RED+']')
                sleep(1)
            sleep(1)
            length = len(scroll_element.find_elements_by_tag_name('button'))
        print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"scroll"+Fore.BLUE+"~"+Fore.WHITE+"@Complete"+Fore.RED+']')

    def follow_button_click(self, target, type_='followers', scroll_element="//div[@class='isgrP']"):
        count = 0
        scroll_element = self.driver.find_element_by_xpath(scroll_element)
        buttons = scroll_element.find_elements_by_tag_name('button')
        for button in buttons:
            try:
                self.driver.execute_script(
                    "return arguments[0].scrollIntoView();", button)
                if button.text == 'Follow':
                    self.focus_and_click(button)
                    count += 1
                    print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"followed"+Fore.BLUE+"~"+Fore.WHITE+f"@{count}"+Fore.RED+']', end='\r')

                    if count >= target:
                        print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"target"+Fore.BLUE+"~"+Fore.WHITE+f"@Met"+Fore.RED+']')
                        break
                    elif count == 25:
                        sleep(10)
                    elif count == 50:
                        sleep(20)
                    elif count == 100:
                        sleep(30)
                    sleep(6)
                tries = 0
                while tries < 20:
                    if button.text == 'Follow':
                        sleep(6)
                        if button.text == 'Follow':
                            self.focus_and_click(button)
                            tries += 1
                    elif button.text == 'Following' or button.text == 'Requested':
                        break
                    sleep(1)
                    try:
                        if scroll_element.find_element_by_tag_name('button').text == 'Unfollow':
                            scroll_element.find_element_by_tag_name(
                                'button').click()
                            break
                    except:
                        pass
                    if tries == 20:
                        sleep(60)
            except:
                pass
        return count

    
    
    def focus_and_click(self, element):
        self.driver.execute_script(
            "return arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def get_followers_of(self, username = ""):
        log = open("log.txt", 'a')
        if not username: username=self.username
        file = username + "_followers"
        list_ = open(file, "w+")
        sleep(2)

        self.driver.get('https://www.instagram.com/' + username + '/')
        sleep(4)

        fol = int((self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]").text).split()[0])
        print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"followers"+Fore.BLUE+"~"+Fore.WHITE+f"@{fol}"+Fore.RED+']')
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()

        self.scroll_followers_list(int(fol))
        scroll_box = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        links = scroll_box.find_elements_by_tag_name('a')
        usernames = [name.text for name in links if name.text != '']
        list_.writelines(["%s\n" % follower for follower in usernames])
        list_.close()

        str_ = "\n\tTask "+str(self.task)+": Fetched " + str(len(usernames)) + '/' + str(fol) + " followers of " + username
        log.write(str_)
        print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"done"+Fore.BLUE+"~"+Fore.WHITE+f"@Extracting"+Fore.RED+']')
        log.close()
    def follow_followers_of(self, username, target=0):
        log = open("log.txt", 'a')
        self.task += 1
        self.driver.get('https://www.instagram.com/' + username + '/')
        sleep(5)

        no_f = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]").text
        if "k" or "m" in no_f:
            fol = no_f.replace(" followers", "")
            fol = fol.replace(",", "")
            print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"followers"+Fore.BLUE+"~"+Fore.WHITE+f"@{fol}"+Fore.RED+']')
            self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
                .click()
            sleep(2)
            count = 0
            if target == 0:
            
                target = int(input (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+f"{username}"+Fore.BLUE+"~"+Fore.WHITE+f"@Home"+Fore.RED+']✗ '+Fore.WHITE+'Enter max people to follow: '))
            log.write("\n\tTask "+str(self.task)+": Following " +
                    str(target) + " followers of "+username)
            print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"now"+Fore.BLUE+"~"+Fore.WHITE+f"@Following"+Fore.RED+']')
            batch = 1
            while count < target:
                batch_size = min((target-count), 100)
                self.scroll_followers_list(batch_size)
                print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"batch"+Fore.BLUE+"~"+Fore.WHITE+f"@{batch}"+Fore.RED+f']✘ '+Fore.WHITE+f'of size {Fore.RED}{batch_size}{Style.RESET_ALL}.')
                count += self.follow_button_click(batch_size)
                string = '\n\t\tFollowed ' + \
                    str(count)+' users till batch '+str(batch)
                print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"followed"+Fore.BLUE+"~"+Fore.WHITE+f"@{count}"+Fore.RED+f']✘ '+Fore.WHITE+f'users till batch.')
                log.write(string)
                batch += 1
            
            log.write("\n\tTask "+str(self.task)+": Followed " +
                    str(count) + " followers of "+username)
            self.count += count
            log.close()
        else:

            fol = no_f.replace(" followers", "")
            fol = int(fol.replace(",", ""))
            print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"followers"+Fore.BLUE+"~"+Fore.WHITE+f"@{fol}"+Fore.RED+']')
            self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
                .click()
            sleep(2)
            count = 0
            if target == 0:
            
                target = int(input (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+f"{username}"+Fore.BLUE+"~"+Fore.WHITE+f"@Home"+Fore.RED+']✗ '+Fore.WHITE+'Enter max people to follow: '))
            log.write("\n\tTask "+str(self.task)+": Following " +
                    str(target) + " followers of "+username)
            print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"now"+Fore.BLUE+"~"+Fore.WHITE+f"@Following"+Fore.RED+']')
            batch = 1
            while count < target:
                batch_size = min((target-count), 100)
                self.scroll_followers_list(batch_size)
                print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"batch"+Fore.BLUE+"~"+Fore.WHITE+f"@{batch}"+Fore.RED+f']✘ '+Fore.WHITE+f'of size {Fore.RED}{batch_size}{Style.RESET_ALL}.')
                count += self.follow_button_click(batch_size)
                string = '\n\t\tFollowed ' + \
                    str(count)+' users till batch '+str(batch)
                print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"followed"+Fore.BLUE+"~"+Fore.WHITE+f"@{count}"+Fore.RED+f']✘ '+Fore.WHITE+f'users till batch.')
                log.write(string)
                batch += 1
            
            log.write("\n\tTask "+str(self.task)+": Followed " +
                    str(count) + " followers of "+username)
            self.count += count
            log.close()
    
    def follow_users_followed_by(self, username, target=0):
        log = open("log.txt", 'a')
        self.task += 1
        log.write("\n\tTask "+str(self.task) +
                  ": Following users followed by "+username)
        self.driver.get('https://www.instagram.com/' + username + '/')
        sleep(5)

        no_f = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]").text
        fol = no_f.replace(" followers", "")
        fol = int(fol.replace(",", ""))

        print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"followers"+Fore.BLUE+"~"+Fore.WHITE+f"@{fol}"+Fore.RED+f']✘ '+Fore.WHITE+f'users till batch.')
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(2)
        count = 0
        if target == 0:
            target = int(input (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+f"{username}"+Fore.BLUE+"~"+Fore.WHITE+f"@Home"+Fore.RED+']✗ '+Fore.WHITE+'Enter max people to follow: '))
        print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"now"+Fore.BLUE+"~"+Fore.WHITE+f"@Following"+Fore.RED+']')
        batch = 1
        while count < target:
            batch_size = min((target-count), 100)
            self.scroll_followers_list(batch_size)
            print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"batch"+Fore.BLUE+"~"+Fore.WHITE+f"@{batch}"+Fore.RED+f']✘ of size {Fore.RED}{batch_size}{Style.RESET_ALL}.')
            count += self.follow_button_click(batch_size, 'following')
            string = '\n\t\tFollowed ' + \
                str(count)+' users in batch '+str(batch)
            print (Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"followed"+Fore.BLUE+"~"+Fore.WHITE+f"@{count}"+Fore.RED+f']✘ '+Fore.WHITE+f'users till batch.')
            log.write(string)
            batch += 1

        log.write("\n\tTask "+str(self.task)+": Followed " +
                  str(count) + " users followed by "+username)
        self.count += count
        log.close()

    

        
        

    def __del__(self):
        log = open("log.txt", 'a')
        print(Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"Bot"+Fore.BLUE+"~"+Fore.WHITE+f"@terminated"+Fore.RED+']')
        print(Fore.RED+"\n                       ["+Fore.LIGHTGREEN_EX+"Followed"+Fore.BLUE+"~"+Fore.WHITE+f"@{self.count}"+Fore.RED+']')
        log.write("\n\n\tFollowed total "+str(self.count) +' users and performed '+str(self.task)+' tasks \n__Session_End__ \n\n')
        log.close()
        # }

# }