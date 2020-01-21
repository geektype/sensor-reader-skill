from mycroft import MycroftSkill, intent_file_handler


class SensorReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.sensor.intent')
    def handle_reader_sensor(self, message):
        self.speak_dialog('reader.sensor')


def create_skill():
    return SensorReader()

