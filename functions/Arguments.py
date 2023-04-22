

def concatenate_args(*names):
    results = ""
    for name in names:
        results +=name
    return results


def concatenate_kwargs(**persons):
    result = ""
    for person in persons.values():
        result += person
    return result