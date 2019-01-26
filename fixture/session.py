

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_id("sign-in-link").click()
        wd.find_element_by_id("login_email7598429390711118").send_keys(username)
        wd.find_element_by_id("login_password06060568254534293").send_keys(password)
        wd.find_element_by_xpath("//button[@type='submit']").click()


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[2]/div/button").click()
        wd.find_element_by_link_text(u"Выйти").click()
        wd.find_element_by_xpath("//h1[@id='dropbox-logo']/a/img[2]").click()

    #def ensure_logout(self):
    #    wd = self.app.wd
    #    if self.is_logged_in():
    #        self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        if wd.find_elements_by_xpath("//h1") > 0 and wd.find_elements_by_xpath("//div[2]/div/div/div/div/button") > 0:
            return True
        else:
            return False


    #def is_logged_in_as(self, username):
    #    wd = self.app.wd
    #    return self.get_logged_user() == username

    #def get_logged_user(self):
    #    wd = self.app.wd
    #    return wd.find_element_by_css_selector("td.login-info-left span").text

    #def ensure_login(self, username, password):
    #    wd = self.app.wd
    #    if self.is_logged_in():
    #        if self.is_logged_in_as(username):
    #            return
    #        else:
    #            self.logout()
    #    self.login(username, password)


