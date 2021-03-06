from GraphicsEngine.Views.SubViews.GUI.BasicGUISubView import BasicGUISubView
from InputManaging.InputManager import InputManager
from InputManaging.ControlEvents import ControlEvents
from Utilities.GraphicsUtilities.GraphicsUtility import GraphicsUtility
import ogre.gui.CEGUI as CEGUI

class CombatMapMenuSubView(BasicGUISubView):

    # Class Constants--------------------------------------------------------------------------------------------------#
    GUI_LAYOUT = 'BattleMenu.layout'
    # -----------------------------------------------------------------------------------------------------------------#

    def __init__(self, mode, guiSheet, schemeFile):
        BasicGUISubView.__init__(self, mode, guiSheet, schemeFile, CombatMapMenuSubView.GUI_LAYOUT)

    def registerHandlers(self):
        self.ui.getChild("BaseCombatMenu/ActionSelection").getChild("BaseCombatMenu/ActionSelection/MoveButton-Clickable").subscribeEvent(
            CEGUI.PushButton.EventClicked, self, 'transition'
        )
#        self.ui.getChild("Second Demo Window").getChild("Second Demo Window/Button2-Clickable").subscribeEvent(
#            CEGUI.PushButton.EventClicked, self, 'printFunction'
#        )

    def transition(self, e):
        InputManager.getSingleton().setControlEvent(ControlEvents.TRANSITION_FORWARD)
