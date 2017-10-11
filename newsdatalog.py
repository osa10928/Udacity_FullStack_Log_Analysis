#! /usr/bin/env python3

# Script is used to produce useful log information from a
# newspaper database. They script answers 3 question:

# 1. What are the most popular 3 articles of all time?

# 2. Who are the most popular article authors of all time (top 4)?

# 3. On which days did more than 1% of the requests lead to errors?

# Runs on python3
# 'python3' >= '3.5.2'
import psycopg2


# Connect to database
def connect(database_name="news"): 
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except:
        print("<error message>")

# This execute finds the top three articles
def top3articles():
    db, c = connect()
    query = "SELECT path, count(path) \
    FROM log \
    GROUP BY path \
    HAVING path like '/article%' \
    ORDER BY count desc \
    LIMIT 3"

    c.execute(query)
    top3 = c.fetchall()

    print("The top 3 articles are:")
    for i in top3:
        article = i[0]
        num = i[1]

        # Process article name
        article = article.split("/")[2].split("-")
        articleTitle = " ".join(article)
        print("%s - %s" % (articleTitle, str(num)))

    db.close()


# This execute finds the most popular article authors of all time
def popauthors():
    db, c = connect()
    query = "SELECT authors.name, sum(authorcount.count) \
    FROM authors join \
    (SELECT hitcount.count, articles.author \
        FROM \
            (SELECT path, count(path) \
            FROM log \
            GROUP BY path \
            HAVING path like '/article%' \
            ORDER BY count desc limit 8) \
            AS hitcount join articles \
            ON ('/article/' || articles.slug) like hitcount.path) \
    AS authorcount on authorcount.author = authors.id \
    GROUP BY authors.name \
    ORDER BY sum DESC"

    c.execute(query)
    top4 = c.fetchall()

    print("\nThe top article authors of all time are:")
    for j in top4:
        author = j[0]
        hits = j[1]
        print("%s - %s" % (author, str(hits)))

    db.close()


# This final execute gets dates with errors above 1%
def errordates():
    db, c = connect()
    query = "SELECT fails.fordate, \
    (cast(fails.failed AS float)/cast(fails.totalhits AS float)*100) AS error \
    FROM (\
        SELECT date(time) AS fordate, count(status) AS totalhits, \
        count(case when status != '200 OK' then 1 else null end) AS failed \
        FROM log GROUP BY fordate ORDER BY fordate) AS fails \
    WHERE cast(fails.failed AS float) / cast(fails.totalhits AS float) > 0.01"

    c.execute(query)
    errors = c.fetchall()

    print("\nDates with errors greater than 1%:")
    for k in errors:
        date = k[0]
        errornum = k[1]
        print("%s - %s%% errors" % (date, str(round(errornum, 1))))

    db.close()


# Now execute the 3 functions to get the answers

top3articles()
popauthors()
errordates()