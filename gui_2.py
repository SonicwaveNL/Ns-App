from tkinter import *
from tkinter import ttk
import requests
import xmltodict
import c_station
import stationlist



labels = []
station_label = None



def on_select_station(event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    welkom_bij_NS.destroy()

    station_label["text"] = value

    for a_label in labels:
        a_label.destroy()
    c_station.get_trains_of_stations(innerframe, labels, value)


def NS():
    print("Welkom bij NS")

class Startpage(ttk.Frame):
    def click():
        ttk.Frame.click(self,parent)
        label=tk.Label(self, text="Terug", font=LARGE_FONT)
        label.pack(pady-10, padx=10)

        button = tk.Button(self, text="Terug1", command=NS)
        button.pack()




auth_details = ('j.vanbuuren7@gmail.com', 'ieJAkpfjnTqlQK4_J3So53ddvTk4_zElya4Psi5mnudqqwYAoWHLSg')
api_url = 'https://webservices.ns.nl/ns-api-avt?station='
response = requests.get(api_url, auth=auth_details)
vertrekXML = xmltodict.parse(response.text)

#GUI Tkinter voor NS stations
window = Tk()
frame = None
innerframe = None
welkom_bij_NS = None
station_label = None
photo = None
photo_label = None
button1 = None
p = None
f1 = None

frame = Frame(master=window, background='gold', width=60, height=60)
frame.pack(side=LEFT, fill=BOTH)

innerframe = Frame(master=frame, background='gold')
innerframe.pack(fill=BOTH, expand=True)

welkom_bij_NS = Label(innerframe, text='Welkom bij NS', background='gold',
                      fg='darkblue', width=30, height=1, font=("Arial", 50, "bold italic"))
welkom_bij_NS.pack(pady=(300, 0))

station_label = Label(innerframe, background='gold',
                      fg='darkblue', width=30, height=0, font=("Arial", 50, "bold italic"))
station_label.pack(side=TOP)

photo = PhotoImage(file='NS logo.png')
photo_label = Label(innerframe, image=photo, background='gold', height=200)
photo_label.pack()

button1 = Button(frame, text='Terug', background='darkblue', fg='gold',
                 width=15, height=2, font=('Arial', 15, 'bold'))
button1.pack(side=RIGHT)

p = ttk.PanedWindow(window, orient=HORIZONTAL)
f1 = ttk.LabelFrame(p, text='Station', width=26, height=47, )
p.add(f1)
p.pack()

stationlist.make(on_select_station, f1)

window.mainloop()



# I TRIED SO HARD YET I FAILED #feelsbadman


#def make_gui():
#    frame = Frame(master=window, background='gold', width=60, height=60)
#    frame.pack(side=LEFT, fill=BOTH)

#    innerframe = Frame(master=frame, background='gold')
#    innerframe.pack(fill=BOTH, expand=True)

#    welkom_bij_NS = Label(innerframe, text='Welkom bij NS', background='gold',
#                          fg='darkblue', width=30, height=1, font=("Arial", 50, "bold italic"))
#    welkom_bij_NS.pack(pady=(300, 0))

#    station_label = Label(innerframe, background='gold',
#                          fg='darkblue', width=30, height=0, font=("Arial", 50, "bold italic"))
#    station_label.pack(side=TOP)

#    photo = PhotoImage(file='NS logo.png')
#    photo_label = Label(innerframe, image=photo, background='gold', height=200)
#    photo_label.pack()

#    button1 = Button(frame, text='Terug', background='darkblue', fg='gold',
#                     width=15, height=2, font=('Arial', 15, 'bold'))
#    button1.pack(side=RIGHT)

#    p = ttk.PanedWindow(window, orient=HORIZONTAL)
#    f1 = ttk.LabelFrame(p, text='Station', width=26, height=47, )
#    p.add(f1)
#    p.pack()

 #   stationlist.make(on_select_station, f1)

#make_gui()