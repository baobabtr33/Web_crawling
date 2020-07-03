import requests
from bs4 import BeautifulSoup

url = 'https://edition.cnn.com/2020/06/08/entertainment/ludacris-george-floyd-kid-nation/index.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
photo_url = soup.find('img', attrs={'class':'media__image media__image--responsive'}).get('data-src-large')

photo_url = 'https:' + photo_url
photo_url


# get photo
import shutil

def get_picture(picture_url): # to save the image file
    response = requests.get(picture_url, stream=True)

    f = open('test_image.jpg', 'wb')
    shutil.copyfileobj(response.raw, f)
    f.close()
    del response

get_picture(photo_url)

# 얼굴 감지
import os
import sys
import requests
client_id = "SRTjrcFlUsmiuX0ubd35"
client_secret = "78IeaHfyYg"
url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
# url = "https://openapi.naver.com/v1/vision/celebrity" // 유명인 얼굴인식
files = {'image': open('test_image.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
results1 = response.json()


results1


results1['faces'][0]['emotion']

# 유명인 얼굴인식
client_id = "SRTjrcFlUsmiuX0ubd35"
client_secret = "78IeaHfyYg"
# url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
files = {'image': open('test_image.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code
results2 = response.json()

results2

print(results2['faces'][0]['celebrity'])

