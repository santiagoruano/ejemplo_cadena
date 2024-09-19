text1 = "Fundamentos con"
text2 = "Python"
text3 = 5
result = text1 + text3
print(result)

name = "Santiago"
lastName = "Ruano"
fullName = name + " " + lastName
print(fullName)

price = 97
text3 = f"The price is{price:.2f} dollars"
print(text3)

text4 = f"la multiplicacion es {20 * 59} "
print(text4)

text5 = "python es un lenguaje de alto nivel de programacion"
result1 = text5.capitalize()
print(result1)

title = "Cien Años de Soledad"
titleConvert = title.casefold()
print(titleConvert)

fruit = "banana"
textCenter = fruit.center(20, "-")
print(textCenter)

title1 = "I love apples, apple are my favorite fruit"
result2 = title1.count("apple")
print(result2)

text6 = "Curso, fundmentos con Python."
result3 = text6.endswith(".")
print(result2)

letter = "F\tU\tP"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)

text7 = "Hola, bienvenidos a Colombia."
result4 = text7.find("bienvenidos")
print(result4)

text8 = "welcome to my world"
result5 = text8.title()
print(result5)

alphanumeric = "Python312"
result6 = alphanumeric.isalnum()
print(result6)

letters = "Space X"
result7 = letters.isalpha()
print(result7)


