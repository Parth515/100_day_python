# List and Dict Comprehension

numbers = ['1', '2', '3']
new_number = [int(n) for n in numbers]
print(new_number)

name = "Angela is"
letter_list = [letter for letter in name.split()]
print(letter_list)

double_list = [n for n in range(1, 5) if n%2 == 0]
print(double_list)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n%2 != 0]
print(result)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp_c * 9 / 5) + 32 for day, temp_c in weather_c.items()}
print(weather_f)





import time

nums = range(10_000_00)  # 1 million numbers

# --- List comprehension ---
start = time.time()
squares_comp = [x * x for x in nums]
end = time.time()
print(f"List comprehension: {end - start:.5f} seconds")

# --- For loop ---
start = time.time()
squares_loop = []
for x in nums:
    squares_loop.append(x * x)
end = time.time()
print(f"For loop: {end - start:.5f} seconds")

# --- Generator expression (lazy) ---
start = time.time()
squares_gen = (x * x for x in nums)
# Actually consume the generator to measure real work
for _ in squares_gen:
    pass
end = time.time()
print(f"Generator expression: {end - start:.5f} seconds")
