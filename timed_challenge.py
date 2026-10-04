# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# Timed Challenge: Balanced Symbols
#
# Check if the brackets in a string are balanced.
# Input: "{[()]}"
# Output: True
#
# Input: "{[(])}"
# Output: False


def balanced_symbols(text):
    # A stack is useful because the most recently opened bracket
    # must be the first bracket that gets closed.
    stack = []

    matching_brackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in text:
        # Add opening brackets to the stack
        if char in "([{":
            stack.append(char)

        # Check closing brackets
        elif char in ")]}":
            # If there is nothing to match, it is not balanced
            if len(stack) == 0:
                return False

            # Remove the most recent opening bracket
            last_opening = stack.pop()

            # Check whether the brackets match
            if last_opening != matching_brackets[char]:
                return False

    # If the stack is empty, every opening bracket was closed
    return len(stack) == 0


# Test cases

print(balanced_symbols("{[()]}"))      # True
print(balanced_symbols("{[(])}"))      # False
print(balanced_symbols("()"))          # True
print(balanced_symbols("((("))         # False
print(balanced_symbols(""))            # True
print(balanced_symbols("hello"))       # True
print(balanced_symbols("(hello)"))     # True
print(balanced_symbols("]"))           # False


"""
Reflection

For this timed challenge, I chose to use a stack because the problem requires
checking brackets in the reverse order that they are opened. When an opening
bracket appears, I add it to the stack. When a closing bracket appears, I remove
the most recent opening bracket and check whether the two symbols match. This
works well because a stack follows last-in, first-out behavior. The operations
of adding and removing from the end of the stack are also efficient and usually
take O(1) time. The entire function takes O(n) time because each character is
checked once.

The 30-minute time limit made me focus on finding a simple solution instead of
trying to make the code more complicated. I first identified the main pattern
in the problem, which is that the last bracket opened needs to be the first one
closed. That helped me decide on a stack quickly. I also used a dictionary to
connect each closing bracket to its matching opening bracket.

One trade-off I made was keeping the validation simple. The function ignores
characters that are not brackets instead of checking whether every character
is a valid input. Under time pressure, I focused on the main requirement of
checking balanced symbols. I tested normal cases, incorrect bracket order,
missing closing brackets, an empty string, regular text, and a closing bracket
without an opening bracket. The timed challenge showed me that choosing the
right data structure early can make a problem much easier to solve.
"""