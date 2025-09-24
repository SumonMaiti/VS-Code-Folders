letter='Hey my name is {0} and i am from {1}'
country='India'
name="Sumon"
print(letter.format(name,country)) #--> put name and country variable in second bracket
print(f"Hey my name is {{name}} and i am from {{country}}")#--> if we want to write {} as it is use double {{}} 
print(f"Hey my name is {name} and i am from {country}") #--> it will replece variable into string
price=45.6753776
print(f'The price of the element is {price:.2f}')#--> it will print only 2 character after point
