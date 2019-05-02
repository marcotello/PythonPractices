def chunker(iterable, size):
    # Implement function here
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]
        
for chunk in chunker(range(25), 4):
    print(list(chunk))

for chunk in chunker('python programming', 5):
    print(list(chunk))