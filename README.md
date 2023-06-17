# Python Syntax Highlighter

This program implements a syntax highlighter for Python programs using regular expressions. Its main function is to take a Python file as input, highlight the different lexical categories the programming language: comments, keywords, identifiers, operators, delimiters, numbers, strings, built-in functions and generate an HTML file that displays the highlighted code.

## Algorithm

The algorithm used by the program is as follows:

1. Iterate over each line of the Python file recursively.
2. For each line, call the `highlight_line` function to process it with the tokens found.
3. The `highlight_line` function, in turn, calls the `highlight_token` function to process each token that is matched at the beginning of the line and generate a `<span></span>` html element with a class of the type of token found and the actual token.
4. The final result is stored and appended as each line is processed.

## Algorithm Complexity

The complexity of the algorithm depends on the number of tokens and lines in the Python file. In the worst case scenario, if there are `n` lines and `m` tokens in each line, the complexity would be `O(n * m)`. However, the complexity also depends on the performance of regular expression matching and string manipulation operations in the underlying programming language implementation.

## Efficiency and Performance

Regular expressions are a powerful tool for pattern matching in text. However, if the Python file is very large or contains a large number of tokens, the intensive use of regular expressions may impact the program's performance. In such cases, alternative approaches, such as more advanced lexical and grammatical analysis, could be considered for improved efficiency.

## Ethical Implications

The greatest ethical implication I could find was that Regular expressions can be effective in many cases, but they may not accurately address all possible variations of tokens in the code. For instance, I am well aware that even though I tried to cover as many lexical categories as possible, it could be that the language adds new ones or that I missed some. If the syntax highlighter relies solely on regex, there is a risk of false positives or negatives, which could lead to an inaccurate representation of the code. This can be problematic if developers blindly rely on the syntax highlighter and make decisions based on a misinterpretation of their code.

## Usage

To run an Elixir script file (`.exs`) from the terminal, follow these steps:

1. Make sure you have Elixir installed on your system. You can check the installation by running the following command:

   ```shell
   elixir --version
   ```

   If Elixir is not installed, you can download and install it from the [official Elixir website](https://elixir-lang.org/).

2. Clone this repository in a directory.

2. Open your terminal or command prompt.

3. Navigate to the directory where you cloned this repository. 

4. Once you are in the correct directory, run the Elixir script file using the `elixir syntax-highlighter.exs` or `iex syntax-highlighter.exs` command. 

5. Run the program by executing the following:

```
SyntaxHighlighter.highlight_file("./in_file1.py", "./out_file.html")
```

6. You can try the program with the different .py files that are in the repository.
