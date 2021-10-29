# x=1

# for x in range(1,3):
    
#     print('it works fine')
#     q= input('Enter q to quit :')
#     x=1
    # if q.upper() == 'Q':
    #     break

keyword = 'freemason'

import requests as Rq
from wikipedia import wikipedia as Wp
import os 

wp= Wp.page(keyword)
imagelibrary = wp.images
# for image in imagelibrary:
#     rq = Rq.get(wp.images[image])
#     image = open(f'sukhoi/sukhoi{image}.jpg','wb')
#     image.write(rq.content)

for x in range(imagelibrary.__len__()):
    rq = Rq.get(imagelibrary[x])

    image = open(f'{keyword}/{keyword}{x}.jpg','wb')
    image.write(rq.content)    







