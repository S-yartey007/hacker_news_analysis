# Hacker News Post Engagement Analysis

## 📌 Project Overview

This project analyzes Hacker News posts to determine **which type of posts (“Ask HN” vs “Show HN”) receive more engagement** and **the best times to post for maximum comments**.

The analysis focuses on identifying patterns in user interaction based on post type and posting time.

---

## 🎯 Objectives

- Compare engagement between **Ask HN** and **Show HN** posts
- Identify **peak hours** for user interaction
- Compute **average number of comments per hour**
- Extract actionable insights for maximizing engagement

---

## 🛠️ Tools & Technologies

- Python
- CSV module
- Datetime module

---

## 📂 Dataset

The dataset contains Hacker News posts with the following fields:

- `id`
- `title`
- `url`
- `num_points`
- `num_comments`
- `author`
- `created_at`

---

## 🔍 Methodology

1. **Data Loading**
   - Read dataset using Python’s `csv` module
   - Separated header and data

2. **Data Cleaning**
   - Filtered posts into:
     - Ask HN
     - Show HN

   - Normalized text using lowercase matching

3. **Data Analysis**
   - Calculated:
     - Total comments
     - Average comments per post

   - Extracted posting hour using `datetime`

4. **Aggregation**
   - Computed:
     - Total comments per hour
     - Number of posts per hour
     - Average comments per hour

5. **Sorting & Ranking**
   - Sorted hours by highest average engagement
   - Selected top 5 hours

---

## 📊 Results

### 🔹 Ask HN (Top 5 Hours)

1. 15:00 → 38.6 comments
2. 02:00 → 23.8 comments
3. 20:00 → 21.5 comments
4. 16:00 → 16.8 comments
5. 21:00 → 16.0 comments

---

### 🔹 Show HN (Top 5 Hours)

1. 18:00 → 15.8 comments
2. 00:00 → 15.7 comments
3. 14:00 → 13.4 comments
4. 23:00 → 12.4 comments
5. 22:00 → 12.4 comments

---

## 📈 Key Insights

- **Ask HN posts generate significantly more engagement** than Show HN posts
- The best time to post Ask HN is **15:00**, with the highest average comments
- Ask HN also performs well during late-night hours (e.g., 02:00)
- Show HN posts have **lower and more evenly distributed engagement**
- Peak times for Ask HN and Show HN **do not overlap significantly**

---

## ✅ Conclusion

- To maximize engagement:
  - Post **Ask HN** around **15:00**
  - Post **Show HN** in the **evening (18:00–23:00)**

- Ask HN is better suited for **discussion-driven content**, while Show HN attracts **moderate, consistent interaction**

---

## 🚀 Future Improvements

- Visualize results using Matplotlib
- Re-implement analysis using Pandas
- Expand dataset for more robust insights
- Analyze additional factors (e.g., points, authors, topics)

---

## 📎 Author

Emmanuel Yartey
Computer Science & Mathematics Student
Interested in Backend Engineering, AI, and Data Science
