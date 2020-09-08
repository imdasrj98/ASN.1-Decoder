def integerConverter(data):
    l=len(data)
    output=[]
    for i in range(l):
        output.append(int(data[i], 2))
    return output

def bitStringConverter(data):
    pass

def octetStringConverter(data):
    pass

def objectIdentifierConverter(data):
    pass

def printableStringConverter(data):
    pass

def t61StringConverter(data):
    pass

def ia5StingConverter(data):
    l=len(data)
    output=""
    for i in range(l):
        output+=chr(int(data[i], 2))
    return output

def utcTimeConverter(data):
    pass

def decodeData(data):
    tag=data[0]
    length=int(data[1], 2)
    tag_class=int(tag[:2], 2)
    pc=int(tag[2], 2)
    tag_number=int(tag[3:], 2)
    #print(tag, length, tag_class, pc, tag_number)
    decoded_data=[]
    if pc==0:
        data_types={
            2: integerConverter(data[2: length+2]),
            3: bitStringConverter(data[2: length+2]),
            4: octetStringConverter(data[2: length+2]),
            5: None,
            6: objectIdentifierConverter(data[2: length+2]),
            16: "sequence",
            17: "set",
            19: printableStringConverter(data[2: length+2]),
            20: t61StringConverter(data[2: length+2]),
            22: ia5StingConverter(data[2: length+2]),
            23: utcTimeConverter(data[2: length+2])
        }
        output=data_types[tag_number]
        return output, length

    else:
        i=0
        while i<length:
            d, l=decodeData(data[i+2: i+length+2])
            decoded_data.append(d)
            i+=l+2

    return decoded_data

def main():
    f=open("log.txt")
    encoded_data=f.read().split()
    #print(encoded_data)
    binary_data=[]
    for ed in encoded_data:
        binary_data.append("{0:08b}".format(int(ed, 16)))
    #print(binary_data)
    decoded_data=decodeData(binary_data)
    print(decoded_data)

if __name__=='__main__':
    main()
