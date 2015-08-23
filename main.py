import hashlib
import os.path
import imp
import traceback

import nltk
from textblob import TextBlob
from textblob import Word

__project_name__ = """perspect|ve"""
__notice__ = """\
[]=====================[]
|| can machines think? ||
[]=====================[]
"""

nltk.data.path.append("~/Projects/ohai/nltk_data/")

loop = True

def load_module(code_path):
    try:
        try:
            code_dir = os.path.dirname(code_path)
            code_file = os.path.basename(code_path)
            fin = open(code_path, 'rb')
            return imp.load_source(hashlib.md5(code_path).hexdigest(), code_path, fin)
        except ImportError:
            traceback.print_exc(file = sys.stderr)
            raise
        finally:
            try: fin.close()
            except: pass
    except:
        traceback.print_exc(file = sys.stderr)
        raise
        
def prompt():
    prompt_text = __project_name__ + "> "
    return input(prompt_text)
    
def command(string):
    args = string[1:].split(' ')
    if args[0] == "exit":
        global loop
        loop = False
        print("exiting...")

print('\n'+__project_name__+'\n')
print(__notice__)

while loop:
    t = prompt()
    if t.find('/') == 0:
        command(t)
        continue
    blob = TextBlob(t)
    print(blob.tags)
    lemmized_str = ""
    for word in blob.words:
        lemmized_str += word.lemmatize() + " "
    print(lemmized_str)

