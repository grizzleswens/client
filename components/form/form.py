# components/form/form.py
from django_components import Component, register

@register("basic_form")
class BasicFormComponent(Component):
    template_name = "template.html"

    # This component takes one parameter: the form instance
    def get_context_data(self, form, button_text="Submit", button_color="btn-primary", ):
        return {
            "form": form,
        }

    class Media:
        css = "style.css"  # Add any additional styles if needed
        js = "script.js"
