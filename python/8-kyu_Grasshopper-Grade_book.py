import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Grade book
    Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

    Numerical Score	Letter Grade<br/>
    90 <= score <= 100	'A'<br/>
    80 <= score < 90	'B'<br/>
    70 <= score < 80	'C'<br/>
    60 <= score < 70	'D'<br/>
    0 <= score < 60	'F'<br/>
    Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

    **Used Resources:**
    """)
    return


@app.function
def get_grade(s1, s2, s3):
    score_avg = (s1 + s2 + s3) / 3
    if score_avg >= 90 and score_avg <= 100:
        return "A"
    if score_avg >= 80 and score_avg < 90:
        return "B"
    if score_avg >= 70 and score_avg < 80:
        return "C"
    if score_avg >= 60 and score_avg < 70:
        return "D"
    return "F"


@app.cell
def _():
    print(get_grade(95, 90, 93), "| A", "get_grade(95, 90, 93)")
    print(get_grade(70, 85, 93), "| B", "get_grade(70, 85, 93)")
    print(get_grade(70, 70, 70), "| C", "get_grade(70, 70, 70)")
    print(get_grade(65, 70, 59), "| D", "get_grade(65, 70, 59)")
    print(get_grade(44, 55, 52), "| F", "get_grade(44, 55, 52)")
    return


if __name__ == "__main__":
    app.run()
