def print_fibonacci(length):
    if length == 0:
        print([])
        return
    
    fibonacci_sequence = [0]
    if length > 1:
        fibonacci_sequence.append(1)
    
    for i in range(2, length):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    
    print(fibonacci_sequence)


if __name__ == "__main__":
    print_fibonacci(10) 
