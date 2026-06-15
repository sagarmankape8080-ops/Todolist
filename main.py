from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class ToDoLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.tasks = []

        self.input_task = TextInput(
            hint_text="Enter a task",
            size_hint=(1, 0.1)
        )
        self.add_widget(self.input_task)

        self.add_button = Button(
            text="Add Task",
            size_hint=(1, 0.1)
        )
        self.add_button.bind(on_press=self.add_task)
        self.add_widget(self.add_button)

        self.task_label = Label(
            text="No tasks yet",
            valign="top"
        )
        self.add_widget(self.task_label)

    def add_task(self, instance):
        task = self.input_task.text.strip()

        if task:
            self.tasks.append(task)
            self.task_label.text = "\n".join(
                [f"{i+1}. {t}" for i, t in enumerate(self.tasks)]
            )
            self.input_task.text = ""

class ToDoApp(App):
    def build(self):
        return ToDoLayout()

if __name__ == "__main__":
    ToDoApp().run()