my_users = [
 {'username': 'username', 'password': 'password', 'role': 'role'},
 {'username': 'admin01', 'password': 'AdminPass!23', 'role': 'admin'},
 {'username': 'jdoe', 'password': 'UserPass!45', 'role': 'user'},
 {'username': 'asmith', 'password': 'UserPass!67', 'role': 'user'},
 {'username': 'superadmin', 'password': 'RootPass!89', 'role': 'admin'},
 {'username': 'mbrown', 'password': 'UserPass!90', 'role': 'user'}]




usrname_tester = ''
pwd_tester = ''

juistelogin = False

inloggen = True

keuzemenu = '''
1) alle gebruikers bekijken
2) gebruiker toevoegen
3) afmelden
Uw Keuze:
'''


while inloggen:
    login_user = input('geef je gebruikernaaam in: ')
    login_password = input('geef je wachtwoord in: ')
    testing = 6
    for i in my_users:
        temp_dict = i
        testing -= 1
        counter_logins = len(my_users)
        #print(type(temp_dict))
        usrname_tester = temp_dict['username']
        pwd_tester = temp_dict['password']

        if usrname_tester == login_user and pwd_tester == login_password:
                print('login succesvol')
                juistelogin = True


                keuzemaken = True

                while keuzemaken:
                    # print(int(juistelogin))

                    if int(juistelogin) == 1:

                        keuze = input(keuzemenu)

                        if int(keuze) == 1:
                            for z in my_users:

                                if z['role'] == 'user':
                                    print(i['username'], i['role'])
                                elif z['role'] == 'admin':
                                    print(i['username'], i['role'])
                                else:
                                    pass
                            keuzemaken = False
                        elif int(keuze) == 2:
                            for j in my_users:

                                if j['role'] == 'admin':
                                    print('welcome admin')
                                    new_username = input('geef een unieke username in vam minstens 3 char: ')
                                    j.update('user', new_username)

                                elif j['role'] == 'user':
                                    print('you are do not have sufficient permission')
                                    keuzemaken = False
                                else:
                                    print('how did u get here')

                        elif int(keuze) == 3:
                            print('goodbye')
                            keuzemaken = False
                            inloggen = False
                        else:
                            print('foutive invoer')

        else:
            if testing == 0:
                print('foutive invoer')
            else:
                pass


