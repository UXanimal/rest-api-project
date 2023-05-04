"""
blocklist.py

This file contains the blocklist for JWT Tokens. 
It is used to store tokens that have been revoked.

This is a bad way of doing this. The better way is to use a database.

The Blocklist set will be cleared every time the server is restarted.

Reddis is a good option for this.
"""

BLOCKLIST = set()