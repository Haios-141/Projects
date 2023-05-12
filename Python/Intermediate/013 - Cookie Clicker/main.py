from cookie import Cookie
from datetime import datetime

# The time, in seconds, to wait before checking if there is anything available to buy.
# Change the value to suit your needs.
TIME_BEFORE_BUY = 20

END_GAME = 1  # Game ends after 1 minutes

url = "https://orteil.dashnet.org/cookieclicker/"
cookie = Cookie(url=url)

now = datetime.now()
seconds = now.time().second
minutes = now.time().minute

while True:
    cookie.cookie_click()
    new_now = datetime.now()
    new_seconds = new_now.time().second
    new_minutes = new_now.time().minute

    if abs(new_seconds - seconds) >= TIME_BEFORE_BUY:
        cookie.check_to_buy()
        seconds = new_seconds

    if abs(new_minutes - minutes) >= END_GAME:
        # print(f"Cookies/second: {cookie.cookies_per_second()}")
        break

cookie.close_window()
