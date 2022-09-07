####################################################################
#           ______________________________________
#  ________|               0xBuster               |_______
#  \       |                                      |      /
#   \      |              @0x68616469             |     /
#   /      |______________________________________|     \
#  /__________)                                (_________\
#
# A Handy Script for Finding Website Directories using Wordlists
#
# Github repo : https://github.com/0x68616469/oxbuster
#
####################################################################

import requests, sys, os, time
from oxflags import Flag
from oxansi import Short as a

def format_url(url):
    print(f"{a.b}[{a.g}?{a.b}] {a.rst}Formating url \"{a.c}{url}{a.rst}\"")
    if not url.startswith("https://") and not url.startswith("http://"):
        url = "https://" + url
    if not url.endswith("/"):
        url = url + "/"
    print(f"{a.b}> {a.rst}{url}")
    return url

def parse_wordlist(path):
    print(f"{a.b}[{a.g}?{a.b}] {a.rst}Parsing WordList \"{a.c}{path}{a.rst}\"")
    try:
        with open(path) as file:
            wordlist = file.read().strip().split('\n')
        print(f"{a.b}> {a.rst}Done {a.b}({len(wordlist)} results){a.rst}")
        return wordlist
    except IOError:
        print(f"{a.b}[{a.r}!{a.b}] {a.rst}Error while parsing WordList \"{a.c}{path}{a.rst}\"")
        sys.exit(1)

def status_url(url):
    try:
        response = requests.get(url)
    except Exception:
        print(f"{a.b}[{a.r}!{a.b}] {a.rst}Error unexpected while reaching \"{a.c}{url}{a.rst}\"")
        sys.exit(1)
    return response

def progress_bar(i, length):
    print(a.sc, end="")
    print(f"{a.mv(2,0)}{a.b}", end="")
    percent = int(i / length * os.get_terminal_size().columns)
    for hashtag in range(percent):
        print("#", end="")
    print(f"{a.rst}{a.rc}", end="")
    
