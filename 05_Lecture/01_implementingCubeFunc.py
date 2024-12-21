def cubeVolume(sidelength) : 
    volume = sidelength ** 3
    return volume 

def main():
    result1 = cubeVolume(2)
    result2 = cubeVolume(4)

    print("A cube with side length 2 has volume:",result1)
    print("A cube with side length 4 has volume:",result2)
    print("A cube with side length 10 has volume:",cubeVolume(10))
    
main()