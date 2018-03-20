import pyforms
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlText import ControlText


class Stage1Window(pyforms.BaseWidget):

    def __init__(self):
        super(Stage1Window, self).__init__('Etap 1')
        self._list = ControlList()
        self._list.readonly = True
        for i in range(100):
            self._list.__add__('aaa')

        # self._label2 = ControlText('dupa')
        # self._label3 = ControlText('dupa')
        # self._label4 = ControlText('dupa')
        # self._label5 = ControlText('dupa')
        # self._label6 = ControlText('dupa')
        # self._label7 = ControlText('dupa')
        # self._label8 = ControlText('dupa')
        # self._label9 = ControlText('dupa')
        # self._label0 = ControlText('duasdpa')
        # self._labeldf = ControlText('dupa')
        # self._labelsd = ControlText('dsdaupa')
        # self._labela = ControlText('dupa')
        # self._labelb = ControlText('dasdupa')
        # self._labelc = ControlText('dupasda')
        # self._labeld = ControlText('dupa')
        # self._labele = ControlText('dupa')
        # self._labelf = ControlText('duasdpa')
        # self._labelg = ControlText('dupa')
        # self._labelh = ControlText('dupa')
        # self._labeli = ControlText('duasdpa')
        # self._labelj = ControlText('duasdpa')
        # self._labelk = ControlText('dupa')
        # self._labell = ControlText('dusdpa')
        # self._labelm = ControlText('dupa')
        # self._labeln = ControlText('dupa')
        # self._labelo = ControlText('dupa')
        # self._labelp = ControlText('dupa')
        # self._labelr = ControlText('dupa')
        # self._labels = ControlText('dupa')
        # self._labelt = ControlText('dupa')
        # self._labelq = ControlText('dupa')
        # self._labelx = ControlText('dupa')
        # self._labely = ControlText('dupa')
        # self._labelz = ControlText('dupa')
        print(self.formset)
        self._list.autoscroll = True
