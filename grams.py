
#Ask the user to enter the amount of gram
gram = int(input("Enter gram: "))

# Formula
kilogram = gram / 1000
milligram = gram * 1000
microgram = gram * 1000000
pound = gram * 453.6
ounce = gram / 28.35
liter = gram / 1000

#Convert the value of gram into the given sample
print(gram, "gram to kilogram = ", kilogram)
print(gram, "gram to milligram = ", milligram)
print(gram, "gram to microgram = ", microgram)
print(gram, "gram to pound = ", pound)
print(gram, "gram to ounce = ", ounce)
print(gram, "gram to liter = ", liter)
