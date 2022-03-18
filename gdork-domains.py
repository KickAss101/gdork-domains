#! /usr/bin/python3

from googlesearch import search
import tldextract
import argparse

def main():
    usage = '''
    gdork-domains -f <file> -n <no-of-domains>
    gdork-domains -d <dork> -n <no-of-domains> -t <google-top-level-domain>
    '''

    # Command line arguments
    parser =  argparse.ArgumentParser(usage=usage)
    parser.add_argument("-f","--file",help="provide file with list of dorks")
    parser.add_argument("-d","--dork",help="provide single dork")
    parser.add_argument("-n","--no-domains",help="Number of domains to enumerate (optional)",type=int,default=50)
    parser.add_argument("-t","--tld",help=" (optional)",type=str,default="com")
    args = parser.parse_args()

    if args.file is None and args.dork is None:
        parser.print_help()
        exit()

    domains = open('./result.txt', 'w')

    # if dorks file 
    if args.file is not None:
        dorks = open(args.file, 'r')

        # Get all domains
        for dork in dorks:
            print(dork)
            scrape(dork, args, domains)

    # if single dork is given
    else:
        scrape(dork, args, domains)
        
    domains.close()
    dorks.close()

# Scrape domains from google results
def scrape(dork, args, domains):
    for url in search(dork, tld=args.tld, lang="en",num=args.no_domains, start=0, stop=None, pause=2):
        ext = tldextract.extract(url)
        domain = f'{ext.domain}.{ext.suffix}\n'
        print(domain)
        domains.write(domain)

if __name__ == '__main__':
    main()