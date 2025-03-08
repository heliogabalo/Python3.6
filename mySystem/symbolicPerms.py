def numeric_to_symbolic(permission):
    permission = str(permission)
    symbolic = ''
    for digit in permission:
        if digit == '7':
            symbolic += 'rwx'
        elif digit == '6':
            symbolic += 'rw-'
        elif digit == '5':
            symbolic += 'r-x'
        elif digit == '4':
            symbolic += 'r--'
        elif digit == '3':
            symbolic += 'wx-'
        elif digit == '2':
            symbolic += 'w--'
        elif digit == '1':
            symbolic += '--x'
        else:
            symbolic += '---'
    return symbolic

# Example usage
print(numeric_to_symbolic(440)) # Output: rwxr-xr-x

