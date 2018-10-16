import requests
import xmltodict
from flask import Flask, render_template, Markup

labels = []
station_label = None
app = Flask(__name__)

auth_details = ('j.vanbuuren7@gmail.com', 'ieJAkpfjnTqlQK4_J3So53ddvTk4_zElya4Psi5mnudqqwYAoWHLSg')

@app.route("/")
def home():

    stationsListCode = sidebar()

    return render_template('home.html', stationsList=stationsListCode)

def sidebar():
    api_url = 'https://webservices.ns.nl/ns-api-stations-v2'
    stations = requests.get(api_url, auth=auth_details)

    stationsXML = xmltodict.parse(stations.text)

    stationsList = "<ul>"

    for station in stationsXML['Stations']['Station']:
        stationName = station["Namen"]["Lang"].replace("a/d", "aan den")


        if station['Land'] == "NL":
            stationsList += '<a class="station" href="/tijden/%s"><li>%s</li></a>' % (stationName, stationName)

    stationsList += "</ul>"

    stationsListCode = Markup(stationsList)

    return stationsListCode

@app.route("/tijden/<string:thisstation>")
def departures(thisstation):

    # this_station_code sets the code from the station where the application is running.
    # This has to be set by hand to show the first time. Later can be chosen by the user to show there wanted station.
    this_station_code = thisstation

    api_url_departure = 'http://webservices.ns.nl/ns-api-avt?station=' + this_station_code
    departure = requests.get(api_url_departure, auth=auth_details)

    departures = xmltodict.parse(departure.text)

    table = '<table><tr class="tableHeader"><th>Tijd</th><th>Naar</th><th>Vervoerder</th><th>Spoor</th></tr>'
    if 'ActueleVertrekTijden' in departures:
        for departure in departures['ActueleVertrekTijden']['VertrekkendeTrein']:
            destination = departure['EindBestemming']

            if 'RouteTekst' in departure:
                departureVia = departure['RouteTekst']

            departureTime = departure['VertrekTijd']
            departureTime = departureTime[11:16]
            departureTrack = departure['VertrekSpoor']

            if "#text" in departureTrack:
                departureTrack = departure['VertrekSpoor']["#text"]
            else:
                departureTrack = 1

            transporter = departure['Vervoerder']

            table += '<tr valign="top" class="trMain"><td> %s </td><td> %s ' % (departureTime, destination)

            if 'RouteTekst' in departure:
                table += '</br><span class="via">Via: %s</span>' % (departureVia)
            table += '</td><td> %s </td><td> %s </td></tr>' % (transporter, departureTrack)
    else:
        table += '<tr><td><b>Er zijn geen vertrektijden van dit station.</b></td></tr>'

    table += '</table>'
    tableCode = Markup(table)

    stationsListCode = sidebar()

    return render_template('vertrektijden.html',  name=thisstation, stationsList=stationsListCode, departure=tableCode)

app.run()