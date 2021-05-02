# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:11:03 2021

@author: Will Ponton
main.py
guid_generator project
"""

# import libraries
import guid_generator as g_gen
import random as rand

# main function
def main():
    print("Hello world!  from main()")
    guid_test = g_gen.guid_hex_generate()
    print("Testing the GUID generator {}".format(guid_test))

    return 0

# control  initiating event
if __name__ == '__main__':
    main()


