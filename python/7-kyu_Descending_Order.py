import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

    **Examples:**
    ```text
    Input: 42145 Output: 54421
    Input: 145263 Output: 654321
    Input: 123456789 Output: 987654321
    ```

    **Used Resources:**
    - https://www.geeksforgeeks.org/python/python-convert-number-to-list-of-integers/
    - [Classisc Computer algoritme course: Bsearch](https://bataklik.notion.site/1-Zoeken-en-sorteren-dc422f01c4c7483491444839ff90762b?pvs=74)
    - https://www.w3schools.com/python/ref_string_join.asp
    """)
    return


@app.cell
def _():
    def descending_order(num:int):
        num_list = list(map(int,str(num)))
        return descending(num_list)
    def descending(a):
        n = len(a)-1
        descending_recursive(a,0,n)
    def descending_recursive(a,left,right):
        if left < right:
            middle = (left + right) // 2
            descending_recursive(a,left,middle)
            descending_recursive(a, middle+1, right)
            merge(a,left, middle, right)
    def merge(a,left,middle,right):
        pass

    return (descending_order,)


@app.cell
def _(descending_order):
    print(descending_order(42145))
    return


@app.cell
def _():
    def descending_order_b(num:int):
        nums = list(map(int,str(num)))
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    nums[i],nums[j] = nums[j],nums[i]
        return int("".join(map(str,nums)))
    print(descending_order_b(42145))
    return


if __name__ == "__main__":
    app.run()
