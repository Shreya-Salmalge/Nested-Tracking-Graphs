xd = 192
yd = 64
zd = 48

def createNode(level,id):
    newNode = {}
    newNode['id'] = id
    newNode['level'] = level
    newNode['xmin'] = xd+1
    newNode['xmax'] = -1
    newNode['ymin'] = yd+1
    newNode['ymax'] = -1
    newNode['zmin'] = zd+1
    newNode['zmax'] = -1

    return newNode

def floodfill(i, j, k, level,id,compNo):
 
    # create a queue and enqueue starting pixel
    q = []
    compNo[((k * yd + j) * xd + i)]= 0 # 0 implies added to queue
    q.append((i, j, k))
    newNode = createNode(level,id)

    def modifyMinMax(x,y,z,newNode):
        if(newNode['xmin']>x):
            newNode['xmin'] = x
        if(newNode['xmax']<x):
            newNode['xmax'] = x

        if(newNode['ymin']>y):
            newNode['ymin'] = y
        if(newNode['ymax']<y):
            newNode['ymax'] = y

        if(newNode['zmin']>z):
            newNode['zmin'] = z
        if(newNode['zmax']<z):
            newNode['zmax'] = z

    # break when the queue becomes empty
    while len(q):
 
        # dequeue front node and process it
        x, y, z = q[0]
        del q[0]
        compNo[((z * yd + y) * xd + x)] = id

        modifyMinMax(x,y,z,newNode)

        #if valid and unexplored neighbours then add them to queue
        if(x>0 and compNo[((z * yd + y) * xd + x-1)]==-2):
            compNo[((z * yd + y) * xd + x-1)] = 0
            q.append((x-1,y,z))
        if(x<xd-1 and compNo[((z * yd + y) * xd + x+1)]==-2 ):
            compNo[((z * yd + y) * xd + x+1)] = 0
            q.append((x+1,y,z))

        if(y>0 and compNo[((z * yd + y-1) * xd + x)]==-2 ):
            compNo[((z * yd + y-1) * xd + x)] = 0
            q.append((x,y-1,z))
        if(y<yd-1 and compNo[((z * yd + y+1) * xd + x)]==-2 ):
            compNo[((z * yd + y+1) * xd + x)] = 0
            q.append((x,y+1,z))

        if(z>0 and compNo[(((z-1) * yd + y) * xd + x)]==-2 ):
            compNo[(((z-1) * yd + y) * xd + x)] = 0
            q.append((x,y,z-1))
        if(z<zd-1 and compNo[(((z+1) * yd + y) * xd + x)]==-2 ):
            compNo[(((z+1) * yd + y) * xd + x)] = 0
            q.append((x,y,z+1))

    # newNode['componentMatrix']  = compNo  
    return (newNode,compNo)

