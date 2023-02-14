def age_assignment(*names, **ages):
    result = []

    for letter, age in ages.items():
        person_name = ""
        for name in names:

            if name.startswith(letter):
                person_name = name
                break

        result.append(f"{person_name} is {age} years old.")

    return "\n".join(sorted(result, key=lambda x: (x[0])))


