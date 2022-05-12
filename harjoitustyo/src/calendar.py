"""Kalenteriin merkittyjen aikuistumisten näyttämisen ja poistamisen hoitava luokka"""

def open_eventfile_return_for_listbox():
    """Avaa tapahtumatiedoston ja palauttaa joko 'Ei tapahtumia' tai tapahtumat tekstinä"""
    content = "Ei tapahtumia"
    try:
        with open("events.csv") as datafile:
            content = datafile.read()
    except FileNotFoundError:#mikäli tiedostoa ei ole vielä luotu, luodaan se
        with open("events.csv", "w") as datafile:
            pass
    if content != "Ei tapahtumia":
        content = []
        year = None
        month = None
        day = None
        list_content = open_eventfile_return_list()
        for event in list_content:
            year = f"{event[0][0]}{event[0][1]}{event[0][2]}{event[0][3]}"
            month = f"{event[0][4]}{event[0][5]}"
            day = f"{event[0][6]}{event[0][7]}"
            content.append(f"{day}.{month}.{year}    {event[1]}")
        content.reverse()
    return content#palauttaa joko sisällön tai tiedon siitä, että tapahtumia ei ole vielä tallennettu

def open_eventfile_return_list():
    """Avaa tapahtumatiedoston ja palauttaa listan"""
    list1 = []
    try:
        with open("events.csv") as datafile:
            for event in datafile:
                event = event.replace("\n", "")
                event = event.split(";")
                try:
                    event_tuple = (event[0], event[1])
                except IndexError:
                    pass
                list1.append(event_tuple)
    except FileNotFoundError:#mikäli tiedostoa ei ole vielä luotu, luodaan se
        with open("events.csv", "w") as datafile:
            pass
    return list1#palauttaa listan


def write_eventfile(date, event):
    """Lisää funktion argumentteina olevan päivämäärän ja tapahtuman listaan, järjestää listan ja kirjoittaa tapahtumat tiedostoon"""
    date_event_tuple = (str(date), event)
    events = open_eventfile_return_list()#hakee tiedoston listamuodossa

    if date_event_tuple not in events:#tarkistaa, että lisättävä tapahtuma ei ole listassa jo
        events.append(date_event_tuple)
    else:
        return False

    events.sort()#järjestää listan

    with open("events.csv", "w") as datafile:#avataan tiedosto kirjoitettavaksi
        for event in events:
            datafile.write(f"{event[0]};{event[1]}\n")

    return True#palauttaa arvon True onnistumisen merkiksi

def find_event_by_name(name):
    """Hakee tiedostosta tapahtuman nimellä ja palauttaa sen"""
    content = ""
    events = open_eventfile_return_list()
    for event in events:
        #print(event)
        if name in event[1]:
            year = f"{event[0][0]}{event[0][1]}{event[0][2]}{event[0][3]}"
            month = f"{event[0][4]}{event[0][5]}"
            day = f"{event[0][6]}{event[0][7]}"
            content += f"{day}.{month}.{year}    {event[1]}\n"
    if content == "":
        return f"Hakusanalla {name} ei löydy tapahtumia"
    return content
    

def delete_event_by_name(name):
    """Hakee tiedostosta tapahtuman nimellä ja poistaa sen"""
    events = open_eventfile_return_list()
    index = [events.index(x) for x in events if x[1] == name]
    index = str(index)
    index = index.strip("[]")
    index = int(index)
    events.pop(index)

    with open("events.csv", "w") as datafile:#avataan tiedosto kirjoitettavaksi
        for event in events:
            datafile.write(f"{event[0]};{event[1]}\n")

    return True

def delete_eventfile():
    """Tyhjentää tapahtumatiedoston täydellisesti"""
    open("events.csv", "w").close()
    return True
    

class EventCalendar:
    """Luokka tapahtumien hallintaan"""
    def __init__(self):
        self._events = None
        self._newdate = None
        self._newevent = None

    def show_events(self):
        """Palauttaa tämänhetkiset tapahtumat"""
        self._events = open_eventfile_return_for_listbox()
        return self._events

    def form_event(self, event):
        """"Muotoilee tapahtuman nimiosuuden ja palauttaa sen"""
        self._newevent = str(event)
        self._newevent = self._newevent.split(";")
        return self._newevent[1]

    def form_date(self, event):
        """Muotoile tapahtuman päivämääräosuuden ja palauttaa sen"""
        self._newevent = str(event)
        self._newevent = self._newevent.split(";")
        self._newdate = self._newevent[0].split("/")
        self._newdate = f"{self._newdate[2]}{self._newdate[1]}{self._newdate[0]}"
        return self._newdate

    def new_event(self, event):
        """Lisää kalenteriin uuden tapahtuman"""
        self._newdate =  EventCalendar.form_date(self, event)
        self._newevent = EventCalendar.form_event(self, event)
        val = write_eventfile(self._newdate, self._newevent)
        return val

    def search_for_event(self, name):
        """Hakee tapahtumaa annetulla hakusanalla"""
        self._events = find_event_by_name(name)
        return self._events

    def delete_event(self, event):
        delete_event_by_name(event)
        self._events = open_eventfile_return_text()
        return self._events

    def remove_all_events(self):
        delete_eventfile()
        self._events = None
        return self._events

if __name__ == "__main__":
#
    delete_eventfile()
    evcal = EventCalendar()
#    value = evcal.new_event("11/11/2011;Marilyn (Idolomantis diabolica)")
#    print(value)
#    events = evcal.show_events()
#    print(events)
    write_eventfile(20221205, "Mandy (Brachypelma albiceps)")
    write_eventfile(20221205, "Mandy (Brachypelma albiceps)")
    write_eventfile(20221205, "Andy (Brachypelma albiceps)")
    write_eventfile(20210131, "Armi")
    write_eventfile(20230101, "Kaaleppi")
    write_eventfile(20220315, "Mango")
    events = evcal.show_events()
    print(events)
#inde = delete_event_by_name("Armi")
#print(inde)
#cont = open_eventfile_return_list()
#print(cont)
    #cont = find_event_by_name("Brache")
    #print(cont)
