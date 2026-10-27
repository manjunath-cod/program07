import sys

def check_palindrome(text):
    if text == text[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

if __name__ == "__main__":
    text = sys.argv[1] if len(sys.argv) > 1 else "madam"
    print("Input:", text)
    check_palindrome(text)
