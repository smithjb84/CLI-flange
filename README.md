# CLI-flange

Command line interface to look up standard flange dimensions

## Installation

install using git or download and extract the zip file

```bash
git clone https://github.com/smithjb84/CLI-flange.git
```

## Requirements

```bash
pip install rich
```

## Usage

```bash
python flange.py 28 300 -s a
```
* Positional arg 1 = Nominal Flange Size
* Positional arg 2 = Flange Class
* -s (--series) = Flange Series [a or b] (defaults to a if no arg)

If you want to run without the need to specify python then add a reference to the folder path in your environment variables

```bash
flange 28 300 -s a
```

## To do
* Add ASME B16.5 for smaller ASME Flange Sizes
* Add other Standards

## License

[MIT](https://choosealicense.com/licenses/mit/)
