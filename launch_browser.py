# Tutorial: http://www.idiotinside.com/2015/03/07/open-an-url-on-web-browser-programmatically-in-python
# Documentation: https://docs.python.org/3/library/webbrowser.html
# Tested Python 2.7.6

import webbrowser

url = 'http://idiotinside.com'

# Open URL in new browser window
webbrowser.open_new(url) # opens in default browser

# Opens in safari browser
webbrowser.get('safari').open_new(url)

# Open URL in a new tab
webbrowser.open_new_tab(url) # opens in default browser

# Opens in safari browser
webbrowser.get('safari').open_new_tab(url)

