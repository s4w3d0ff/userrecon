from requests import Session
from bs4 import BeautifulSoup

_s = Session()

URLS = {
    "instagram": "https://www.instagram.com/%s",
    "facebook": "https://www.facebook.com/%s",
    "twitter": "https://www.twitter.com/%s",
    "youtube": "https://www.youtube.com/%s",
    "blogspot": "https://%s.blogspot.com",
    "google": "https://plus.google.com/+%s/posts",
    "reddit": "https://www.reddit.com/user/%s",
    "wordpress": "https://%s.wordpress.com",
    "pinterest": "https://www.pinterest.com/%s",
    "github": "https://www.github.com/%s",
    "tumblr": "https://%s.tumblr.com",
    "flickr": "https://www.flickr.com/people/%s",
    "steam": "https://steamcommunity.com/id/%s",
    "vimeo": "https://vimeo.com/%s",
    "soundcloud": "https://soundcloud.com/%s",
    "disgus": "https://disqus.com/%s",
    "medium": "https://medium.com/@%s",
    "deviantart": "https://%s.deviantart.com",
    "vk": "https://vk.com/%s",
    "about.me": "https://about.me/%s",
    "imgur": "https://imgur.com/user/%s",
    "flipboard": "https://flipboard.com/@%s",
    "slideshare": "https://slideshare.net/%s",
    "fotolog": "https://fotolog.com/%s",
    "spotify": "https://open.spotify.com/user/%s",
    "mixcloud": "https://www.mixcloud.com/%s",
    "scribd": "https://www.scribd.com/%s",
    "badoo": "https://www.badoo.com/en/%s",
    "patreon": "https://www.patreon.com/%s",
    "bitbucket": "https://bitbucket.org/%s",
    "dailymotion": "https://www.dailymotion.com/%s",
    "etsy": "https://www.etsy.com/shop/%s",
    "cash.me": "https://cash.me/%s",
    "behance": "https://www.behance.net/%s",
    "goodreads": "https://www.goodreads.com/%s",
    "instructables": "https://www.instructables.com/member/%s",
    "keybase": "https://keybase.io/%s",
    "kongregate": "https://kongregate.com/accounts/%s",
    "livejournal": "https://%s.livejournal.com",
    "angel": "https://angel.co/%s",
    "last.fm": "https://last.fm/user/%s",
    "dribbble": "https://dribbble.com/%s",
    "codecademy": "https://www.codecademy.com/%s",
    "gravatar": "https://en.gravatar.com/%s",
    "pastebin": "https://pastebin.com/u/%s",
    "foursquare": "https://foursquare.com/%s",
    "roblox": "https://www.roblox.com/user.aspx?username=%s",
    "gumroad": "https://www.gumroad.com/%s",
    "newgrounds": "https://%s.newgrounds.com",
    "wattpad": "https://www.wattpad.com/user/%s",
    "canva": "https://www.canva.com/%s",
    "creativemarket": "https://creativemarket.com/%s",
    "trakt": "https://www.trakt.tv/users/%s",
    "500px": "https://500px.com/%s",
    "buzzfeed": "https://buzzfeed.com/%s",
    "tripadvisor": "https://tripadvisor.com/members/%s",
    "hubpages": "https://%s.hubpages.com",
    "contently": "https://%s.contently.com",
    "houzz": "https://houzz.com/user/%s",
    "blip.fm": "https://blip.fm/%s",
    "wikipedia": "https://www.wikipedia.org/wiki/User:%s",
    "ycombinator": "https://news.ycombinator.com/user?id=%s",
    "codementor": "https://www.codementor.io/%s",
    "reverbnation": "https://www.reverbnation.com/%s",
    "designspiration": "https://www.designspiration.net/%s",
    "bandcamp": "https://www.bandcamp.com/%s",
    "colourlovers": "https://www.colourlovers.com/love/%s",
    "ifttt": "https://www.ifttt.com/p/%s",
    "ebay": "https://www.ebay.com/usr/%s",
    "slack": "https://%s.slack.com",
    "okcupid": "https://www.okcupid.com/profile/%s",
    "skyscanner": "https://www.trip.skyscanner.com/user/%s",
    "ello": "https://ello.co/%s",
    "tracky": "https://tracky.com/user/%s",
    "tripit": "https://www.tripit.com/people/%s#/profile/basic-info",
    "basecamp": "https://%s.basecamphq.com/login",
}

# redirects regex
REGEX = {
    'google': '',
    'wordpress': '',
    'reddit': '',
    'ycombinator': '',
    'tripit': '',
    'pastebin': '',
    'ebay': '': ,
    'mixcloud': '',
    'steam': ''
}


def get(username, ignore=[]):
    results = {
        "good": [],
        "bad": [],
        "error": []
    }
    for name in URLS:
        if name not in ignore:
            try:
                r = _s.get(URLS[name] % str(username))
                print('%s: status_code:%s' % (name, str(r.status_code)))
                if r.status_code < 500 and r.status_code > 399:
                    results['bad'].append(name)
                else:
                    print(r.url)
                    results['good'].append(name)
            except Exception as e:
                print(e)
                results['error'].append(name)

    print(results)
    return results
