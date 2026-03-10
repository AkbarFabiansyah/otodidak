
number = 10
if number > 5:
     Exception(f"The number should not exceed 5. ({number=})")
print(number)

number = 1
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number=})")
print(number)

number = 1
assert (number < 5), f"The number should not exceed 5. ({number=})"
print(number)

def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")

try:
    linux_interaction()
except RuntimeError as error:
    print(error)
else:
    print("Doing even more Linux things.")
