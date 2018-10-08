from tkinter import *
import requests
import xmltodict
import codecs

def get_trains_of_stations(frame, labelist, station) :
    auth_details = ('alanblokker2000@gmail.com', 'tNxX_VUBVU6zopAzo3RZ3n0pEDOp-fGTdDEFPC321Lw-4kMVMez2Jw')
    api_url = 'https://webservices.ns.nl/ns-api-avt?station=' + station
    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)

    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']
        soorttrein = vertrek['TreinSoort']
        vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]  # 18:36
        if 'RouteTekst' in vertrek:
            routetekst = vertrek['RouteTekst']
            routeLabel = Label(frame, background='gold', fg='darkblue', font = ('Arial', 14, 'bold'), text = 'Om ' + vertrektijd + ' vertrekt de ' + soorttrein +
                  ' naar ' + eindbestemming + ' die langs de station(s) ' + routetekst + ' gaat')
            routeLabel.pack(side=TOP)
            labelist.append(routeLabel)
        else:
            routeLabel = Label(frame,background='gold', fg='darkblue', font = ('Arial', 14, 'bold'), text='Om ' + vertrektijd + ' vertrekt de ' + soorttrein + ' naar ' + eindbestemming)
            routeLabel.pack(side=TOP)
            labelist.append(routeLabel)


def get_xml():
    file = codecs.open('stations.xml', 'r', 'UTF-8')
    data = xmltodict.parse(file.read())
    file.close()
    return data