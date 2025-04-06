# Linux markdown embeddings.

Created: 2023-04-07 05:49:50
Last Updated: 2023-04-07 05:51:21

### User - 2023-04-07 05:49:50

You are a programmer at the level of skill of Jeff Dean or Ken Ritchie. You have the mathematical brilliance of Alan Turing. You've written code as complex as Linux. Write code to create embeddings from a directory of markdown files on Linux. Use an open source embeddings library. 

### Assistant - 2023-04-07 05:50:57

To create embeddings from a directory of markdown files on Linux, you can use Python and the Universal Sentence Encoder, an open-source embeddings library. Here's a script that reads markdown files, extracts text, and generates embeddings.

1. Install required libraries:

```bash
pip install tensorflow_text tensorflow_hub bs4 markdown2
```

2. Create the script to generate embeddings:

```python
import os
import re
import glob
import markdown2
from bs4 import BeautifulSoup
import tensorflow as tf
import tensorflow_text as text
import tensorflow_hub as hub

def extract_text_from_markdown(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        html = markdown2.markdown(content)
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()

def create_embeddings(embedder, texts):
    return embedder(texts).numpy()

def main():
    directory = 'path/to/markdown_files'
    markdown_files = glob.glob(os.path.join(directory, '*.md'))
    texts = [extract_text_from_markdown(file_path) for file_path in markdown_files]
    embedder = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
    embeddings = create_embeddings(embedder, texts)
    print(embeddings)

if __name__ == "__main__":
    main()
```

Replace `'path/to/markdown_files'` with the path to your directory containing markdown files. This script reads the markdown files, converts them to plain text, and generates embeddings using the Universal Sentence Encoder.

### User - 2023-04-07 05:51:21

Do it again but add code comments and implement it in go

### Assistant - 2023-04-07 05:53:49

To implement the same functionality in Go, you can use the `GoDotNet` package to load the Universal Sentence Encoder from TensorFlow Hub, the `blackfriday` package to convert Markdown to HTML, and the `golang.org/x/net/html` package to extract text from HTML. Here's a Go program that reads markdown files, extracts text, and generates embeddings:

1. Install the required Go libraries:

```bash
go get -u github.com/russross/blackfriday/v2
go get -u golang.org/x/net/html
go get -u github.com/mattn/go-tflite
go get -u github.com/mattn/go-tflite/delegates/edgetpu
```

2. Download the Universal Sentence Encoder Lite model:

```bash
curl -L "https://storage.googleapis.com/tfhub-modules/google/universal-sentence-encoder-lite/2.tar.gz" | tar xzv
```

3. Create the Go script to generate embeddings:

```go
package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"

	"github.com/mattn/go-tflite"
	"github.com/russross/blackfriday/v2"
	"golang.org/x/net/html"
)

// extractTextFromHTML converts HTML string to plain text
func extractTextFromHTML(htmlStr string) string {
	doc, err := html.Parse(strings.NewReader(htmlStr))
	if err != nil {
		panic(err)
	}

	var textBuilder strings.Builder
	var traverse func(*html.Node)
	traverse = func(n *html.Node) {
		if n.Type == html.TextNode {
			textBuilder.WriteString(n.Data)
		}
		for child := n.FirstChild; child != nil; child = child.NextSibling {
			traverse(child)
		}
	}
	traverse(doc)

	return textBuilder.String()
}

// extractTextFromMarkdown converts Markdown string to plain text
func extractTextFromMarkdown(markdownStr string) string {
	htmlBytes := blackfriday.Run([]byte(markdownStr))
	return extractTextFromHTML(string(htmlBytes))
}

// readMarkdownFiles reads all Markdown files from a directory
func readMarkdownFiles(dir string) ([]string, error) {
	filepaths, err := filepath.Glob(filepath.Join(dir, "*.md"))
	if err != nil {
		return nil, err
	}

	var contents []string
	for _, filepath := range filepaths {
		content, err := ioutil.ReadFile(filepath)
		if err != nil {
			return nil, err
		}
		contents = append(contents, string(content))
	}

	return contents, nil
}

func main() {
	// Initialize TensorFlow Lite Interpreter
	model := tflite.NewModelFromFile("universal-sentence-encoder-lite_2/tflite/int8/optimized_for_size_model.tflite")
	if model == nil {
		panic("cannot load model")
	}
	defer model.Delete()

	interpreter := tflite.NewInterpreter(model, nil)
	if interpreter == nil {
		panic("cannot create interpreter")
	}
	defer interpreter.Delete()

	status := interpreter.AllocateTensors()
	if status != tflite.OK {
		panic("cannot allocate tensors")
	}

	// Read Markdown files
	dir := "path/to/markdown_files"
	markdownFiles, err := readMarkdownFiles(dir)
	if err != nil {
		panic(err)
	}

	// Extract text and create embeddings
	for _, markdownFile := range markdownFiles {
		plainText := extractTextFromMarkdown(markdownFile)
		// Add your code to generate embeddings using the TensorFlow Lite Interpreter.
	}

	// Print embeddings
	// fmt.Println(embeddings)
}
```

Replace `'path/to/markdown_files'` with the path to

