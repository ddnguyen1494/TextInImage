# TextInImage
TextInImage is a python3 program that hides text messages in an image. It embeds the data in the image by breaking down the message length and message into bits and modifying the least significant bit of every pixel's RGB values. It decodes the message by reading the all the least significant bits then reconstruct the message.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
* [Python3](https://www.python.org/)
* [pip Package Manager](https://pip.pypa.io/en/stable/#)

### Installing
Install dependencies 
 `pip3 install -r requirements.txt`

### Examples
* Embed image with the souce code
 
`python3 StegaImage.py -x ./TestImages/meme.png`
* Extracting the message

`python3 StegaImage.py -e StegaImage.py `

## Built With
[bitarray](https://pypi.python.org/pypi/bitarray)

## Authors
* Daniel Nguyen

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
* [Reza Nikoopour](https://github.com/rnikoopour) for this awesome project
