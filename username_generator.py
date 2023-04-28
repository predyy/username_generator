#!/usr/bin/python3

# Script for generating usernames for bruteforcing from given name
# Author: predyy

import argparse

def add_keywords(name, keywords, separators):
    names_with_keywords = []
    for keyword in keywords:
        for separtor in separators:
            names_with_keywords.append(name + separtor + keyword)
            names_with_keywords.append(keyword + separtor + name)

    return names_with_keywords

def get_transformations(name, keywords, separators):
    names = []
    
    names.append(name[0])    
    for separator in separators:
        names.append(separator.join(name))
        names.append(name[0][0] + separator + name[-1])    

    if (keywords):
        names_with_keywords = []
        for generated_name in names:
            names_with_keywords += add_keywords(generated_name, keywords, separators)
        names = names + names_with_keywords
        
    return names

def get_and_print_transformations(name, keywords, separators):    
    print('\n'.join(get_transformations(name, keywords, separators)))
    name.reverse()
    print('\n'.join(get_transformations(name, keywords, separators)))

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', metavar='name', help='First and last name eg. "Joe Doe".')
parser.add_argument('-N', '--name-wordlist', metavar='name_wordlist', help='Fist and last name wordlist, one name per row')
parser.add_argument('-k', '--keywords', metavar='keywords', nargs="+", help='Personal keywords such as years, bussines name etc.')
parser.add_argument('-s', '--separators', metavar='separators', nargs="+", default=['.', '-', '_', '+'], help='Characters to be used as first and last name separators eg. \'.\' \'_\' -> fisrt.name, first_name')

args = parser.parse_args()

separators = args.separators
separators.insert(0, '')

keywords = args.keywords

if (args.name):
    name = args.name.lower().split()
    get_and_print_transformations(name, keywords, separators)
elif (args.name_wordlist):
    name_wordlist = args.name_wordlist
    with open(name_wordlist, "r") as wordlist:
        lines = wordlist.readlines()
        for line in lines:
            get_and_print_transformations(line.lower().split(), keywords, separators)
else:
    print("Please provide name or list of names file")