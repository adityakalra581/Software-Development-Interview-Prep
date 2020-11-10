## No need to create a file. Once you give a write command the file will be created automatically.
## Writing into a Binary File:

numbers = [1,2,3,4]
## Will enter this list into a binary file. 

## Uncomment the below write code for writing into a file.

with open("binary1", "bw") as bin:
    bin.write(bytes(numbers))

## Bytes will convert numbers into Hexadecimal.
## 1 = 01
## 2 = 02

## Reading the content of Binary file:

with open("binary1", "br") as f:
    print(f.read())

## OUTPUT:

## b'\x01\x02\x03\x04'

## b: bytes
## x: Hexadecimal
## 01,02,03,04