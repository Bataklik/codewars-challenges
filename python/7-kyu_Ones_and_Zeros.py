import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given an array of ones and zeroes, convert the equivalent binary value to an integer.

    Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

    Examples:
    ```text
    Testing: [0, 0, 0, 1] ==> 1
    Testing: [0, 0, 1, 0] ==> 2
    Testing: [0, 1, 0, 1] ==> 5
    Testing: [1, 0, 0, 1] ==> 9
    Testing: [0, 0, 1, 0] ==> 2
    Testing: [0, 1, 1, 0] ==> 6
    Testing: [1, 1, 1, 1] ==> 15
    Testing: [1, 0, 1, 1] ==> 11
    ```
    However, the arrays can have varying lengths, not just limited to 4.
    """)
    return


@app.function
def binary_array_to_number(arr):
    result = 0
    for i,e in enumerate(reversed(arr)):
        result += pow(2,i) if e == 1 else 0
    return result


@app.cell
def _():
    print(binary_array_to_number([0,0,0,1]), 1)
    print(binary_array_to_number([0,0,1,0]), 2)
    print(binary_array_to_number([1,1,1,1]), 15)
    print(binary_array_to_number([0,1,1,0]), 6)
    return


if __name__ == "__main__":
    app.run()
