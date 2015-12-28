''' Welcome! Please refer to final project deliverables for more
details on class structure and arguments'''

class Video(object):
    def __init__(self, title, yt_link, seen):
        self.title = title
        self.yt_link = yt_link
        self.seen = seen
    def check_seen(self):
        return self.seen
class Film(Video):
    def __init__(self, title, yt_link, seen, director, year):
        Video.__init__(self, title, yt_link, seen)
        self.director = director
        self.year = year       
    def email_template(self):
        return 'Hi, Zachary!' + '\n' + '\n' + 'Here is your movie for \
for the week:' + '\n' + 'Title: ' + self.title + '\n' \
+ 'Year: ' + self.year + '\n' + 'Link to Trailer: ' + self.yt_link \
+ '\n' + 'Director(s): ' +self.director + '\n' + '---------------------------------'
class Google_Talk(Video): 
    def __init__(self, title, yt_link, seen, category):
        Video.__init__(self, title, yt_link, seen)
        self.category = category
    def email_template(self):
        return '\n' +'And, here is your Talk at Google for \
for the week:' + '\n' + 'Title: ' + self.title + '\n' \
+ 'Category: ' + self.category + '\n' + 'Youtube link: ' + self.yt_link \
+ '\n' + '\n' +'Enjoy! These are curated picks from the Udacity Programming \
Foundations in Python final project that you created.'+ '\n' + '-ZT'



