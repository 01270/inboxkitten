[![Downloads](https://static.pepy.tech/badge/inboxkitten)](https://pepy.tech/project/inboxkitten)

# inboxkitten v0.0.2
Python Package to make temp email from https://inboxkitten.com/

## Installation

This package can be installed with pip:

```pip3 install inboxkitten```


## Configuration

inboxkitten instance can be created like this:

```python 
from inboxkitten import *

email = InboxKitten('NAME_HERE@inboxkitten.com')
setup = email.setup()
```


## Example

```python 
from inboxkitten import *

email = InboxKitten('minute-health-99@inboxkitten.com')

# setup the email
setup = email.setup()

if setup:
    mails = email.senders
    print(mails)

    if any(mails):
        print(f'({len(mails)}) Mails Found')

        # index 0 is the last message
        message = email.view(0)

        # Get the email message html as text
        print(message.text)

        # Save the html text to html file
        print(message.save_html('test.html'))
    else: print('Email is empty')
```

## Mulit emails

If you are trying to make more than one email
You have to use .clear() method after each email created

```python 
from inboxkitten import *

email = InboxKitten('NAME_HERE1@inboxkitten.com')
email.setup()
#....Code here....#
email.clear()

another_email = InboxKitten('NAME_HERE2@inboxkitten.com')
another_email.setup()
#....Code here....#
another_email.clear()

another_email_2 = InboxKitten('NAME_HERE3@inboxkitten.com')
another_email_2.setup()
#....Code here....#
another_email_2.clear()

```
