# In components/button/button.py
from django_components import Component, register

@register("button")
class Button(Component):
    # The template for the button component
    template_name = "template.html"

    # This component takes one parameter, the text to display on the button
    def get_context_data(self, button_text, button_color):
        return {
            "button_text": button_text,
            "button_color": button_color,
        }

    # Media for CSS and JavaScript
    class Media:
        css = "style.css"
        js = "script.js"
