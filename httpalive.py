import requests

import colorama

import random

from colorama import Fore, Back, Style

colorama.init(autoreset=True)

import argparse

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

red = Fore.RED

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

colors = [magenta,cyan,mixed,red,blue,yellow, white]

random_color = random.choice(colors)

bold = Style.BRIGHT

def banner():

    print(f'''{bold}{random_color}

██╗░░██╗████████╗████████╗██████╗░░░░░░░░█████╗░██╗░░░░░██╗██╗░░░██╗███████╗
██║░░██║╚══██╔══╝╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██║░░░░░██║██║░░░██║██╔════╝
███████║░░░██║░░░░░░██║░░░██████╔╝█████╗███████║██║░░░░░██║╚██╗░██╔╝█████╗░░
██╔══██║░░░██║░░░░░░██║░░░██╔═══╝░╚════╝██╔══██║██║░░░░░██║░╚████╔╝░██╔══╝░░
██║░░██║░░░██║░░░░░░██║░░░██║░░░░░░░░░░░██║░░██║███████╗██║░░╚██╔╝░░███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝
      
        Author   : Aashish💕💕  
                                              
        Github   : https://github.com/aashish36
          
        httpAlive is a tool designed to efficiently probe for alive subdomains and Urls from a provided list.
          
      ''')


parser=argparse.ArgumentParser(description=f"{bold}{random_color}httpAlive is a tool designed to efficiently probe for alive subdomains and Urls from a provided list.")
parser.add_argument('-l','--DomainList',metavar='list',type=str,required=True,help=f"[{bold}{random_color}INFO]: {bold}{random_color}List of Subdomains or URLs.")
parser.add_argument('-o','--output',metavar='output',type=str,default="output.txt",required=False,help=f"[{bold}{random_color}INFO]: {bold}{random_color}File to save our output.")
args=parser.parse_args()
DominList=args.DomainList
output=args.output

global_output=[]


def httpAlive(urlfile):
  
  banner()
  attempts=0
  global global_output
  
  with open(urlfile,"r") as subdomains:

    for subdomain in subdomains:

        try:

            subdomain = subdomain.strip("\n")

            if subdomain[0:5]=="https" or subdomain[0:7]=="http://":
                  
                  url=subdomain

            else:
                  
                  url="https://{}".format(subdomain)

            request=requests.get(url,timeout=10)

            statusCode=request.status_code

            if statusCode== 200:
               
               content_length = request.headers.get('Content-Length')

               if content_length is not None:
                   
                   print(f"{bold}{green}(Status: {statusCode}) --[Size: {content_length}]---> {subdomain}")
                   global_output.append(f"(Status: {statusCode}) --[Size: {content_length}]---> {subdomain}\n")

               else:
                   
                   print(f"{bold}{green}(Status: {statusCode}) --[Size: {len(request.content)}]---> {subdomain}")
                   global_output.append(f"(Status: {statusCode}) --[Size: {len(request.content)}]---> {subdomain}\n")

            else:
               
                print(f"{bold}{random_color}(Status: {statusCode}) --[Size: {len(request.content)}]---> {subdomain}")
                global_output.append(f"(Status: {statusCode}) --[Size: {len(request.content)}]---> {subdomain}\n")
                
        except:
            pass

        attempts +=1


def saveOutput(output):
    with open(output,'w') as file:
        file.write('\n'.join(global_output))
        



def main():
        httpAlive(DominList)
        saveOutput(output)   


if __name__ == "__main__":
    main()
