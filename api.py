import requests
import xmltodict

auth_details = ('j.vanbuuren7@gmail.com', 'ieJAkpfjnTqlQK4_J3So53ddvTk4_zElya4Psi5mnudqqwYAoWHLSg')
eindstation = input('Wat is uw station? ')
api_url = 'https://webservices.ns.nl/ns-api-avt?station=' + eindstation
response = requests.get(api_url, auth=auth_details)
vertrekXML = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen:')

for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']
    vertrekspoor = vertrek['VertrekSpoor']
    soorttrein = vertrek['TreinSoort']
    vertrektijd = vertrek['VertrekTijd'] # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16] # 18:36
    if 'RouteTekst' in vertrek:
        routetekst = vertrek['RouteTekst']
        print('Om '+vertrektijd+' vertrekt de ' + soorttrein +
              ' naar '+ eindbestemming + ' die langs de station(s) '+ routetekst+ ' gaat')
    else:
        print('Om '+vertrektijd+' vertrekt de ' + soorttrein+ ' naar ' + eindbestemming)