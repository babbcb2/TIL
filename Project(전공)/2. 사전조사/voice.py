import subprocess 
import wave
from OCR import main



text = main('./book.jpg','2607c58891135f8fdd19a8d0206e9f2f')
print(text)

url = "https://kakaoi-newtone-openapi.kakao.com/v1/synthesize"

speak = '<speak>'+text+'</speak>'

res = subprocess.Popen(['curl', '-v', '-X', 'POST', url,
                        '-H', "Content-Type: application/xml",
                        '-H', "Authorization: 2607c58891135f8fdd19a8d0206e9f2f",
                        '-d', speak], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
output, err = res.communicate()

f = open('book.wav', 'wb')
f.write(output)
f.close()

# print(err)
