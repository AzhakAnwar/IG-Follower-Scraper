from instagramBot import InstagramBot
from collections import deque

person = InstagramBot('acasty', 'Mandy006!')

with open('private', 'r') as fp:
    private = set(fp.read().split('\n'))

with open('dequed', 'r') as fp:
    dequed = set(fp.read().split('\n'))

private.difference_update(dequed)
q = deque(private)
newQ = q
person.signIn()
while newQ:
    username = newQ.popleft()
    person.getUserFollowers(username)
