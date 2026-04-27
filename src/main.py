import csv

with open("data/hacker_news.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header= next(reader)
    print(", ".join(header))

    data = list()
    for i,row in enumerate(reader):
        data.append(row)

    show_hn_list = [row for row in data if row[1].startswith("Show HN") ]
    ask_hn_list = [row for row in data if row[1].startswith("Ask HN") ]
    print("show_hn_list", len(show_hn_list))
    print("ask_hn_list", len(ask_hn_list))













