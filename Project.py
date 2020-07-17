from random import randint
import time
import sys
import random
import os

#Here we create the User calls which containes the users age, name, and their morality.
class User:
    def __init__(self, name, age, morality=0):
        self.name = name
        self.age = age
        self.morality = morality
    def name_m(self):
        message = "Hello there {}, my name is Mr.M...I hope you are ready to play this game...".format(self.name)
        return message
    def age_r(self):
        text=""
        if(self.age>=15 and self.age<20):
            text = "very young"
        elif(self.age>=20 and self.age<30):
            text = "somewhat young"
        if (self.age >= 30 and self.age < 50):
            text = "somewhat old"
        elif (self.age >=50):
            text = "very old "
        return text

    def age_c(self):
        chance = 0
        if(self.age>=15 and self.age<20):
            chance = 0.001
        elif(self.age>=20 and self.age<30):
            chance = 0.01
        if (self.age >= 30 and self.age < 50):
            chance = 0.1
        elif (self.age >=50):
            chance = 0.00001
        return chance

    def age_m(self):
        message = "I see so you are {} years old.. you are {} for this game, your chances of surviving are {} percent.".format(self.age, User.age_r(self), User.age_c(self))
        return message

    def increase_morality(self):
        self.morality = self.morality+1

    def decrease_morality(self):
        self.morality = self.morality-1

class NPC:
    def __init__(self, name):
        self.name = name




def restart():
    restarting = False
    while (restarting !=True):
        response = str(input("Would you like to start again?: "))
        response.lower()
        if(response == "yes" or response =="y"):
            restarting = True
            spaces()
            message("Welcome....")
            Name = str(input("What is your name?: "))
            age = int(input("What is your age?: "))
            while (age < 15):
                age = int(input("What is your age?: "))
            user = User(Name, age)
            message(user.name_m())
            message(user.age_m())

            b()


        elif(response == "no" or response =="n"):
            restarting = True
            sys.exit()






def spaces():
    for i in range(30):
        print('\n')


def message(text):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.06)
    spaces()

def action_input():
    action = str(input("What do you do? :"))
    action.lower()
    return action




def sentence():
    message = "As you heard this, you began to look around where you were. All you could is an empty room that barely had anything in it except for a desk, and what seemed to be claw marks all around the room.."
    return message



def help():
    text = "The commands you can type are 'look', 'hear', 'go to desk', 'yell' , inspect, and 'go to door'"
    message(text)
    action = action_input()
    switcher = {
        "look": look,
        "hear": hear,
        "touch desk": td,
        'yell': yell,
        'inspect': inspect,
        'go to door': gd

    }
    def action_response(argument):
        func = switcher.get(argument, help)
        return func()
    action_response(action)
def look():
    text = "You looked around, and all you saw were perculiar claw marks around the room, you couldn't hlep but wonder what the hell was in this room before you. You wondred how long was this room unkept due to the vast amounts of vegetaion growing within the room, making it seem like an ancient ruin"
    message(text)
    action = action_input()
    switcher = {
        "look": look,
        "hear": hear,
        "touch desk": td,
        'yell': yell,
        'inspect': inspect,
        'go to door': gd

    }
    def action_response(argument):
        func = switcher.get(argument, help)
        return func()

    action_response(action)
def hear():
    text = "You stood still and began listening to your surroundings. All you could hear was silence...it was really discomforting."
    message(text)
    action = action_input()
    switcher = {
        "look": look,
        "hear": hear,
        "touch desk": td,
        'yell': yell,
        'inspect': inspect,
        'go to door': gd

    }
    def action_response(argument):
        func = switcher.get(argument, help)
        return func()

    action_response(action)
def td():
    text = "You walked towards the desk and noticed that it was covered with vegetation and vines. It was as if it hadn't been tocuhed in more than a decade...as you placed your hand on it, you uncovered a name scribed onto the wooden desk...William Weishenturg.."
    message(text)
    action = action_input()
    switcher = {
        "look": look,
        "hear": hear,
        "touch desk": td,
        'yell': yell,
        'inspect': inspect,
        'go to door': gd

    }
    def action_response(argument):
        func = switcher.get(argument, help)
        return func()

    action_response(action)
