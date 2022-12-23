my_dict = {
    "Spider": "photographer",
    "Bat": "philanthropist",
    "Wonder Wo": "nurse"
}

my_dict = {
    (key+"man" if key != "Spider" else "Superman"):
    (val if val != "photographer" else "journalist")
    for (key, val) in my_dict.items()
}

print(my_dict)
