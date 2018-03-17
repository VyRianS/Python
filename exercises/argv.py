#!/usr/bin/python3.6

# ARGV.PY
# My attempt to create an argument parsing system similar to the original DOOM's m_argv.c
# CheckParam() returns the argument position offset by 1
# If no parameter is found, returns 0

def CreateArgList( argstring ):
    return argstring.split(' ')

def CheckParam( parameter, arglist ):
    for i in range(len(arglist)):
        if arglist[i] == parameter:
            return i+1 # Arguments are listed beginning with 1 ...
    return 0

def StartDebug():
    print('Starting debug ...')

def DisplayVersion():
    print('Version 3.01')

if __name__ == '__main__':
    cmdargs = CreateArgList('-s --version -trace -debug')
    if CheckParam('-debug', cmdargs):
        StartDebug()
    if CheckParam('--version', cmdargs):
        DisplayVersion()
