serveur = smtplib.SMTP('smtp.gmail.com', 587)    ## Connexion au serveur sortant (en precisant son nom et son port)
serveur.starttls()    ## Specification de la securisation
serveur.login("xxx", "xxx")    ## Authentification
message = "Debut actualisation xxx"    ## Message à envoyer
serveur.sendmail("xxx", "xxx", message)    ## Envoie du message
serveur.quit()    ## Deconnexion du serveur

##Code API

serveur = smtplib.SMTP('smtp.gmail.com', 587) ## Connexion au serveur sortant (en précisant son nom et son port)
serveur.starttls() ## Spécification de la sécurisation
serveur.login("xxx", "xxx") ## Authentification
message = "Actualisation bien reussite xxx" ## Message à envoyer
serveur.sendmail("xxx", "xxx", message) ## Envoie du message
serveur.quit() ## Déconnexion du serveur
