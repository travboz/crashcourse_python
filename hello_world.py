message = "Hello world!"
print(message)

words = "am I going\t to do"

message = f"wtf\n\t {words} with my life         "
print(message.rstrip() + " howdy")


badWords = "fuck what am I going to do"
print(badWords.removeprefix("fuck w"))
# needs to match exactly what's in the braces