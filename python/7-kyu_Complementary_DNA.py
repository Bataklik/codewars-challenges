import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

    If you want to know more: http://en.wikipedia.org/wiki/DNA

    In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

    More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

    Example: (input --> output)
    ```text
    "ATTGC" --> "TAACG"
    "GTAT" --> "CATA"
    ```

    **Used Resources:**
    """)
    return


@app.function
def DNA_strand(dna):
    complements= {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join([complements[e] for e in dna])


@app.cell
def _():
    print(DNA_strand("AAAA"),"TTTT","String AAAA is")
    print(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
    print(DNA_strand("GTAT"),"CATA","String GTAT is")
    return


if __name__ == "__main__":
    app.run()
