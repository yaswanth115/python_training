class Device:
    def power_on(self):
        print("Device is powered on")


class Camera(Device):
    def take_photo(self):
        print("Taking a photo")


class Phone(Device):
    def make_call(self):
        print("Making a call")


class SmartDevice(Camera, Phone):
    def connect_wifi(self):
        print("Connected to Wi-Fi")


device = SmartDevice()

device.power_on()
device.take_photo()
device.make_call()
device.connect_wifi()

print([cls.__name__ for cls in SmartDevice.mro()])