import requests
from bs4 import BeautifulSoup


class GooglePlay(object):
    def get_playstore_info(self, app):
        # Fetch android app page
        app_page = requests.get(app)

        # Provide the app page content to BeautifulSoup parser
        soup = BeautifulSoup(app_page.content, 'html.parser')

        # Get value by id
        title = soup.select('div.id-app-title')

        # Get value from meta tag url
        url = soup.find("meta", {"itemprop": "url"})['content']

        # Get value from meta tag rating
        ratingsValue = soup.find("meta", {"itemprop": "ratingValue"})['content']
        ratingsCount = soup.find("meta", {"itemprop": "ratingCount"})['content']

        # Get value by attribute
        num_downloads = soup.find("div", {"itemprop": "numDownloads"}).text

        num_downloads_abs = num_downloads.split("-")[1]

        app_details = dict()
        app_details['title'] = title[0].text
        app_details['url'] = url
        app_details['rating'] = float(ratingsValue)
        app_details['rated_by'] = int(ratingsCount)
        app_details['downloads'] = int(num_downloads_abs.replace(" ", "").replace(",", ""))
        app_details['downloads_range'] = num_downloads
        return app_details


playstore = GooglePlay()
app_url = "https://play.google.com/store/apps/details?id=com.whatsapp"
app_details =  playstore.get_playstore_info(app_url)

print app_details