# Book selection and graphing.

Created: 2023-04-15 20:42:17
Last Updated: 2023-04-15 21:06:23

### User - 2023-04-15 20:42:17

Write code that loads book data from a csv file. The csv has a title column and an author column. Once the data is loaded, start a loop on the command line where two books are displayed and the user is prompted to choose one. Each time they choose between two, ask again. Use this data to create a directed graph between books. When the user selects an option to make a graph, write  a graphviz file that renders the directed graph. The command line tool should print the instructions for rendering the file and then prompt for the next pair of books. The code should be in concise, readable, idiomatic python.

### Assistant - 2023-04-15 20:43:25

```python
import csv
import random
from collections import defaultdict
import graphviz

def load_books(file_path):
    books = []

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append({"title": row["title"], "author": row["author"]})

    return books

def user_choice(book1, book2):
    print(f"Choose a book:\n1. {book1['title']} by {book1['author']}\n2. {book2['title']} by {book2['author']}")
    choice = input("Enter 1 or 2: ").strip()
    return int(choice)

def build_graph(books, book_edges):
    graph = graphviz.Digraph('Book_Graph')
    for book in books:
        graph.node(book['title'])

    for edge in book_edges:
        graph.edge(edge[0], edge[1])

    graph.render('book_graph.gv', view=False)

def main():
    file_path = "books.csv"
    books = load_books(file_path)
    book_edges = defaultdict(int)

    while True:
        book1, book2 = random.sample(books, 2)
        choice = user_choice(book1, book2)

        if choice == 1:
            book_edges[(book1['title'], book2['title'])] += 1
        elif choice == 2:
            book_edges[(book2['title'], book1['title'])] += 1
        else:
            print("Invalid choice. Please enter 1 or 2.")

        action = input("Enter 'g' to generate the graph or 'c' to continue choosing books: ").strip()

        if action.lower() == 'g':
            build_graph(books, book_edges)
            print("Graph generated as 'book_graph.gv'. To render the graph, use the following command:\n")
            print("dot -Tpng book_graph.gv -o book_graph.png")
        elif action.lower() == 'c':
            continue
        else:
            print("Invalid action. Please enter 'g' or 'c'.")

if __name__ == "__main__":
    main()
```

This code reads book data from a CSV file with a "title" column and an "author" column. It then prompts the user to choose between two randomly selected books in a loop. As the user makes choices, a directed graph is created with edges representing the chosen book pairs. When the user selects to create a graph, a Graphviz file is written, and instructions for rendering the file are printed.

Remember to install the Graphviz library before running the code:
```
pip install graphviz
```

### User - 2023-04-15 20:45:33

Update the code to make the input and output file names command line arguments. Update the code to print a usage message if the write arguments aren't present. 

### Assistant - 2023-04-15 20:46:46

```python
import csv
import random
from collections import defaultdict
import graphviz
import sys
import argparse

def load_books(file_path):
    books = []

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append({"title": row["title"], "author": row["author"]})

    return books

def user_choice(book1, book2):
    print(f"Choose a book:\n1. {book1['title']} by {book1['author']}\n2. {book2['title']} by {book2['author']}")
    choice = input("Enter 1 or 2: ").strip()
    return int(choice)

def build_graph(books, book_edges, output_file):
    graph = graphviz.Digraph('Book_Graph')
    for book in books:
        graph.node(book['title'])

    for edge in book_edges:
        graph.edge(edge[0], edge[1])

    graph.render(output_file, view=False)

def main(input_file, output_file):
    books = load_books(input_file)
    book_edges = defaultdict(int)

    while True:
        book1, book2 = random.sample(books, 2)
        choice = user_choice(book1, book2)

        if choice == 1:
            book_edges[(book1['title'], book2['title'])] += 1
        elif choice == 2:
            book_edges[(book2['title'], book1['title'])] += 1
        else:
            print("Invalid choice. Please enter 1 or 2.")

        action = input("Enter 'g' to generate the graph or 'c' to continue choosing books: ").strip()

        if action.lower() == 'g':
            build_graph(books, book_edges, output_file)
            print(f"Graph generated as '{output_file}'. To render the graph, use the following command:\n")
            print(f"dot -Tpng {output_file} -o {output_file.split('.')[0]}.png")
        elif action.lower() == 'c':
            continue
        else:
            print("Invalid action. Please enter 'g' or 'c'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a directed graph from book choices.")
    parser.add_argument("input_file", help="CSV file containing book data with 'title' and 'author' columns.")
    parser.add_argument("output_file", help="Output file name for the generated Graphviz file.")
    args = parser.parse_args()

    if args.input_file and args.output_file:
        main(args.input_file, args.output_file)
    else:
        print("Usage: python book_graph.py <input_file> <output_file>")
```

This updated code accepts the input and output file names as command-line arguments. It also prints a usage message if the required arguments are not provided. The `argparse` library is used to handle command-line argument parsing.

To run the updated script, use the following command:

