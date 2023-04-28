# username_generator.py
## Options
| Option | Use |
|---|---|
| -n, --name | Name to generate usernames from |
| -N, --name-wordlist | List of names file |
| -k, --keywords | Keywords to be used with names |
| -s, --separators | Characters to be used in generated username as separators, default ['.', '-', '_', '+'] |

## Basic usage
`python ./username_generator.py -n "John Smith"` will generate usernames from the name "John Smith":
```
john
johnsmith
jsmith
john.smith
j.smith
...
```

### Separators
`python ./username_generator.py -n "John Smith" -s '.' '-'` will generate usernames from the name "John Smith" using separators '.' and '-':
```
john
johnsmith
...
john.smith
j.smith
...
john-smith
j-smith
...#z
```


## Wordlist 
`python ./username_generator.py -N wordlist.lst` will generate usernames from names specified in the provided wordlist. One name per row.

## Keywords
`python ./username_generator.py -n "John Smith" -k 1990 megasoft` will generate usernames with keywords at the begining and the end of generated names. __(use with caution this can result in large number of usernames)__

