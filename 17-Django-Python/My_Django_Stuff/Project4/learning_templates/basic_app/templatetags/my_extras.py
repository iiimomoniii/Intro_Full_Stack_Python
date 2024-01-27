from django import template

register = template.Library()
#create custom filter for cut string
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')

register.filter('cut',cut) 
