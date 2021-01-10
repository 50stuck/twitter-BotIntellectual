from intellectuals import intellectual_names
from process import get_name_tuple

def syl_breakdown(name):
    en_name = intellectual_names.get(name, 'NaN')
    name_tuple = get_name_tuple(en_name)

    return en_name, name_tuple

print(syl_breakdown("אודרי לורד"))
