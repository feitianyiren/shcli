[![Build Status](https://travis-ci.org/jaywink/shcli.svg?branch=master)](https://travis-ci.org/jaywink/shcli) [![codecov.io](https://codecov.io/github/jaywink/shcli/coverage.svg?branch=master)](https://codecov.io/github/jaywink/shcli?branch=master) [![Dependency Status](https://gemnasium.com/badges/github.com/jaywink/shcli.svg)](https://gemnasium.com/github.com/jaywink/shcli)

[![PyPI version](https://badge.fury.io/py/shcli.svg)](https://pypi.python.org/pypi/shcli)  [![Documentation Status](http://readthedocs.org/projects/shcli/badge/?version=latest)](http://shcli.readthedocs.io/en/latest/?badge=latest) [![PyPI](https://img.shields.io/pypi/pyversions/shcli.svg?maxAge=2592000)](https://pypi.python.org/pypi/shcli) [![PyPI](https://img.shields.io/pypi/l/shcli.svg?maxAge=2592000)](https://pypi.python.org/pypi/shcli)

[![chat on freenode](https://img.shields.io/badge/chat-on%20freenode-brightgreen.svg)](http://webchat.freenode.net?channels=%23socialhome&uio=d4) [![Chat on Gitter](https://badges.gitter.im/Socialhome/Lobby.svg)](https://gitter.im/Socialhome/Lobby) [![chat on matrix](https://img.shields.io/badge/chat-on%20matrix-orange.svg)](https://riot.im/app/#/room/#socialhome:matrix.org)

# shcli

Python client for [Socialhome](https://socialhome.network).

## Introduction

Interact with your Socialhome account using the `shcli` client. This library will provide a CLI utility and a Python API. 

## Status

Alpha.

## Installation

    pip install shcli
    
## Usage

### Creating content
  
    import shcli
    
    shcli.create("socialhome domain", "api token", "text", "visibility")
  
Visibility parameter can be one of `public`, `limited`, `site` or `self`.

Returns the created `Content` object as JSON.

## License

[MIT](https://www.tldrlegal.com/l/mit)

## Author

Jason Robinson / https://jasonrobinson.me / https://github.com/jaywink
