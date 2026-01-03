class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def display_details(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print()
dog1 = dog("Buddy", "Golden Retriever")
dog2 = dog("Max", "German Shepherd")
dog1.display_details()
dog2.display_details()