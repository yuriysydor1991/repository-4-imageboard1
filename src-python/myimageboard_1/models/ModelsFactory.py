from .GeneralModel import GeneralModel

class ModelsFactory:
    
    def getByName(self, modelName = None):
        if modelName == "generalmodel":
                return GeneralModel()
            
        return None