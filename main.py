import requests

api_key = "78b53e7dfb1441f28cdfd8e91ad73f39"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-03-16&sortBy=publishedAt&apiKey=" \
      "78b53e7dfb1441f28cdfd8e91ad73f39"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
for article in content["articles"]:
      print(article["title"])

