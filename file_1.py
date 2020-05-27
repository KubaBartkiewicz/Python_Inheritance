class User:
    def __init__(self, mail):
        self.mail = mail
        self.is_admin = False
        self.password = ''
        self.is_logged = False

    def create(self, password):
        self.password = password
        print(self.mail, ' ', password)

    def login(self, password):
        if password == self.password: self.is_logged = True

    def show_inbox(self):
        if self.is_logged: print('Email Inbox')

    def logout(self):
        if self.is_logged: self.is_logged = False

    def admin_panel(self):
        print('Admin panel') if self.is_admin else print('You are not an admin')


class Admin(User):
    def __init__(self, mail):
        User.__init__(self, mail)
        self.is_admin = True

    def admin_panel(self):
        if self.is_admin: print('You are in admin Panel and this is overwritten User method')

kruk = User(mail='kruk@kruk.pl')
kruk.create('qwerty123')
kruk.login('qwerty123')
kruk.show_inbox()
kruk.logout()
kruk.admin_panel()

adek = Admin(mail='adek@kruk.pl')
adek.create('qwerty')
adek.login('qwerty')
adek.show_inbox()
adek.logout()
adek.admin_panel()
