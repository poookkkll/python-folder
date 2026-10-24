import random
result = 0
points = 1
superpoint = 2
megapoint = 4
a = "\033[91mTYPE YOUR QUESTION CATEGORY\033[0m"
b = "AVAILABLE CATEGORIES---------"
c = "\033[94mMATHS\033[0m"
d = "\033[95mGENERAL KNOWLEDGE\033[0m"
e = "\033[93mGEOGRAPHY\033[0m"
f = "-----------------"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
x = input(' ').lower().rstrip()
#---------------------------MATHLEVEL1SETTING----------------------------------------------------

if(x=="maths" or x=="math" or x =='mathamatics'):
    print("\033[91m||||USER YOU HAVE CHOSEN .....MATHS.....AS YOUR CATEGORY|||\033[0m")
    print("\033[93m>>>THERE WILL BE 3 LEVEL AND THERE WILL BE 6 QUIZZES IN TOTAL---\033[0m")
    print("\033[93m----LEVEL 1 CONTAINS 3 QUESTIONS||EACH WORTH 1 POINT\033[0m")
    print("\033[93m----LEVEL 2 CONTAINS 2 QUESTIONS||EACH WORTH 2 POINT\033[0m")
    print("\033[93m----LEVEL 3 CONTAINS 1 QUESTIONS||EACH WORTH 4 POINT\033[0m")
    level1 = [
        ("What is 17 + 8?  OPTIONS 1) 24.  2) 25.  3) 26.  4) 27.", "25","2"),
        ("What is 3 x 3 x 3?  OPTIONS 1) 9.  2) 24.  3) 81.  4) 27. ", "27",'4'),
        ("What is 1001 - 4? OPTIONS 1) 995.  2) 997.  3) 996.  4) 998. ", "997",'2'),
        ("What is 151 + 121?  OPTIONS 1) 272 .  2) 172.  3) 271.  4) 271. ", "272",'1'),
        ("What is 123 / 3? OPTIONS 1) 40.  2) 42.  3) 41.  4) 5. ", "41",'3'),
        ("What is 32 % 4? OPTIONS 1) 3.  2) 6.  3) 4.  4) 8. ", "8",'4')
    ]
#--------------------------------------------------------------------------------    
    lvl1s=0
    lvl2s=0
    lvl3s=0
    print("\033[91m-------DIFFICULTY LEVEL: EASY-------\033[0m")
    
    questions1 = random.sample(level1, 3)
    for q, ans, ans1 in questions1:
        user_ans = input(q + " ")
        if  (user_ans.title().rstrip() == ans or user_ans.rstrip()== ans1):
            lvl1s += points
            print("\033[92mCorrect! +1 points\033[0m")


        else:
            print(f"\033[91mWrong!\033[0m The answer was: \033[93m{ans1}) {ans}\033[0m")

#-----------------------------MATHLEVEL2SETTING---------------------------------------------------
    print("\033[91m-------DIFFICULTY LEVEL: NORMAL-------\033[0m")        
    level2 = [('What is 12²? Options: 1) 124  2) 144  3) 134  4) 154', '144','2'),
    ('What is the square root of 81? Options: 1) 7  2) 8  3) 9  4) 10', '9','3'),
    ('Solve for x : x + 7 = 20? Options: 1) 13  2) 27  3) -13  4) -27','13', '1'),
    ('What is 6² + 6²? Options: 1) 72  2) 76  3) 64  4) 58', '72','1')]
    
    questions2 = random.sample(level2, 2)
    for q, ans,ans1 in questions2:
        user_ans = input(q + " ")
        if  (user_ans.title().rstrip() == ans or user_ans.rstrip()== ans1):
            lvl2s += superpoint
            print("\033[92mCorrect! +2  points\033[0m")




        else:
            print(f"\033[91mWrong!\033[0m The answer was: \033[93m{ans1}) {ans}\033[0m")


    # ------------------ Level 3 Questions
    print("\033[91m-------DIFFICULTY LEVEL: HARD-------\033[0m")
    level3 = [
        ('What is the value of π (pi) up to 2 decimal places? Options: 1) 3.13  2) 3.15  3) 3.14  4) 3.12', '3.14','3'),
    ('What is 2 to the power of 5? Options: 1) 16  2) 32  3) 64  4) 24', '32','2')    ]
    question3 = random.sample(level3,1)
    for q,ans,ans1 in question3:
        user_ans = input(q + " ")
        if  (user_ans.title().rstrip() == ans or user_ans.rstrip()== ans1):
            lvl3s += megapoint
            print("\033[92mCorrect! +4points\033[0m")


        else:
            print(f"\033[91mWrong!\033[0m The answer was: \033[93m{ans1}) {ans}\033[0m")

            

    # ------------------ Final Result --------
    print(f"your level 1 score is : {lvl1s}")
    print(f"your level 2 score is : {lvl2s}")
    print(f"your level 3 score is : {lvl3s}")
    result = lvl1s+lvl2s+lvl3s
    print(f"\nYour total score is: {result} out of 11")
    if result >= 11:
        print("🏆 Your Rank: Quiz Master!")
    elif result >= 8:
        print("🤓 Your Rank: Smart Thinker!")
    elif result >= 5:
        print("🙂 Your Rank: Learning Brain!")
    elif result >= 3:
        print("😐 Your Rank: Needs Practice!")
    else:
        print("😅 Your Rank: Are you even trying!")

