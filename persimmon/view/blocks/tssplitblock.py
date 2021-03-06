from persimmon.view.util import InputPin, OutputPin
from persimmon.view.blocks import Block

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from sklearn.model_selection import TimeSeriesSplit


Builder.load_file('view/blocks/tssplitblock.kv')

class TSSplitBlock(Block):
    out_1 = ObjectProperty()

    def function(self):
        self.out_1.val = TimeSeriesSplit()
