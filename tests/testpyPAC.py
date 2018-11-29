import os

import pypac


# PyPAC découvrira automatiquement les paramètres du fichier PAC
pac = pypac.get_pac(url='http://127.0.0.1:9000/localproxy.pac')

# On récupère le proxy associé à Cloudant (idem, on aurait pu utiliser n'importe quelle autre URL)
proxies = pac.find_proxy_for_url('https://rest.apisandbox.zuora.com', 'zuora.com')
#proxies = pac.find_proxy_for_url('https://www.google.com', 'google.com')

# Ce qui retourne quelque chose comme : 'PROXY 4.5.6.7:8080; PROXY 7.8.9.10:8080'
# On prend la premier résultat :
proxy = 'http://{}/'.format(proxies.split()[1].rstrip(';'))

# On injecte les valeurs dans les variables d'environnement
os.environ['HTTP_PROXY'] = os.environ['HTTPS_PROXY'] = proxy