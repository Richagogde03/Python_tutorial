import re


def extract_dates(text):
    pattern = r"\b([\d]{2}[-/][\d]{2}[-/][\d]{4})\b"
    dates = re.findall(pattern, text)

    return dates


print(extract_dates("""Yesterday we discussed that the meaatin will be on
                    31/12/2025 but it is rescheduled to 05/01/2026"""))
