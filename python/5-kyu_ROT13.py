import marimo

__generated_with = "0.23.3"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    How can you tell an extrovert from an introvert at NSA?
    Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

    I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
    According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

    For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

    Test examples:
    ```text
    "EBG13 rknzcyr." -> "ROT13 example."

    "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

    **Used Resources:**
    - https://en.wikipedia.org/wiki/ROT13
    - https://www.geeksforgeeks.org/python/python-check-given-key-already-exists-in-a-dictionary/
    - https://www.geeksforgeeks.org/python/string-punctuation-in-python/
    - https://www.w3schools.com/python/ref_string_lower.asp
    - https://www.w3schools.com/python/ref_string_isalpha.asp
    """)
    return


@app.cell
def _():
    import re

    UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    def rot13_encode(letter_position:int,isUpper:bool):
        ROT13 = 13
        MAX = 26
        rot13_index = letter_position + ROT13
        if (rot13_index <= 25): return UPPER_ALPHABET[rot13_index] if isUpper else LOWER_ALPHABET[rot13_index]
        rot13_index -= MAX
        return UPPER_ALPHABET[rot13_index] if isUpper else LOWER_ALPHABET[rot13_index]

    def rot13(message):
        #your code here

        result = ""
        for letter in message:
            if letter.isalpha():
                letter_index = LOWER_ALPHABET.index(letter.lower())
                result += rot13_encode(letter_index, letter.isupper())
            else:
                result += letter
        return result

    print(rot13("o[[o0mTf:'&"))
    return (rot13,)


@app.cell
def _(rot13):
    print(rot13("EBG13 rknzcyr."), "ROT13 example.")
    print(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."), "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
    print(rot13("123"), "123")
    print(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"), "This is actually the first kata I ever made. Thanks for finishing it! :)")
    print(rot13('@[`{"'), '"@[`{')
    print(rot13(']e)    r~~FH?C%U~@"`J}'))
    return


if __name__ == "__main__":
    app.run()
