import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

    Additionally, if the number is negative, return 0.

    Note: If a number is a multiple of both 3 and 5, only count it once.

    Courtesy of projecteuler.net (Problem 1)

    **Used Resources:**

    3, 5, 9 , 10, 12, 15, 16, 18, 20, 21, ...
    """)
    return


@app.cell
def _():
    result = []
    for i in range(3,16):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)
    result

    return


@app.function
def solution(number):
    sol_sum = 0
    if number < 0: return 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sol_sum += i
    return sol_sum


@app.cell
def _():
    print(solution(4), 3)
    print(solution(6), 8)
    print(solution(16), 60)
    print(solution(3), 0)
    print(solution(5), 3)
    print(solution(15), 45)
    print(solution(0), 0)
    print(solution(10), 23)
    print(solution(20), 78)

    return


if __name__ == "__main__":
    app.run()
