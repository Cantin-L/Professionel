#importation des différents modules
import requests
import datetime 
import json
import __version__.py
from openpyxl import load_workbook
import smtplib 

serveur = smtplib.SMTP('smtp.gmail.com', )    ## Connexion au serveur sortant (en précisant son nom et son port)
serveur.starttls()    ## Spécification de la sécurisation
serveur.login("", "")    ## Authentification
message = "Debut actualisation"    ## Message à envoyer
serveur.sendmail("", "", message)    ## Envoie du message
serveur.quit()    ## Déconnexion du serveur

#déclaration du contenu du document, et du token  
headers = {'Content-Type': 'application/json',
           'Authorization': "Token ..."}

#ouverture du fichier excel et des feuilles
path=''
wb = load_workbook(path)
ws1 = wb['Factures Clients']
ws2 = wb['Factures Fournisseurs']

#incrémentation de nos variables
page1 = page2 = 1
o = i = 2
n1=n2=0

'''------------------------------------------------------------------------------------------------------------------'''

#boucle pour les données clients
url ="https://app.azopio.com/public_api/v1/documents/?date_start=2020-01-01&page=1&state_checked=checked&type=client"
f = requests.get(url,headers=headers)
data = f.content
data_dict =json.loads(data)

for element in data_dict :
    nombre_doc = data_dict["count"]
    print (nombre_doc)
    while n1!= nombre_doc :
        url="https://app.azopio.com/public_api/v1/documents/?date_start=2020-01-01&page={0}&state_checked=checked&type=client".format(page1)
        f = requests.get(url,headers=headers)
        data = f.content
        data_dict =json.loads(data)
        page1+=1
        print(url)
        for element in data_dict["results"]:
            uuid=element["uuid"]
            print("Clients :",n1)       
            url1 = "https://app.azopio.com/public_api/v1/document/{0}".format(uuid)
            f1 = requests.get(url1,headers=headers)
            data1 = f1.content
            data_dict1 =json.loads(data1)
            ws1['B'+str(o)] = data_dict1["issuer"]
            ws1['C'+str(o)] = data_dict1["reference"]
            ws1['D'+str(o)] = data_dict1["date"]
            ws1['F'+str(o)] = data_dict1["currency"]
            htt = data_dict1["untaxed_amount"].replace(",",".")
            HT = float(htt)
            ws1['G'+str(o)] = HT
            ttct = data_dict1["total_amount"].replace(",",".")
            TTC = float(ttct)
            ws1['H'+str(o)] = TTC
            tvat = data_dict1["vat_amount"].replace(",",".")
            TVA = float(tvat)
            ws1['I'+str(o)] = TVA
            ws1['S'+str(o)] = data_dict1["state_paid"]
            #ws2['T'+str(o)] = #data_dict3["inserted"]
            ws1['V'+str(o)] = data_dict1["expense_category"]
            ws1['W'+str(o)] = data_dict1["payment_method"]
            ws1['X'+str(o)] = data_dict1["due_date"]
            ws1['Y'+str(o)] = data_dict1["comment"]
            ws1['Z'+str(o)] = data_dict1["web_url"]
            o+=1
            n1+=1

'''--------------------------------------------------------------------------------------------------------------------'''

#boucle pour les données fournisseurs
url2 ="https://app.azopio.com/public_api/v1/documents/?date_start=2020-01-01&page=1&state_checked=checked&type=supplier"
f2 = requests.get(url2,headers=headers)
data2 = f2.content
data_dict2 =json.loads(data2)

for element in data_dict2 :
    nombre_doc = data_dict2["count"]
    print (nombre_doc)
    while n2!= nombre_doc :
        url2="https://app.azopio.com/public_api/v1/documents/?date_start=2020-01-01&page={0}&state_checked=checked&type=supplier".format(page2)
        f2 = requests.get(url2,headers=headers)
        data2 = f2.content
        data_dict2 =json.loads(data2)
        page2+=1
        print(url2)
        for element1 in data_dict2["results"]:
            uuid=element1["uuid"]
            print("Fournisseurs :",n2)  
            url3 = "https://app.azopio.com/public_api/v1/document/{0}".format(uuid)
            f3 = requests.get(url3,headers=headers)
            data3 = f3.content
            data_dict3 =json.loads(data3)
            if data_dict3["expense_category"]=='wages' :
                n2+=1
            else :
                ws2['B'+str(i)] = data_dict3["issuer"]
                ws2['C'+str(i)] = data_dict3["reference"]
                ws2['D'+str(i)] = data_dict3["date"]
                ws2['F'+str(i)] = data_dict3["currency"]
                htt = data_dict3["untaxed_amount"].replace(",",".")
                HT = float(htt)
                ws2['G'+str(i)] = HT
                ttct = data_dict3["total_amount"].replace(",",".")
                TTC = float(ttct)
                ws2['H'+str(i)] = TTC
                tvat = data_dict3["vat_amount"].replace(",",".")
                TVA = float(tvat)
                ws2['I'+str(i)] = TVA
                ws2['S'+str(i)] = data_dict3["state_paid"]
                #ws2['T'+str(i)] = #data_dict3["inserted"]
                ws2['V'+str(i)] = data_dict3["expense_category"]
                ws2['W'+str(i)] = data_dict3["payment_method"]
                ws2['X'+str(i)] = data_dict3["due_date"]
                ws2['Y'+str(i)] = data_dict3["comment"]
                ws2['Z'+str(i)] = data_dict3["web_url"]
                i+=1 
                n2+=1

'''---------------------------------------------------------------------------------------------------------------'''

serveur = smtplib.SMTP('smtp.gmail.com', )    ## Connexion au serveur sortant (en précisant son nom et son port)
serveur.starttls()    ## Spécification de la sécurisation
serveur.login("", "")    ## Authentification
message = "Actualisation bien reussite ..."    ## Message à envoyer
serveur.sendmail("", "", message)    ## Envoie du message
serveur.quit()    ## Déconnexion du serveur

#sauvegarde de l'excel
wb.save(filename=path) 
