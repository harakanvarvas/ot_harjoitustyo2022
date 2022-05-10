"""Kalenteriin merkittyjen aikuistumisten näyttämisen ja poistamisen hoitava luokka"""

def open_eventfile_return_text():
    """Avaa tapahtumatiedoston ja palauttaa joko 'Ei tapahtumia' tai tapahtumat tekstinä"""
    content = "Ei tapahtumia"
    try:
        with open("events.csv") as datafile:
            content = datafile.read()
    except FileNotFoundError:
        with open("events.csv", "w") as datafile:
            pass
    return content

def open_eventfile_return_list():
    """Avaa tapahtumatiedoston ja palauttaa listan"""
    list1 = []
    try:
        with open("events.csv") as datafile:
            for event in datafile:
                list1.append(event)
    except FileNotFoundError:
        with open("events.csv", "w") as datafile:
            pass
    return list1

def write_eventfile(date, event):
    """Lisää funktion argumentteina olevan päivämäärän ja tapahtuman listaan, järjestää listan ja kirjoittaa tapahtumat tiedostoon"""
    date_event = f"{date};{event}"
    events = open_eventfile_return_list()
    events.append(date_event)
    events.sort()
    print(events)
    with open("events.csv", "w") as datafile:
        if len(events) <= 1:
            date_event = str(events)#tämän voisi varmasti tehdä yksinkertaisemminkin
            date_event = date_event.replace("\n", "")
            date_event = date_event.replace("[", "")
            date_event = date_event.replace("]", "")
            date_event = date_event.replace("'", "")
            date_event = date_event.split(";")
            datafile.write(f"{date_event[0]};{date_event[1]}\n")
        else:
            for event in events:
                date_event = str(event)
                date_event = date_event.replace("\n", "")
                date_event = date_event.split(";")
                datafile.write(f"{date_event[0]};{date_event[1]}\n")


 

def delete_eventfile():
    """Tyhjentää tapahtumatiedoston täydellisesti"""
    open("events.csv", "w").close()
    

#class EventCalendar:
#    """Luokka tapahtumien hallintaan"""
#    def __init__(self):

delete_eventfile()
write_eventfile(20221205, "Mandy (Brachypelma albiceps)")
write_eventfile(20221205, "Andy (Brachypelma albiceps)")
write_eventfile(20210131, "Armi")
write_eventfile(20230101, "Kaaleppi")
write_eventfile(20220315, "Mango")
cont = open_eventfile_return_text()
print(cont)