```
python book_graph.py books.csv book_graph.gv
```

### User - 2023-04-15 20:48:21

Now update the code so that it checks if the output file already exists. If it does, load the file and use the contents to initiate the directed graph. 

### Assistant - 2023-04-15 20:49:39

```python
import csv
import random
from collections import defaultdict
import graphviz
import sys
import argparse
import os

def load_books(file_path):
    books = []

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append({"title": row["title"], "author": row["author"]})

    return books

def user_choice(book1, book2):
    print(f"Choose a book:\n1. {book1['title']} by {book1['author']}\n2. {book2['title']} by {book2['author']}")
    choice = input("Enter 1 or 2: ").strip()
    return int(choice)

def load_existing_graph(output_file):
    if os.path.exists(output_file):
        return graphviz.Source.from_file(output_file)
    else:
        return None

def update_graph(existing_graph, books, book_edges):
    graph = existing_graph if existing_graph else graphviz.Digraph('Book_Graph')

    for book in books:
        graph.node(book['title'])

    for edge in book_edges:
        graph.edge(edge[0], edge[1])

    return graph

def main(input_file, output_file):
    books = load_books(input_file)
    book_edges = defaultdict(int)
    existing_graph = load_existing_graph(output_file)

    while True:
        book1, book2 = random.sample(books, 2)
        choice = user_choice(book1, book2)

        if choice == 1:
            book_edges[(book1['title'], book2['title'])] += 1
        elif choice == 2:
            book_edges[(book2['title'], book1['title'])] += 1
        else:
            print("Invalid choice. Please enter 1 or 2.")

        action = input("Enter 'g' to generate the graph or 'c' to continue choosing books: ").strip()

        if action.lower() == 'g':
            updated_graph = update_graph(existing_graph, books, book_edges)
            updated_graph.render(output_file, view=False)
            print(f"Graph generated as '{output_file}'. To render the graph, use the following command:\n")
            print(f"dot -Tpng {output_file} -o {output_file.split('.')[0]}.png")
        elif action.lower() == 'c':
            continue
        else:
            print("Invalid action. Please enter 'g' or 'c'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a directed graph from book choices.")
    parser.add_argument("input_file", help="CSV file containing book data with 'title' and 'author' columns.")
    parser.add_argument("output_file", help="Output file name for the generated Graphviz file.")
    args = parser.parse_args()

    if args.input_file and args.output_file:
        main(args.input_file, args.output_file)
    else:
        print("Usage: python book_graph.py <input_file> <output_file>")
```

This updated code checks if the output file already exists. If it does, the existing graph is loaded and used as the initial state for the directed graph. If the file does not exist, a new directed graph is created. The `load_existing_graph` function handles loading the existing graph, while the `update_graph` function updates the graph with the current user selections.

### User - 2023-04-15 20:50:55

Update the code to not show a pair to a user if that pair has already been ranked. That is, if they have a direct edge between them. 

### Assistant - 2023-04-15 20:52:32

```python
import csv
import random
from collections import defaultdict
import graphviz
import sys
import argparse
import os

def load_books(file_path):
    books = []

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append({"title": row["title"], "author": row["author"]})

    return books

def user_choice(book1, book2):
    print(f"Choose a book:\n1. {book1['title']} by {book1['author']}\n2. {book2['title']} by {book2['author']}")
    choice = input("Enter 1 or 2: ").strip()
    return int(choice)

def load_existing_graph(output_file):
    if os.path.exists(output_file):
        return graphviz.Source.from_file(output_file)
    else:
        return None

def update_graph(existing_graph, books, book_edges):
    graph = existing_graph if existing_graph else graphviz.Digraph('Book_Graph')

    for book in books:
        graph.node(book['title'])

    for edge in book_edges:
        graph.edge(edge[0], edge[1])

    return graph

def main(input_file, output_file):
    books = load_books(input_file)
    book_edges = defaultdict(int)
    existing_graph = load_existing_graph(output_file)

    while True:
        book1, book2 = random.sample(books, 2)

        # Check if the pair has already been ranked
        if (book1['title'], book2['title']) in book_edges or (book2['title'], book1['title']) in book_edges:
            continue

        choice = user_choice(book1, book2)

        if choice == 1:
            book_edges[(book1['title'], book2['title'])] += 1
        elif choice == 2:
            book_edges[(book2['title'], book1['title'])] += 1
        else:
            print("Invalid choice. Please enter 1 or 2.")

        action = input("Enter 'g' to generate the graph or 'c' to continue choosing books: ").strip()

        if action.lower() == 'g':
            updated_graph = update_graph(existing_graph, books, book_edges)
            updated_graph.render(output_file, view=False)
            print(f"Graph generated as '{output_file}'. To render the graph, use the following command:\n")
            print(f"dot -Tpng {output_file} -o {output_file.split('.')[0]}.png")
        elif action.lower() == 'c':
            continue
        else:
            print("Invalid action. Please enter 'g' or 'c'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a directed graph from book choices.")
    parser.add_argument("input_file", help="CSV file containing book data with 'title' and 'author' columns.")
    parser.add_argument("output_file", help="Output file name for the generated Graphviz file.")
    args = parser.parse_args()

    if args.input_file and args.output_file:
        main(args.input_file, args.output_file)
    else:
        print("Usage: python book_graph.py <input_file> <output_file>")
```