def yell():
    text = "You  yelled at the top of your lungs but you heard no response. All you heard was your echo bellowing throughout the empty and abanoned room."
    message(text)
    action = action_input()
    switcher = {
        "look": look,
        "hear": hear,
        "touch desk": td,
        'yell': yell,
        'inspect': inspect,
        'go to door': gd

    }
    def action_response(argument):
        func = switcher.get(argument, help)
        return func()
    action_response(action)
def inspect():
    text = "You began to inspect the room, you noticed the vast amount of vegetation and stumbled upon what seemed to be the skull of a person"
    message(text)
    action = action_input()
    switcher = {
        "look": look,
        "hear": hear,
        "touch desk": td,
        'yell': yell,
        'inspect': inspect,
        'go to door': gd

    }
    def action_response(argument):
        func = switcher.get(argument, help)
        return func()
    action_response(action)







def help2():
    text = "The commands you can type are 'go left', 'go right' , 'go back' , 'go forward'  "
    message(text)
    action = action_input()
    switcher = {
        "go left": go_L,
        "go right": go_R,
        "go back": go_B,
        "go forward": go_F
    }
    def action_response(argument):
        func = switcher.get(argument, help2)
        return func()
    action_response(action)







def help3():
    text = "The commands you can type are 'go back', 'inspect', and 'listen'  "
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect": inspect2,
        "listen": listen
    }
    def action_response(argument):
        func = switcher.get(argument, help3)
        return func()
    action_response(action)
def listen():
    text = "You began listening to your surroundings...but all you heard was the wind...but you could hear an eery howl from beyond the rubble...."
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect": inspect2,
        "listen": listen
    }
    def action_response(argument):
        func = switcher.get(argument, help3)
        return func()
    action_response(action)
def inspect2():
    text = "You inspected the rubble in front of you...it's ood..it seems as if this building had just collpased, but the mass amounts of moss surroudning it make it seem like it's been here for a long time..."
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect": inspect2,
        "listen": listen
    }
    def action_response(argument):
        func = switcher.get(argument, help3)
        return func()
    action_response(action)
def go_L():
    text = "You turned left and began walking, hoping to find anyone that could help you...however all you see are just more vines. As you look for help, you realize that there is nowhere else you can go. The street has been blocked by the rubble of what seemed to be a bridge...it seems all uou can do is head back.."
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect": inspect2,
        "listen": listen
    }
    def action_response(argument):
        func = switcher.get(argument, help3)
        return func()
    action_response(action)



def help4():
    text = "The commands you can type are 'go back', 'inspect bag', 'listen', 'go forward' "
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect bag": lookthroughB,
        "listen": listen2,
        "go forward": goF
    }
    def action_response(argument):
        func = switcher.get(argument, help4)
        return func()
    action_response(action)
def goF():
    text = "As you went forward, you were approached by a gaisnt creature...it was practcially difficult for you to comprehend what was happening.....the creature pounced upon and began eating you..........\n YOU HAVE DIED"
    message(text)
    restart()
def lookthroughB():
    text = "You inspected the bag, as you rummaged through the bag...you noticed a notebook which only has one page.. it seems to say 'Subject 01.......every one is....the government has.....', you can't seem to understand what was written and decided to place the notebakk back into the bag, and left the bag alone..."
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect bag": lookthroughB,
        "listen": listen2,
        "go forward": goF
    }
    def action_response(argument):
        func = switcher.get(argument, help4)
        return func()
    action_response(action)
def listen2():
    text = "You began to listen to your surroundings and noticed that there seems to be some unusual sounds coming from ahead...the sounds don't seem natural nor do they seem to be the noise corresponding to people.. "
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect bag": lookthroughB,
        "listen": listen2,
        "go forward": goF
    }
    def action_response(argument):
        func = switcher.get(argument, help4)
        return func()
    action_response(action)
def go_R():
    text = "You turned right and began walking, however as you walked past the various destroyed building you come across a very old and worned out bag....it seems like there are no roadblocks ahead either...."
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect bag": lookthroughB,
        "listen": listen2,
        "go forward": goF
    }
    def action_response(argument):
        func = switcher.get(argument, help4)
        return func()
    action_response(action)





