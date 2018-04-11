def get(msg):
    return input(msg)

def getInt(msg):
    success = False
    while not success:
        try:
            return int(input(msg))
        except:
            put("You need to use an integer for your answer.")

def put(*msg):
    out = ""
    for i in msg:
        out += str(i)
    print(out)
