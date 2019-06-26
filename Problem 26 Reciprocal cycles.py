def answer():
    for num in range(1, 1001):
        curr = str(1 / num)[2:]
        if len(curr) > 15:
            print("repeating")
            for start in range(0, 3):
                for length in range(1, 3):
                        if curr[start] == curr[start + length]:
                            break
        print("answer: " + curr)

answer()
