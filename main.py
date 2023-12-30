import argparse
import uuid
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import requests
import colorama

def main():
    art = colorama.Fore.RED + """
    `""*$b..
         ""*$o.
             "$$o.
               "*$$o.        -coded by @Meed_Man-
                  "$$$o.
                    "$$$$bo...       ..o:
                      "$$$$$$$$booocS$$$    ..    ,.
                   ".    "*$$$$SP     V$o..o$$. .$$$b
                    "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
              ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
                 "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
                   "$$$o.4$$$$$$$$X
                    "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                           .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                          $$P""V$$$$$$$:    .        ""*****"
                        .*"    A$$$$$$$$o.4;      .
                             .oP""   "$$$$$$b.  .$;
                                      A$$$$$$$$$$P
                                      "  "$$$$$P"
                                          $$P*"
                                         .$
                                         "
    """ + colorama.Fore.RESET

    print(art)

    parser = argparse.ArgumentParser()
    parser.add_argument('-test', action='store_true', help='start')

    args = parser.parse_args()

    retry_strategy = Retry(
        total=5,
        backoff_factor=0.1,
        status_forcelist=[500, 502, 503, 504],
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)

    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    while True:
        random_uuid = str(uuid.uuid4())
        url = f"https://chat.openai.com/share/{random_uuid}"

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'}

        response = session.get(url, headers=headers)

        def get_resp():
            resp = session.get(url, headers=headers)
            if resp.status_code == 200:
                print(colorama.Fore.GREEN + f"[+] Successfully shared chat! : {url}" + colorama.Fore.RESET)
            else:
                print(colorama.Fore.RED + f"[-] Failed: {resp.status_code} - {url}" + colorama.Fore.RESET)

        get_resp()

        if args.test:
            test_url = "https://chat.openai.com/share/a0964cb3-fb6d-48f4-9f06-0b78de1e226e"

            test_response = session.get(test_url, headers=headers)

            def get_test_resp():
                test_resp = session.get(test_url, headers=headers)
                if test_resp.status_code == 200:
                    print(colorama.Fore.GREEN + f"[+] Successfully shared chat! : {test_url}" + colorama.Fore.RESET)

            get_test_resp()

if __name__ == "__main__":
    main()