def help5():
    text = "The commands you can type are 'leave' , 'yell' , 'inspect' "
    message(text)
    action = action_input()
    switcher = {
        "leave": returned,
        "yell": yelling,
        "inspect": inspecting_again
    }
    def action_response(argument):
        func = switcher.get(argument, help5)
        return func()
    action_response(action)
def inspecting_again():
    text = "You began inspecting the room but you noticed that there is something else here...and it's defiently not another person...its best to get the hell out of dodge.."
    message(text)
    action = action_input()
    switcher = {
        "leave": returned,
        "yell": yelling,
        "inspect": inspecting_again
    }
    def action_response(argument):
        func = switcher.get(argument, help5)
        return func()
    action_response(action)
def yelling():
    text = "You yelled...but instead of silenee, in front of you was a gigantic beast that was practically impossible to identify..before you could think of what to do next..it poucned upon...your life flashed in front of your eyes.........\n YOU DIED"
    message(text)
    restart()
def go_B():
    text = "You turned back, and went back inside the building. For some reason it seems like you aren't alone this time...."
    message(text)
    action = action_input()
    switcher = {
        "leave": returned,
        "yell": yelling,
        "inspect": inspecting_again
    }
    def action_response(argument):
        func = switcher.get(argument, help5)
        return func()
    action_response(action)




def help6():
    text = "The commands you can type are 'go back' , 'inspect' , 'yell' ,  'continue moving forward'  "
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect": inspect_evenmore,
        "listen": listen_around,
        "yell": yell_evenmore,
        "continue moving forward": keepmf
    }
    def action_response(argument):
        func = switcher.get(argument, help6)
        return func()
    action_response(action)
def inspect_evenmore():
    text = "You began inspecting the area around you, you noticed that someone or something was following you...."
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect": inspect_evenmore,
        "listen": listen_around,
        "yell": yell_evenmore,
        "continue moving forward": keepmf
    }
    def action_response(argument):
        func = switcher.get(argument, help6)
        return func()
    action_response(action)
def listen_around():
    text = "You began to listen to your surroundings, you can hear the wind passing through the desolate street that was once filled wih cars, and people. You can't help but feel a bit unsettled by the silence... "
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect": inspect_evenmore,
        "listen": listen_around,
        "yell": yell_evenmore,
        "continue moving forward": keepmf
    }
    def action_response(argument):
        func = switcher.get(argument, help6)
        return func()
    action_response(action)
def yell_evenmore():
    text = "You yelled at the top of your lungs for help hoping you can get a response, but nobody responded....you can't help but feel like someone or something is silently watching you..."
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect": inspect_evenmore,
        "listen": listen_around,
        "yell": yell_evenmore,
        "continue moving forward": keepmf
    }
    def action_response(argument):
        func = switcher.get(argument, help6)
        return func()
    action_response(action)
def go_F():
    text = "You walked forward, as you began venturing forth, you noticed the vast amount of buildings that look destroyed and look like the reamins of the past. You still don't understand who Mr.M is nor do you really understand why you are here."
    message(text)
    action = action_input()
    switcher = {
        "go back": returned,
        "inspect": inspect_evenmore,
        "listen": listen_around,
        "yell": yell_evenmore,
        "continue moving forward": keepmf
    }
    def action_response(argument):
        func = switcher.get(argument, help6)
        return func()
    action_response(action)















def help9():
    text = "The commands you can type are 'turn around' , 'inspect' , 'listen', 'go forward' "
    message(text)
    action = action_input()
    switcher = {
        "turn around": turnaround,
        "inspect": inspecting_againagain,
        "listen": listentos,
        "go forward": go_F2
    }
    def action_response(argument):
        func = switcher.get(argument, help9)
        return func()
    action_response(action)
def ignorethem():
    text = "You ignored the young man, as you did he was pleading for help but you kept walking until you couldn't hear their voice anymore... "
    message(text)
    user.decrease_morality()
    action = action_input()
    switcher = {
        "turn around": turnaround,
        "inspect": inspecting_againagain,
        "listen": listentos,
        "go forward": go_F2
    }
    def action_response(argument):
        func = switcher.get(argument, help9)
        return func()
    action_response(action)
