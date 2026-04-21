import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

    Your task is to write a function maskify, which changes all but the last four characters into '#'.

    Examples (input --> output):
    ```text
    "4556364607935616" --> "############5616"
         "64607935616" -->      "#######5616"
                   "1" -->                "1"
                    "\" -->                 "\"
    ```
    // "What was the name of your first pet?"
    ```text
    "Skippy" --> "##ippy"
    "Nananananananananananananananana Batman!" --> "####################################man!"
    ```

    **Used Resources:**
    - https://stackoverflow.com/a/663175
    - https://stackoverflow.com/a/12723785
    - https://medium.com/@andrewdass/python-how-to-make-and-use-single-line-for-loops-3dbadb2ab811
    """)
    return


@app.function
def maskify(cc):
    if len(cc) <= 4:
        return cc
    left = ["#" for x in range(len(cc)-4)]
    return "".join(left) + cc[-4:]


@app.cell
def _():
    print(maskify("4556364607935616"),"############5616")
    print(maskify("64607935616"),"#######5616")
    print(maskify("1"),"1")
    print(maskify(""), "")
    return


if __name__ == "__main__":
    app.run()
