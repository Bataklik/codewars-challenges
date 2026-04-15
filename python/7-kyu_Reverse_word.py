import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

    **Examples:**
    ```text
    "This is an example!" ==> "sihT si na !elpmaxe"
    "double  spaces"      ==> "elbuod  secaps"
    ```
    ** Used Resources:**
    - https://stackoverflow.com/a/4978792
    """)
    return


@app.function
def reverse_words(text):
    text = "".join(reversed(list(text))).split(" ")
    return " ".join(reversed(text))


@app.cell
def _():
    print(reverse_words("This is an example!"))
    print(reverse_words("double  spaces"))
    return


if __name__ == "__main__":
    app.run()
