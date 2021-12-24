print('''
            _                                                      
            __ -                                                   
        /     __   \                                               
          /   _ -    |                                             
      | '  | (_)  |                        _L/L                    
         |  __  /   /                    _LT/l_L_                  
        \ \  __  /                     _LLl/L_T_lL_                
            -      _T/L              _LT|L/_|__L_|_L_              
                 _Ll/l_L_          _TL|_T/_L_|__T__|_l_            
               _TLl/T_l|_L_      _LL|_Tl/_|__l___L__L_|L_          
             _LT_L/L_|_L_l_L_  _'|_|_|T/_L_l__T _ l__|__|L_        
           _Tl_L|/_|__|_|__T _LlT_|_Ll/_l_ _|__[ ]__|__|_l_L_      
jjs_ ___ _LT_l_l/|__|__l_T _T_L|_|_|l/___|_ _|__l__|__|__|_T_l_  __
        . ";;:;.;;:;.;;;;_Ll_|__|_l_/__|___l__|__|___l__L_|_l_LL_  
          .  .:::.:::..:::.";;;;:;;:.;.;;;;,;;:,;;;.;:,;;,;::;:".' 
              . ,::.:::.:..:.: ::.::::;..:,:::,::::.::::.:;:.:..   
                 . .:.:::.:::.:::: .::.::. :::.::::..::..:.::. . . 
                   . ::.:.: :. .:::  ::::.::.:::.::...:. .:::. .   
                       .:. ..   . ::.. .: ::. ::::.:: ::::::.   .  
                       .  :.         .. :::.::: ::.::::. ::. .     
                         . .           .:. :.. :::. ::..: :.       
             nn_r   nn_r   .              :  .:::.:: ::..:  .      
            /l(\   /l)\      nn_r          . ::. :. : : ..         
            `'"``  ``"``    /\(\              . . .:. . : .        
                            ' "``                  . :. .          
                                                    .   .          
                                                       .
''')
print("Welcome to the Pyramids of Egypt!")
print("Your mission is to find the mummy before getting caught in a trap.") 

start = input("Start Game? Y or N: ")

if start == "Y\n: " or "y\n: ":
  direction = input("You recently arrived in Egypt and take a tour to visit the pyramids. \nUnfortunately, you somehow lose your party and are now at a crossroads inside a pyramid.\n Where do you want to go? Type left or right. ")
if direction == "left":
  print('''
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M)(MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 vanishing point 888888888888888888888888888888888888888888888 fL 888
''')
  doors = input ("You walk down a long narrow tunnel and are confronted with 3 doors..\n One red, one green and one blue.\n Which door do you choose? ")
  if doors == "red":
    print("You have stepped into a trap and died! Game over.")
    exit(0)
  elif doors == "green":
    print('''
      _                   .-=-.          .-==-.
     { }      __        .' O o '.       /  -<' )
     { }    .' O'.     / o .-. O \     /  .--v`
     { }   / .-. o\   /O  /   \  o\   /O /
      \ `-` /   \ O`-'o  /     \  O`-`o /
       `-.-`     '.____.'       `.____.'
    ''')
    print("You step on a poisonous snake and die! Game over.")
    exit(0)
  else:
    print('''
 ,-"""--.___
  ,gg-._ 
.:_YP_.-""""
  |`.    ,-.
  '  `-.__.'
    ''')
    print("You have been cursed by the mummy and die! Game over.")
    exit(0)
if direction =="right":
    print('''
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M)(MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 vanishing point 888888888888888888888888888888888888888888888 fL 88
    ''')
    doors = input("You stumble and roll down a steep corridor and find yourself in a room with two doors.\n Which door do you choose?\n Yellow, or Black: ")
    if doors == "yellow":
      print('''         
             ____"_                   |   |
            /"  _)))                  |\_/|______,
           /===( _\                  /::| Q  ____)
          ("___|   >   ,_           /:::|   /    ,_
             o  _=    / _///       /::::|_ /    / _///
       _______| |____/ |         _|:::::| |:___/ |
      |  __)  \_/ /____|        | '----'\_/  /___|
     _| / \    ) )             _| /  \   :  /
 _..\__/   \    /          _..\__/    \    /
           /   (                      /===(
          / \   \                    /     \
         /   \   \                  /       \
         |    \   \                 |        \
         |     \   \                |         \
         |      \   \               |,_________\
         |       \   \               /  )  / )
         |,_______\___\             /  /  (  |
           | /   \ |                | /    \ |
           |/     \|                |/      \|
           S__     S__              S__      S__
          /___\   /___\            /___\    /___\
      ''')
      print("You have found the mummy! The mummy grants any wishes you want.\n You WIN!")
    else: 
      print('''
          ,/`.
        ,'/ __`.
      ,'_/_  _ _`.
    ,'__/_ ___ _  `.
  ,'_  /___ __ _ __ `.
 '-.._/___...-"-.-..__`.
      ''')
      print("You have been killed by a rolling boulder!")
      exit(0)
elif start == "N" or "n":
  exit(0)

