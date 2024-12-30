from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)

class Channel(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User, related_name="channels", related_query_name="channel")

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    text = models.TextField()

def create_channel(name):
    return Channel.objects.create(name=name)

def create_user(name):
    return User.objects.create(name=name)

def create_message(user, channel, text):
    return Message.objects.create(user=user, channel=channel, text=text)

def messages_for(channel):
    return Message.objects.filter(channel=channel)

def active_users(channel):
    return User.objects.filter(message__channel=channel).distinct()

def lurkers(channel):
    return User.objects.exclude(message__channel=channel).distinct()



 # class Book(models.Model):
#     title = models.TextField()
#     rating = models.FloatField()
#     author_name = models.TextField()
#     publisher_name = models.TextField()

# class Author(models.Model):
#     name = models. TextField()
#     hometown = models. TextField()

# class Publisher(models.Model):
#     name = models.TextField()
#     founding_year = models.IntegerField()

# book = Book.objects.get(title="The Great Gatsby")
# author = Author.objects.get(name=book.author_name)
# print(author.hometown)

# publisher = Publisher.objects.get(publisher_name = book.publisher_name)
# print(publisher.founding_year)

# publisher = Publisher.objects.get(name=book.publisher_name) #name(the name of the publisher from Publisher) = book(The book linked to Book) . (accessing) publisher_name (The publisher name of the book in Book)
# books = Book.objects.filter(publisher_name=publisher.name) #publisher_name(the publisher name) = publisher(The publisher accessed with this variable) . (accessing) name (The publisher's name in Publisher)
