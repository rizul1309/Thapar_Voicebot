# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


cabins ={
    "dean":"B001",
    "doaa":"B001",
    "dosaa":"B002",
    "director":"A001"
}

class Actioncabin(Action):

    def name(self) -> Text:
        return "action_show_cabin_dir"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        designation = tracker.get_slot("designation")
        roomno = cabins.get(designation.lower())

        if roomno is None:
            output = "Could not find the direction of {}".format(designation)
        else:
            output = "The room number of {} is {}".format(designation,roomno)

        dispatcher.utter_message(text=output)

        return []

"""labs = {
"PG Activity Space 1":"L001",
"Gaming and Animation Lab":"L002",
"Language Technologies and machine learning Research lab ":"L003",
"Data Structures and Algorithms Lab 1 ":"L004",
"Data Structures and Algorithms Lab 2 ":"L005",
"Motion Capture Lab ":"L006",
"programming lab 1":"L007",
"Programming Lab 2":"L008",
"Machine Learning Lab":"L009",
"Programming Lab 3":"L010",
"Programming Lab 4":"L011",
"Café-1":"L013",
"Engineering Design Lab 1":"L101",
"Networks System Lab 1":"L102",
"Networks System Lab 2":"L103",
"Software Engineering Lab 1":"L104",
"Software Engineering Lab 2":"L105",
"General Computing  Lab 1":"L106",
"General Computing  Lab 2":"L107",
"Lab Staff CSED":"L108",
"Meeting Room CITM ":"L109",
"IT Support team":"L110",
"Data Centre":"L115",
"System Software Lab 1":"L201",
"System Software Lab 2":"L202",
"Program Manager":"L203",
"Office Csed":"L204",
"Database management system lab 1":"L206",
"Database management system lab 2":"L207",
"Programming lab 5":"L208",
"Engineering Design lab 2":"L209",
"Associate Head,CSED ":"L211",
"Head,CSED":"L212",
"Cyber and Information Security Research Lab":"L301",
"Cloud and IoT Research Lab":"L302",
"Smart Cities Research lab":"L306",
"Artificial Intelligence Lab":"L307",
"Data Science Lab":"L308",
"High Performance Computing Lab":"L312",
"PG Research Lab":"L313",
"Board Room,CSED":"L314",
"Big Data Research Lab":"L315",
"Embedded Systems Lab 1":"L401",
"Embedded Systems Lab 2":"L402",
"Computer Vision Research lab ":"L403",
"Doctoral Research Lab 1":"L404",
"Doctoral Research Lab 2":"L405",
"Doctoral Research Lab 3":"L406",
"Doctoral Research Lab 4":"L407",
"Information Security Lab 1":"L408",
"Information Security Lab 2":"L409",
"PG Activity Space 2":"L410",
"Computer Graphics Lab 2":"L429",
"Computer Graphics Lab 1":"L430",
"Software Design Lab":"L501",
"Computational Intelligence Research Lab":"L531"
}"""
labs ={
    "PG Activity Space":"L001",
"computer graphics lab":"L429",
"programming lab 1":"L007"
}
class Actionlab(Action):

    def name(self) -> Text:
        return "action_show_lab"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        lab = tracker.get_slot("lab")
        labno = labs.get(lab.lower())

        if labno is None:
            output = "Could not find the direction of {}".format(lab)
        else:
            output = "The room no of {} is {}".format(lab,labno)

        dispatcher.utter_message(text=output)

        return []
