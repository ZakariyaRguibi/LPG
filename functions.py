import random
import LPD

def roll():
    """Uses the cyberpunk red formula 1d10-7 to define friends enemies and lovers
    """
    return (random.randint(1,10)-7)

def flist():
    """Uses the formula in roll()  loop yield friends
    """
    rr = roll()
    if rr <= 0:
        yield  "\n        - none"

    for i in range(0,rr):
        yield f"\n        - {random.choice(LPD.Friends)}\n"

def enemies():
    rr = roll()
    if rr <= 0:
        yield  "\n        - none"
    for i in range(0,rr):
        yield(f"""\n        - This enemy is {random.choice(LPD.Enemies)}
        	- they hates you for this reason {random.choice(LPD.cause)}
        	- they have the following means at their disposal {random.choice(LPD.throw)}
        	- Their revenge plan is {random.choice(LPD.ven)}\n""")

def lovers():
    rr = roll()
    if rr <= 0:
        yield  "\n        - none"
    for i in range(0,rr):
        yield f"\n        - {random.choice(LPD.lovers)}\n"



def appendWithNewLine(text,stringToAppend):
	"""this is the mdrasa function"""
	return text+stringToAppend+"\n" #we append the new string to the general text, the \n stand for a new line


def Rockerpath():
    text = "RockerBoy\n"
    text=appendWithNewLine(text,f"""### Type of Rockerboy :
- {random.choice(LPD.TypeOfRboy)}""") # append the random choice and a new line
    Rpathresult = input("""are you a solo or  are you in a group?
    1 for solo 2 for group
    """)
    if int(Rpathresult) == 1:
        text=appendWithNewLine(text,"""- you are solo""")
        answer = int(input("were you once in a group ? 1 yes 2 no"))
        if answer == 1:
            text=appendWithNewLine(text,f"""- you left the group because {random.choice(LPD.ReasonYouLeft)}""")
        elif answer == 2:
            pass
    elif int(Rpathresult) == 2:
        text=appendWithNewLine(text,"""- you are in a group""")
    else :
        print("choose 1 or 2")
        return
    text=appendWithNewLine(text,f"""- the type of venue you perform in is {random.choice(LPD.TypeOfVenue)}""")
    text=appendWithNewLine(text,f"""- the person gunning for you is {random.choice(LPD.Gunning)}""")
    return text

def SoloPath():
    text = "Solo\n"
    text=appendWithNewLine(text,f"- you are a {random.choice(LPD.SoloType)}")
    text=appendWithNewLine(text,f"- your moral compass is {random.choice(LPD.MoralCompass)}")
    text=appendWithNewLine(text,f"- you operate in {random.choice(LPD.OperatingTerritory)}")
    text=appendWithNewLine(text,f"- Someone is gunning for you {random.choice(LPD.SoloGunning)}")
    return text

def NetrunnerPath():
    text = "Netrunner\n"
    text=appendWithNewLine(text,f"- {random.choice(LPD.TypeOfNetrunner)}") # append the random choice and a new line
    Rpathresult = input("""Do you have a partner or do you work alone ?
    1 for solo 2 for group
    """)
    if int(Rpathresult) == 1:
        text=appendWithNewLine(text,"- you are solo")
    elif int(Rpathresult) == 2:
        text=appendWithNewLine(text,f"- your partner is{random.choice(LPD.PartnerIdentity)}")

    text=appendWithNewLine(text,f"- workspace {random.choice(LPD.TypeOfWorkspace)}")
    text=appendWithNewLine(text,f"- some of your clients are {random.choice(LPD.TypeOfClients)}")
    text=appendWithNewLine(text,f"- you get your programs this way :  {random.choice(LPD.ProgramsOrigin)}")
    text=appendWithNewLine(text,f"- Someone is gunning for you  {random.choice(LPD.NetrunnerGunning)}")
    return text

def TechPath():
    text = "Tech\n"
    text=appendWithNewLine(text,f"- {random.choice(LPD.TypeOfTech)}") # append the random choice and a new line
    Rpathresult = input("""Do you have a partner or do you work alone ?
    1 for solo 2 for group
    """)
    if int(Rpathresult) == 1:
        text=appendWithNewLine(text,"- you are solo")
    elif int(Rpathresult) == 2:
        text=appendWithNewLine(text,f"- your partner is{random.choice(LPD.TechPartnerIdentity)}")

    text=appendWithNewLine(text,f"- workspace {random.choice(LPD.TechTypeOfWorkspace)}")
    text=appendWithNewLine(text,f"- some of your clients are {random.choice(LPD.TechTypeOfClients)}")
    text=appendWithNewLine(text,f"- you get your supplies this way :  {random.choice(LPD.SuppliesOrigin)}")
    text=appendWithNewLine(text,f"- Someone is gunning for you  {random.choice(LPD.TechGunning)}")
    return text

