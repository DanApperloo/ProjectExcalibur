from GraphicsEngine.Views.SubViews.Scene.BasicSceneSubView import *
from GraphicsEngine.Controllers.CharacterPlacementController import CharacterPlacementController

class CharacterPlacementSubView(BasicSceneSubView):
    """Controls the combat map mode"""

    def __init__(self, nameIn, sceneManagerIn, inputLayout, meshsIn):
        BasicSceneSubView.__init__(self, nameIn)
        self.sceneManager = sceneManagerIn
        self.layout = inputLayout
        self.meshs = meshsIn

    def initialize(self):
        CharacterPlacementController.createCharacterPlacement((self.sceneManager, self.layout, self.meshs))

    def getTransition(self, transitionTypeKey):
        return CharacterPlacementController.getTransition(transitionTypeKey)

    def cleanUp(self):
        CharacterPlacementController.deleteCharacterPlacement()

    def __del__(self):
        self.sceneManager = None
        self.layout = None
        self.mesh = None