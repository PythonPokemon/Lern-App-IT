from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class LearningApp(App):
    def build(self):
        self.questions = [
            {
                'question': 'What is the capital of France?',
                'choices': ['Paris', 'Berlin', 'Madrid', 'Rome'],
                'correct_choice': 0
            },

             {
                'question': 'Was ist das beste RPG?',
                'choices': ['PoE', 'Diablo 4', 'ESO', 'FF-Online'],
                'correct_choice': 0
            },
            # Add more questions here
        ]
        
        self.current_question_index = 0
        self.layout = BoxLayout(orientation='vertical')
        
        self.question_label = Label(text=self.questions[self.current_question_index]['question'])
        self.layout.add_widget(self.question_label)
        
        self.choice_buttons = []
        for i, choice in enumerate(self.questions[self.current_question_index]['choices']):
            button = Button(text=choice, on_release=self.check_answer)
            self.choice_buttons.append(button)
            self.layout.add_widget(button)
        
        return self.layout
    
    def check_answer(self, button):
        correct_choice = self.questions[self.current_question_index]['correct_choice']
        chosen_choice = self.questions[self.current_question_index]['choices'].index(button.text)
        
        if chosen_choice == correct_choice:
            self.question_label.text = "Correct!"
        else:
            self.question_label.text = "Incorrect. The correct answer is: " + self.questions[self.current_question_index]['choices'][correct_choice]
    
    def next_question(self):
        self.current_question_index = (self.current_question_index + 1) % len(self.questions)
        self.question_label.text = self.questions[self.current_question_index]['question']
        
        for i, choice in enumerate(self.questions[self.current_question_index]['choices']):
            self.choice_buttons[i].text = choice
    
if __name__ == '__main__':
    LearningApp().run()
