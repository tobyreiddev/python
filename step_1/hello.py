def greet_person(name, greeting):
    full_greeting = "{}, {}".format(greeting, name)
    return full_greeting


print(greet_person("turnosaurus", "hello"))