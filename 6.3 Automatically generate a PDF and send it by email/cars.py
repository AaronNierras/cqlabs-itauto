#!/usr/bin/env python3


import json
import locale
import sys

import reports
import emails


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

    Returns a list of lines that summarize the information.
    """
    max_revenue = {"revenue": 0}
    model_sales = {}
    max_sales = {"total": 0}
    sales_year = {}
    max_year = {"total": 0}
    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item

        # TODO: also handle max sales
        car = format_car(item["car"]) #item["car"]["car_model"]
        sales = item["total_sales"]
        if car not in model_sales:
            model_sales[car] = 0
        model_sales[car] += sales

        # TODO: also handle most popular car_year
        year = item["car"]["car_year"]
        if year not in sales_year:
            sales_year[year] = 0
        sales_year[year] += sales
    
    # print(model_sales, sales_year)

    for car, total in model_sales.items():
        # print(car, total)
        # if car == "Acura Integra (1995)":
        #     print(">>>", car, total)
        if total > max_sales["total"]:
            max_sales["car"] = car
            max_sales["total"] = total
            # print(">>>", max_sales)
    
    for year, total in sales_year.items():
        if total > max_year["total"]:
            max_year["year"] = year
            max_year["total"] = total

    summary = [
    "The {} generated the most revenue: ${}".format(format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(max_sales["car"], max_sales["total"]),
    "The most popular year was {} with {} sales.".format(max_year["year"], max_year["total"])
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("car_sales.json")
    summary = process_data(data)
    summary_text = "\n".join(summary)
    print(summary)

    # TODO: turn this into a PDF report
    reports.generate("/tmp/cars.pdf", "Sales summary for last month", summary_text, cars_dict_to_table(data))

    # TODO: send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "student@example.com" #"{}@example.com".format(os.environ.get('USER'))
    subject = "TEST Sales summary for last month"
    body = summary_text

    message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")

    emails.send(message)

if __name__ == "__main__":
    main(sys.argv)