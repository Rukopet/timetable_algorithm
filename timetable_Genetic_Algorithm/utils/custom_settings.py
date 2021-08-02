from abc import abstractmethod


class IDataFromFront:
    @abstractmethod
    def setGroupsJSON(self):
        pass

    @abstractmethod
    def setDisciplinesJSON(self):
        pass

    @abstractmethod
    def setLoadPlanJSON(self):
        pass

    @abstractmethod
    def setPedagogsJSON(self):
        pass

    @abstractmethod
    def setAudiencesJSON(self):
        pass


