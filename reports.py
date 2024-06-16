#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

import os

from run import get_desc


def generate_report(filename, title, paragraph = None):
    """Generate a PDF report."""

    # Style
    styles = getSampleStyleSheet()
    # File
    report = SimpleDocTemplate(filename)

    # Contents
    empty_line = Spacer(1,20)
    report_title = Paragraph(text=title, style=styles["h1"])
    item_list = [report_title, empty_line]
    if paragraph:
        for pair in paragraph:
            name, weight = pair.split(",")
            item_list.append(Paragraph(text=name, style=styles["BodyText"]))
            item_list.append(Paragraph(text=weight, style=styles["BodyText"]))
            item_list.append(empty_line)
    
    # Build PDF
    report.build(item_list)