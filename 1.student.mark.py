# list
x = 30
print(f"--Primes up to {x}: {[_ for _ in range(2, x+1) if all([_%i for i in range(2, _)])]}")

# tuple
print("--Unlike list, tuples are immutable/unhashable, mean modify a tuple will raise an error:")

# dict
d = {"Bio": 3, "Math": 10, "His": 5}
print(f"--Keys in dict are immutable/unhashable, for list d = {d}; ", end = "")
print(f"Using 'sorted(d.items(), key = lambda _, _[1]' to sort this dict by number of books:' {sorted(d.items(), key = lambda _: _[1])}")