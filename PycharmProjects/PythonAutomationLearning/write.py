with open('test.txt','r') as R1:
    content=R1.readlines()
    reversed(content)
    with open('test.txt','w')as w1:
        for line in reversed(content):
            w1.write(line)

