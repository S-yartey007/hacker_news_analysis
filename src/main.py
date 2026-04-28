import csv
header = list()
data = list()

with open("data/hacker_news.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header= next(reader)
    print(", ".join(header))
    for row in reader:
        data.append(row)

show_hn_posts = [row for row in data if row[1].lower().startswith("show hn") ]
ask_hn_posts = [row for row in data if row[1].lower().startswith("ask hn") ]
print("show_hn_list", len(show_hn_posts))
print("ask_hn_list", len(ask_hn_posts))

ask_comments_num = 0

for row in ask_hn_posts:
    ask_comments_num += int(row[4])

if len(ask_hn_posts) > 0:
    avg_ask_comments_num  = ask_comments_num / len(ask_hn_posts)
else:
    avg_ask_comments_num = 0

print("ask_comments_num", ask_comments_num)
print("avg_ask_comments_num", avg_ask_comments_num)















