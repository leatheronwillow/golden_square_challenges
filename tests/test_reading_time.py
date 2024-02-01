# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

# 2. Design the Function Signature
# The signature of a function includes:

# The name of the function: reading_time
# What parameters it takes, their names and data types: text(string), reading_speed (int) which defaults to 200 words/min
# What it returns and the data type of that value: fstring containing the estimate in a nice format with units
# Steps 3 and 4 then operate as a cycle.

from lib.reading_time import *

"""
if the string is empty, return "0 mins"
if the string is not empty but less than or equal to 200 words, "1 min"
if the string is between 200 and 400 words, "2 min"
"""
def test_returns_string ():
    assert type(reading_time("")) == str

def test_empty_string():
    assert reading_time("") == "0 mins"

def test_short_string():
    assert reading_time("Hello World") == "1 min"

def test_long_string():
    long_string = "Tellus vestibulum lacus primis duis commodo et et ac. Dapibus placerat. Id platea ante quis torquent condimentum etiam viverra ultricies phasellus gravida sem sed diam felis. Enim. At at sociis adipiscing. Morbi elit phasellus metus vivamus, tincidunt porta, congue pharetra nibh habitasse vehicula euismod Non tempus facilisi viverra nunc. Porta. Vel Elementum odio penatibus felis nonummy a nisl fames interdum semper hendrerit sociosqu cubilia nascetur lacus ornare lacus penatibus mattis hymenaeos class orci Ut ad magnis ligula habitant sem donec luctus nam consequat justo platea curae; nulla auctor. Ligula rutrum blandit pulvinar eu tempor luctus ac commodo duis at gravida neque dolor pellentesque. Habitant faucibus. Pellentesque phasellus cubilia dui duis gravida est aliquam eleifend mollis Cum. Fringilla mi. Quam eleifend ultricies mus primis semper mi natoque mollis consequat duis ipsum mauris eget porta ornare nullam adipiscing pede primis erat mauris fusce dignissim viverra Sociosqu rutrum dapibus. Sociis sodales, malesuada blandit enim malesuada Neque fringilla feugiat. Aptent penatibus torquent ipsum non eleifend risus at sed semper ultrices mollis posuere ut natoque fermentum cubilia adipiscing arcu conubia dolor potenti. Non felis lobortis senectus lectus torquent. Vulputate adipiscing dui at primis semper nibh congue fusce nonummy. Sem sit sagittis molestie fringilla hymenaeos nonummy urna, sollicitudin cum. Magna leo integer mattis ligula Quisque congue. Placerat aliquet fermentum amet Consequat scelerisque purus ipsum eu Fames felis mollis magna est commodo etiam porta. Curabitur semper rutrum dolor, justo ornare vel velit donec est convallis integer rhoncus morbi. Leo a convallis Dui quam fusce tristique convallis ultrices tempor ultrices. Cursus convallis aenean. Ultricies. Ullamcorper convallis praesent quam accumsan eu nam. Maecenas. Nulla dui faucibus sem duis conubia. Eget tristique vivamus sociis. In. Posuere erat nisl suscipit eu. Nunc commodo parturient mauris facilisis penatibus hendrerit hymenaeos. Vitae varius. Feugiat penatibus a nec cubilia nibh pellentesque. Metus pulvinar magna."
    assert reading_time(long_string) == "2 mins"




