from django_viewcomponent import component


@component.register("form")
# This gives it the name "button" for reference in the html template
class ExampleComponent(component.Component):
    template_name = "form/form.html"

    def __init__(self, **kwargs):
        self.label = kwargs['label']