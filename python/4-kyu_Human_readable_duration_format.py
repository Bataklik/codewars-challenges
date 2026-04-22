import marimo

__generated_with = "0.23.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

    The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

    It is much easier to understand with an example:

    * For seconds = 62, your function should return
        "1 minute and 2 seconds"
    * For seconds = 3662, your function should return
        "1 hour, 1 minute and 2 seconds"
    For the purpose of this Kata, a year is 365 days and a day is 24 hours.

    Note that spaces are important.

    Detailed rules

    The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

    The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

    A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

    Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

    A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

    A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.


    **Used Resources:**
    - https://ai.thestempedia.com/python-function/math-ceil/#:~:text=In%20Python%2C%20the%20math.,greater%20than%20the%20number%20itself.
    """)
    return


@app.cell
def _():

    import math


    def format_duration(seconds:float):
        WEEK = 604800
        DAY = 86400
        HOUR = 3600
        MINUTE = 60
        MONTH = 2.628e+6
        YEAR = 3.154e+7

        current_seconds = seconds

        def get_time(current_seconds,time):
            result = 0
            if current_seconds >= time:
                result = (current_seconds // time)
                current_seconds = round(current_seconds - (result * time),2)
            return (current_seconds,result)

        def create_stringformat():
            result_string = ""
            if jaar > 1:
                result_string +=f"{int(jaar)} years, "
            elif jaar == 1:
                result_string +=f"{int(jaar)} year, "

            if dag > 1:
                result_string +=f"{int(dag)} days, "
            elif dag == 1:
                result_string +=f"{int(dag)} day, "

            if uur > 1:
                result_string +=f"{int(uur)} hours, "
            elif dag == 1:
                result_string +=f"{int(uur)} hour, "

            if minuten > 1:
                result_string +=f"{int(minuten)} minutes "
            elif dag == 1:
                result_string +=f"{int(minuten)} minute "

            if current_seconds > 1:
                result_string +=f"and {int(current_seconds)} seconds"
            elif dag == 1:
                result_string +=f"and {int(current_seconds)} second "
            return result_string

        current_seconds,jaar = get_time(current_seconds,YEAR)
        current_seconds,dag = get_time(current_seconds,DAY)
        current_seconds,uur = get_time(current_seconds,HOUR)
        current_seconds,minuten = get_time(current_seconds,MINUTE)

        #? String maken

        return create_stringformat()

    return (format_duration,)


@app.cell
def _(format_duration):
    print(format_duration(0), "| now")
    print(format_duration(1), "| 1 second")
    print(format_duration(62), "| 1 minute and 2 seconds")
    print(format_duration(120), "| 2 minutes")
    print(format_duration(3600), "|1 hour")
    print(format_duration(3662), "| 1 hour, 1 minute and 2 seconds")
    print(format_duration(15731080), "| 182 days, 1 hour, 44 minutes and 40 seconds")
    print(format_duration(132030240), "4 years, 68 days, 3 hours and 4 minutes")
    print(format_duration(205851834), "6 years, 192 days, 13 hours, 3 minutes and 54 seconds")
    print(format_duration(253374061), "8 years, 12 days, 13 hours, 41 minutes and 1 second")
    print(format_duration(242062374), "7 years, 246 days, 15 hours, 32 minutes and 54 seconds")
    print(format_duration(101956166), "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")
    print(format_duration(33243586), "1 year, 19 days, 18 hours, 19 minutes and 46 seconds")

    return


if __name__ == "__main__":
    app.run()
