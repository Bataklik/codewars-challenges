import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

    Note: no empty arrays will be given.

    ```python
    Examples
    [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
    [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
    [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
    ```

    **Used Resources:**
    - https://medium.com/@atatus/https-www-atatus-com-blog-python-converting-lsts-to-dictionaries-c3f038a8ce30
    """)
    return


@app.cell
def _():
    from collections import Counter
    def highest_rank(arr):
        most_frequent = None
        ranks_amount:dict= dict(Counter(arr))
        highest = max(ranks_amount.items(), key=lambda item: (item[1], item[0]))
        return highest

    return (highest_rank,)


@app.cell
def _(highest_rank):
    print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]),12)
    print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]), 12)
    print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]),3)

    return


if __name__ == "__main__":
    app.run()