def start_scan(flag):
    try:
        url = format_url(flag.url)
        wordlist = parse_wordlist(flag.wordlist)
        target = flag.target
        suffix = flag.suffix
        length = len(wordlist)
        print(f"{a.clr}\033[H", end="")
        print(f"{a.b}", end="")
        for col in range(int((os.get_terminal_size().columns - 10) / 2)):
            print("-", end="")
        print(f"[{a.c}{a.bld}PROGRESS{a.rst}{a.b}]", end="")
        for col in range(int((os.get_terminal_size().columns - 10) / 2)):
            print("-", end="")   
        print(f"{a.rst}\n\n")
        if flag.output != False:
            try:
                file = open(flag.output, 'w')
            except:
                print(f"{a.b}[{a.r}!{a.b}] {a.rst}Error unexpected while opening \"{a.c}{flag.output}{a.rst}\"")
                sys.exit(1)
            
            file.write(f"[-] Dirbuster [By @0x68616469]\n")
            file.write("\n")
            file.write(f"- Target : {url}\n")
            file.write(f"- Wordlist : {flag.wordlist} ({length})\n")
            file.write(f"- Targeted status code : {flag.target}\n")
            file.write(f"- Verbose mode : {flag.verbose}\n")
            file.write(f"- Filter length : {flag.filterlength}\n")
            file.write(f"- Show length : {flag.showlength}\n")
            file.write(f"- Print full url : {flag.fullurl}\n")
            file.write(f"- Suffix : {flag.suffix}\n")
            file.write(f"- Output report : {flag.output}\n\n")
        print(f"{a.b}[{a.c}-{a.b}] {a.rst}Dirbuster {a.b}[By @0x68616469]{a.rst}")
        print()
        print(f"{a.b}[{a.b}-{a.b}] {a.rst}Target : {a.c}{url}{a.rst}")
        print(f"{a.b}[{a.b}-{a.b}] {a.rst}Wordlist : {a.c}{flag.wordlist}{a.rst} {a.b}({length}){a.rst}")
        print(f"{a.b}[{a.b}-{a.b}] {a.rst}Targeted status code : {a.c}{flag.target}{a.rst}")
        print(f"{a.b}[{a.b}-{a.b}] {a.rst}Verbose mode : {a.c}{flag.verbose}{a.rst}")
        print(f"{a.b}[{a.b}-{a.b}] {a.rst}Filter length : {a.c}{flag.filterlength}{a.rst}")
        print(f"{a.b}[{a.b}-{a.b}] {a.rst}Show length : {a.c}{flag.showlength}{a.rst}")
        print(f"{a.b}[{a.b}-{a.b}] {a.rst}Print full url : {a.c}{flag.fullurl}{a.rst}")
        print(f"{a.b}[{a.b}-{a.b}] {a.rst}Suffix : {a.c}{flag.suffix}{a.rst}")
        print(f"{a.b}[{a.b}-{a.b}] {a.rst}Output report : {a.c}{flag.output}{a.rst}")
        print(f"{a.b}[{a.c}...{a.b}] {a.rst}Start scanning in 3 seconds", end="")
        sys.stdout.flush()
        time.sleep(3)
        print(a.cll)

        if flag.robotstxt == True:
            try:
                response = requests.get(f"{url}robots.txt")
            except Exception:
                print(f"{a.b}[{a.r}!{a.b}] {a.rst}Error unexpected while reaching \"{a.c}{url}{a.rst}\"")
                sys.exit(1)
            if response.status_code == 200:
                print(f"{a.b}[{a.g}v{a.b}] {a.rst}Robots.txt :\n {a.b}{response.text}{a.rst}")
                if flag.output != False:
                    file.write(f"- Robots.txt :\n {response.text}\n")
            else:
                print(f"{a.b}[{a.r}x{a.b}] {a.rst}Robots.txt not found{a.rst}")
                if flag.output != False:
                    file.write("- Robots.txt not found\n")

        result = 0
        if suffix == None:
            suffix = ""
        for i in range(length):
            progress_bar(i, length)
            sys.stdout.flush()
            response = status_url(f"{url}{wordlist[i]}{suffix}")
            if response.status_code == int(target) or target == "*" or flag.verbose:
                if flag.filterlength != False or flag.showlength == True:
                    l = len(response.text)
                    if flag.filterlength == l:
                        continue
                result += 1
                if flag.fullurl == True:
                    print(f"{a.b}[{a.m}{response.status_code}{a.b}] {a.rst}{url}{wordlist[i]}{suffix}", end="")
                    if flag.output != False:
                        file.write(f"[{response.status_code}] {url}{wordlist[i]}{suffix}")
                else:
                    print(f"{a.b}[{a.m}{response.status_code}{a.b}] {a.rst}/{wordlist[i]}{suffix}", end="")
                    if flag.output != False:
                        file.write(f"[{response.status_code}] /{wordlist[i]}{suffix}")
                if flag.showlength == True:
                    print(f" {a.b}len:{l}{a.rst}", end="")
                    if flag.output != False:
                        file.write(f"len:{l}")
                
                if flag.output != False:
                    file.write("\n")        
                print()
        if flag.output != False:
            file.close()    
        print(f"\n{a.b}[{a.g}v{a.b}] {a.rst}Scan done, found {result} results !{a.rst}")
    except KeyboardInterrupt:
        print(f"\n{a.b}[{a.r}!{a.b}] {a.rst}Error, Keyboard Interrupt")
        sys.exit(1)

def main():
    flag = Flag(description="A Handy Script for Finding Website Directories using Wordlists")

    flag.new(short="-u", full="--url", required=True, help="Choose Target URL")
    flag.new(short="-w", full="--wordlist", required=True, help="WordList path")
    flag.new(short="-o", full="--output", default=False, type="string", help="Write in output path")
    flag.new(short="-v", full="--verbose", default=False, type="bool", help="Verbose mode")
    flag.new(short="-f", full="--full-url", default=False, type="bool", help="Print the entire URL")
    flag.new(short="-t", full="--target", default="200", help="Choose Target Status Code")
    flag.new(short="-s", full="--suffix", default=None, help="Suffix (.html/.php...)")
    flag.new(short="-sl", full="--show-length", default=False, type="bool", help="Print content length")
    flag.new(short="-fl", full="--filter-length", type="int", default=False, help="Filter by content length")
    flag.new(short="-ro", full="--robots-txt", type="bool", default=False, help="Search for robots.txt")

    flag.parse()

    start_scan(flag)

if __name__ == '__main__':
    main()
