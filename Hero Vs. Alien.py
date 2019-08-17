import time
import random
class Hero(object):
    def __init__(self,name="Aphrodite"):
        self.name = name
        self.health = 10
        self.ammo = 10
        self.life = 1
        self.bullet = 1
    def blast(self, enemy):
        print(self.name," blasts an Alien")
        enemy.die()
    def die(self):
        self.ammo = self.ammo -1
        self.bullet = 0
        if(self.ammo == 0 and self.bullet == 0):
            print(self.name," is out of ammo!")
        self.health = self.health-1
        self.life = 0
        if(self.health == 0 and self.life == 0):
            print("Ok you got me.",self.name," dies.\n\nWe will now give silence for a few seconds for our friend, ",self.name);
        else:
            print("You just nicked me.\n")
            
class Alien(object):
    def __init__(self,name="Nap Time"):
        self.name = name
        self.health = 10
        self.ammo = 10
        self.life = 1
        self.bullet = 1
    def blast(self, enemy):
        print(self.name," blasts the Hero")
        enemy.die()
    def die(self):
        self.ammo = self.ammo -1
        self.bullet = 0
        if(self.ammo == 0 and self.bullet == 0):
            print(self.name," is out of ammo!")
        self.health = self.health-1
        self.life = 0
        if(self.health == 0 and self.life == 0):
            print("The alien gasps and says, 'Oh, this is it. This is the big one. \n" \
                  "Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them... \n" \
                  "Good-bye, cruel universe.'")
            print("...We will now give silence for a few seconds for each larvae to say few words for ",self.name)
            print("woehe fieowe feow.\nwoehe fieowe feow\nwoehe fieowe feow\nOK, Shut up!")
        else:
            print("You can't even hit a schlurg.\n")
            
def main():
    choice=input("Continue with default names for players (y/n):")
    if(choice.upper()=="Y"):
        hero = Hero()
        invader = Alien()
    elif(choice.upper()=="N"):
        heroName=input("Hero character Name:");
        alienName=input("Alien character Name:");
        hero = Hero(heroName)
        invader = Alien(alienName)
    else:
        print("Invalid response.Exiting..");
        return
    print("\n\t\tThe Alien Wars.\n\n")
    while(True):
        time.sleep(1)
        true=random.choice([True,False])
        if(true):
            hero.blast(invader);
            if(invader.health==0 and invader.life==0):
                print("\nGame Over!")
                break;
        else:
            invader.blast(hero);
            if(hero.health==0 and hero.life==0):
                print("\nGame Over!")
                break;
    key=input("\nPress the Enter key to exit:")
    if key:
        return
main()