def turnaround():
    text = "You turned around but you didn't see the young man any more, all you could muster to see was a puddle of blood. "
    message(text)
    action = action_input()
    switcher = {
        "turn around": turnaround,
        "inspect": inspecting_againagain,
        "listen": listentos,
        "go forward": go_F2
    }
    def action_response(argument):
        func = switcher.get(argument, help9)
        return func()
    action_response(action)
def inspecting_againagain():
    text = "You began to inspect your suroundings...you see a puddle of blood but you can't seem to see anything else around you. It seems that what ever was following you has left... "
    message(text)
    action = action_input()
    switcher = {
        "turn around": turnaround,
        "inspect": inspecting_againagain,
        "listen": listentos,
        "go forward": go_F2
    }
    def action_response(argument):
        func = switcher.get(argument, help9)
        return func()
    action_response(action)
def listentos():
    text = "You began to listen to your surroundings, you could only hear the wind but for some reason you could hear some silent screams...it's a bit unsettling...  "
    message(text)
    action = action_input()
    switcher = {
        "turn around": turnaround,
        "inspect": inspecting_againagain,
        "listen": listentos,
        "go forward": go_F2
    }
    def action_response(argument):
        func = switcher.get(argument, help9)
        return func()
    action_response(action)








def help10():
    text = "The commands you can type are 'look around' , 'inspect corpse' , 'inspect journal' , 'inspect watch' , 'go forward' "
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings,
        "inspect corpse": inspect_corpse,
        "inspect journal": inspect_journal,
        "inspect watch": inspect_watch,
        "go forward": go_FF2
    }
    def action_response(argument):
        func = switcher.get(argument, help10)
        return func()
    action_response(action)
def surroundings():
    text = "You looked around your surroundings...there doesn't seem to be anything around you for now... "
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings,
        "inspect corpse": inspect_corpse,
        "inspect journal": inspect_journal,
        "inspect watch": inspect_watch,
        "go forward": go_FF2
    }
    def action_response(argument):
        func = switcher.get(argument, help10)
        return func()
    action_response(action)
def inspect_corpse():
    text = "You began to inspect the corpse..you noticed that the watch seems to have the date 9-10-17 enscribed onto it.....the corpse seems to be rotting...you can see some worms within the eye sockets"
    user.decrease_morality()
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings,
        "inspect corpse": inspect_corpse,
        "inspect journal": inspect_journal,
        "inspect watch": inspect_watch,
        "go forward": go_FF2
    }
    def action_response(argument):
        func = switcher.get(argument, help10)
        return func()
    action_response(action)
def inspect_journal():
    text = "You began to inspect the journal..there doesn't seem to be anything of importance except for a strange drawing of a tube and what seems to be a lion within the tube...."
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings,
        "inspect corpse": inspect_corpse,
        "inspect journal": inspect_journal,
        "inspect watch": inspect_watch,
        "go forward": go_FF2
    }
    def action_response(argument):
        func = switcher.get(argument, help10)
        return func()
    action_response(action)
def inspect_watch():
    text = "You began to inspect the watch without getting too close to the corpse..you can't seem ti see anything perculiar however you noticed it saying something around 9-?1-????...the rest of it can't be read unless you gte a bit closer to the corpse however that would be very immoral..."
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings,
        "inspect corpse": inspect_corpse,
        "inspect journal": inspect_journal,
        "inspect watch": inspect_watch,
        "go forward": go_FF2
    }
    def action_response(argument):
        func = switcher.get(argument, help10)
        return func()
    action_response(action)
def go_F2():
    text = "You continued walking forward, as you began walking past the empty streets, you come across a corpse wearing an antique watch, and holding what seems to be a journal.... it seems to have been decomposing for a while..."
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings,
        "inspect corpse": inspect_corpse,
        "inspect journal": inspect_journal,
        "inspect watch": inspect_watch,
        "go forward": go_FF2
    }
    def action_response(argument):
        func = switcher.get(argument, help10)
        return func()
    action_response(action)












def help13():
    text = "The commands you can type are 'talk' "
    message(text)
    action = action_input()
    switcher = {
        "talk": talking2
    }
    def action_response(argument):
        func = switcher.get(argument, help13)
        return func()
    action_response(action)
