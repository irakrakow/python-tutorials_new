my_string = "hi442nm233ag2"

new_string = "".join(
    ["d" if i == "4"
     else "e" if i == "2"
     else "s" if i == "3"
     else i
     for i in my_string]
)
print(new_string)
