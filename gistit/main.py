#!/usr/bin/env python3

import atexit
import argparse
import os
import platform
import sys

import gistit.creator

def stop_for_windows():
    ''' If on windows platform, stop and wait for input
    '''
    if os.name == 'nt' or platform.system() == 'Windows':
        input('Press Enter or Close the window to exit !')

def main():
    ''' Main Function '''
    atexit.register(stop_for_windows)
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, dest="file",
                        help="Use the specified file")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-r", "--private", required=False, action='store_true',
                       dest="private", help='Make the gist private')
    group.add_argument("-u", "--public", required=False, action='store_true',
                       dest="public", help='Make the gist public (DEFAULT)')
    args, otherthings = parser.parse_known_args()

    content_to_post = ''
    filename = None
    if args.file:
        filename = args.file
        content_to_post = get_file_content(filename)
    elif len(otherthings) > 0:
        filename = otherthings[0]   #TODO: Add support for full filelist
        content_to_post = get_file_content(filename)
    else:
        input_list = sys.stdin.readlines()
        content_to_post = "".join(input_list)

    public = True   #args.public
    if args.private:
        public = False
    try:
        print('Uploading...')
        creator_obj = gistit.creator.Creator()
        jsoon = creator_obj.create(content_to_post, public=public, filename=filename)
    except:
        print('Unexpected Error:', sys.exc_info()[0])
        print('Details:', sys.exc_info()[1])
        return -1
    #print(jsoon)
    if 'html_url' in jsoon.keys():
        print('Upload Successful: ')
        print(jsoon['html_url'])
    else:
        return -2
    return 0

def get_file_content(filename):
    # Check that file conforms size limit of 1MB
    statinfo = os.stat(filename)
    if statinfo.st_size < 1000000:
        fhan = open(filename, 'rU')
        content = fhan.read()
        fhan.close()
    else:
        print('ERROR: File size exceeds specified limit of 1MB')
        sys.exit(-1)
    return content


if __name__ == '__main__':
    try:
        return_code = main()
        sys.exit(return_code)
    except KeyboardInterrupt:
        print('\nClosing garacefully :)', sys.exc_info()[1])
    except SystemExit:
        pass
    except:
        print('Unexpected Error:', sys.exc_info()[0])
        print('Details:', sys.exc_info()[1])
        #raise

