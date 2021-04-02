from django import template

register = template.Library()


def upper(value: str):
    return value.upper() + ' @'

def replaceN(value: str, tag):
    return value.replace("\n", tag)

# username|default:"Отсутствует"
# def default(value, param):
#     return value or param
register.filter('replaceN', replaceN)
register.filter('upper', upper)
