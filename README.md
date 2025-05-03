# Purr API

> ⚠️ **Disclaimer**: This is an unofficial community wrapper for the PurrBot API. It is not affiliated with or endorsed by the PurrBot team.

A Python wrapper for the PurrBot API (api.purrbot.site). This package provides an easy-to-use interface to interact with the PurrBot API endpoints.

## Installation

You can install the package using pip:

```bash
pip install purr-api
```

## Usage

Here's a simple example of how to use the package:

```python
from purr_api import Purr

# Initialize the client
purr = Purr()

# Get a random SFW image
angry_gif = purr.img.sfw.angry.get()
print(angry_gif)  # Prints the URL of a random angry GIF

# Use the owoify endpoint
owo_text = purr.owoify.get()
print(owo_text)  # Prints owoified text
```

## Features

- Access to all PurrBot API endpoints
- Simple and intuitive interface
- Support for both SFW and NSFW endpoints
- Owoify text transformation

## Documentation

For detailed documentation, please refer to the [PurrBot API documentation](https://api.purrbot.site/docs).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
