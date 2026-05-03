import argparse

# Create the parser
parser = argparse.ArgumentParser(description="My first argparse demo")

# Add arguments
parser.add_argument("--name", help="Your name")
parser.add_argument("--age", type=int, help="Your age")

# Parse what the user typed
args = parser.parse_args()

# Display the results
print(f"Hello {args.name}!")
if args.age:
    print(f"You are {args.age} years old")