from django.template.defaulttags import register


@register.filter
def sum(value, arg):
    return (value + arg)

@register.filter
def res(value, arg):
    return (value - arg)

# Change - to +
@register.filter
def mod(value):
    return (-value)

# For iteration: for i in range(5)
@register.filter
def times(number):
    return range(number)
