from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlCombo import ControlCombo
from pyforms.gui.controls.ControlEmptyWidget import ControlEmptyWidget
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlText import ControlText

from generation import Stage3, Category
from base import Saver


class Stage3Window(BaseWidget):

    def __init__(self, erd, categories, project):
        super(Stage3Window, self).__init__('Etap 3')
        self.set_margin(40)

        self._categories_editor =  ControlEmptyWidget()
        self._save_button = ControlButton('Zapisz')

        self.erd = erd
        self._project = project
        self.categories = categories

        self.generate_categories()

        self._save_button.value = self.__save_action

        self._project = project

        self.stage = self._project.get_stage(3)

        self._categories_editor.value = CategoriesEditor(self.categories)

        self.formset = ['_categories_editor', '_save_button']

    def generate_categories(self):
        if not self.categories:
            for entity in self.erd.entities:
                self.categories.append(Category(entity, ''))

    def __save_action(self):
        if self._project.stages[3] is None:
            self.stage = Stage3(self.erd, self.categories)
            self._project.add_stage(self.stage)
        Saver.get_saver().save()
        self.parent.populate_buttons()


class CategoryCombo(ControlCombo):

    def __init__(self, categories, edit_description):
        super(CategoryCombo, self).__init__()

        self.categories = categories
        self.edit_description = edit_description

    def activated_event(self, index):
        category = self.categories[index]
        self.edit_description.value = category.description


class CategoriesEditor(BaseWidget):

    def __init__(self, categories):
        super(CategoriesEditor, self).__init__()

        self.categories = categories

        self._description_edit_text = ControlText()
        self._combo = CategoryCombo(self.categories, self._description_edit_text)
        self._save_button = ControlButton('Zapisz')

        self._save_button.value = self.__save_category_action

        self._combo.parent = self

        self.formset = ['_combo', ('Opis kategorii' ,'_description_edit_text', '_save_button')]

        self.populate()

    def populate(self):
        for category in self.categories:
            self._combo.add_item(category.entity.name_singular, category)

    def __save_category_action(self):
        self.categories[self._combo.current_index].description = self._description_edit_text.value
        Saver.get_saver().save()


