from django_viewcomponent import component


@component.register("button")
# This gives it the name "button" for reference in the html template
class ExampleComponent(component.Component):
    template_name = "button/button.html"

    def __init__(self, **kwargs):
        self.label = kwargs['label']
        self.btn_class = kwargs['btn_class']