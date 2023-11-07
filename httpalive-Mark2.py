import requests


print('''
      

██╗░░██╗████████╗████████╗██████╗░░░░░░░░█████╗░██╗░░░░░██╗██╗░░░██╗███████╗
██║░░██║╚══██╔══╝╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██║░░░░░██║██║░░░██║██╔════╝
███████║░░░██║░░░░░░██║░░░██████╔╝█████╗███████║██║░░░░░██║╚██╗░██╔╝█████╗░░
██╔══██║░░░██║░░░░░░██║░░░██╔═══╝░╚════╝██╔══██║██║░░░░░██║░╚████╔╝░██╔══╝░░
██║░░██║░░░██║░░░░░░██║░░░██║░░░░░░░░░░░██║░░██║███████╗██║░░╚██╔╝░░███████╗
╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░░░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝
      
        Author   : Aashish💕💕  
                                              
        Github   : https://github.com/aashish36
        
        Just wait things takes time.................
        
        Output will be in the form bellow😎😎
        
        {status-code}--{content-size}---> {url}
        
      ''')

def httpAlive(urlfile):
  
  attempts=0
  
  with open(urlfile,"r") as subdomains:

    for subdomain in subdomains:

        try:

            subdomain = subdomain.strip("\n")

            if subdomain[0:5]=="https" or subdomain[0:7]=="http://":
                  
                  url=subdomain

            else:
                  
                  url="https://{}".format(subdomain)

            request=requests.get(url)

            statusCode=request.status_code

            if statusCode== 200:
               
               content_length = request.headers.get('Content-Length')

               if content_length is not None:
                   
                   print("{} --{}---> {}".format(statusCode,content_length,subdomain))

               else:
                   
                   print("{} --{}---> {}".format(statusCode,len(request.content),subdomain))

            else:
               
               print("{} --{}---> {}".format(statusCode,len(request.content),subdomain))
                      
               
        except:

            pass

        attempts +=1


list="waymore.txt"

httpAlive(list)