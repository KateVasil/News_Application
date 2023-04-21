import requests
from send_email import send_email

api_key = "78b53e7dfb1441f28cdfd8e91ad73f39"
topic = "tesla"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&from=2023-03-21&" \
      "sortBy=publishedAt&" \
      "apiKey=78b53e7dfb1441f28cdfd8e91ad73f39&" \
      "language=en"


# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""
for article in content["articles"][:20]:
    body = "Subject: Today's news" \
           + "\n" + body + article["title"] \
           + "\n" + article["description"] \
           + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")

# Send the titles to my email address
send_email(message=body)
