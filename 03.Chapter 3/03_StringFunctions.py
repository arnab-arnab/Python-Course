story='''Once upon a time there Was a doggy named devesh who Loved a girl named sneha,
but the girl Betrayed devesh and that bitch was soon found with a cow named deborshi'''

# STRING FUNCTIONS:-

print(len(story))                     #Calculates the length of the string
print(story.endswith("ffhhdfdh"))     #Returns false
print(story.endswith("deborshi"))     #Returns true
print(story.count("o"))               #It counts the number of times 'o' appears in the string
print(story.count('doggy'))           #It counts the number of times 'doggy' appears in the string
print(story)
print(story.capitalize())             #It will capitalize the first letter of the string
print(story.lower())                  #It will uncapitalize the entire string
print(story.find("sneha"))            #It finds whether 'sneha' is present in the string or not, if presents it returns the index value of first letter
print(story[71])
print(story.find("named"))            #If the word appears more than once then python will only consider the first time the word appears
print(story.find("subh"))             #It returns -1 if the word is not present in the string
print(story.replace("sneha","doggy's bitch"))        
#It will replace the word "sneha" with "doggy's" bitch

print(story.casefold())               #It is used for caseless comparison

# CASEFOLD METHOD

va="JaCkIE CHaN"
vb="jacKIE chaN"

if va.casefold()==vb.casefold():
    print("The strings are equal")
else:
    print("Unequal")