def go_FF2():
    text = "You Continued moving forward hoping to see if you could find a safe space away from the 'things' that killed {}".format(Issac.name)
    message(text)
    action = action_input()
    switcher = {
        "talk": talking3
    }
    def action_response(argument):
        func = switcher.get(argument, help13)
        return func()
    action_response(action)
def talking3():
    text = "Who would you even be talking to....no one is around you...."
    message(text)
    action = action_input()
    switcher = {
        "talk": talking3
    }

    def action_response(argument):
        func = switcher.get(argument, help13)
        return func()

    action_response(action)























def help8():
    text = "The commands you can type are 'talk' , 'look', 'stay' , 'go forward' "
    message(text)
    action = action_input()
    switcher = {
        "talk": talking,
        "look": lookaround_more,
        "stay": staystill,
        "go forward": go_F3
    }
    def action_response(argument):
        func = switcher.get(argument, help8)
        return func()
    action_response(action)
def helpthem():
    text = "You helped the young man...he looks at you with a horrified face... "
    message(text)
    user.increase_morality()
    action = action_input()
    switcher = {
        "talk": talking,
        "look": lookaround_more,
        "stay": staystill,
        "go forward": go_F3
    }
    def action_response(argument):
        func = switcher.get(argument, help8)
        return func()
    action_response(action)
def talking():
    Issac.name = "Young Man"
    text = " You: are you okay?"
    message(text)
    text = " {} : ...I thought I was a goner...those things...almost killed me...".format(Issac.name)
    message(text)
    text = " You: those things?, what are you talking about?"
    message(text)
    text = " {} : Have you not seen those things!? They are all over this place...I'm surprised they haven't attacked you yet...".format(Issac.name)
    message(text)
    text = " You: We should get going...."
    message(text)
    text = " {} : your telling me..the names Issac".format(Issac.name)
    message(text)
    text = " You: the names {}...lets get going".format(user.name)
    message(text)
    Issac.name = "Issac"
    action = action_input()
    switcher = {
        "talk": talking,
        "look": lookaround_more,
        "stay": staystill,
        "go forward": go_F3
    }
    def action_response(argument):
        func = switcher.get(argument, help8)
        return func()
    action_response(action)
def lookaround_more():
    text = "You looked around your surroundings, you noticed that there seems to be a strange figure staring at you...you should probably get moving... "
    message(text)
    action = action_input()
    switcher = {
        "talk": talking,
        "look": lookaround_more,
        "stay": staystill,
        "go forward": go_F3
    }
    def action_response(argument):
        func = switcher.get(argument, help8)
        return func()
    action_response(action)
def staystill():
    text = "You stayed , and continued conversing with {}...".format(Issac.name)
    message(text)
    text = "{}:...wait what's that behind you....AGGGGGGHHHHHH!!!".format(Issac.name)
    message(text)
    text = "Before you could realize what was occurring.....You could feel fangs on your neck...you couldn't believe that just like that your life is over"
    message(text)
    text = "YOU DIED"
    message(text)
    restart()










def help11():
    text = "The commands you can type are 'look around' , 'inspect corpse' , 'inspect journal' , 'talk', 'go forward' "
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings2,
        "inspect corpse": inspectcorpse2,
        "inspect watch": inspect_watch2,
        "inspect journal": inspect_journal,
        "talk": talkingagain_one,
        "go forward": go_FF
    }
    def action_response(argument):
        func = switcher.get(argument, help11)
        return func()
    action_response(action)
def go_F3():
    text = "You continued walking forward, as you began walking past the empty streets, you come across a corpse wearing an antique watch, and holding what seems to be a journal.... it seems to have been decomposing for a while..."
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings2,
        "inspect corpse": inspectcorpse2,
        "inspect watch": inspect_watch2,
        "inspect journal": inspect_journal,
        "talk": talkingagain_one,
        "go forward": go_FF
    }
    def action_response(argument):
        func = switcher.get(argument, help11)
        return func()
    action_response(action)
