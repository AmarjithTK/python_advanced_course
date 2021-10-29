The 'with' statement


    python code of writing an downloaded image to local disk


    1) without 'with' statement

    request = requests.get('https://www.google.com/doodle.png)
    doodle_file = open('files/doodle.png,'wb') 
    doodle_file.write(request.content)
    doodle_file.close()

    2) with the 'with' statement

    with open('files/doodle.png','wb') as doodle_file:
        doodle_file.write(request.content)





The 'wb' string in opens statement

    'wb' - write permission in binary mode
    'rb' - read permission in binary mode
    'w' - write in normal mode
    'r' read in normal mode

    dict = ['rb','r','wb','w']

    file = open('file.png,dict[x])

    file.write  or  file.read

