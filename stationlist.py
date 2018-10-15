from tkinter import *
import c_station

# Stationlist

def make(select_event, frame_label):
    scrollbar = Scrollbar(frame_label)
    scrollbar.pack(side=RIGHT, fill=Y)

    stationlist = Listbox(frame_label, yscrollcommand=scrollbar.set, background = 'gold',
                      fg= 'darkblue',width = 26, height=47, font = ('Arial', 12, 'bold'))
    xml = c_station.get_xml()
    for stations, keys in xml.items():
        for station, key in keys.items():
            for stat in key:
                stationlist.insert(END, stat['name'])
    stationlist.bind('<<ListboxSelect>>', select_event)
    stationlist.pack(side=LEFT, fill=Y, expand=1)
    scrollbar.config(command=stationlist.yview)