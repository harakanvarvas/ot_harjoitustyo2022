"""Kalenteriin merkittyjen aikuistumisten näyttämisen ja poistamisen hoitava luokka"""

def open_eventfile():
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
    previous_events = open_eventfile()
    length = len(previous_events)
    calc = 0
    previous = None#########################################################################################################################################################
    with open("events.csv", "w") as datafile:
        if length == 0:
            datafile.write(f"{date};{event}\n")
            return
        if length >= 1:
            for row in previous_events:
                row = row.replace("\n", " ")
                part = row.split(";")
                print(f"rivi {row}, part[0] {part[0]}, calc {calc}, length {length}")
                if int(part[0]) == date:#jos päivämäärä on sama
                    if part[1] < event:#listan on aakkosjärjestyksessä pienempi
                        datafile.write(f"{part[0]};{part[1]}\n")
                        datafile.write(f"{date};{event}\n")
                        previous = (date, event)
                    elif part[1] == event:
                        pass
                    else:
                        datafile.write(f"{date};{event}\n")
                        datafile.write(f"{part[0]};{part[1]}\n")
                        previous = (part[0], part[1])
                    calc += 2
                elif int(part[0]) < date:#jos listan on pienempi kuin päivämäärä 
                    datafile.write(f"{part[0]};{part[1]}\n")
                    previous = (part[0], part[1])
                    calc += 1
                elif int(part[0]) > date:
                    datafile.write(f"{date};{event}\n")
                    calc += 1
#                else:
#                    datafile.write(f"{part[0]};{part[1]}\n")
#                    calc += 1

        if calc <= length:
            datafile.write(f"{date};{event}\n")
            calc += 1
 

def delete_eventfile():
    open("events.csv", "w").close()
    

#class EventCalendar:
#    """Luokka tapahtumien hallintaan"""
#    def __init__(self):

delete_eventfile()
write_eventfile(20221205, "Mandy (Brachypelma albiceps)")
write_eventfile(20221205, "Andy (Brachypelma albiceps)")
write_eventfile(20210131, "Armi")
write_eventfile(20230101, "Kaaleppi")
opened = open_eventfile()
print(opened)