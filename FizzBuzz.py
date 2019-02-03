data = []
for x in range(1,100):
	if (x % 3 == 0) and (x % 5 == 0):
		data.append("FizzBuzz")
		continue
	if (x % 3 == 0):
		data.append("Fizz")
		continue
	if (x % 5 == 0):
		data.append("Buzz")
		continue
	data.append(x)


print(data);