The code has been updated to not show a pair to the user if the pair has already been ranked. Before presenting the book choices to the user, the code now checks if the selected book pair already has a direct edge between them. If the edge exists, the code skips the current iteration and continues with the next random book pair.

### User - 2023-04-15 20:53:11

Update main to extract methods with descriptive names. There should be minimal code in main

### Assistant - 2023-04-15 20:54:31

```python
import csv
import random
from collections import defaultdict
import graphviz
import sys
import argparse
import os

def load_books(file_path):
    books = []

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append({"title": row["title"], "author": row["author"]})

    return books

def user_choice(book1, book2):
    print(f"Choose a book:\n1. {book1['title']} by {book1['author']}\n2. {book2['title']} by {book2['author']}")
    choice = input("Enter 1 or 2: ").strip()
    return int(choice)

def load_existing_graph(output_file):
    if os.path.exists(output_file):
        return graphviz.Source.from_file(output_file)
    else:
        return None

def update_graph(existing_graph, books, book_edges):
    graph = existing_graph if existing_graph else graphviz.Digraph('Book_Graph')

    for book in books:
        graph.node(book['title'])

    for edge in book_edges:
        graph.edge(edge[0], edge[1])

    return graph

def get_unique_book_pair(books, book_edges):
    while True:
        book1, book2 = random.sample(books, 2)

        if (book1['title'], book2['title']) not in book_edges and (book2['title'], book1['title']) not in book_edges:
            return book1, book2

def prompt_user_to_choose_books(books, book_edges):
    book1, book2 = get_unique_book_pair(books, book_edges)
    choice = user_choice(book1, book2)

    if choice == 1:
        book_edges[(book1['title'], book2['title'])] += 1
    elif choice == 2:
        book_edges[(book2['title'], book1['title'])] += 1
    else:
        print("Invalid choice. Please enter 1 or 2.")

def generate_graph_or_continue(existing_graph, books, book_edges, output_file):
    action = input("Enter 'g' to generate the graph or 'c' to continue choosing books: ").strip()

    if action.lower() == 'g':
        updated_graph = update_graph(existing_graph, books, book_edges)
        updated_graph.render(output_file, view=False)
        print(f"Graph generated as '{output_file}'. To render the graph, use the following command:\n")
        print(f"dot -Tpng {output_file} -o {output_file.split('.')[0]}.png")
        return False
    elif action.lower() == 'c':
        return True
    else:
        print("Invalid action. Please enter 'g' or 'c'.")
        return True

def main(input_file, output_file):
    books = load_books(input_file)
    book_edges = defaultdict(int)
    existing_graph = load_existing_graph(output_file)

    continue_choosing = True

    while continue_choosing:
        prompt_user_to_choose_books(books, book_edges)
        continue_choosing = generate_graph_or_continue(existing_graph, books, book_edges, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a directed graph from book choices.")
    parser.add_argument("input_file", help="CSV file containing book data with 'title' and 'author' columns.")
    parser.add_argument("output_file", help="Output file name for the generated Graphviz file.")
    args = parser.parse_args()

    if args.input_file and args.output_file:
        main(args.input_file,

### User - 2023-04-15 20:54:33

Reorder the methods so they are in the order of use. 

### Assistant - 2023-04-15 20:55:21

```python
import csv
import random
from collections import defaultdict
import graphviz
import sys
import argparse
import os

def load_books(file_path):
    books = []

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            books.append({"title": row["title"], "author": row["author"]})

    return books

def load_existing_graph(output_file):
    if os.path.exists(output_file):
        return graphviz.Source.from_file(output_file)
    else:
        return None

def user_choice(book1, book2):
    print(f"Choose a book:\n1. {book1['title']} by {book1['author']}\n2. {book2['title']} by {book2['author']}")
    choice = input("Enter 1 or 2: ").strip()
    return int(choice)

def get_unique_book_pair(books, book_edges):
    while True:
        book1, book2 = random.sample(books, 2)

        if (book1['title'], book2['title']) not in book_edges and (book2['title'], book1['title']) not in book_edges:
            return book1, book2

def prompt_user_to_choose_books(books, book_edges):
    book1, book2 = get_unique_book_pair(books, book_edges)
    choice = user_choice(book1, book2)

    if choice == 1:
        book_edges[(book1['title'], book2['title'])] += 1
    elif choice == 2:
        book_edges[(book2['title'], book1['title'])] += 1
    else:
        print("Invalid choice. Please enter 1 or 2.")

def generate_graph_or

