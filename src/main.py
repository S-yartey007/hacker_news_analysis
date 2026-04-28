import csv
from datetime import datetime
import math
header = list()
data = list()

#Read csv file and extract data
with open("data/hacker_news.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header= next(reader)
    print(", ".join(header))
    for row in reader:
        data.append(row)

#Extract show hn posts and ask hn posts
show_hn_posts = [row for row in data if row[1].lower().startswith("show hn") ]
ask_hn_posts = [row for row in data if row[1].lower().startswith("ask hn") ]

#Calculate sum of comments for posts
def sum_of_comments(posts):
    comments_total = 0
    for row in posts:
        comments_total += int(row[4])
    return comments_total

#Calculate avg number of comments for posts
def avg_num_of_comments(posts):
    if len(posts) > 0:
        avg_comments_num  = sum_of_comments(posts)/ len(posts)
        return avg_comments_num
    else:
        return 0


print("total number of ask hn comments", sum_of_comments(ask_hn_posts))
print("average number of ask hn comments", avg_num_of_comments(ask_hn_posts))
print("total number of show hn comments", sum_of_comments(show_hn_posts))
print("average number of show hn comments", avg_num_of_comments(show_hn_posts))

#Analyse time of posts
def analyze_times_of_post(posts):
    count = {}
    total = {}
    for row in posts:
        dt = datetime.strptime(row[6], "%m/%d/%Y %H:%M")
        hour = dt.hour
        comment_num = row[4]
        if hour not in count:
            count[hour] = 0
        if hour not in total:
            total[hour] = 0
        count[hour] += 1
        total[hour] += int(comment_num)

    avg_dic = {}
    for hour,cnt  in count.items():
        avg_dic[hour] = total[hour]/ count[hour]

    return [(hour,avg) for hour, avg in avg_dic.items()]


avg_ask_hn_comments_per_hour = analyze_times_of_post(ask_hn_posts)
sorted_avg_ask_hn_comments_per_hour = sorted(avg_ask_hn_comments_per_hour,key=lambda x: x[1], reverse=True)
top_5_ask_hn = sorted_avg_ask_hn_comments_per_hour[:5]
print("Top 5 hours for maximum ask hacker news engagements")
for i, item in enumerate(top_5_ask_hn):
            print(f"{i+1}. {item[0]:02d}:00   {round(item[1],1)} comments")


avg_show_hn_comments_per_hour = analyze_times_of_post(show_hn_posts)
sorted_avg_show_hn_comments_per_hour = sorted(avg_show_hn_comments_per_hour,key=lambda x: x[1], reverse=True)
top_5_show_hn = sorted_avg_show_hn_comments_per_hour[:5]
print("Top 5 hours for maximum show hacker news engagements")
for i, item in enumerate(top_5_show_hn):
            print(f"{i+1}. {item[0]:02d}:00   {round(item[1],1)} comments")



















