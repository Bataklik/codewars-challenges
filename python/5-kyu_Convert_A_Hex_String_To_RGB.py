import marimo

__generated_with = "0.23.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component values for a color. Implement a function that meets these requirements:

    Accepts a case-insensitive hexadecimal color string as its parameter (ex. `"#FF9933"` or `"#ff9933"`)
    Returns a Map<String, int> with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255
    Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")

    Example
    ```text
    "#FF9933" --> {r: 255, g: 153, b: 51}
    ```

    **Used Resources:**
    - https://www.tutorialspoint.com/article/split-string-of-size-n-in-python
    - https://stackoverflow.com/questions/56574309/create-a-mapping-of-elements-from-two-arrays
    """)
    return


@app.function
def hex_string_to_RGB(hex_string):
    # your code here
    rgb_arr = ["r","g","b"]
    hex_arr =[int(hex_string[index: index + 2],16) for index in range(1,len(hex_string),2)]
    return dict(zip(rgb_arr,hex_arr))


@app.cell
def _():
    print(hex_string_to_RGB("#FF9933"), {'r':255, 'g':153, 'b':51})
    print(hex_string_to_RGB("#beaded"), {'r':190, 'g':173, 'b':237})
    print(hex_string_to_RGB("#000000"), {'r':0, 'g':0, 'b':0})
    print(hex_string_to_RGB("#111111"), {'r':17, 'g':17, 'b':17})
    print(hex_string_to_RGB("#Fa3456"), {'r':250, 'g':52, 'b':86})
    return


if __name__ == "__main__":
    app.run()
