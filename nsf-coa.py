#! /usr/bin/env python

import ads, re, csv
from nameparser import HumanName
from argparse import ArgumentParser

# Read token from token.txt, so that we don't need to put the token in the script
#
def ReadToken(tokenfile='token.txt'):
    with open(tokenfile,'r') as f:
        token=f.readline()
    return token

# choose the best name from the similar names
#
def choose_best(names):
    lengths = [len(n.original) for n in names]
    longest = 0
    best = None
    for n, l in zip(names, lengths):
        if l > longest:
            best = n
    #print(f'out of {[name.original for name in names]}, choose {n.original}')
    return n

# compare the names
#
def almost_equal(name1, name2):
    return name1.last.lower() == name2.last.lower() and name1.first[0].lower() == name2.first[0].lower()

# query_papers by author and year
#
def query_papers(author, years):
    papers  = []
    for y in years:
        papers=papers+list(ads.SearchQuery(author=author,year=y, fl=['author', 'title', 'aff']))
    return papers

# TODO: get more info
# get the author and aff info
#
def get_paper_info(papers):
    authors_aff = {}
    for paper in papers:
        authors = paper.author
        affs = paper.aff
        for i in range(len(authors)):
            authors_aff[authors[i]]=affs[i]
    authors_aff = dict(sorted(authors_aff.items()))
    return authors_aff

# remove name duplication
#
def remove_duplication(authors_aff, verbose=False):
    no_dups = {}
    previous = HumanName('Hello Dotty')
    to_compare = []
    if(verbose):
        print('')
        print('Compared names:')
    for author in authors_aff.keys():
        name = HumanName(author)
        if almost_equal(name, previous):
            if(verbose):
                print(f'{name}, {previous} being compared')
            to_compare.append(name)
        else:
            if len(to_compare) > 1:
                no_dups[choose_best(to_compare)]=authors_aff[author]
                to_compare = []
            else:
                no_dups[name]=authors_aff[author]
                to_compare = []
        previous = name
    if(verbose):
        print('')
    return no_dups

# TODO: populate other tables
# write the data into table-4
#
def write_table4(no_dups, filename='coa_table_4.csv'):
    f=open(filename,'w')
    writer = csv.writer(f)
    writer.writerow(['4', 'Name:', 'Organizational Affiliation', 'Optional  (email, Department)', 'Last Active'])
    for auth in no_dups.keys():
        writer.writerow(['A', '%s %s %s'%(auth.last, auth.middle, auth.first), no_dups[auth],' ',' '])
    f.close()

def main():
    parser = ArgumentParser(description="Usage for NSF COA file population")
    parser.add_argument("--author",type=str, dest="author", help="author name")
    parser.add_argument("--year",type=str, dest="year", help="year range. For example, 2018-2023")
    parser.add_argument("--fn",type=str, dest="fn", default='coa_table_4.cvs', help="output file name. By default, it's `coa_table_4.cvs`.")
    parser.add_argument("--verbose", dest="verbose",action="store_true", default=False, help="print out information")
    opts = parser.parse_args()
    ads.config.token = ReadToken()
    # get auther name
    if(type(opts.author) == 'NoneType'):
        print('Please specify the auther name.')
        return

    #generate the year list
    ystr = opts.year.split('-')
    if(len(ystr) == 1):
        year = ystr
    else:
        year = []
        for y in range(int(ystr[1]), int(ystr[0])-1, -1):
            year.append(str(y))
    
    papers = query_papers(opts.author, year)
    if(opts.verbose):
        print('Paper Number: %d'%len(papers))
        print('Paper List:')
        for p in papers:
            print(p.title)
    authors_aff = get_paper_info(papers)
    no_dups = remove_duplication(authors_aff, opts.verbose)
    write_table4(no_dups, opts.fn)
    print('Done!')

if __name__ == "__main__":
    main()