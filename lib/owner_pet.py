class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an Owner instance")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # register this pet
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of Pet instances that belong to this owner."""
        return [p for p in Pet.all if p.owner is self]

    def add_pet(self, pet):
        """Associate a Pet instance with this owner.

        Raises Exception if the provided object is not a Pet.
        """
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance")

        pet.owner = self

    def get_sorted_pets(self):
        """Return the owner's pets sorted by pet name."""
        return sorted(self.pets(), key=lambda p: p.name)