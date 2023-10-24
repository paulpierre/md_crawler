import argparse
from markdown_crawler import (
    md_crawl,
    DEFAULT_TARGET_LINKS,
    BANNER
)

def main():
    print(BANNER)
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--max-depth', '-d', required=False, default=3, type=int, help='Max depth of child links to crawl')
    arg_parser.add_argument('--num-threads', '-t', required=False, default=5, type=int, help='Number of threads to use for crawling')
    arg_parser.add_argument('--base-dir', '-b', required=False, default='markdown', type=str, help='Base directory to save markdown files in')
    arg_parser.add_argument('--debug', '-e', required=False, type=bool, default=False, help='Enable debug mode')
    arg_parser.add_argument('--target-content', '-c', required=False, type=str, default=None, help='CSS target path of the content to extract from each page')
    arg_parser.add_argument('--target-links', '-l', required=False, type=str, default=DEFAULT_TARGET_LINKS, help='CSS target path containing the links to crawl')
    arg_parser.add_argument('--valid-paths', '-v', required=False, type=str, default=None, help='Comma separated list of valid relative paths to crawl, (ex. /wiki,/categories,/help')
    arg_parser.add_argument('--domain-match', '-m', required=False, type=bool, default=True, help='Crawl only links that match the base domain')
    arg_parser.add_argument('--base-path-match', '-p', required=False, type=bool, default=True, help='Crawl only links that match the base path of the base_url specified in CLI')
    arg_parser.add_argument('base_url', type=str, help='Base URL to crawl (ex. 🐍🎷 https://rickandmorty.fandom.com/wiki/Evil_Morty')
    if len(arg_parser.parse_args().__dict__.keys()) == 0:
        arg_parser.print_help()
        return
    # ----------------
    # Parse target arg
    # ----------------
    args = arg_parser.parse_args()

    md_crawl(
        args.base_url,
        max_depth=args.max_depth,
        num_threads=args.num_threads,
        base_dir=args.base_dir,
        target_content=args.target_content.split(',') if args.target_content and ',' in args.target_content else None,
        target_links=args.target_links.split(',') if args.target_links and ',' in args.target_links else [args.target_links],
        valid_paths=args.valid_paths.split(',') if args.valid_paths and ',' in args.valid_paths else None,
        is_domain_match=args.domain_match,
        is_base_path_match=args.base_match,
        is_debug=args.debug
    )


# --------------
# CLI entrypoint
# --------------
if __name__ == '__main__':
    main()