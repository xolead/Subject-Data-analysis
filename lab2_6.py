from collections import defaultdict

with open('mbox.txt', 'r', encoding='utf-8') as file:
    all_lines = file.readlines()

author_counts = defaultdict(int)

for line in all_lines:
    if line.startswith('From '):
        parts = line.split()
        if len(parts) > 1:
            email = parts[1]
            author_counts[email] += 1

if author_counts:
    most_frequent_author = max(author_counts.items(), key=lambda x: x[1])
    print(f"Автор с наибольшим количеством писем: {most_frequent_author[0]}")
    print(f"Количество писем: {most_frequent_author[1]}")
else:
    print("Письма не найдены")