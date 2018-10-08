import requests
import xmltodict
import codecs

# Authentication details
auth_details = ('alanblokker2000@gmail.com', 'tNxX_VUBVU6zopAzo3RZ3n0pEDOp-fGTdDEFPC321Lw-4kMVMez2Jw')

is_new_database = input('Wilt u de stations database ververessen (Y/N)')

if is_new_database == 'Y':
    api_url = 'https://webservices.ns.nl/ns-api-stations'
    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)

    filename = 'stations.xml'
    file = codecs.open(filename, 'w', 'UTF-8')
    file.write(response.text)
    file.close()


def vertrektijden(station):
    api_url = 'https://webservices.ns.nl/ns-api-avt?station=' + station
    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)

    return vertrekXML