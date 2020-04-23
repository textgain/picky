import os
import shutil
import json

class Tags(dict):

    def __init__(self, path, *args, **kwargs):
        """ Returns the given JSON export from Picky
            as a (path, [tags])-dict
        """
        if os.path.exists(path or ''):
            self.update(json.load(open(path, 'rb')))
        self.update(*args)
        self.update(kwargs)
        self.path = path

    def save(self):
        json.dump(self, open(self.path, 'w'))

    def find(self, f=lambda v: True):
        return {k: v for k, v in self.items() if f(v)}

def merge(*tags):
    """ Returns a dict of the merged Tags.
    """
    m = {}
    for t in tags:
        for k, v in t.items():
            m.setdefault(k, []).extend(v)
    return m

# Merging two sets of Tags:

# t1 = Tags(None, {'1.jpg': ['cat'], '2.jpg': ['dog']})
# t2 = Tags(None, {'1.jpg': ['hat']})
# t3 = Tags(None, merge(t1, t2))
# print(t3)

# Finding a subset of Tags:

# t1 = Tags(None, {
#     '1.jpg': ['+'],
#     '2.jpg': ['+'],
#     '3.jpg': ['-'],
# })
# for f1 in t1.find(lambda tags: '+' in tags):
#     f2 = os.path.basename(f1)
#     f2 = os.path.join('subset', f2)
#     shutil.copy(f1, f2)
#     print(f1)