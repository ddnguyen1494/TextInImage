# TextInImage
Steganography is the practice of hiding of secret messages within another medium. TextInImage is a python3 program that encode/decode text messages in an image by reading/writing each bit of the message to the least significant bit of every pixel.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
[Python3](https://www.python.org/)

### Installing
Install dependencies 
 `pip3 install -r requirements.txt`

### Examples
* Embed image with the souce code
 
`python StegaImage.py -x ./TestImages/meme.png`
* Extracting the message

`python StegaImage.py -e StegaImage.py `

## Built With
[bitarray](https://pypi.python.org/pypi/bitarray)

## Authors
* Daniel Nguyen

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
* [Reza Nikoopour](https://github.com/rnikoopour) for this awesome project
