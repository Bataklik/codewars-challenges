import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Count the number of Duplicates
    Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

    Example
    ```text
    "abcde" -> 0 # no characters repeats more than once
    "aabbcde" -> 2 # 'a' and 'b'
    "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
    "indivisibility" -> 1 # 'i' occurs six times
    "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
    "aA11" -> 2 # 'a' and '1'
    "ABBA" -> 2 # 'A' and 'B' each occur twice
    ```

    **Used Resources:**
    - https://stackoverflow.com/a/40950955
    """)
    return


@app.function
def duplicate_count(text):
    duplicates = 0
    dict_text = {e:text.lower().count(e) for e in set(text.lower())}
    print(dict_text)
    for letter, count in zip (dict_text.keys(),dict_text.values()):
        if count > 1:
            duplicates = duplicates + 1
    return duplicates


@app.cell
def _():
    print(duplicate_count(""),        0, 'duplicate_count("")'       )
    print(duplicate_count("abcde"),   0, 'duplicate_count("abcde")'  )
    print(duplicate_count("abcdeaa"), 1, 'duplicate_count("abcdeaa")')
    print(duplicate_count("abcdeaB"), 2, 'duplicate_count("abcdeaB")')
    print(duplicate_count("Indivisibilities"), 2, 'duplicate_count("Indivisibilities")')

    return


if __name__ == "__main__":
    app.run()
