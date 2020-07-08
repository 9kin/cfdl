"""Console script for codeforces2html."""
import argparse
from argparse import RawTextHelpFormatter

from codeforces2html import codeforces2html, pdf, xhr
from codeforces2html.models import clean
from codeforces2html.utils import clean_contests, clean_tasks, problemset

# cf download 1365-1367 1362A     (xhr support aiohttp !!!!!!!!!!!!)
# --pdf (generate pdf)    outfile update
# --refresh           not updated if task  in db
# --debug             +-
# --lang=ru         (translate)      -
# cf update         (git  update)    -
# cf pdf 1365-1367 1362A
#
# TODO xhr запрос на мини сервер когда закрытие
# "~/.cf/config" (как в flask-shop)
# 200 status code
# todo  1365
#


def download(arguments, debug=True, generate_pdf=False):
    download_contests = set()
    download_tasks = set()

    for argument in arguments:
        if "-" in argument:
            start, end = map(int, argument.split("-"))
            for contest_id in range(start, end + 1):
                download_contests.add(contest_id)
        elif not argument.isdigit():
            for i, char in enumerate(argument):
                if not char.isdigit():
                    if int(argument[:i]) not in download_contests:
                        download_tasks.add(argument)
                    break
        else:
            download_contests.add(int(argument))

    download_contests = clean_contests(download_contests)
    download_tasks = clean_tasks(list(download_tasks))
    codeforces2html.main(download_contests, download_tasks, debug=debug)
    xhr.main(download_contests, download_tasks, debug=debug)
    if generate_pdf:
        pdf.pdf(download_contests, download_tasks)


if __name__ == "__main__":

    arg_parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
    arg_parser.add_argument(
        "--download",
        default=False,
        action="store_true",
        help="download contest and tasks",
    )
    arg_parser.add_argument(
        "specifier",
        nargs="*",
        help="contest       1365\ncontest-range 1350-1356\ntask          1365A",
    )

    arg_parser.add_argument(
        "-d",
        "--debug",
        default=True,
        action="store_false",
        help="show progress bar",
    )

    arg_parser.add_argument(
        "--pdf", default=False, action="store_true", help="generate pdf",
    )

    args = arg_parser.parse_args()
    if "download" in args.specifier:
        args.specifier.remove("download")
    print(args)
    # clean()
    # if args.download:
    #    download(args.specifier, args.debug, args.pdf)
