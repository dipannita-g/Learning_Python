import pandas
import datetime as dt
import smtplib
import random

MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "example_password"

now = dt.datetime.now()
current_month = now.month
current_date = now.day

date_file=  pandas.read_csv("birthdays.csv")
birthday_list = date_file.to_dict(orient="records")

letter_to_use = f"letter_templates/letter_{random.randint(1,3)}.txt"

for record in birthday_list:

    if record["month"] == current_month and record["day"] == current_date:

        with open(letter_to_use, "r") as template:

            new_letter = template.read()
            new_letter = new_letter.replace("[NAME]", record["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login(user=MY_EMAIL, password=MY_PASSWORD)
            server.sendmail(
                from_addr= MY_EMAIL,
                to_addrs= record["email"],
                msg=f"Subject: Happy Birthday\n\n{new_letter}"
            )
