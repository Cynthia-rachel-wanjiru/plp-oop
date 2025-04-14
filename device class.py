class Device:  # Base class
    """
    Represents a generic device.
    """
    def __init__(self, brand, model):
        """
        Initializes a Device object.

        Args:
            brand (str): The brand of the device.
            model (str): The model of the device.
        """
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

    def turn_on(self):
        print(f"Turning on {self}...")

    def turn_off(self):
        print(f"Turning off {self}...")


class Smartphone(Device):  # Inherits from Device
    """
    Represents a smartphone.
    """
    def __init__(self, brand, model, os, storage_gb, camera_mp):
        """
        Initializes a Smartphone object.

        Args:
            brand (str): The brand of the smartphone.
            model (str): The model of the smartphone.
            os (str): The operating system of the smartphone.
            storage_gb (int): The storage capacity in GB.
            camera_mp (float): The camera resolution in megapixels.
        """
        # Call the constructor of the base class (Device)
        super().__init__(brand, model)  # Encapsulation: calling base class constructor
        self.os = os
        self.storage_gb = storage_gb
        self.camera_mp = camera_mp
        self._is_on = False  # Encapsulation:  private attribute

    def __str__(self):
        return f"{super().__str__()} ({self.os}, {self.storage_gb}GB, {self.camera_mp}MP)"

    def turn_on(self):
        super().turn_on() # Polymorphism: Overriding base class method
        self._is_on = True
        print("Smartphone is ready.")

    def turn_off(self):
        super().turn_off() # Polymorphism
        self._is_on = False
        print("Smartphone is off.")

    def take_photo(self):
        if self._is_on:
            print(f"Taking a photo with the {self.camera_mp}MP camera.")
        else:
            print("Cannot take photo. Smartphone is off.")

    def install_app(self, app_name):
        if self._is_on:
            print(f"Installing {app_name}...")
            print(f"{app_name} installed successfully.")
        else:
            print("Cannot install app. Smartphone is off.")

    def get_storage_info(self):
        return f"Total Storage: {self.storage_gb}GB"
    
    #Getter method for is_on
    def is_on(self):
        return self._is_on

# Example Usage
if __name__ == "__main__":
    my_phone = Smartphone("Google", "Pixel 8", "Android 14", 128, 50.0)
    print(my_phone)  # Uses the __str__ method
    my_phone.turn_on()
    my_phone.take_photo()
    my_phone.install_app("WhatsApp")
    print(my_phone.get_storage_info())
    my_phone.turn_off()

    print("\nCreating another smartphone:")
    another_phone = Smartphone("Samsung", "Galaxy S24", "Android 14", 256, 108.0)
    print(another_phone)
    another_phone.turn_on()
    another_phone.take_photo()
    another_phone.turn_off()
