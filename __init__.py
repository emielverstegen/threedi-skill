from mycroft import MycroftSkill, intent_file_handler


class Threedi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('threedi.intent')
    def handle_threedi(self, message):
        self.speak_dialog('threedi')


def create_skill():
    return Threedi()

