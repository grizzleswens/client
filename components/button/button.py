# In components/button/button.py
from django_components import Component, register

@register("button")
class Button(Component):
    # The template for the button component
    template_name = "template.html"

    # Default values are set in the parameters
    def get_context_data(self, button_text="default", button_color="btn-secondary"):
        return {
            "button_text": button_text,
            "button_color": button_color,
        }

    # Media for CSS and JavaScript
    class Media:
        css = "button/style.css"
        js = "script.js"
