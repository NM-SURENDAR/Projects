import speech recognition a

Ivww.stocknowledge.com Python eind Areint to draft Cente

14

while True:

1st.Recognizer()

with sr.Microphone() as source:

audio r.listen(source)

try:

filename "draft.txt

fopen(filename, "a")

recognized textr.recognize google (audio)

print (recognized_text)

13

16

remainder recognized_text.split()

while remainder:

27

28

line, remainder remainder [13), remainder[51] f.write(.join(line) "\n"

if recognized_text by:

20

23

23

24

break

except sr.UnknownValueEΣΣΟΣΙ

print("Google could not understand audio")

except sz. RequestEzzor AR

25

print("Google azzor: (01".format(e))
