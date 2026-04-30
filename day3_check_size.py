import os

small_file = "small_file.txt"
large_file = "large_file.pdf"

small_size = os.path.getsize(small_file)
large_size = os.path.getsize(large_file)

print(f"{small_file} is {small_size} bytes")
print(f"{large_file} is {large_size} bytes")

large_mb = large_size / (1024 * 1024)
print(f"{large_file} is {large_mb:.2f} MB")

if large_size > 10 * 1024 * 1024:
    print("This file is LARGE")
else:
    print("This file is SMALL")