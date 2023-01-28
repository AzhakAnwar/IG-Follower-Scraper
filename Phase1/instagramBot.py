from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time, json

class InstagramBot():
    def __init__(self, email, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'profile.managed_default_content_settings.images':2,
                'intl.accept_languages': 'en,en_US', #'disk-cache-size': 4096
                                                              })
##        self.browserProfile.add_argument('--headless')
        self.browser = webdriver.Chrome('chromedriver.exe', options=self.browserProfile)
##        self.browser.set_window_size(1920, 1080)
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
##        ## notification bypasser
##        try:
##            self.browser.find_elements_by_css_selector('button.aOOlW')[1].click()
##        except:
##            pass
        
    # def followWithUsername(self, username):
        # self.browser.get('https://www.instagram.com/' + username + '/')
        # time.sleep(2)
        # followButton = self.browser.find_element_by_css_selector('button')
        # if (followButton.text != 'Following'):
            # followButton.click()
            # time.sleep(2)
        # else:
            # print("You are already following this user")
    
    # def unfollowWithUsername(self, username):
        # self.browser.get('https://www.instagram.com/' + username + '/')
        # time.sleep(2)
        # followButton = self.browser.find_element_by_css_selector('button')
        # if (followButton.text == 'Following'):
            # followButton.click()
            # time.sleep(2)
            # confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            # confirmButton.click()
        # else:
            # print("You are not following this user")
            
    def writeFile(self, username, followers):
        with open('dequed', 'a+', errors = 'ignore') as f1, open('private2.json', 'r+', errors = 'ignore') as f2:
            f1.write(username + '\n')

            users = json.load(f2)
            users.update({username: followers})
            f2.seek(0)
            f2.truncate()
            json.dump(users, f2)

    # def getUserFollowings(self, parent):
        # prev1 = prev2 = 0
        # self.browser.get('https://www.instagram.com/' + parent)
        # time.sleep(2)
        # followersLink = self.browser.find_elements_by_css_selector('ul li a')[1]
        # maxFollowers = followersLink.find_element_by_css_selector('span').text
        # maxFollowers = int(maxFollowers.replace(',', ''))
        # followersLink.click()
        # time.sleep(2)
        
        # followersList = self.browser.find_element_by_css_selector("div[role='dialog'] ul")
        # numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    
        # followersList.click()
        # actionChain = webdriver.ActionChains(self.browser)
        
        # while (numberOfFollowersInList < maxFollowers):
            # actionChain.key_down(Keys.END).key_up(Keys.END).perform()
            # followerList = followersList.find_elements_by_css_selector('li')
            # time.sleep(0.7)

            # prev2 = prev1
            # prev1 = numberOfFollowersInList
            # numberOfFollowersInList = len(followerList)

            # if (prev1 == numberOfFollowersInList): time.sleep(0.8)                      ## if new followers are not loaded
            # if (prev1 == prev2 == numberOfFollowersInList): followersList.click()       ## if followers not loaded for 2 iterations

        # print(f'Got {numberOfFollowersInList} no. of followers')

        # followings = []
        # for user in followerList:
            # username = user.find_element_by_css_selector("div.d7ByH").text
            # followings.append(username)
            
            # if (len(followings) == maxFollowers): break
        # return followings
    
    def getUserFollowers(self, parent):
        prev1 = prev2 = prev3 = prev4 = prev5 = 0
        self.browser.get('https://www.instagram.com/' + parent)
        time.sleep(5)
        try:
            followersLink = self.browser.find_element_by_xpath("//ul/li[2]/a[contains(@href, 'follow')]")
        except NoSuchElementException:
            time.sleep(10)
            try:
                followersLink = self.browser.find_element_by_xpath("//ul/li[2]/a[contains(@href, 'follow')]")
            except NoSuchElementException:
                with open('failed', 'a+') as fp:
                    fp.write(parent + '\n')
                    
                return None
        # except NoSuchElementException:      ## private account
            # print('Private Account')
            # with open('private2', 'a+') as fp:
                # fp.write(parent + '\n')
            # return []
        maxFollowers = followersLink.find_element_by_css_selector('span').get_attribute('title')
        maxFollowers = int(maxFollowers.replace(',', ''))
        print(f'Max Follower = {maxFollowers}')
        followersLink.click()
        time.sleep(5)
        followersList = self.browser.find_element_by_css_selector("div[class='isgrP']")
        followerList = followersList.find_elements_by_css_selector('li')
        numberOfFollowersInList = len(followerList)
        if numberOfFollowersInList <= 5: return self.getUserFollowers(parent)
    
        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        
        while (numberOfFollowersInList < maxFollowers):
            #actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            actionChain.key_down(Keys.END).key_up(Keys.END).perform()
            time.sleep(0.5)
            followerList = followersList.find_elements_by_css_selector('li')
            
            prev5 = prev4
            prev4 = prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = numberOfFollowersInList
            numberOfFollowersInList = len(followerList)

            if (prev1 == numberOfFollowersInList): time.sleep(0.5)                      ## if new followers are not loaded
            if (prev1 == prev2 == numberOfFollowersInList): followersList.click()       ## if followers not loaded for 2 iterations
            if (prev1 == prev2 == prev3 == prev4 == prev5 == numberOfFollowersInList):
                if (numberOfFollowersInList / maxFollowers) < 0.90:
                    if maxFollowers < 1000:
                        self.closeBrowser()
                        self.browser = webdriver.Chrome('chromedriver.exe', options=self.browserProfile)
                        self.signIn()
                        return self.getUserFollowers(parent)
                    with open('failed', 'a+') as fp:
                        fp.write(parent + '\n')
                    return None
                break
            print(numberOfFollowersInList, end = ',')

        print(f'\nGot {numberOfFollowersInList} no. of followers')

        followers = []
        for user in followerList:
            try:
                username = user.find_element_by_css_selector("div.d7ByH").text
            except:
                username = ''
                continue
            followers.append(username)
            if (len(followers) == maxFollowers):
                break
        self.writeFile(parent, followers)

    def closeBrowser(self):
        self.browser.close()
        self.browser.quit()
            
    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()
