# Syntax Highlighter for Python files

# Santiago Benitez Perez - A01782813


defmodule SyntaxHighlighter do

    @doc """
      Function to find a match at the beginning of the line passed to it.

      The function tries every regular expression against the line passed to it in order to find a match at the beginning of the line.

      If there is a match at the beginning of the line, it reaches the base case where the token found is processed as a html <span> element and the match found is removed from the line. The result is then received by the caller of this function using pattern matching.

      If there is no match at the beginning of the line with the current regular expression, the next regular expression tries to make a match against the beginning of the line.

    """

    def highlight_token(line), do: do_highlight_token([
      whitespace: ~r/^\s+/, #whitespace
      comment: ~r/^#.*/, #comments
      keyword: ~r/^\b(None|True|False|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|print|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b/, #reserved keywords
      built_in_function: ~r/^\b(abs|aiter|all|any|anext|ascii|append|pop|bin|bool|breakpoint|bytearray|bytes|callable|chr|classmethod|compile|complex|delattr|dict|dir|divmod|enumerate|eval|exec|filter|float|format|frozenset|getattr|globals|hasattr|hash|help|hex|id|input|int|isinstance|issubclass|iter|len|list|locals|map|max|memoryview|min|next|object|oct|open|ord|pow|print|property|range|repr|remove|reversed|round|set|seattr|slice|sorted|staticmethod|str|sum|super|tuple|type|vars|zip)\b/, # built in functions
      number: ~r/^[+|-]{0,1}\d+(\.\d+)?/, #numbers
      identifier: ~r/^[\w][\w]*/, #identifiers
      string: ~r/^(['"]).*\1/, #strings
      delimiter: ~r/^[()\[\]{},:.`=;]/, #delimiters
      operator: ~r/^\*\*|\*|%|@|<<|>>|&|\||\^|~|:=|<|>|<=|>=|==|!=|\+=|=|\*=|-=|\/\/=|\/=|%=|@=|&=|\|=|\^=|>>=|<<=|\*\=|\/\/|\/|\+|\-|/ #operators
    ], line, [])

    defp do_highlight_token(_matches, _line, result) when length(result) != 0, do: result # case where match was found

    defp do_highlight_token(matches, line, result) do # function that tries to match the beginning of the line with a regular expression
      [{token_type, regex} | tail] = matches
      if Regex.match?(regex, line) do

        [match | _] = Regex.run(regex, line)

        if token_type == :whitespace do # if a whitespace token is found, do not process it as a html <span> element
          do_highlight_token(matches, line, [match, String.replace_leading(line, match, "")])
        else
          do_highlight_token(matches, line, ["<span class=\"#{token_type}\">#{match}</span>", String.replace_leading(line, match, "")])  # if there is a match, process the token found and remove the match found from the line
        end

      else
        do_highlight_token(tail, line, result) # if no match was found with the current regex, try the next one
      end
    end

     @doc """
      Function that processes a line with the tokens found by calling the function `highlight_token`

    """

    def highlight_line(line) do
      if line == "" do  # base case when the line is empty
        ""
      else
        [processedToken, tail] = line # pattern matching to receive the token found and the new line (tail) to process
        |> highlight_token() # function that finds a match at the beginning of the line
        processedToken <> highlight_line(tail)
      end
    end

    @doc """
      Function that processes every line of a python file with the tokens found by calling the function `highlight_line`

    """

    def highlight_file({in_filename, out_filename}) do # function that receives the python file to highlight and the output html file
          data = in_filename
                |> File.stream!()
                |> Enum.map(&highlight_line/1)
                |> Enum.join("")
          File.write(out_filename, to_html(data))
    end


    # sequential version
    def highlight_files(in_directory) do
      "#{in_directory}/**/*.py"
        |> Path.wildcard()
        |> make_tuples()
        |> Enum.map(&highlight_file/1)
    end


    #parallel version
    def highlight_files_parallel(in_directory) do
      "#{in_directory}/**/*.py"
        |> Path.wildcard()
        |> make_tuples()
        |> Enum.map(&Task.async(fn -> highlight_file(&1) end))
        |> Enum.map(&Task.await(&1))
    end

    def make_tuples(files), do: do_make_tuples(files, 1, [])

    defp do_make_tuples([], _i, res), do: Enum.reverse(res)

    defp do_make_tuples([head | tail], i, res), do: do_make_tuples(tail, i + 1,  [{head, "out_file#{i}.html"} | res])

    defp to_html(code) do # function to generate a html format document
      "<html lang=\"en\">
        <head>
          <meta charset=\"UTF-8\">
          <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
          <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
          <link rel=\"stylesheet\" href=\"./style.css\">
          <title>Syntax Highlighter</title>
        </head>
        <body>
          <pre>
            <code>
              #{code}
            </code>
          </pre>
        </body>
      </html>"
    end

end
