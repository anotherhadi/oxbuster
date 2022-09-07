# 0xMenu  <img width="60px" src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif">

A Handy Script for Finding Website Directories using Wordlists

# Installation :

From pip :

```bash
pip3 install oxbuster
```

From source :

```bash
git clone https://github.com/0x68616469/oxbuster/
```

### Requirements :

[oxansi](https://github.com/0x68616469/oxansi/)
[oxflags](https://github.com/0x68616469/oxflags/)
(downloaded automatically with pip)

# Arguments :

|     | Option          | Description               | Default |
| --- | --------------- | ------------------------- | ------- |
| -u  | --url           | Choose Target URL         |         |
| -w  | --wordlist      | WordList path             |         |
| -o  | --output        | Write in output path      | False   |
| -v  | --verbose       | Verbose mode              | False   |
| -f  | --full-url      | Print the entire URL      | False   |
| -t  | --target        | Choose Target Status Code | 200     |
| -s  | --suffix        | Suffix (.html/.php...)    | None    |
| -sl | --show-length   | Print content length      | False   |
| -fl | --filter-length | Filter by content length  | False   |
| -ro | --robots-txt    | Search for robots.txt     | False   |

# Example :

```bash
oxbuster -u localhost:8080 -w wordlist.txt
```

result :

<img src="https://media.giphy.com/media/sFeiGMQeyPRXTSxCWd/giphy.gif" />

## Wordlists

- [Node-Dirbuster WordLists](https://github.com/daviddias/node-dirbuster/tree/master/lists)
- [Dirbuster-ng](https://github.com/digination/dirbuster-ng/tree/master/wordlists)
- [KaliLists](https://github.com/3ndG4me/KaliLists/blob/master/wfuzz/webservices/ws-dirs.txt)
- [Web wordlists in 2021](https://blog.sec-it.fr/en/2021/03/02/web-wordlists/)

<hr>

![Follow me](https://img.shields.io/badge/-Follow%20Me-222222?logo=twitter&logoColor=black&color=272838&labelColor=C09891&style=for-the-badge&logoWidth=30&link=https://twitter.com/0x68616469)