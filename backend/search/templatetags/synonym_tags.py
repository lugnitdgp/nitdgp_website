from django import template
register = template.Library()

DEPT_SYNONYMS = [
    ['CS', 'CSE', 'IT'],
    ['ME', 'MECH']
]

# MUST Add space for exact word match
GENERAL_SYNONYMS = [
    ['exam ', 'examination '],
    ['examination ', 'exam '],
    ['sem ', 'semester '],
    ['semester ', 'sem '],
    ['b.tech ', 'b. tech ', 'btech '],
    ['b. tech ', 'b.tech ', 'btech '],
]


@register.filter
def add_dept_synonyms(dept_name):
    synonyms = dept_name
    for syn_list in DEPT_SYNONYMS:
        if dept_name.upper() in syn_list:
            synonyms = " ".join(syn_list)
    return synonyms


@register.filter
def add_general_synonyms(text_data):
    try:
        text_data = text_data.lower()
        for syn_list in GENERAL_SYNONYMS:
            if syn_list[0] in text_data:
                text_data = text_data.replace(
                    syn_list[0], "".join(syn_list), 1)
                return text_data
    except Exception as e:
        print(e)

    return text_data
