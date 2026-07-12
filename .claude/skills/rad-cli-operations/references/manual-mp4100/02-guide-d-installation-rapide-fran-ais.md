# Guide d’installation rapide (français)

*Manual `Megaplex-4_4.91_Mn_07-26_GA.pdf`, pages 32–35.*


## Installation de l’unité  *(p.32)*


## Connexion des interfaces  *(p.32)*


## Connexion au terminal  *(p.32)*


## Connexion à l’alimentation  *(p.32)*

Guide d’installation rapide (français) 
Cette section décrit la configuration minimale nécessaire pour préparer le Megaplex-4 au 
fonctionnement. 
Installation de l’unité 
Suivez les étapes suivantes pour installer l'unité: 
1. Déterminez la configuration requise de le Megaplex-4  en fonction de votre application. 
2. Installez le boîtier du Megaplex-4. 
3. Installez les modules conformément au plan d'installation du site. 
4. Connectez le terminal ASCII au port CONTROL RS-232. 
5. Connectez l'alimentation à l'unité. 
Connexion des interfaces 
 Pour connecter les interfaces : 
1. Insérez les modules SFP (le cas échéant) dans les ports Ethernet correspondants basés sur SFP. 
2. Reportez-vous au plan d'installation du site et connectez les câbles prescrits aux modules 
Megaplex-4. 
Connexion au terminal 
 Pour connecter l'appareil à un terminal: 
1. Connectez un côté du câble fourni par RAD (CBL-DB9F-DB9M-STR pour le Megaplex-4100, CBL-
MUSB-DB9F pour le Megaplex-4104) au connecteur Megaplex, désigné CONTROL DCE. 
2. Connectez l'autre extrémité du câble terminal à l'équipement terminal ASCII. 
Connexion à l’alimentation 
Branchez d'abord le(s) câble(s) d'alimentation sur le connecteur du module PS, puis sur la prise de 
courant. Pour les câbles DC, faites attention à la polarité.Connect the power cable(s) first to the 
connector on the PS module, and then to the power outlet. For DC cables, pay attention to polarity. 

## Configuration de l'unité pour le management  *(p.33)*


## Démarrer une session de terminal pour la première fois  *(p.33)*

Configuration de l'unité pour le management 
Configurez Megaplex-4 pour le management, en utilisant un terminal basé sur ASCII local. 
Démarrer une session de terminal pour la première fois 
 Pour démarrer la session de terminal: 
1. Assurez-vous que tous les câbles et connecteurs de Megaplex-4 soient correctement connectés. 
2. Connectez le Megaplex-4 à un PC équipé d'une application d'émulation de terminal ASCII. 
Reportez-vous au chapitre Installation et Configuration pour plus de détails sur la connexion au 
port de contrôle. 
3. Connectez un terminal ASCII au connecteur CONTROL DCE du module CL actif (utilisez un câble 
droit). 
4. Démarrez le programme d'émulation de terminal PC et créez une nouvelle connexion de 
terminal. 
5. Configurez les paramètres du port de communication du PC sur un débit en bauds de 9,6 kbps, 8 
bits / caractère, 1 bit d'arrêt, pas de parité et pas de contrôle de flux. 
6. Si vous utilisez HyperTerminal, réglez le mode terminal sur le mode 132 colonnes pour une vue 
optimale des menus système (Properties> Settings> Terminal Setup> 132 column mode). 
7. Mettez l'unité sous tension. 
Remarque 
Les modules Megaplex-4 PS ne comportent pas d'interrupteur d'alimentation. 
Utilisez un interrupteur externe, par exemple le disjoncteur utilisé pour 
protéger les lignes électriques. 
8. Attendez la fin du processus d'initialisation de la mise sous tension. Pendant cet intervalle, 
surveillez les indications de mise sous tension : 
 
Après quelques secondes, le Megaplex-4 commence à décompresser son logiciel.  
 
Une fois la décompression terminée, tous les indicateurs s'éteignent pendant quelques 
secondes (à l'exception des indicateurs POWER) pendant que le Megaplex-4 effectue son 
initialisation de mise sous tension.  
Vous pouvez surveiller le processus de décompression et d'initialisation sur le terminal connecté 
au Megaplex-4.  
9. Lorsque le processus d'initialisation est terminé, vous êtes invité à appuyer sur <Enter> pour 
recevoir l'invite de connexion. 
10. Appuyez sur <Enter> jusqu'à ce que vous receviez l'invite de connexion. 

## Configuration du routeur  *(p.34)*


## Enregistrement de la configuration de management  *(p.34)*


## Enregistrement de la configuration  *(p.34)*

11. Si le nom d'utilisateur et le mot de passe par défaut du Megaplex-4 n'ont pas encore été 
modifiés, connectez-vous en tant qu'administrateur en utilisant su comme nom d'utilisateur (su 
pour la configuration complète et l'accès de surveillance) et 1234 pour le mot de passe. 
12. Tapez les commandes CLI nécessaires. 
13. Poursuivez la configuration du produit. 
 
Configuration du routeur  
Le routeur doit être configuré avec une interface de routeur qui est liée au SVI utilisé pour les flux de 
gestion, et une adresse IP doit lui être attribuée. De plus, une route statique doit être configurée pour la 
passerelle par défaut. 
Cette section illustre la configuration suivante : 
• 
Interface de routeur 1 : 
 
Lié au SVI 1 
 
Adresse IP 172.17.154.96 avec masque 255.255.255.0 
• 
Routeur : Route statique associée à l'adresse IP 172.17.154.1 (passerelle par défaut). 
 Pour définir le routeur : 
• 
Entrez les commandes suivantes : 
configure router 1 
interface 1 
bind svi 1 
# IP address 172.17.154.96 with mask 255.255.255.0 
address 172.17.154.96/24 
no shutdown 
exit 
# Default gateway 172.17.154.1 
static-route 0.0.0.0/0 address 172.17.154.1 
exit all 
Enregistrement de la configuration de management  
Enregistrement de la configuration 
Entrez save dans n'importe quel niveau pour enregistrer votre configuration dans startup-config.  

## Copie de la configuration utilisateur dans la configuration par défaut  *(p.35)*


## Vérification de la connectivité  *(p.35)*


## Configuration des services  *(p.35)*

Copie de la configuration utilisateur dans la configuration par défaut 
En plus d'enregistrer votre configuration dans startup-config, vous souhaiterez peut-être également 
enregistrer votre configuration en tant que configuration par défaut de l'utilisateur. 
 Pour enregistrer la configuration par défaut de l'utilisateur:  
• 
Entrez les commandes suivantes: 
exit all 
file copy startup-config user-default-config  
Vérification de la connectivité 
Sur le terminal ASCII, envoyez une requête ping à l'adresse IP attribuée à l'interface du routeur de 
gestion et vérifiez que les réponses sont reçues. S'il n'y a pas de réponse au ping, vérifiez votre 
configuration et apportez les corrections nécessaires. 
Configuration des services 
Procédez à la configuration du service (reportez-vous au chapitre Services pour plus de détails sur les 
différents scénarios de provisionnement des services pris en charge). 