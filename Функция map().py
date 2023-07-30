values = [1, 2, '3', 'forth', 'end', 99, True, None]
variable = lambda x: str(x) if isinstance(x, int) else x
value = list(map(variable, values))
print(value)






