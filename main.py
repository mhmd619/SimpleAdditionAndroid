"""A simple two-number addition app for Android and Windows (Kivy)."""

__version__ = "1.0.0"

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from arithmetic import add_numbers


class SimpleAdditionApp(App):
    title = "Simple Addition"

    def build(self):
        Window.clearcolor = (0.96, 0.97, 0.99, 1)
        root = BoxLayout(orientation="vertical", padding=24, spacing=12)
        root.add_widget(Widget(size_hint_y=1))

        root.add_widget(
            Label(
                text="Add Two Numbers",
                font_size="25sp",
                bold=True,
                color=(0.12, 0.18, 0.28, 1),
                size_hint_y=None,
                height=60,
            )
        )

        self.first_input = TextInput(
            hint_text="First number",
            multiline=False,
            input_type="number",
            font_size="22sp",
            halign="center",
            size_hint_y=None,
            height=58,
        )
        root.add_widget(self.first_input)

        self.second_input = TextInput(
            hint_text="Second number",
            multiline=False,
            input_type="number",
            font_size="22sp",
            halign="center",
            size_hint_y=None,
            height=58,
        )
        root.add_widget(self.second_input)

        button = Button(
            text="Add",
            font_size="22sp",
            size_hint_y=None,
            height=58,
            background_normal="",
            background_color=(0.13, 0.39, 0.75, 1),
        )
        button.bind(on_press=self.on_add)
        root.add_widget(button)

        self.result_label = Label(
            text="Sum: -",
            font_size="24sp",
            bold=True,
            color=(0.12, 0.18, 0.28, 1),
            size_hint_y=None,
            height=70,
        )
        root.add_widget(self.result_label)
        root.add_widget(Widget(size_hint_y=1))
        return root

    def on_add(self, _button):
        try:
            result = add_numbers(self.first_input.text, self.second_input.text)
        except ValueError:
            self.result_label.text = "Enter two valid numbers"
            return
        self.result_label.text = f"Sum: {result}"


if __name__ == "__main__":
    SimpleAdditionApp().run()
