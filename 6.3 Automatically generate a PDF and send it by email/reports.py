#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie



def generate(filename, title, additional_info, table_data: list):
    """Generate a PDF."""
    # Style
    styles = getSampleStyleSheet()
    # File
    report = SimpleDocTemplate(filename)
    # Contents
    report_title = Paragraph(text=title, style=styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])

    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
    
    # Process data
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

    empty_line = Spacer(1,20)

    # report_pie = Pie()
    # report_pie.x = 150
    # report_pie.y = 30
    # report_pie.sideLabels = True
    # report_pie.data = []
    # report_pie.labels = []

    # for fruit_name in sorted(fruit):
    #     report_pie.data.append(fruit[fruit_name])
    #     report_pie.labels.append(fruit_name)

    # report_chart = Drawing()
    # report_chart.add(report_pie)

    # Build PDF
    report.build([report_title, empty_line, report_info, empty_line, report_table])


if __name__ == "__main__":
    fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
    }

    table_data = []

    for k, v in fruit.items():
        table_data.append([k, v])

    generate("report.pdf", "A Complete Inventory of My Fruit", "This is all my fruit", table_data)