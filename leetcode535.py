#Encode and Decode TinyURL
class Codec:
    def __init__(self):
        self.url_db = {}


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        unique_id = str(len(self.url_db))
        # unique_id = str(len(longUrl))
        short_url = "http://tinyurl.com/" + unique_id
        self.url_db[short_url] = longUrl
        print(self.url_db)

        return short_url

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_db[shortUrl]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))