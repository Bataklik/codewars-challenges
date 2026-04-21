import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

    For example (Input --> Output):
    ```text
    39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
    999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
    4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
    ```

    **Used Resources:**
    - https://stackoverflow.com/a/47927295
    - https://www.geeksforgeeks.org/python/reduce-in-python/
    """)
    return


@app.cell
def _():
    from functools import reduce
    import operator

    def persistence(n):
        if n < 10: return 0
        i = 0
        while (n >= 10):
            temp = list(map(int,str(n)))
            n:int = reduce(operator.mul, temp)
            i+= 1
        return i

    return (persistence,)


@app.cell
def _(persistence):
    print(persistence(39), 3)
    print(persistence(4), 0)
    print(persistence(25), 2)
    print(persistence(999), 4)
    return


if __name__ == "__main__":
    app.run()
