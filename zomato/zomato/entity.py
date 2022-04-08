class Restaurant:

    def __init__(self, id, name, description, address, photo, openingHours, comments):
        self._id = id
        self._name = name
        self._description = description
        self._address = address
        self._photo = photo
        self._openingHours = openingHours
        self._comments = comments

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getDescription(self):
        return self._description

    def setDescription(self, description):
        self._description = description

    def getAddress(self):
        return self._address

    def setAddress(self, address):
        self._address = address

    def getPhoto(self):
        return self._photo

    def setPhoto(self, photo):
        self._photo = photo

    def getOpeningHours(self):
        return self._openingHours

    def setOpeningHours(self, openingHours):
        self._openingHours = openingHours

    def getComments(self):
        return self._openingHours

    def setComments(self, comments):
        self._comments = comments
