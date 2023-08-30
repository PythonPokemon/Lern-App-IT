from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

# Beispieldaten für die Kategorien
vocabulary = {
    1: [
        ("Frage 1", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 2", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 3", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 4", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 5", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 6", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 7", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 8", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 9", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 10", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 11", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 12", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 13", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ],

    2: [
        ("Frage 1", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 2", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 3", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 4", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 5", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 6", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 7", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 8", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 9", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 10", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 11", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 12", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 13", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ],

    3: [
        ("Frage 1", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 2", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 3", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 4", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 5", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 6", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 7", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 8", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 9", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 10", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 11", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 12", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 13", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ],

    4: [
        ("Frage 1", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 2", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 3", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 4", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 5", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 6", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 7", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 8", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 9", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 10", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 11", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 12", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 13", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ],

    5: [
        ("Frage 1", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 2", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 3", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 4", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 5", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 6", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 7", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 8", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 9", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 10", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 11", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 12", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ("Frage 13", "Definition 1"), ("Praxis Tipp", "Beispiel"),
        ],
}


class VocabularyApp(App):
    def build(self):
        self.title = 'IT- Kompetenzcheck '
        self.layout = BoxLayout(orientation='vertical')
        
        self.category_buttons = []
        for category in range(1, 6):
            button = Button(text=f'Lernfeld {category}', size_hint=(1, None), height=50)
            button.bind(on_press=self.show_category_vocabulary)
            self.category_buttons.append(button)
            self.layout.add_widget(button)

        self.developer_label = Label(
            text='All Rights Reserved © 2023 by Python Pokemon',
            size_hint=(1, None),
            height=30,
            halign='center',
            valign='middle'
        )
        self.layout.add_widget(self.developer_label)
        
        return self.layout
    
    def show_category_vocabulary(self, instance):
        self.layout.clear_widgets()
        category = int(instance.text.split()[-1])
        
        category_label = Label(text=f'Lernfeld {category} Fragen', size_hint=(1, None), height=50)
        self.layout.add_widget(category_label)
        
        scroll_view = ScrollView()
        layout_inside_scroll = GridLayout(cols=1, spacing=10, size_hint_y=None)
        
        for word, definition in vocabulary[category]:
            word_label = Label(text=f'{word}: {definition}', size_hint_y=None, height=40, valign='middle')
            layout_inside_scroll.add_widget(word_label)
        
        layout_inside_scroll.bind(minimum_height=layout_inside_scroll.setter('height'))
        scroll_view.add_widget(layout_inside_scroll)
        self.layout.add_widget(scroll_view)
        
        back_button = Button(text='Zurück', size_hint=(1, None), height=50)
        back_button.bind(on_press=self.go_back)
        self.layout.add_widget(back_button)
    
    def go_back(self, instance):
        self.layout.clear_widgets()
        for button in self.category_buttons:
            self.layout.add_widget(button)

if __name__ == '__main__':
    VocabularyApp().run()
