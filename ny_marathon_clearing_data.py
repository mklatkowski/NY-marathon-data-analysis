import pandas as pd
import csv
import re

with open("runners_data.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)

    for row in rows[1:]:
        if isinstance(row[7], str):
            row[7] = row[7].replace(",", "")
        if row[0] == "Anonymous":
            rows.remove(row)
        if row[2] == "X":
            rows.remove(row)
        try:
            if int(row[3])>75:
                rows.remove(row)
        except ValueError: continue

    data = pd.DataFrame(rows[1:], columns=rows[0])

    country_counts = data[' Country'].value_counts()
    selected_countries = country_counts[country_counts >= 50].index
    filtered_data = data[data[' Country'].isin(selected_countries)]

    with open("cleared_runners_data.csv", 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(["Name","LastName","Sex","Age","Country","BibNumber","Result","Place"])
        writer.writerows(filtered_data.values.tolist())
