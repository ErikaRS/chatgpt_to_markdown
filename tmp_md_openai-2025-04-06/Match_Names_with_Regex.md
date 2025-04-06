# Match Names with Regex

Created: 2023-09-22 08:59:03
Last Updated: 2023-09-22 08:59:03

### User - 2023-09-22 08:59:03

Regular expression that matches Eric, Erik, Erika, Erica

### Assistant - 2023-09-22 08:59:19

The regular expression that matches the names "Eric", "Erik", "Erika", and "Erica" is:

\[
\texttt{^Eri(c|k)(a?)$}
\]

Here's a breakdown of the regex:

1. `^` - asserts the start of a line.
2. `Eri` - matches the common prefix of the names.
3. `(c|k)` - matches either "c" or "k".
4. `(a?)` - matches zero or one occurrence of "a".
5. `$` - asserts the end of a line.

This regex ensures that only the specified names are matched in their entirety.