def surroundings2():
    text = "You looked around your surroundings...there doesn't seem to be anything around you for now....{} seems to be cautious, and is constantly looking around his surroundings.. ".format(Issac.name)
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings2,
        "inspect corpse": inspectcorpse2,
        "inspect watch": inspect_watch2,
        "inspect journal": inspect_journal,
        "talk": talkingagain_one,
        "go forward": go_FF
    }
    def action_response(argument):
        func = switcher.get(argument, help11)
        return func()
    action_response(action)
def inspectcorpse2():
    user.decrease_morality()
    text = "You began to inspect the corpse..you noticed that the watch seems to have the date 9-10-17 enscribed onto it.....the corpse seems to be rotting...you can see some worms within the eye sockets"
    message(text)
    text ="{} : What the hell are you doing!?".format(Issac.name)
    message(text)
    text = "You : What do you think..I am investigating.."
    message(text)
    text = "{} : I know that but still..it's a corpse shouldn't we leave it alone?".format(Issac.name)
    message(text)
    text = "You : Under normal circumstances I would but in this case I think it's an exception"
    message(text)
    text = "{} : I mean but still...it's a corpse....".format(Issac.name)
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings2,
        "inspect corpse": inspectcorpse2,
        "inspect watch": inspect_watch2,
        "inspect journal": inspect_journal,
        "talk": talkingagain_one,
        "go forward": go_FF
    }
    def action_response(argument):
        func = switcher.get(argument, help11)
        return func()
    action_response(action)
def inspect_watch2():
    text = "You began to inspect the watch without getting too close to the corpse..you can't seem ti see anything perculiar however you noticed it saying something around 9-?1-????...the rest of it can't be read unless you gte a bit closer to the corpse however that would be very immoral..."
    message(text)
    text = "{}: Did you find anything of importance?".format(Issac.name)
    message(text)
    text = "You: not really..I don't know if I should inspect the corpse.. "
    message(text)
    text = "{}: I mean I wouldn't recommend that...we don't know if there is still one of those damn things around the area....".format(Issac.name)
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings2,
        "inspect corpse": inspectcorpse2,
        "inspect watch": inspect_watch2,
        "inspect journal": inspect_journal,
        "talk": talkingagain_one,
        "go forward": go_FF
    }
    def action_response(argument):
        func = switcher.get(argument, help11)
        return func()
    action_response(action)
def inspect_journal2():
    text = "You began to inspect the journal..there doesn't seem to be anything of importance except for a strange drawing of a tube and what seems to be a lion within the tube...."
    message(text)
    text = "{}: wait a second...this journal looks like the journal one of my co-workers had..but they left work only a month ago...what the hell is going on...".format(Issac.name)
    message(text)
    action = action_input()
    switcher = {
        "look around": surroundings2,
        "inspect corpse": inspectcorpse2,
        "inspect watch": inspect_watch2,
        "inspect journal": inspect_journal,
        "talk": talkingagain_one,
        "go forward": go_FF
    }
    def action_response(argument):
        func = switcher.get(argument, help11)
        return func()
    action_response(action)
def talkingagain_one():
    text = "You: So what do you think killed them..."
    message(text)
    if(user.morality > 0):
        text = "{}: It had to be one of those things that's for sure".format(Issac.name)
        message(text)
    else:
        text = "{}: I believe that's the least of our concerns..how can I trust you?".format(Issac.name)
        message(text)
        text = "You : what do you mean?".format(Issac.name)
        message(text)
        text = "{}: I mean...how can I trust you..you may have saved my life...but how do I know if you won't throw me to the side to save your own skin? ".format(Issac.name)
        message(text)
        text = "You : I believe that's something you need to decide...it's either teaming up with me or geting killed by whatever the hell those things you keep mentioning are...".format(Issac.name)
        message(text)
    action = action_input()
    switcher = {
        "look around": surroundings2,
        "inspect corpse": inspectcorpse2,
        "inspect watch": inspect_watch2,
        "inspect journal": inspect_journal,
        "talk": talkingagain_one,
        "go forward": go_FF
    }
    def action_response(argument):
        func = switcher.get(argument, help11)
        return func()
    action_response(action)









