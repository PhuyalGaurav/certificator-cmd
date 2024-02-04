# Cetificator command line

Does the same thing as the [web version](https://github.com/PhuyalGaurav/certificator). but through command line. 🤯

## Requirements

- [Python 3.x (3.12 recommended)](https://www.python.org/downloads/)
- [Pip](https://www.python.org/downloads/ "Should be able to be installed using python installer")
- [Git](https://git-scm.com/downloads)

## Installation

```
# Clone the repository
> git clone https://github.com/PhuyalGaurav/certificator-cmd
# Now change to dir
> cd certificator-cmd
# Install dependencies
> pip install -r requirements.txt
```

> Now you should be able to run the project

## Usage

- Place your template in the directory
- delete all the names in names.csv and place in your own
- Now Run using `> python main.py <your_template> names.csv`
  - If you want to use your own font use ` --font <your_font_file>` (should be a `.ttf` file)
  - If you want to change the font size use `--font <your_font_size>`
- Now click on where the text should be for all files.
- Now the zip file with all the certificates should be generated

  #### Example run

```
> python.exe .\main.py .\template.png .\names.csv --font 'arial.ttf' --size 44
 getting coordinates...
 (Here, a window will open. Where you will have to click where you want the text to be.)
 x = 313, y = 327
 Generated certificate for gaurav phuyal.
 Generated certificate for john doe.
 Generated certificate for justin bieber.
 Generated certificate for kanye west.
 Generated certificate for kim kardashian.
 Generated certificate for pratik dahal.
 Saving certificates in certificates.zip .....
 Certificates generated and saved in certificates.zip
>
```

## License

[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2024 Gaurav Phuyal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## How to contribute

Create a issue and send a normal pull request.

## Author

- [Gaurav Phuyal](https://www.github.com/phuyalgaurav90)
