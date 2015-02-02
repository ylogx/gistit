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
    # Run this function everytime on exit
    atexit.register(stop_for_windows)
    # Parse command line arguments
    #usage = "%prog [-f credential_file]"
    #parser = ArgumentParser(usage=usage)
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, dest="file",
            help="Use the specified file")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-r", "--private", required=False, action='store_true',
            dest="private", help='Make the gist private')
    group.add_argument("-u", "--public", required=False, action='store_true',
            dest="public", help='Make the gist public (DEFAULT)')
    #parser.add_argument('otherthings', nargs='*')
    #args = parser.parse_args()
    args, otherthings = parser.parse_known_args()

    if args.file:
        filename = args.file
    elif len(otherthings) > 0:
        #TODO Add support for full filelist
        filename = otherthings[0]
    else:
        print('FATAL: Filename not specified')
        return -1
    # Check that file conforms size limit of 1MB
    statinfo = os.stat(filename)
    if statinfo.st_size < 1000000:
        fhan = open(filename, 'rU')
        file_content = fhan.read()
        fhan.close()
    else:
        print('ERROR: File size exceeds specified limit of 1MB')
        return -1
    public = True   #args.public
    if args.private:
        public = False
    print('Uploading...')
    creator_obj = gistit.creator.Creator()
    jsoon = creator_obj.create(file_content, public=public, filename=filename)
    #print(jsoon)
    if 'html_url' in jsoon.keys():
        print('Uploaded to the url: ', jsoon['html_url'])

if __name__ == '__main__':
    try:
        return_code = main()
        sys.exit(return_code)
    except KeyboardInterrupt:
        print('\nClosing garacefully :)', sys.exc_info()[1])
    #TODO: Handle other errors
    except SystemExit:
        pass
    except:
        print('Unexpected Error:', sys.exc_info()[0])
        print('Details:', sys.exc_info()[1])
        raise

