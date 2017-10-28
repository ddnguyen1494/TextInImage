# TextInImage
TextInImage is a python3 program that hides text messages in an image. It embeds the data in the image by breaking down the message length and message into bits. It iterates through every pixel's RGB values and modify the least significant bit starting from the bottom right(first 11 bits are used for text length). The program can decode the message by reading the least significant bits from every pixels' RGB values.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
* [Python3](https://www.python.org/)
* [pip Package Manager](https://pip.pypa.io/en/stable/#)

### Installing
Install dependencies: `pip3 install -r requirements.txt`

### Examples
* Embed image with the souce code
`python3 StegaImage.py -e test.txt image.jpg`
* Extracting the message
`python3 StegaImage.py -x image.png`

## Built With
[bitarray](https://pypi.python.org/pypi/bitarray)

## Authors
* Daniel Nguyen

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
* [Reza Nikoopour](https://github.com/rnikoopour) for this awesome project
