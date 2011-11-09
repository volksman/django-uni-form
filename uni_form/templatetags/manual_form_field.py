from django import template

register = template.Library()

@register.inclusion_tag('uni_form/field.html')
def manual_form_field(field):
    return {
            'field': field
            }
