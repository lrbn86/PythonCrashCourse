name = "ada lovelace"
print(name.title()) # prints name in titlecase
print(name.upper()) # prints name in UPPERCASE

name = name.upper() # set name to UPPERCASE version

print(name) # should print the UPPERCASE version

print(name.lower()) # should print back to original lowercase


# string concatenation
first_name = "ada"
last_name = "lovelace"
name = first_name + " " + last_name # set name to be the string concatenation
print(name) # should get "ada lovelace"

# whitespaces
print("Hello\nworld") # newline
print("Hello\tworld") # tabspace

# remove whitespaces
phrase = " Hello world "
print(phrase) # should get " Hello World "
phrase = phrase.strip()
print(phrase) # should get "Hello World"
# strip() only works when the whitespaces are between the string
phrase = "Hello\nWorld"
print(phrase)
phrase = phrase.strip()
print(phrase)
