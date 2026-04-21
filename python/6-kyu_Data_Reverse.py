import marimo

__generated_with = "0.23.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A stream of data is received and needs to be reversed.

    Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
    ```text
    11111111  00000000  00001111  10101010
     (byte1)   (byte2)   (byte3)   (byte4)
    ```
    should become:
    ```text
    10101010  00001111  00000000  11111111
     (byte4)   (byte3)   (byte2)   (byte1)
    ```
    The total number of bits will always be a multiple of 8.

    The data is given in an array as such:
    ```text
    [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
    ```
    Note: In the C and NASM languages you are given the third parameter which is the number of segment blocks.

    **Used Resources:**
    - https://www.geeksforgeeks.org/python/break-list-chunks-size-n-python/
    - https://stackoverflow.com/questions/6771428/most-efficient-way-to-reverse-a-numpy-array
    - https://www.geeksforgeeks.org/python/flatten-a-list-of-lists-in-python/
    """)
    return


@app.function
def data_reverse(data):
    result = []
    i = len(data)
    while (len(result) != len(data)):
        result.extend(data[i-8:i])
        i = i - 8
    return result


@app.cell
def _():
    data1 = [1,1,1,1,1,1,1,1,  0,0,0,0,0,0,0,0,    0,0,0,0,1,1,1,1,  1,0,1,0,1,0,1,0]
    data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
    print(data_reverse(data1),"\n",data2)
    print("----")
    data3 = [0,0,1,1,0,1,1,0,   0,0,1,0,1,0,0,1]
    data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
    print(data_reverse(data3),data4)
    return


if __name__ == "__main__":
    app.run()
