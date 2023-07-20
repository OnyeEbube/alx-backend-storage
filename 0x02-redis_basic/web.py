import redis
import requests
from functools import wraps

# Initialize the Redis client
r = redis.Redis()

# Define the decorator for counting URL accesses and caching
def url_access_count(method):
    @wraps(method)
    def wrapper(url):
        key = "cached:" + url
        cached_value = r.get(key)
        if cached_value:
            return cached_value.decode("utf-8")

        # Get new content and update cache
        key_count = "count:" + url
        html_content = method(url)

        r.incr(key_count)  # Increment the count for the URL
        r.set(key, html_content, ex=10)  # Cache the HTML content with a 10-second expiration time
        r.expire(key, 10)  # Set the expiration time for the cache
        return html_content

    return wrapper

# Apply the decorator to the get_page function
@url_access_count
def get_page(url: str) -> str:
    results = requests.get(url)
    return results.text

if __name__ == "__main__":
    # Test the get_page function with the slowwly.robertomurray.co.uk URL
    html_content = get_page('http://slowwly.robertomurray.co.uk')
    print(html_content)
