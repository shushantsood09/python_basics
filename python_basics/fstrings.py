letter = "Hey my name is {1} and I am from {0}"
country = "india"
name = "Shushant"
print(letter.format(country, name))

# F-string
print(f"Hey my name is {name} and I am from {country}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))