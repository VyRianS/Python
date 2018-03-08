#!/usr/bin/python3.6

# COMMAND LINE PARSER

def parse(string):

  # Create dicts and lists
  VALID_OPTIONS = {}
  DISCARDED_OPTIONS = []

  # Before splitting, neutralize all white spaces
  string = string.strip()
  TOKEN_LIST = string.split(' ')

  # Remove first argument, usually the script or binary name
  if len(TOKEN_LIST) > 1:
    TOKEN_LIST.pop(0)
    for token in TOKEN_LIST:
      if len(token) > 1 and  token[0] == '-' or token[0:2] == '--':
        # Check for arguments or parse for '='
        SPLIT_LIST = token.split('=')
        if len(SPLIT_LIST) == 1:
          VALID_OPTIONS[SPLIT_LIST[0]] = None
        else:
          VALID_OPTIONS[SPLIT_LIST[0]] = SPLIT_LIST[1]
      else:
        DISCARDED_OPTIONS.append(token)
  else:
    print('No options or arguments detected.')
    return None

  # Load options into respective pools

  #print('Tokens:', TOKEN_LIST) 
  #print('Discarded:', DISCARDED_OPTIONS)
  #print('Valid options:', VALID_OPTIONS)
  return VALID_OPTIONS # Return dictionary for further processing

if __name__ == '__main__':
  user_input = input('Command line:')
  print(parse(user_input))

