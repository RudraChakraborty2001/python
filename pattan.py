# with the help of this code we are able to finde a word in a paragraph
import re

pattern = "of"

text = '''Most of us have childhood memories of gaping at our elders in wonder
 when they narrated to us the amusing fables of Aesop, the picturesque fairy tales,
   the funny anecdotes, the lyrical short stories, and so on. Classic bedtime stories 
   take us into the world of imagination. These short stories are identified with brevity
     and compact narrative. Vedantu brings forth some of the most amazing kids' stories 
     with colourful illustrations to make the most of the leisure reading of kids. 
'''

match = re.search(pattern, text)
print(match)