def MedtechPath():
    text = "Medtech\n"
    text=appendWithNewLine(text,f"- you are a {random.choice(LPD.MedtechType)}")
    text=appendWithNewLine(text,f"- you have a partner :  {random.choice(LPD.MedtechPartner)}")
    text=appendWithNewLine(text,f"- workspace {random.choice(LPD.MedTechTypeOfWorkspace)}")
    text=appendWithNewLine(text,f"- some of your clients are {random.choice(LPD.MedTechTypeOfClients)}")
    text=appendWithNewLine(text,f"- you get your supplies this way :  {random.choice(LPD.SuppliesOrigin)}")
    return text

def MediaPath():
    text = "Media\n"
    text=appendWithNewLine(text,f"- you are a {random.choice(LPD.MediaType)}")
    text=appendWithNewLine(text,f"- you publish your work via :  {random.choice(LPD.MediaPublications)}")
    text=appendWithNewLine(text,f"- How Ethical are you ? {random.choice(LPD.MediaEthics)}")
    text=appendWithNewLine(text,f"- The type of stories you tell are  {random.choice(LPD.MediaStories)}")
    return text

def ExecPath():
    text = "Exec\n"
    text=appendWithNewLine(text,f"- Corpo type : {random.choice(LPD.CorpoType)}")
    text=appendWithNewLine(text,f"- Division : {random.choice(LPD.CorpoDivision)}")
    text=appendWithNewLine(text,f"- Type of Boss : {random.choice(LPD.CorpoAlignement)}")
    text=appendWithNewLine(text,f"- Corpo's base of operation : {random.choice(LPD.CorpoBased)}")
    text=appendWithNewLine(text,f"- Person Gunning : {random.choice(LPD.CorpoGunning)}")
    return text

def LawmanPath():
    text = "Lawman\n"
    text=appendWithNewLine(text,f"- Your Position within the force is {random.choice(LPD.LawmanRank)}")
    text=appendWithNewLine(text,f"- Your group's jurisdiction is  {random.choice(LPD.LawmanJurisdiction)}")
    text=appendWithNewLine(text,f"- Your group is {random.choice(LPD.GroupAlignement)}")
    text=appendWithNewLine(text,f"- Some one is Gunning for you : {random.choice(LPD.LawmanGunning)}")
    text=appendWithNewLine(text,f"- Your group's Target of choice is  {random.choice(LPD.GroupTarget)}")
    return text

def FixerPath():
    text = "Fixer\n"
    text=appendWithNewLine(text,f"- You {random.choice(LPD.TypeOfFixer)}") # append the random choice and a new line
    Rpathresult = input("""Do you have a partner or do you work alone ?
    1 for solo 2 for group
    """)
    if int(Rpathresult) == 1:
        text=appendWithNewLine(text,"- you are solo")
    elif int(Rpathresult) == 2:
        text=appendWithNewLine(text,f"- your partner is{random.choice(LPD.FixerPartnerIdentity)}")

    text=appendWithNewLine(text,f"- Your Office is {random.choice(LPD.FixerOffice)}")
    text=appendWithNewLine(text,f"- your side clients are {random.choice(LPD.FixerTypeOfClients)}")
    text=appendWithNewLine(text,f"- Someone is gunning for you  {random.choice(LPD.FixerGunning)}")
    return text

def NomadPath():
    text = "Nomad\n"
    text=appendWithNewLine(text,f"- Your pack is {random.choice(LPD.NomadPackSize)}")
    Rpathresult = input("""Where is your tribe based ?
    1 for land  2 for air 3 for Sea
    """)
    if int(Rpathresult) == 1:
        text=appendWithNewLine(text,f"- your family is Land based they their type is  {random.choice(LPD.NomadLandOperations)}")
    elif int(Rpathresult) == 2:
        text=appendWithNewLine(text,f"- your family is Air based they their type is {random.choice(LPD.NomadAirOperations)}")
    elif int(Rpathresult) == 3:
        text=appendWithNewLine(text,f"- your family is Sea based they their type is {random.choice(LPD.NomadSeaOperations)}")

    text=appendWithNewLine(text,f"- Your role within the pack is {random.choice(LPD.PlayerPackRole)}")
    text=appendWithNewLine(text,f"- Your pack's overall philosophy is {random.choice(LPD.PlayerPackPhilosophy)}")
    text=appendWithNewLine(text,f"- Someone is gunning for you  {random.choice(LPD.NomadGunning)}")
    return text