#-------------------------------GENERAL KNOWLEDGE ONE--------------------------------------------------------------------------------------------   
elif(x=="generalknowledge" or x=="general knowledge" or x=="gk"):
    print("\033[91m||||USER YOU HAVE CHOSEN .....GENERAL KNOWLEDGE.....AS YOUR CATEGORY|||\033[0m")
    print("\033[93m>>>THERE WILL BE 3 LEVEL AND THERE WILL BE 6 QUIZZES IN TOTAL---\033[0m")
    print("\033[93m----LEVEL 1 CONTAINS 3 QUESTIONS||EACH WORTH 1 POINT\033[0m")
    print("\033[93m----LEVEL 2 CONTAINS 2 QUESTIONS||EACH WORTH 2 POINT\033[0m")
    print("\033[93m----LEVEL 3 CONTAINS 1 QUESTIONS||EACH WORTH 4 POINT\033[0m")
#----------------------------------LEVEL1QUES-----------------------------------------------------------    
  
    level1 = [
    ("What is the capital of India? Options: 1) Mumbai  2) New Delhi  3) Kolkata  4) Chennai", "New Delhi", '2'),
    ("How many continents are there? Options: 1) 5  2) 6  3) 7  4) 8", "7", '3'),
    ("Which planet is known as the Red Planet? Options: 1) Earth  2) Mars  3) Venus  4) Jupiter", "Mars", '2'),
    ("How many days are there in a week? Options: 1) 5  2) 6  3) 7  4) 8", "7", '3'),
    ("Which animal is called the 'King of the Jungle'? Options: 1) Tiger  2) Lion  3) Elephant  4) Leopard", "Lion", '2'),
    ("Which is the largest organ in the human body? Options: 1) Heart  2) Skin  3) Liver  4) Lungs", "Skin", '2')
    
    
]
#-----------------------------------LEVEL1SETTING------------------------------------------------------------
    lvl1s=0
    lvl2s=0
    lvl3s=0
    print("\033[91m-------DIFFICULTY LEVEL: EASY-------\033[0m")
    
    questions1 = random.sample(level1, 3)
    for q, ans, ans1 in questions1:
        user_ans = input(q + " ")
        if  (user_ans.title().rstrip() == ans or user_ans.rstrip()== ans1):
            lvl1s += points
            print("\033[92mCorrect! +1 points\033[0m")


        else:
            print(f"\033[91mWrong!\033[0m The answer was: \033[93m{ans1}) {ans}\033[0m")

            
            
 #----------------------------------LEVEL2SETTING------------------------------------------------------------
    print("\033[91m-------DIFFICULTY LEVEL: NORMAL-------\033[0m")        
    level2 = [
    ("Which ocean is the largest? Options: 1) Atlantic  2) Pacific  3) Indian  4) Arctic", "Pacific", '2'),
    ("What is the currency of Japan? Options: 1) Yen  2) Won  3) Yuan  4) Dollar", "Yen", '1'),
    ("Who discovered gravity? Options: 1) Newton  2) Galileo  3) Einstein  4) Tesla", "Newton", '1'),
    ("Which country is known for the Eiffel Tower? Options: 1) Italy  2) Germany  3) France  4) UK", "France", '3'),
    ("What gas do plants absorb from air? Options: 1) Oxygen  2) Hydrogen  3) Carbon Dioxide  4) Nitrogen", "Carbon Dioxide", '3'),
    ]
    
    questions2 = random.sample(level2, 2)
    for q, ans,ans1 in questions2:
        user_ans = input(q + " ")
        if  (user_ans.title().rstrip() == ans or user_ans.rstrip()== ans1):
            lvl2s += superpoint
            print("\033[92mCorrect! +2  points\033[0m")




        else:
            print(f"\033[91mWrong!\033[0m The answer was: \033[93m{ans1}) {ans}\033[0m")
 
            
 #----------------------------------LEVEL3SETTING-------------------------------------------------------------
    print("\033[91m-------DIFFICULTY LEVEL: HARD-------\033[0m")
    level3 = [("Who was the first person to go to space? Options: 1) Neil Armstrong  2) Buzz Aldrin  3) Rakesh Sharma  4) Yuri Gagarin", "Yuri Gagarin", '4'),
    
    ("What is the full form of DNA? Options: 1) Dynamic Nucleic Acid  2) Deoxyribonucleic Acid  3) Double Nucleic Acid  4) Densely Natural Acid", "Deoxyribonucleic Acid", '2'),
    ("Which planet has the most moons? Options: 1) Earth  2) Saturn  3) Mars  4) Jupiter", "Saturn", '2')
            ]
    question3 = random.sample(level3,1)
    for q,ans,ans1 in question3:
        user_ans = input(q + " ")
        if  (user_ans.title().rstrip() == ans or user_ans.rstrip()== ans1):
            lvl3s += megapoint
            print("\033[92mCorrect! +4points\033[0m")


        else:
            print(f"\033[91mWrong!\033[0m The answer was: \033[93m{ans1}) {ans}\033[0m")


 #----------------------------------FINAL RESULT SETUP-----------------------------------------------------------------
    print(f"your level 1 score is : {lvl1s}")
    print(f"your level 2 score is : {lvl2s}")
    print(f"your level 3 score is : {lvl3s}")
    result = lvl1s+lvl2s+lvl3s
    print(f"\nYour total score is: {result} out of 11")
    if result >= 11:
        print("🏆 Your Rank: Quiz Master!")
    elif result >= 8:
        print("🤓 Your Rank: Smart Thinker!")
    elif result >= 5:
        print("🙂 Your Rank: Learning Brain!")
    elif result >= 3:
        print("😐 Your Rank: Needs Practice!")
    else:
        print("😅 Your Rank: Are you even trying!")
        
