original_array = [2, 8, 9, 48, 8, 22, -12, 2]
print(original_array)

processed_array = []
for x in original_array:
    if x > 5:
        processed_array.append(x + 2)

print(processed_array)