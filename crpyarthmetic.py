from itertools import permutations

def solve_cryptarithmetic():
    words = ['SEND', 'MORE', 'MONEY']
    letters = set(''.join(words))  # Unique letters

    # Try all digit permutations for the letters
    for perm in permutations(range(10), len(letters)):
        letter_to_digit = dict(zip(letters, perm))
        send = sum(letter_to_digit[char] * (10 ** (len('SEND') - i - 1)) for i, char in enumerate('SEND'))
        more = sum(letter_to_digit[char] * (10 ** (len('MORE') - i - 1)) for i, char in enumerate('MORE'))
        money = sum(letter_to_digit[char] * (10 ** (len('MONEY') - i - 1)) for i, char in enumerate('MONEY'))
        
        if send + more == money:  # Check if equation holds
            return letter_to_digit, send, more, money
    
    return None

solution = solve_cryptarithmetic()
if solution:
    letter_to_digit, send, more, money = solution
    print(f"Solution: {letter_to_digit}, SEND={send}, MORE={more}, MONEY={money}")
else:
    print("No solution found.")
