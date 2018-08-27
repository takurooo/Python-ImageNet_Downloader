#-------------------------------------------
# import
#-------------------------------------------
import os
import argparse
import downloader

#-------------------------------------------
# global
#-------------------------------------------


#-------------------------------------------
# functions
#-------------------------------------------
def arg_parser():
    parser = argparse.ArgumentParser(description="Download images from ImageNet.")
    parser.add_argument("wnid", type=str, help="download wnid")
    parser.add_argument("-root", type=str, help="root dir", default=None)
    parser.add_argument("-limit", type=int, help="max save num", default=0)
    parser.add_argument("-r", "--recursive", action='store_true', help="save recursive")
    parser.add_argument("-v", "--verbose", action='store_true', help="show process message")

    return parser

def main(args):
    root_dir = args.root or os.getcwd()
    wnid = args.wnid
    verbose = args.verbose
    limit = args.limit

    api = downloader.ImageNet(root_dir)

    if not args.recursive:
        api.download(wnid, limit=limit, verbose=verbose)
    else:
        wnids = api.wnid_children(wnid, recursive=True)
        for _wnid in wnids:
            api.download(_wnid, limit=limit, verbose=verbose)

#-------------------------------------------
# main
#-------------------------------------------
if __name__ == '__main__':
    parser = arg_parser()
    args = parser.parse_args()
    main(args)
