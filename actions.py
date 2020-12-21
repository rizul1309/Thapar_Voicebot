# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import webbrowser 
import time 


faculty = {
    "biotechnology":"http://btd.thapar.edu/faculty",
    "computer":"http://csed.thapar.edu/faculty",
    "civil":"http://ced.thapar.edu/faculty",
    "chemical":"http://ched.thapar.edu/faculty",
    "electrical and instrumentation":"http://eied.thapar.edu/faculty",
    "electronic":"http://eced.thapar.edu/faculty",
    "mechanical":"http://med.thapar.edu/faculty",
    "mathematics":"http://som.thapar.edu/faculty",
    "humanities":"http://smss.thapar.edu/faculty",
    "energy and environment":"http://see.thapar.edu/faculty",
    "physics and materials science":"http://spms.thapar.edu/faculty"
}

cabins ={
    "dean":"B block",
    "doaa":"B001",
    "dosa":"B002",
    "director":"A001"
}

labs = {
    "pG activity space 1":"L001",
    "gaming and animation lab":"L002",
    "language technologies and machine learning research lab ":"L003",
    "data structures and algorithms lab 1 ":"L004",
    "data structures and algorithms lab 2 ":"L005",
    "motion capture lab ":"L006",
    "programming lab 1":"L007",
    "programming lab 2":"L008",
    "machine learning lab":"L009",
    "programming lab 3":"L010",
    "programming lab 4":"L011",
    "cafe-1":"L013",
    "engineering design lab 1":"L101",
    "networks system lab 1":"L102",
    "networks system lab 2":"L103",
    "software engineering lab 1":"L104",
    "software engineering lab 2":"L105",
    "general computing  lab 1":"L106",
    "general computing  lab 2":"L107",
    "lab staff csed":"L108",
    "meeting room citm ":"L109",
    "it support team":"L110",
    "data centre":"L115",
    "system software lab 1":"L201",
    "system software lab 2":"L202",
    "program manager":"L203",
    "office csed":"L204",
    "database management system lab 1":"L206",
    "database management system lab 2":"L207",
    "programming lab 5":"L208",
    "engineering design lab 2":"L209",
    "associate head csed ":"L211",
    "head csed":"L212",
    "cyber and information security research lab":"L301",
    "cloud and ioT research lab":"L302",
    "smart cities research lab":"L306",
    "artificial intelligence lab":"L307",
    "data science lab":"L308",
    "high performance computing lab":"L312",
    "pg research lab":"L313",
    "board room csed":"L314",
    "big data research lab":"L315",
    "embedded systems lab 1":"L401",
    "embedded systems lab 2":"L402",
    "computer vision research lab ":"L403",
    "doctoral research lab 1":"L404",
    "doctoral research lab 2":"L405",
    "doctoral research lab 3":"L406",
    "doctoral research lab 4":"L407",
    "information security lab 1":"L408",
    "information security lab 2":"L409",
    "pg activity space 2":"L410",
    "computer graphics lab 2":"L429",
    "computer graphics lab 1":"L430",
    "software design lab":"L501",
    "computational intelligence research lab":"L531"
 }
blocks ={
    "directorate office":"Just in Front of the main lawns of thapar",
    "h block":"Adjacent to the Day Scholar Parking ",
    "b block":"Adjacent to K lawns and main Cafeteria",
    "e block":"Near the Aahaar Cafeteria",
    "f block":"Opposite to the mechanical workshop",
    "g block":"Adjacent to sbop lawns",
    "e block":"Near the Aahaar Cafeteria",
    "f block":"Opposite to the mechanical workshop",
    "csed building":"Near the New nava nalanda Central Library ",
    "tan building":"opposite to iconic girls hostel",
    "cos":"Adjacent to football ground and thapar university synthetic running track"
}
url = 'http://www.mattcole.us/'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
class Actioncabin(Action):

    def name(self) -> Text:
        return "action_show_cabin_dir"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        designation = tracker.get_slot("designation")
        roomno = cabins.get(designation.lower())
        """webbrowser.get(chrome_path).open(url) 
        time.sleep(2)"""
        if roomno is None:
            output = "Your on your own mate as I Could not find the direction of {}".format(designation)
        else:
            output = "The room number of {} is {}".format(designation,roomno)

        dispatcher.utter_message(text=output)

        return []

class Actionlab(Action):

    def name(self) -> Text:
        return "action_show_lab"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        lab = tracker.get_slot("lab")
        labno = labs.get(lab.lower())

        if labno is None:
            output = "Your on your own mate as I Could not find the direction of {}".format(lab)
        else:
            output = "The room no of {} is {}".format(lab,labno)

        dispatcher.utter_message(text=output)

        return []

class ActionBlock(Action):

    def name(self) -> Text:
        return "action_show_block"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        block = tracker.get_slot("block")
        blocklocation = blocks.get(block.lower())

        if blocklocation is None:
            output = "Your on your own mate as I could not find the direction of {}".format(block)
        else:
            output = "{} is {}".format(block,blocklocation)

        dispatcher.utter_message(text=output)

        return []

class Actionfaculty(Action):

    def name(self) -> Text:
        return "action_show_faculty"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        department_name = tracker.get_slot("department_name")
        info = faculty.get(department_name.lower())

        if info is None:
            output = "Could not find info of {} department".format(department_name)
        else:
            output = "This is {} department".format(department_name)
            webbrowser.get(chrome_path).open(info) 
            time.sleep(2)

        dispatcher.utter_message(text=output)

        return []
    
class Actionfaculty(Action):

    def name(self) -> Text:
        return "action_wifi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        wifi = tracker.get_slot("wifi")
        output= "Here is your {} wifi password".format(wifi)
        url='https://myherupa.com/pages/wifi.html'
        webbrowser.get(chrome_path).open(url) 
        time.sleep(2)
        dispatcher.utter_message(text=output)

        return []
class Actionfaculty(Action):

    def name(self) -> Text:
        return "action_timetable"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= "Enter your details here and see your timetable".format(wifi)
        url='https://myherupa.com/pages/time-table.html#more-stuff'
        webbrowser.get(chrome_path).open(url) 
        time.sleep(2)
        dispatcher.utter_message(text=output)

        return []
class Actionfaculty(Action):

    def name(self) -> Text:
        return "action_society"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= "Some brief informtion about thapar societies is here"
        url='https://myherupa.com/pages/societies.html'
        webbrowser.get(chrome_path).open(url) 
        time.sleep(2)
        dispatcher.utter_message(text=output)

        return []
class Actionfaculty(Action):

    def name(self) -> Text:
        return "action_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        output= "These are few famous restaurants nearby Thapar"
        url='https://myherupa.com/pages/food.html'
        webbrowser.get(chrome_path).open(url) 
        time.sleep(2)
        dispatcher.utter_message(text=output)

        return []