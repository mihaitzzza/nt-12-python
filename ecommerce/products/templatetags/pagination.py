from django.template import Library

register = Library()


# @register.filter()
# def my_custom_filter(value):
#     return value[0].upper() + value[1:]

# @register.filter()
# def my_custom_filter(value):
#     if value > 1:
#         return 's'
#
#     return ''

@register.filter(name="add_filter")
def my_custom_filter(value, other_value):
    print('value', value, 'other_value', other_value)
    return value + other_value
