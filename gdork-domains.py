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
    parser.add_argument("-t","--tld",help="google TLD (optional)",default="com")
    args = parser.parse_args()

    if args.file is None and args.dork is None:
        parser.print_help()
        exit()

    domains = open('./result.txt', 'a')

    # if dorks file 
    if args.file is not None:
        dorks = open(args.file, 'r')

        # Get domains for dorks file
        for dork in dorks:
            scrape(dork, args, domains)
        dorks.close()

    # if single dork is given
    else:
        scrape(args.dork, args, domains)
        
    domains.close()


# Scrape domains from google results
def scrape(dork, args, domains):
    print(dork)
    for url in search(dork, tld=args.tld, lang="en",num=args.no_domains, start=0, stop=None, pause=2):
        ext = tldextract.extract(url)
        domain = f'{ext.subdomain}.{ext.domain}.{ext.suffix}\n'
        print(domain)
        domains.write(domain)

if __name__ == '__main__':
    main()