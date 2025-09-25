# Instalação do KivyMD
# Código da Aula

# %pip install kivymd

from kivy.app import App

from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem


Builder.load_string(
    """

<TabsLayout>:

    TabbedPanel:

        do_default_tab: False

        TabbedPanelItem:

            text: 'Tab 1'

            BoxLayout:

                orientation: 'vertical'

                Label:

                    text: 'Content for Tab 1'

        TabbedPanelItem:

            text: 'Tab 2'

            BoxLayout:

                orientation: 'vertical'

                Label:

                    text: 'Content for Tab 2'

"""
)


class TabsLayout(BoxLayout):

    pass


class TabsApp(App):

    def build(self):

        return TabsLayout()


if __name__ == "__main__":

    TabsApp().run()

#####################################

# Código refatorado, estava dando erro
# O erro vinha do Kivy tentando abrir um .kv automático que não existia.
# Desliguei esse carregamento e passamos a
# controlar a interface só pelo Builder.load_string.
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_string(
    """
<TabsLayout>:
  TabbedPanel:
    do_default_tab: False
    TabbedPanelItem:
      text: 'Tab 1'
      BoxLayout:
        orientation: 'vertical'
        Label:
          text: 'Content for Tab 1'
    TabbedPanelItem:
      text: 'Tab 2'
      BoxLayout:
        orientation: 'vertical'
        Label:
          text: 'Content for Tab 2'
"""
)


class TabsLayout(BoxLayout):
    pass


class MyTabsApp(App):
    def build(self):
        return TabsLayout()

    def load_kv(self, filename=None):
        # impede que o Kivy tente abrir um arquivo .kv
        return None


if __name__ == "__main__":
    MyTabsApp().run()
