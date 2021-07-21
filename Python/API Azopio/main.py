#importation des différents modules
import requests
import datetime 
import json
import __version__.py
from openpyxl import load_workbook
import smtplib 

#donner le lien du fichier excel + ouverture de l'excel avec les différentes pages
path=''
wb = load_workbook(path)
ws1 = wb['Factures Clients']
ws2 = wb['Factures Fournisseurs']

serveur = smtplib.SMTP('smtp.gmail.com', )    ## Connexion au serveur sortant (en précisant son nom et son port)
serveur.starttls()    ## Spécification de la sécurisation
serveur.login("", "")    ## Authentification
message = "Debut actualisation"    ## Message à envoyer
serveur.sendmail("", "", message)    ## Envoie du message
serveur.quit()    ## Déconnexion du serveur

#incrementation de nos variables
o = i = 2
n1 = n2 = 1

#lecture de la date / heure en direct
a=datetime.datetime.now().timestamp()

#Bloc requete client
url = "https://apifeed.sellsy.com/0/"

payload={'request': '1',
'io_mode': 'json',
'do_in': '{"method":"document.getList","params":{"doctype":"invoice","pagination":{"nbperpage":"5000"}}}'}

headers = {
  'Authorization': 'OAuth oauth_consumer_key="...",oauth_token="...",oauth_signature_method="PLAINTEXT",oauth_timestamp={0},oauth_nonce="...",oauth_version="1.0",oauth_signature="..."'.format(a)
}
res = requests.request("POST", url, headers=headers, data=payload)
response=json.loads(res.text)

#début de la boucle for pour remplissage d'Excel
resp = response['response']['result']
for valeur in resp :
  print("Clients : n°",n1)
  v=valeur
  data=resp[v]
  ws1['B'+str(i)] = data["thirdname"]
  ws1['C'+str(i)] = data["id"]
  ws1['D'+str(i)] = data["displayedDate"]
  ws1['F'+str(i)] = data["currencysymbol"]
  HT = float(data["totalAmountTaxesFree"])
  ws1['G'+str(i)] = HT
  TTC = float(data["totalAmount"])
  ws1['H'+str(i)] = TTC
  TVA = float(data["taxesAmountSum"])
  ws1['I'+str(i)] = TVA
  ws1['S'+str(i)] = data["step_label"]
  ws1['T'+str(i)] = data["payDateText"]
  ws1['T'+str(i)] = data["payDateCustom"]
  ws1['V'+str(i)] = data["thirdRelationType"]
  '''
  ws1['W'+str(i)] = data["payment_method"]
  '''
  ws1['X'+str(i)] = data["formatted_payDateCustom"]
  ''''
  ws1['Y'+str(i)] = data["comment"]
  ws1['Z'+str(i)] = data["web_url"]
  '''
  i+=1
  n1+=1

#Bloc requete fournisseur
payload={'request': '1',
'io_mode': 'json',
'do_in': '{"method":"Purchase.getList","params":{"doctype":"invoice","pagination":{"nbperpage":"5000"}}}'}

headers = {
  'Authorization': 'OAuth oauth_consumer_key="",oauth_token="",oauth_signature_method="PLAINTEXT",oauth_timestamp={0},oauth_nonce="",oauth_version="1.0",oauth_signature=""'.format(a)
}
res = requests.request("POST", url, headers=headers, data=payload)
response=json.loads(res.text)

#début de la boucle for pour remplissage d'Excel
resp = response['response']['result']
for valeur in resp :
  print("Fournisseurs : n°",n2)
  v=valeur
  data=resp[v]
  ws2['B'+str(o)] = data["thirdname"]
  ws2['C'+str(o)] = data["id"]
  ws2['D'+str(o)] = data["displayedDate"]
  ws2['F'+str(o)] = data["currencysymbol"]
  HT = float(data["totalAmountTaxesFree"])
  ws2['G'+str(o)] = HT
  TTC = float(data["totalAmount"])
  ws2['H'+str(o)] = TTC
  TVA = float(data["taxesAmountSum"])
  ws2['I'+str(o)] = TVA
  ws2['S'+str(o)] = data["step_label"]
  ws2['T'+str(o)] = data["payDateText"]
  ws2['T'+str(o)] = data["payDateCustom"]
  ws2['V'+str(o)] = data["thirdRelationType"]
  '''
  ws2['W'+str(i)] = data["payment_method"]
  '''
  ws2['X'+str(o)] = data["formatted_payDateCustom"]
  '''
  ws2['Y'+str(i)] = data["comment"]
  ws2['Z'+str(i)] = data["web_url"]
  '''
  o+=1
  n2+=1

serveur = smtplib.SMTP('smtp.gmail.com', )    ## Connexion au serveur sortant (en précisant son nom et son port)
serveur.starttls()    ## Spécification de la sécurisation
serveur.login("", "")    ## Authentification
message = "Actualisation bien reussite ..."    ## Message à envoyer
serveur.sendmail("", "", message)    ## Envoie du message
serveur.quit()    ## Déconnexion du serveur

#sauvegarde de l'excel
wb.save(filename=path) 
