"""Kalenteriin merkittyjen aikuistumisten näyttämisen ja poistamisen hoitava luokka"""

def open_eventfile():
    list1 = []
    try:
        with open("events.csv") as datafile:
            for event in datafile:
                list1.append(event)
            print("read")
    except FileNotFoundError:
        with open("events.csv", "w") as datafile:
            pass
    return list1

def write_eventfile(date, event):
    previous_events = open_eventfile()
    print("prev events", previous_events)
    length = len(previous_events)
    print("Lenght", length)
    calc = 0
    with open("events.csv", "w") as datafile:
        print("Opened")
        if length == calc:
            datafile.write(f"{date};{event}")
            return
        if length >= 1:
            for row in previous_events:
                print("rivi", row)
                if int(row[0]) > date:
                    datafile.write(f"{date};{event}")
                    datafile.write(f"{part[0]};{part[1]}")
                    calc += 2
                elif calc == length:
                    datafile.write(f"{date};{event}")
                    calc += 1
                else:
                    datafile.write(f"{part[0]};{part[1]}")
                    calc += 1

def delete_eventfile():
    open("events.csv", "w").close()
    

#class EventCalendar:
#    """Luokka tapahtumien hallintaan"""
#    def __init__(self):

#delete_eventfile()
write_eventfile(20221205, "Mandy (Brachypelma albiceps)")
write_eventfile(20210131, "Armi")
#write_eventfile(20230101, "Kaaleppi")
opened = open_eventfile()
print(opened)