def help12():
    text = "The commands you can type are 'talk' "
    message(text)
    action = action_input()
    switcher = {
        "talk": talking2
    }
    def action_response(argument):
        func = switcher.get(argument, help12)
        return func()
    action_response(action)
def go_FF():
    text = "You Continued moving forward with {} , hoping to see if you could find a safe space away from the 'things' {} keeps referring to.... ".format(Issac.name , Issac.name)
    message(text)
    action = action_input()
    switcher = {
        "talk": talking2
    }
    def action_response(argument):
        func = switcher.get(argument, help12)
        return func()
    action_response(action)
def talking2():
    text = "You: do you have any idea where we are..."
    message(text)
    if (user.morality > 0):
        text = "{}: Honestly no...all I remember are these streets since I was running as fast as I could from those damn things".format(Issac.name)
        message(text)
        text = "You: how did those things even looked like..."
        message(text)
        text = "{}: They looked like a lion but had legs like an arachnid..one things for sure...they're freaks of nature....tnat's for sure ".format(Issac.name)
        message(text)
    else:
        text = "{}:.......no clue".format(Issac.name)
        message(text)
    action = action_input()
    switcher = {
        "talk": talking2
    }
    def action_response(argument):
        func = switcher.get(argument, help12)
        return func()
    action_response(action)










def help7():
    text = "The commands you can type are 'help them' , 'ignore'  "
    message(text)
    action = action_input()
    switcher = {
        "help them": helpthem,
        "ignore": ignorethem
    }
    def action_response(argument):
        func = switcher.get(argument, help7)
        return func()
    action_response(action)
def keepmf():
    text = "You Continued moving forward... and as you were passing through various empty blocks, you noticed a young man laying on the floor..."
    message(text)
    action = action_input()
    switcher = {
        "help them": helpthem,
        "ignore": ignorethem
    }
    def action_response(argument):
        func = switcher.get(argument, help7)
        return func()
    action_response(action)











def returned():
    text = "What you see in front of you is a strange sight, it looks like the city of Washington DC however there are no bustling streets, nor any sign of people. All you see are buildings covered with vines, and desolate streets filled with nothing but abadoned and destroyed vehicles. You see that you could go left,right, straight forward, or just head back into the abandoned building... "
    message(text)
    action = action_input()
    switcher = {
        "go left": go_L,
        "go right": go_R,
        "go back": go_B,
        "go forward": go_F
    }
    def action_response(argument):
        func = switcher.get(argument, help2)
        return func()
    action_response(action)
def op():
    text = "As you opened the door, you heard Mr.M saying 'Have fun...the game has just begun'..."
    message(text)
    text = "What you see in front of you is a strange sight, it looks like the city of Washington DC however there are no bustling streets, nor any sign of people. All you see are buildings covered with vines, and desolate streets filled with nothing but abadoned and destroyed vehicles. You see that you could go left,right, straight forward, or just head back into the abandoned building... "
    message(text)
    action = action_input()
    switcher = {
        "go left": go_L,
        "go right": go_R,
        "go back": go_B,
        "go forward": go_F
    }
    def action_response(argument):
        func = switcher.get(argument, help2)
        return func()
    action_response(action)










def gd():
    text = "you walked towards a door near the end of the room. As you walked towards it you could hear the strange voice chuckling...it seems that mr.M was expecting you to do that. "
    message(text)
    action = action_input()
    switcher = {
        "look": look,
        "hear": hear,
        "touch desk": td,
        'yell': yell,
        'inspect': inspect,
        'go to door': gd,
        'open door': op
    }
    def action_response(argument):
        func = switcher.get(argument, help)
        return func()
    action_response(action)













def action_event():
    action = action_input()
    switcher = {
        "look": look,
        "hear": hear,
        "touch desk": td,
        'yell': yell,
        'inspect': inspect,
        'go to door': gd

    }
    def action_response(argument):
        func = switcher.get(argument, help)
        return func()
    action_response(action)
def b():
    message(sentence())
    action_event()
    restart()




message("Welcome....")
Name = str(input("What is your name?: "))
age = int(input("What is your age?: "))
while(age<15) :
        age = int(input("What is your age?: "))
user = User(Name, age)
Issac = NPC("Issac")
message(user.name_m())
message(user.age_m())
b()
