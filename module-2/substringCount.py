def count_substring_occurrences(main_string, substring):
    count = 0
    start = 0
    
    while start < len(main_string):
        start = main_string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1
    
    return count

# Example usage:
main_string = "Hello, Hello, Hello, World!"
substring = "Hello"
occurrences = count_substring_occurrences(main_string, substring)
print(f'The substring "{substring}" appears {occurrences} times in the main string.')
