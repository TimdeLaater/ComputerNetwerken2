import json
from ldap3 import Server, Connection, SAFE_SYNC
conn = Connection('ldap.itd.umich.edu',auto_bind=True)
conn.search("dc=umich,dc=edu", "(cn=Amy Newman)")
person = conn.entries[0]
print(json.loads(person.entry_to_json()))