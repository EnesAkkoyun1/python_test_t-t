#sleep importeren van time om een timeout te zetten
from time import sleep

#correcte login gegeven aanmaken
username = "admin"
password = "EHB"

#teller aanmake om de aantal pogingen bij te houden
counter_login = 5

#while loop dat we er in blijven zolang we nog pogingen over hebben
while 6 > counter_login > 0:

    #inlog gegevens aanvragen van de user
    login_name = input("geef je gebruikernaam in: ")
    login_password = input("geef je wachtwoord in: ")

    #checken of de meegegeven inlog juist is
    if login_name != username and login_password != password:
        #als het fout is trekken we een login kans af
        counter_login -= 1

        #we laten de gebruiker weten dat er een kans is verloren en hoeveel hij er over heeft
        print("je hebt nog ", counter_login, "pogingen over!")

        #we checken of we nog poginge over hebben
        if counter_login == 0:
            print("5 foutieve pogingen na elkaar. Inloggen voor 1 minuut geblokkeerd!")
            # we geven de user opnieuw 5 pogingen

            #geen pogingen ovfhj
            # er dus starten we een clock van 60seconden
            sleep(5)
            #we laten user weten dat er een clock aan het aftikken is van 1 minuut

            counter_login = 5
        else:

            #we skippen deze lijn
            pass

    #als de inlog gegeven juist zijn voeren we dit uit
    else:
        #we zetten de aantal pogingen op -1 zodat we uit de while loop geraken
        counter_login = -1
        #geven mee aan de gebruiker dat inloggen is gelukt
        print("je bent ingelogd")
