class Bird:
    def __init__(self, species, location):
        self.species = species
        self.location = location

    def migrate(self, new_location):
        self.location = new_location

# Create Bird objects
bird1 = Bird("sparrow", "Europe")
bird2 = Bird("parrot", "South America")

# Migrate birds
bird1.migrate("Africa")
bird2.migrate("North America")

# Print new locations
print("New location of sparrow:", bird1.location)
print("New location of parrot:", bird2.location)
