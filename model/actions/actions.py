# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import requests

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction


class ActionResetAllSlots(Action):

    def name(self) -> Text:
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
      return [AllSlotsReset()]

class ActionFillSlots(Action):

    def name(self) -> Text:
        return "action_fill_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print(domain)
        myTranslatedContent = "ID123"
        return [SlotSet("translated_content", myTranslatedContent)]

class GetAndShowFoodDetails(Action):

    def name(self) -> Text:
        return "get_and_show_food_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_get_and_show_food_details")
        dispatcher.utter_message(text="雞胸肉今日賣2.50一磅")
        return [FollowupAction(name = "utter_ask_add_to_cart")]

class AddItemToOrder(Action):

    def name(self) -> Text:
        return "action_submit_add_to_order_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_submit_add_to_order_form")
        dispatcher.utter_message(text="已經為你加入到購物車了，你可以繼續添加其他物料")
        return []

class PrepareEmail(Action):

    def name(self) -> Text:
        return "action_prepare_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("action_prepare_email")
        dispatcher.utter_message(text="请review翻译的内容")
        return [SlotSet("translated_content", "This is the translated content"), FollowupAction(name = "utter_confirm_send_email")]