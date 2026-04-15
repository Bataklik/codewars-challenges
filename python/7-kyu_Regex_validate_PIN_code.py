import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - https://stackoverflow.com/a/42674849
    - https://stackoverflow.com/a/12011808
    - https://stackoverflow.com/questions/7864971/regular-expression-for-number-with-length-of-4-5-or-6#comment87032574_7864983
    - https://stackoverflow.com/a/9347456
    """)
    return


@app.cell
def _():
    import marimo as mo
    import re

    return mo, re


@app.cell
def _(re):
    def validate_pin(pin):
        # Check if empty
        if pin == "" or pin is None: return False
        # Replace '\n' to '-'
        pin = pin.replace('\n','-')
        # Check regex in pin
        regex = "^(\d{4}|\d{6})?$"
        return re.search(regex,pin) != None if True else False

    return (validate_pin,)


@app.cell
def _(validate_pin):
    # "1234"   -->  true
    # "12345"  -->  false
    # "a234"   -->  false

    print(validate_pin("1234"))
    print(validate_pin("123456"))
    print(validate_pin("a234"))
    return


if __name__ == "__main__":
    app.run()
