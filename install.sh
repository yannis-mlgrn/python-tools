#******************************************* MAKE BY *********************************************
#                                          yannis-mlgrn 
#   github : https://github.com/yannis-mlgrn/
#   repository : https://github.com/yannis-mlgrn/python-tools/
#
# ***********************************************************************************************

# install tools
echo """
                  _                                    _      
             _   | |                   _              | |     
 ____  _   _| |_ | | _   ___  ____    | |_  ___   ___ | | ___ 
|  _ \| | | |  _)| || \ / _ \|  _ \   |  _)/ _ \ / _ \| |/___)
| | | | |_| | |__| | | | |_| | | | |  | |_| |_| | |_| | |___ |
| ||_/ \__  |\___|_| |_|\___/|_| |_|   \___\___/ \___/|_(___/ 
|_|   (____/                                                  
             _                      _ _                       
            (_)           _        | | |                      
             _ ____   ___| |_  ____| | |                      
            | |  _ \ /___|  _)/ _  | | |                      
            | | | | |___ | |_( ( | | | |                      
            |_|_| |_(___/ \___\_||_|_|_|                      
                                                              

 """
#install python3
echo "install python 3.8"
sudo apt-get install python3.8

# install pip3
echo "install pip3"
sudo apt install python3-pip

echo "install python3 librairies"
pip3 install -r requirements.txt
