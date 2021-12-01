import time
import notify2
from top_news import top_stories

# path to notification window icon
ICON_PATH = "/images/news_icon.png"

# Fetch news items
news_items = top_stories()

# Initialize the d-bus connection
notify2.init("News Notifier")

# Create Notification object
notification = notify2.Notification(None, icon= ICON_PATH)

# Set urgency level
notification.set_urgency(notify2.URGENCY_NORMAL)

# Set Timeout for notification
notification.set_timeout(10000)

for news_item in news_items:

    # Update notification data for Notification object
    notification.update(news_item['title'], news_item['description'])

    # Show notification on screen
    notification.show()

    # Short delay between notifications
    time.sleep(15)