#----------------------------GEOGRAPHYSETTING-------------------------------------
elif(x=='geography'):
    print("\033[91m||||USER YOU HAVE CHOSEN .....GEOGRAPHY.....AS YOUR CATEGORY|||\033[0m")
    print("\033[93m>>>THERE WILL BE 3 LEVEL AND THERE WILL BE 6 QUIZZES IN TOTAL---\033[0m")
    print("\033[93m----LEVEL 1 CONTAINS 3 QUESTIONS||EACH WORTH 1 POINT\033[0m")
    print("\033[93m----LEVEL 2 CONTAINS 2 QUESTIONS||EACH WORTH 2 POINT\033[0m")
    print("\033[93m----LEVEL 3 CONTAINS 1 QUESTIONS||EACH WORTH 4 POINT\033[0m")
#----------------------------------LEVEL1QUES-----------------------------------------------------------    
    
    level1 = [("What is the capital of France? Options: 1) Rome 2) Madrid 3) Paris 4) Berlin", "Paris", '3'),
    ("Which continent is India located in? Options: 1) Africa 2) Asia 3) Europe 4) Australia", "Asia", '2'),
    ("Which is the largest ocean? Options: 1) Indian 2) Atlantic 3) Arctic 4) Pacific", "Pacific", '4'),
    ("Which country has the Great Wall? Options: 1) Japan 2) China 3) India 4) Russia", "China", '2'),
    ("Mount Everest lies in which mountain range? Options: 1) Alps 2) Andes 3) Himalayas 4) Rockies", "Himalayas", '3'),
    ("Which direction does the Sun rise? Options: 1) East 2) West 3) North 4) South", "East", '1')
    
    
    
]
#-----------------------------------LEVEL1SETTING------------------------------------------------------------
    lvl1s=0
    lvl2s=0
    lvl3s=0
    print("\033[91m-------DIFFICULTY LEVEL: EASY-------\033[0m")
    
    questions1 = random.sample(level1, 3)
    for q, ans, ans1 in questions1:
        user_ans = input(q + " ")
        if  (user_ans.title().rstrip() == ans or user_ans.rstrip()== ans1):
            lvl1s += points
            print("\033[92mCorrect! +1 points\033[0m")


        else:
            print(f"\033[91mWrong!\033[0m The answer was: \033[93m{ans1}) {ans}\033[0m")

            
            
 #----------------------------------LEVEL2SETTING------------------------------------------------------------
    print("\033[91m-------DIFFICULTY LEVEL: NORMAL-------\033[0m")        
    level2 = [("Which river is the longest in the world? Options: 1) Amazon 2) Nile 3) Ganga 4) Mississippi", "Nile", '2'),
    ("Which is the smallest continent? Options: 1) Australia 2) Europe 3) Antarctica 4) South America", "Australia", '1'),
    ("Sahara is a desert in which continent? Options: 1) Africa 2) Asia 3) Australia 4) Europe", "Africa", '1'),
    ("Which country has the most time zones? Options: 1) China 2) Russia 3) USA 4) France", "France", '4')
    
    ]
    
    questions2 = random.sample(level2, 2)
    for q, ans,ans1 in questions2:
        user_ans = input(q + " ")
        if  (user_ans.title().rstrip() == ans or user_ans.rstrip()== ans1):
            lvl2s += superpoint
            print("\033[92mCorrect! +2  points\033[0m")




        else:
            print(f"\033[91mWrong!\033[0m The answer was: \033[93m{ans1}) {ans}\033[0m")
 
            
 #----------------------------------LEVEL3SETTING-------------------------------------------------------------
    print("\033[91m-------DIFFICULTY LEVEL: HARD-------\033[0m")
    level3 = [("Which country has the only national flag that is not rectangular? Options: 1) Bhutan 2) Nepal 3) Maldives 4) Sri Lanka", "Nepal", '2'),

("Which is the only sea on Earth with no coastline? Options: 1) Arabian Sea 2) Coral Sea 3) Sargasso Sea 4) Bering Sea", "Sargasso Sea", '3')
    
    
            ]
    question3 = random.sample(level3,1)
    for q,ans,ans1 in question3:
        user_ans = input(q + " ")
        if  (user_ans.title().rstrip() == ans or user_ans.rstrip()== ans1):
            lvl3s += megapoint
            print("\033[92mCorrect! +4points\033[0m")


        else:
            print(f"\033[91mWrong!\033[0m The answer was: \033[93m{ans1}) {ans}\033[0m")


 #----------------------------------FINAL RESULT SETUP-----------------------------------------------------------------
    print(f"your level 1 score is : {lvl1s}")
    print(f"your level 2 score is : {lvl2s}")
    print(f"your level 3 score is : {lvl3s}")
    result = lvl1s+lvl2s+lvl3s
    print(f"\nYour total score is: {result} out of 11")
    if result >= 11:
        print("🏆 Your Rank: Quiz Master!")
    elif result >= 8:
        print("🤓 Your Rank: Smart Thinker!")
    elif result >= 5:
        print("🙂 Your Rank: Learning Brain!")
    elif result >= 3:
        print("😐 Your Rank: Needs Practice!")
    else:
        print("😅 Your Rank: Are you even trying!")

#-------------------------------------# 🔍 Still scrolling? You must really like Python.--------------------------------------
        #---------------------------------------------------------------------------------------------------------------------
        
 #-------------------------------------------------------------------------------------------------------------------------
if x == "paras":
    import time
    import os
    stars=[  
        "   ★★        ★★   ",
        "  ★ ★ ★   ★ ★ ★  ",
        "  ★ ★ ★ ★ ★ ★★  ",
        "    ★★ ★ ★ ★★    ",
        "     ★ ★  ★ ★     ",
        "       ★ ★ ★       ",
        "         ★ ★        ",
        "          ★          "
    ]

    print("\n✨ Secret mode unlocked! ✨\n")
    for line in stars:
        print(line)
        time.sleep(0.3)
    print("\nYou've discovered the hidden Easter Egg! 🎉")
    print("\nYour total score is: 11 out of 11")
    print("🏆 Your Rank: Quiz Master!")
    
    exit()