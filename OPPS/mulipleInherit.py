class Camera:
    def take_photo(self):
        print("Taking a photo")


class MusicPlayer:
    def play_music(self):
        print("Playing music")


class SmartPhone(Camera, MusicPlayer):
    def make_call(self):
        print("Making a phone call")


phone = SmartPhone()

phone.take_photo()
phone.play_music()
phone.make_call()