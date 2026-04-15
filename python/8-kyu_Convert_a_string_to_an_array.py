import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function to split a string and convert it into an array of words.

    **Examples (Input ==> Output):**
    ```text
    "Robin Singh" ==> ["Robin", "Singh"]
    "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
    ```
    """)
    return


@app.function
def string_to_array(s):
    if s == "": return [""]
    return s.split()


@app.cell
def _():
    print(string_to_array("Robin Singh")," | ", ["Robin", "Singh"])
    print(string_to_array("CodeWars")," | ", ["CodeWars"])
    print(string_to_array("I love arrays they are my favorite")," | ", ["I", "love", "arrays", "they", "are", "my", "favorite"])
    print(string_to_array("1 2 3")," | ", ["1", "2", "3"])
    print(string_to_array("")," | ", [""])
    return


if __name__ == "__main__":
    app.run()
