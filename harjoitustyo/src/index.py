"""Main-tideosto"""
from graphic_ui import GraphicUI

def main():
    """Main"""
    try:
        program = GraphicUI()
    except TypeError:
        pass
#        print("TypeError for __init__ requiring 'root'")
    try:
        program.start()
    except UnboundLocalError:
        pass
#        print("UnboundLocalError for refering local variable 'program' before assignment")

if __name__ == "__main__":
    main()
