class Book():
    def __init__(self, name="", authorName="", memberLegajo=0):
        self.name = name
        self.authorName = authorName
        self.memberLegajo = memberLegajo

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def authorName(self):
        return self._authorName

    @authorName.setter
    def authorName(self, authorName):
        self._authorName = authorName

    @property
    def memberLegajo(self):
        return self._memberLegajo

    @memberLegajo.setter
    def memberLegajo(self, memberLegajo):
        self._memberLegajo = memberLegajo
