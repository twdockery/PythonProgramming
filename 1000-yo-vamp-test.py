import os                       # this allows to check on the written file
from random import randint      # this creates a random integer. 


#------------------------------------------------------------------------------------#
# Variable initial states
#------------------------------------------------------------------------------------#

story = 0                   # this is the first digit of the dictionary 
alt = 4                     # this is the second digit of the dictionary



#------------------------------------------------------------------------------------#
# This is the game dictionary. Each round, The key will be determined
# The list in the value will then be cycled though until complete
#------------------------------------------------------------------------------------#

dict = {
"1-1" : ["In your blood-hunger you destroy someone close to you. Kill a mortal Character. Create a mortal if none are available. Take the skill Bloodthirsty."], 
"1-2" : ["You are overcome by panic and maul someone close to you, accidentally turning them into a monster like yourself. Convert a beloved mortal Character into an enemy immortal. Take the Skill Ashamed."], 
"1-3" : ["You are captured and enslaved by a wicked and powerful supernatural entity. Create an immortal Character. How do you eventually escape their servitude? Check a Skill and take the Skill Humans are Cattle. Strike out all mortal Characters, as a hundred years have passed. Take a Resource you have used for evil while in service to your former master."], 
"2-1" : ["Horrified at your new nature, you withdraw from society. Where do you hide? How do you feed? Create a stationary Resource which shelters you."], 
"2-2" : ["You reinvent your existence around the seclusion of your hiding place. You begin to work in an artful way, changing your living environment. How do you come to appreciate beauty or craft in a new way? Create a Skill based on a Memory."], 
"2-3" : ["Your hiding place is destroyed by mortals. What steps had you taken to ensure your survival? What revenge do you wreak upon your persecutors? Degrade a Resource into ruins. Take the Skill Vile Acts. 222"], 
"3-1" : ["A loved one discovers your condition and works to help you. Create a Resource which represents their assistance. Create a mortal Character if none are available."], 
"3-2" : ["You manipulate this mortal into committing atrocious deeds on your behalf. What do you do when they quail at these awful tasks? Take the Skill Humans are Tools."], 
"3-3" : ["At the end of the mortal’s life you convert them into a mindless meat machine, an undying thing from which you feed. What regrets do you have? Change the Character to a Resource. Check a Skill."], 
"4-1" : ["You are exposed and flee to a neighboring region. Lose any stationary Resources. Check a Skill. A mortal flees with you. What new name do you adopt among these strangers?"], 
"4-2" : ["You are adopted into a strange cult who take you in despite (or because of) your outlander origin. Check a Skill and create a Resource, The Secret Cabal. How did they find you? What vile initiation ceremony do you undergo? Do they know what you are?"], 
"4-3" : ["The Secret Cabal, without your knowledge, performs a dark ceremony that changes a mortal Character into a horrific, alien and immortal thing. Convert a mortal Character into an immortal enemy. What alien objectives does this new immortal pursue? Did the Cabal manipulate you into helping with this creation? How does this change your relationship to the Cabal?444"], 
"5-1" : ["You murder someone you love or respect rather than let them expose you. Kill a Character. Check a Skill. If you have no living Characters, kill no one and create a beloved mortal Character who you have betrayed."], 
"5-2" : ["A Character you’ve victimized comes to you in a dream. Do they curse or forgive you? Receive a Mark."], 
"5-3" : ["Love hidden within your soul propels you on a foolish quest for absolution from some great guilt. What wrong did you try to right? How do you fail and make everything much, much worse? Lose a Resource. Check a Skill."], 
"6-1" : ["A mortal Character begins serving you. Who are they? Why are they drawn to you? Create a new mortal Character."], 
"6-2" : ["A trusted mortal Character betrays you in a surprising way. Lose a Resource. Why did they do this? Why do you forgive them?"], 
"6-3" : ["A mortal Character sacrifices themselves to save you. Check a Skill. Gain a Skill relevant to love or trust."], 
"7-1" : ["Your body manifests some trait related to the vampire that created you. How do you become more like them? Create a Skill that reflects this."], 
"7-2" : ["People see a horror in you that you cannot perceive in yourself. What Mark do you possess that you do not know about? Create a Mark and a suspicious mortal who has seen it. What name do the people call you when your back is turned?"], 
"7-3" : ["Through grim work with iron and fire you remove a Mark. Record an Experience of pain and blood. Who do you blame? You may remove a Mark or replace an existing Mark with something worse."], 
"8-1" : ["You are recognized for what you are by another creature like yourself. Create an immortal Character, lose a Resource and gain a Skill. What did you lose to them?"], 
"8-2" : ["You gain an advantage over an immortal Character. What do you take from them? What do you learn? Convert a Memory to a Skill; strike out that Memory. Gain a mysterious Resource."], 
"8-3" : ["A Character you’ve angered has powerful allies. Create a new enemy immortal Character who is the face of this mysterious group which harries you. Check a Skill to escape their grasp. Take the Skill Time to Leave. Move to a far-off region and lose any stationary Resources. Take a new name."], 
"9-1" : ["You develop a system for feeding. What is it? What happens to those who die? Create a Skill that reflects this."], 
"9-2" : ["You not only drink their blood but financially profit from your victims as well! How do you arrange this? What atrocity do you commit to protect this system? Check a Skill, create a Resource."], 
"9-3" : ["Another Character usurps your feeding system and improves it. Do you crawl back to your ouster, begging to be let back in? If so, then gain the Skill Belly on the Ground. If you instead build a new feeding system from scratch, check two Skills and gain one Resource."], 
"10-1" : ["The stars pinwheel above you in the night. The seasons are a blur. You are as an automaton, unconscious of the passage of decades. A century passes. Strike out a Memory. Strike out all mortal Characters."], 
"10-2" : ["A potent artifact, religious or magical or technological, falls into your hands. With it you can remake the world. What is this thing? Who seeks it? Create a mortal Character. Add the item as a Resource. If you still have it when you achieve any game ending result, you may rewrite the ending as you like. You must lose this item first if you lose Resources in an encounter with an immortal Character."], 
"10-3" : ["While fiddling with the artifact you accidentally bring about the end times. Devils rise, angels fall, spirits are made manifest. Human populations are levied in a war which will last centuries and decide the fate of the cosmos itself. Create a Character or Resource that represents the manifestation of a supernatural conflict that fits your story up to this point. Create two immortal Characters aligned with either side of the conflict who are now interested in your Vampire.010"], 
"11-1" : ["How do you find solace from the raging hunger within you? You may lose one checked or unchecked Skill."], 
"11-2" : ["You discover an internal focus which lets you maintain control of your vampire self. Lose a violent Memory and take the Skill I Control the Beast and rewrite any unchecked Skill as something new. What new name do you take to distance yourself from what you once were? How is the name symbolic?"], 
"11-3" : ["Your control breaks. You slaver and kill and revel in blood. You are your hunger. What were the last words of your closest friendly Character, mortal or immortal, as you feasted upon them? Change a beloved Memory to a lie in which you murder to protect yourself. Create a Skill that invokes the name of a dead Character in a mocking way."], 
"12-1" : ["New laws or social mores make it harder for you to hide among the populace. How are you nearly caught and destroyed? Check a Skill. Create a Skill. Create a mortal criminal who assists you."], 
"12-2" : ["Working across generations you change the laws of society to your advantage. How do you bend leaders to your will? What do you change? Create a Resource."], 
"12-3" : ["A mortal protégé outstrips you. They are smarter, crueler, and more capable than you can ever be. They lock you in a dungeon—for what purpose do they use you? Create a wicked mortal Character. 121212"], 
"13-1" : ["Generations of the same family serve you. This line starts from any living mortal Character, or from the descendants of a dead mortal Character. What bizarre rituals do they tie to their servitude? Lose a Resource and create a Servitors of the Lineage Resource."], 
"13-2" : ["Your servants are numerous, enthusiastic, and sometimes useless. Create a Skill based on a Memory, this is the Skill you use to control them."], 
"13-3" : ["Your servants bring you a gift you do not want. Create a problematic Resource."], 
"14-1" : ["An enemy Character uses a lost Resource to turn your few friends against you. Check three Skills to regain the Resource, or check one Skill to barely survive. Which former friend did you kill? Where do you flee?"], 
"14-2" : ["You were born in a time and place much different than that in which you find yourself now. What values must you set aside to survive in this strange world? Create an appropriate contemporary Skill based on your most recent Memory. What new name have you recently adopted?"], 
"14-3" : ["How do you rise to a position of leadership in this place? What neighbors or populations do you subjugate through war and violence? Gain a Resource you took from someone who wanted nothing but peace."], 
"15-1" : ["While traveling you come into conflict with another immortal. Gain a Mark. Who are they? What trick did you play upon them? Create a new immortal Character."], 
"15-2" : ["An immortal proves to be much more than they appear. Check a Skill or else lose a Resource or Memory. Gain a Resource or Skill."], 
"15-3" : ["How does human society change drastically due to the meddling of immortals like yourself? Who benefits? What Resource do you lose? Gain one Resource, Skill or Mark."], 
"16-1" : ["Some mortals have banded together to hunt you, well-armed and wise to your tricks. How do you defeat or evade them? Create a mortal hunter related to one of your checked Skills. Check a Skill."], 
"16-2" : ["The hunters are persistent, capable, and well-informed. They know things about you that you don’t—create a Mark that is revealed in a confrontation. You are driven into hiding in an unpeopled wasteland. Lose any stationary Resources. Learn a new Skill related to this desolate region. What new name comes to you in loneliness?"], 
"16-3" : ["Returning to civilization you wreak a terrible vengeance upon the hapless descendants of your harassers. Songs will be sung of their suffering for a thousand years. Historians will use it as a benchmark for evil. Create a mortal Character that was innocent and good until you exacted your toll. Do not actually write down what acts you committed against these people."], 
"17-1" : ["You commit a despicable murder, but not for the sake of feeding. Why? Check a Skill. Remove a mortal Character, if you like."], 
"17-2" : ["You are hounded for your crime. Check a Skill, lose a Resource. Confess your crime to any Character. Convert an enemy to a friend or a friend to an enemy. If you must create a Character, you become lovers."], 
"17-3" : ["You fight a duel with a beloved Character, create one if you have none. Check a violent Skill or appropriate Resource and win by killing them, or gain a Mark and flee to another land. 171717"], 
"18-1" : ["You have fed too long in one place, destroying a community or social group. Who were they? How did the last community member die? Gain a scavenged Resource, lose a Resource."], 
"18-2" : ["A community outcast has survived and vows to revenge themselves upon you. How did you know them? How did they know to catch you at your most vulnerable? Create a mortal Character bent on your destruction."], 
"18-3" : ["You are hounded out of the land. Lose any stationary Resources. Check one Skill to escape, two to destroy your persecutor, three to make amends."], 
"19-1" : ["Two friendly Characters become embroiled in an internecine conflict. Become involved and check a Skill. Create up to two Characters, if needed. How do you profit? Gain a Resource."], 
"19-2" : ["You scheme while your friends make war on one another. Manipulate the conflict to destroy any Character."], 
"19-3" : ["Too much fighting, too much blood. Acting as peacemaker you try to end the conflict between former friends, but they both turn on you. Lose a Resource. Gain a Mark. 191919"], 
"20-1" : ["There is a great shift in the way society moves goods. How does this work to your advantage? Check a Skill. Create a Skill based on a Memory."], 
"20-2" : ["Your vampiric state enables you to manipulate people across generations, using them to your own advantage. Create one stationary Resource and one ostentatious Resource that symbolizes wealth and power."], 
"20-3" : ["Living off investments and rents makes you lazy and blunts your hunting edge. Check a Skill that is cruel or grasping, lose a checked Skill related to creativity or effort. Gain a stationary Resource that you didn’t truly earn.020"], 
"21-1" : ["You are trapped outside when the sun rises and take shelter some place you are not supposed to be. A child discovers and befriends you. Create a mortal child Character and record a humanizing Experience."], 
"21-2" : ["The child teaches you to appreciate the world again. You see small things, you smile. Create a Skill based on a pleasant Memory."], 
"21-3" : ["Decades pass. The child has died of old age. You stand at their grave. What more could you have done to make their life better? How did you betray them? Strike out that Character with great ceremony."], 
"22-1" : ["Create a mortal Character. You have shaped them from infancy to be exactly what you want. Lose a Resource."], 
"22-2" : ["Your Diary is lost or stolen. Lose the Diary and all Memories it contains. If you have no Diary, lose one Resource. Create a Character who you wrongly blame for this loss."], 
"22-3" : ["You become a loner embedded in the now, manipulating a hundred threads to stay fed and safe. Lose a Memory slot permanently. Take the Skill Feral Cunning. 222222"], 
"23-1" : ["You master a strange new science or field of knowledge. How does your vampire nature give you special insight into these studies? Create an appropriate Skill based on a Memory."], 
"23-2" : ["You strike up a long correspondence and fall in love. Create a mortal Character. Go to them by giving up a Resource, or smother the love and lose a Memory."], 
"23-3" : ["Your mortal love dies through the machinations of another Character unless you check one Skill. If you do save them they will instead die of sickness, or accident, or old age. Either way, you keep a token by which to remember them. Create a Resource."], 
"24-1" : ["You are forced to adopt a new name. Why?"], 
"24-2" : ["Erase the first sentence of any two Memories. You’re not quite sure why. Do not create an Experience about this."], 
"24-3" : ["One place is as another to you, and you simply stop returning home. Lose a stationary Resource. Where do you wander?242424"], 
"25-1" : ["Your methods for acquiring victims are no longer effective. What has changed? Lose a Resource and create a Skill which describes your new feeding techniques."], 
"25-2" : ["What physical labors are necessary to utilize this method? Create a simple, practical Skill and strike out a Memory."], 
"25-3" : ["A mortal Character discovers your feeding system. What compelling argument do they use to get you to abandon it? Check a Skill. 252525"], 
"26-1" : ["You accidentally create a vampire through sloppy feeding. Create an immortal Character from an existing mortal Character. Why do you not destroy them? Check a Skill."], 
"26-2" : ["This immortal Character lurks on the fringes of your existence. They become an embodiment of one of your least savory checked Skills. How do they act when your paths cross? What disturbing gift do they give you? Create a Resource."], 
"26-3" : ["This immortal Character falls into the hands of mortals, indirectly imperiling your existence. Save them by checking three Skills. Lose three Resources if you do not save them. If you cannot lose all three Resources, lose as many as possible and flee to a new land—from now on all humans know vampires are real."], 
"27-1" : ["Wars rage throughout the region in which you reside. You withdraw into a hidden retreat, waiting for them to pass. Lose a Resource."], 
"27-2" : ["Your secretive ways result in you being arrested as a spy. Check a Skill to escape or lose a Resource and gain a Mark from the experiments performed upon you. Either way, create a mortal who heads a well-funded organization that imperils creatures such as yourself."], 
"27-3" : ["You become a spy, selling out the land you call home. Gain two Resources. Check a Skill, gain a Skill, uncheck an ancient and surprising Skill. Which Character suffers and dies because of your actions?272727"], 
"28-1" : ["A long dead mortal Character returns. What do they want from you? How have they survived death? You only recognize them if you still have a related Memory. Check a Skill."], 
"28-2" : ["What peril do they pull down upon you? Create a new enemy Character, mortal or immortal. Check a Skill or lose a Resource."], 
"28-3" : ["You are ceaselessly hunted by potent, supernatural beings. Describe the methods you develop to avoid detection. Lose a Memory to gain a Skill or Resource, or do not lose a Memory and create a mortal servitor."], 
"29-1" : ["You are exposed as a monster and flee to a far-off land. Lose any stationary Resources. You do not know the language of this new place—how do you overcome this obstacle? What new name do you take?"], 
"29-2" : ["You disguise yourself with an entirely new persona. Take an old Memory and modify it to make it contemporary and bland. Create a Skill based on blending in."], 
"29-3" : ["You lose yourself in your assumed personality. Lose your oldest and newest Memories. Throw away your Diary. Create a Skill and Resource tied to your new life."], 
"30-1" : ["What social mores have your forgotten? Lose a checked Skill."], 
"30-2" : ["You feel a love forbidden by the convention of mortals around you. Create a new Character. Lose a Resource."], 
"30-3" : ["You reinvent yourself and how you relate to the world. Uncheck a Skill.030"], 
"31-1" : ["You fall into a deep slumber for a hundred years. Strike out any mortal Characters."], 
"31-2" : ["You recognize the descendant of a dead mortal who features in one of your Memories, and feel compelled to make their acquaintance. How do you share knowledge about their ancestor without revealing your monstrous nature? How is this conversation awkward? Gain a contemporary and unexpected Skill. Create a mortal Character, a new friend."], 
"31-3" : ["Your mortal friend discovers family documents that reveal you for what you are. How does your relationship change? You may regain a forgotten Memory related to the mortal’s ancestor."], 
"32-1" : ["You keep a prisoner. Why this particular person? Why don’t you feed upon them? Create a Character and a Skill related to keeping them captive."], 
"32-2" : ["Mortals rescue your prisoner. Create two mortal rescuers. Lose a Resource."], 
"32-3" : ["Your prisoner returns to you, but on their own terms. What is this strange new relationship?323232"], 
"33-1" : ["You know where the old things are. Create a Resource and make an enemy Character into a friend."], 
"33-2" : ["You publish a book or in some other way cement a Memory (either current or from your Diary) in such a way that it can never be lost. Draw a star next to the Memory to indicate this and change the Memory to make it slightly less interesting. This Memory can never again be changed or struck out. It no longer takes up a Memory slot."], 
"33-3" : ["A massive shift of power happens in the mortal realm—governments fall, wars are waged, a new order is created. Who benefits? Check a Skill. Commit atrocious deeds to gain a Resource related to controlling innocent people. Take the Skill Join the Winning Side or instead check two Skills."], 
"34-1" : ["You destroy something important to you in a purposeless rage. Lose a precious Memory or destroy a Resource."], 
"34-2" : ["Your frenzies terrify even yourself. Do you learn to control them or instead choose to embrace this horror? Kill a mortal Character, if there is one, or create a Mark if not."], 
"34-3" : ["Pull the very skin from your face in an attempt to expunge yourself of lingering humanity. Create a Mark. How do you cover your disfigurement going forward?343434"], 
"35-1" : ["You encounter the descendant of an old foe and help them in some way. Why did you do this? Check a Skill. Create a mortal Character."], 
"35-2" : ["They repay your kindness by lashing out at those they perceive as your enemies. A Character is killed."], 
"35-3" : ["The mortal is in grave peril. Check a Skill or lose a Resource to save them, otherwise they die a terrible death."], 
"36-1" : ["The deceptions you practice fool even yourself. Combine any three Traits to fabricate an Experience that you believe to be true."], 
"36-2" : ["Punish someone because of this false Memory. You kill a or maim a Character. Check a Skill. Take the Skill I Know What’s Real."], 
"36-3" : ["One of your real Memories turns out to be completely fabricated, a fever dream spun of cobwebs. Completely erase one Memory."], 
"37-1" : ["Things fall to dust. Lose a Resource for which you have no corresponding Memory. Do not create a new Experience for this Prompt, it simply happens as you stare in silence."], 
"37-2" : ["You are a creature with habits of unknown origin. Lose an unchecked Skill for which you have no corresponding Memory."], 
"37-3" : ["Your thoughts are calcifying, your habits are tyrants. You are nearly captured by an enemy who has been studying your patterns over many years. Break a Resource and remake it into something new and surprising."], 
"38-1" : ["Your whole being becomes centered in your senses and your hungers. Create a Skill that demonstrates your feral vampire nature and lose an existing Memory."], 
"38-2" : ["You move differently than humans and they unconsciously sense it. Create a Mark."], 
"38-3" : ["You can always find the frail, the weak, the vulnerable. Take the Skill Cull the Herd. Do not meet the eyes of the strong—they are not for you."], 
"39-1" : ["Age has damaged your Diary. Strike out three nouns from the Memories in your Diary, starting from the oldest entry. If you have no Diary, do this to the first three nouns in a Memory of middling age."], 
"39-2" : ["You make a new copy of your crumbling Diary. In your most recent Diary Memory, swap two verbs each for the other. If you have no Diary strike out three verbs in your most recent Memories."], 
"39-3" : ["Find a character record from an earlier play through of this game. Swap a Memory for one from that character sheet."], 
"40-1" : ["How do you conceal yourself while you sleep? What steps have you taken for protection? Check a Skill and create a Resource. Create a mortal servant Character, if you like."], 
"40-2" : ["You are approached by a supernatural Character unknown to you. They take you on a bizarre journey, then offer you spiritual solace in exchange for a terrible pledge. What do they demand? Will you accept? If you accept, gain a Skill."], 
"40-3" : ["The potent beings which populate the spaces beyond sight have been revealed to you and nothing will ever be the same again. Let this bizarre world heavily influence the rest of your game. Take the Skill I See In-Between.040"], 
"41-1" : ["Your body is distant from human concerns. Lose a Memory slot. Erase your oldest extant name."], 
"41-2" : ["A social convention or taboo from some long-forgotten part of your existence is hardwired into your being. What is it? How does this hinder your movement in society? Create a Mark."], 
"41-3" : ["A ghost haunts you, though you do not know if it is real or a manifestation of madness. Bring back a long dead Character as a spirit. 414141"], 
"42-1" : ["What piece of contemporary technology can you notinteract with due to your vampire nature? How did your first encounter with this technology almost get you destroyed? Check a Skill."], 
"42-2" : ["You make the acquaintance of a group of mortals who share an interest in some Resource you possess. Is it a club? Are these friends? Create three mortal Characters. Develop a Skill related to the Resource in question."], 
"42-3" : ["Decades pass. You remain ageless as your friends slowly curl and dry up; you must leave or be exposed as a monster. Stand outside in the darkness, watching them laugh as they tell stories of how they miss you."], 
"43-1" : ["You have archaic ways in spite of your focus on blending in. Create a Resource based on a checked Skill that reflects this."], 
"43-2" : ["Swap around the proper nouns between two Memories. Do not create an Experience about this."], 
"43-3" : ["Examining a Resource you possess sparks a forgotten Memory. That Resource once belonged to another Character, but you had forgotten this. Gain tremendous insight into your history by recalling this Memory. Write this forgotten Experience into your Memory or directly into a Diary. To be clear, you are creating a new “forgotten” Experience, not bringing back a Memory you struck out."], 
"44-1" : ["An immortal Character you’ve met returns to claim a debt. What is it? How have they changed? Do you pay willingly? If you have a Memory of this Character you lose two Resources, if not then lose three Resources and check a Skill."], 
"44-2" : ["What did they do to send you into the darkest despair? Erase your earliest Memory. You will never get it back. Gain a Skill."], 
"44-3" : ["You develop a plan and carry it through with ruthless efficiency, bringing death and destruction to an immortal Character. You may either reclaim a Resource they took, or destroy them. Check a Skill."], 
"45-1" : ["Your body is undergoing further corruption and change. When do you first notice these new changes? Create a Mark."], 
"45-2" : ["Your body is becoming more effective as it becomes less human. Create a Skill based on one of your Marks."], 
"45-3" : ["You find companionship in a group of mortals who are in some way outside society. Do they know what you are? Would they care? Create two friendly mortal Characters, each related to one of your Marks."], 
"46-1" : ["You are exposed and flee to a far-off land. Convert any stationary Resources to a new Resource representing portable cash or treasure. What name do you travel under? What profession do you claim when you come to rest?"], 
"46-2" : ["You flee again, this time to a far-off enclave or colony. How do you use colonial rule to your benefit? Choose one Skill: Occupier, Insurgent, Inconspicuous, or Gone Native along with an appropriate new name."], 
"46-3" : ["Revolution! As a suspicious outlander you are imprisoned. Escape by checking two Skills or bribe your way free with two Resources. Spend an additional Resource to rescue any traveling companions."], 
"47-1" : ["The world has evolved in ways you can’t comprehend, causing you to lose a good amount of wealth. What happened? Check a Skill. Create a Skill that will hopefully prevent this happening again. Lose a Resource."], 
"47-2" : ["You have helpless people put in your charge. Create a Skill that helps you exploit them. Derive it from a happy Memory."], 
"47-3" : ["You are impressed by the fighting spirit of one of your victims. What did they do? How do they remind you of your own earliest memories? Did they survive? Create a mortal Character."], 
"48-1" : ["You awaken covered in dust. Generations have passed. Your sleeping place has been sealed off. How do you escape? Lose a Resource. Strike out all mortal Characters."], 
"48-2" : ["A Mortal you thought dead is still alive, somehow. Remarkable! Bring back the most recently struck out mortal Character."], 
"48-3" : ["In your long dreaming you discover a path to lands beyond the real, a fantastic place of enormous terrors and great beauty. You may abandon this Earth and go where none may follow; leave behind all Characters, Marks, and Resources except a Silver Sword and return to Prompt 10. Proceed forward from there, an unMarked vampire in a realm of dreams. If you land on this Prompt a second time, you awaken and can never return. If you do not travel to this dream land you instead take the Resource A Handwritten Book of Fantastic Dreams."], 
"49-1" : ["What simple, practical skill proves invaluable in your strange existence? How did you learn it? Create a Skill."], 
"49-2" : ["How did you come to be in a place of common laborers? What previously checked Skill convinced them to accept you? What was that night of camaraderie like? Create a mortal Character. Check a Skill."], 
"49-3" : ["Your new friends become a source of food. Create a Resource that reflects this."], 
"50-1" : ["You are captured in a trap set for predatory mortals. What sort of criminal are you taken to be? How does this experience help you learn to better prey on mortals? Make a new Skill that sours the purity of a pleasant Memory."], 
"50-2" : ["You are almost uncovered and must dramatically shift your hunting patterns. Become a member of the lowest classes and lose a Resource. If you already are of the lowest classes instead become a member of the highest and check a Skill."], 
"50-3" : ["You take up with predatory mortals. Create a repugnant mortal Character who becomes your associate. Even you fear these people. Why?505050"], 
"51-1" : ["When you hunger too much you become a hunting creature bereft of intellect. Lose a random Experience from a Memory somewhere in the middle of your Memory list."], 
"51-2" : ["You find companionship in something that is not human. Is it an animal, or maybe something inanimate? How do you interact with it? How did you find it, or did it find you? Create either a Character or Resource to represent this companion."], 
"51-3" : ["All things end, but apparently not this. A mortal Character for whom you hold great affection is un-aging. Is it magic? Some form of infection? They still count as a mortal Character, but they will never die of old age."], 
"52-1" : ["The beauty of the dawn calls you. Create an additional Memory slot dedicated to beauty, nature, or peace."], 
"52-2" : ["You stay long enough to hear the end of a morning bird’s song. You are burned by the Sun—create a Mark."], 
"52-3" : ["Stretch out your arms, feel the warmth. The light pushes through your eyelids and you are not consumed in fire. Sunlight (or some other environmental condition) no longer harms you. Create a Skill about freedom. 525252"], 
"53-1" : ["A mortal Character you trusted, or one of their descendants, leads a hunting party. What shared secrets are being used against you? Check a Skill."], 
"53-2" : ["You have the troublemaking Character at your mercy. Record an Experience of forgiveness."], 
"53-3" : ["They betray you again and escape. Lose a Resource or gain a disfiguring Mark."], 
"54-1" : ["Your strange accent and old ways always reveal you as an outsider, mocked and cheated at best or hated at worst. Smother these useless traits by converting an old Memory to a new Skill for blending in."], 
"54-2" : ["Your old memories are changing to reflect the attitudes you need in the present. Change a Memory to incorporate anachronistic, contemporary aspects. Do not create a new Experience."], 
"54-3" : ["Discard a Resource that is more than a hundred years old."], 
"55-1" : ["Timeless introspection becomes manifest in creative acts. Choose a creative Skill based on a lost Memory."], 
"55-2" : ["You dedicate yourself to an art. Lose a Resource but gain back one lost Memory."], 
"55-3" : ["You achieve fame for your art but must remain in shadow. Destroy a Resource in frustration. Gain a Skill."], 
"56-1" : ["You begin a fantastic construction that puzzles the mortals around you. Give just a hint as to its purpose. Lose a Resource and gain the Skill Visionary."], 
"56-2" : ["Mortals try to prevent you from realizing your vision. Check a Skill to persevere. What awful crime did you commit to protect your construction?"], 
"56-3" : ["You’ve finished your construction. Why did you make this? Does it have a function? Does it change the world?"], 
"57-1" : ["Your knowledge of old things becomes a strength. Based on a checked Skill, what knowledge do you share with contemporary mortals? Check a Skill. Create a Resource."], 
"57-2" : ["What humans seek you out for your knowledge? What do you give them? What do you take? Create a mortal Character who is smarter and more capable than you. Gain a Resource."], 
"57-3" : ["You are brought to the site of one of your oldest crimes. Who brought you here? Why? Do you even remember? Check a Skill. If you have no Memory of this crime, you will be reminded."], 
"58-1" : ["Society has changed. How has travel become easier for you? Recover any stationary Resources for which you still have a Memory, they are re-added to your Resource list."], 
"58-2" : ["What memories are unearthed by wandering these old places? Get back a lost Memory related to the stationary Resource, or gain a new treasure Resource which you’d concealed here."], 
"58-3" : ["What grisly trap was set for you here? Lose a Resource, gain a Mark."], 
"59-1" : ["A mortal discovers the journals of a long dead Character, or your own lost Diary, and approaches you. What do they seek? Gain a Skill or a Resource. Create a mortal Character."], 
"59-2" : ["The mortal harms, shames or exposes you. Check a Skill as you fruitlessly pursue them. Lose a Resource."], 
"59-3" : ["The mortal’s lust for forbidden knowledge results in the release of a supernatural horror upon the world. Is this a gigantic monstrosity that will eventually destroy the world, or a personal horror set upon destroying you in particular? Create an immortal Character or Characters."], 
"60-1" : ["Check a Skill to avoid arrest as a criminal. What happened? Who was arrested in your place? Create a mortal Character if necessary."], 
"60-2" : ["Create an innocent mortal Character. They were executed for a crime you committed. What hobby were you tinkering with the night they were put to death? Take the Skill It’s None of my Concern."], 
"60-3" : ["An entire class of people are blamed for crimes you committed. Take the Skill Always Have a Scapegoat. Who suffers in your place? Create a friendly Character who represents these people and is ignorant of your complicity. Create another Character who is in a position of authority; they know these people are innocent but do not care."], 
"61-1" : ["Someone reminds you of a beloved Character long dead. Check a Skill to curry their acquaintance. Create a mortal Character."], 
"61-2" : ["You frequently confuse living mortals with a dead Character. Take the Mark I See [dead Character] Everywhere."], 
"61-3" : ["Your body is ancient. A Mark becomes disabling. You must seek mortal assistance. Create a mortal Character who is especially capable of helping you."], 
"62-1" : ["You realize that some ancient taboo or limitation you long believed in no longer applies. What circumstances prompted this discovery? How does this make your existence more satisfying? Change one checked or unchecked Skill in a way that’s relevant."], 
"62-2" : ["You discover a point of weakness where you were once strong. What have the ages taken from you? What causes this condition? Lose a checked Skill."], 
"62-3" : ["You receive an injury which incapacitates you. Left alone you would recover, but helpful people rush you to a hospital. There you awaken, and realize that you are known. Create a Character: a horrified mortal medical professional who knows exactly what you are."], 
"63-1" : ["How do you provide for your banal, material needs? Record an Experience about the time this went wrong. Check a Skill."], 
"63-2" : ["How do you avoid the eye of the government? Create a Skill based on a Memory."], 
"63-3" : ["How do you try to fool yourself into thinking you provide a valuable service to society? Take the skill Parasite."], 
"64-1" : ["Vast numbers of humans are migrating around the world. What group becomes easy to feed upon? How do you capitalize on their helplessness? Create a Resource."], 
"64-2" : ["You manipulate society’s leaders to make one group of humans even more vulnerable to your vampiric feeding. What system do you build around victimizing these people? Check a Skill, create a relevant Skill from a Memory. Create a Character who is central to those resisting your machinations."], 
"64-3" : ["Society collapses on a global scale and will not recover for centuries. Millions starve, governments dissolve, there is murder in the streets as cities burn. How do you take advantage of the chaos? Check a Skill. Create two new Resources. Create a Skill. What Character rises to a position of global leadership in these awful times?"], 
"65-1" : ["A possession turns out to have financial value as an antique. Trade your oldest Resource for two contemporary Resources."], 
"65-2" : ["You experience intense regret over a Resource you have given away or lost. Do anything to get it back. Lose two Resources or check two Skills and get back one lost Resource."], 
"65-3" : ["Objects are transient. All is nothing. Throw away your oldest or most precious Resource."], 
"66-1" : ["Your knowledge is outmoded. Lose an unchecked Skill which is now useless."], 
"66-2" : ["Your concept of value is outdated. Lose a Resource."], 
"66-3" : ["You are so ancient you no longer look like the people of today. Create a Mark that reflects this. How do you come to realize that your very body no longer fits in?"], 
"67-1" : ["Language itself leaves you behind. People discuss concepts you cannot grasp using tools you cannot understand. How is this problem dramatically made manifest? Create a Character who will teach you a Skill to help you offset this disadvantage."], 
"67-2" : ["New forms of communication offer new ways to hunt. Modify an old Memory to include an anachronistic use of this sort of contemporary communication technology. Check a Skill, create a Skill."], 
"67-3" : ["Language has grown into something outside your ken. You can invoke phonemic patterns to which mortals will react in certain ways, but you can no longer share actual thoughts or feelings or abstract ideas. Create a Skill that expresses this."], 
"68-1" : ["An antiquity has surfaced which is directly tied to your mortal life. Check a Skill or lose a Resource and gain the antiquity as a Resource, then regain one of your earliest Memories. Record an Experience about acquiring the antique."], 
"68-2" : ["Because of this antiquity someone has begun to hunt you. Create a mortal Character. How do they almost expose you? Check a Skill or lose a Resource."], 
"68-3" : ["The mortal Character hunter corners you. You become the embodiment of one of your Checked Skills to defeat them. Take a Mark."], 
"69-1" : ["You bond with an ancient enemy Character over your shared past, finding in it something more comprehensible than this modern world. Check a Skill. You become friends. Share a Resource and gain a Resource that is shared with you."], 
"69-2" : ["You and your friend retire to a hidden place. There you share real pleasure for the first time in centuries. Create a Skill about love and safety."], 
"69-3" : ["You and your friend concoct a fantastic plan and bring it to fruition. Check a Skill. What is it? Do you conquer the world? Raise the dead? You may end the game now, if appropriate."], 
"70-1" : ["Mortals are cruel and work in ways outside your understanding. How were you mocked or victimized? Why was your response ineffectual and costly? Check a Skill."], 
"70-2" : ["An important Memory is tainted by your exposure to the psychological tricks of contemporary society. Modify a Memory to make it less special. Lose an unchecked anti-social Skill."], 
"70-3" : ["Lose a Memory. Record an Experience driven by a desire for contemporary prestige items. Lose two Resources, gain one prestigious Resource."], 
"71-1" : ["An immortal Character has been destroyed by mortals. How did you come to find out about this? What did you lose? Create a Skill based on a Memory. Create an immortal Character if necessary."], 
"71-2" : ["How were you unintentionally responsible for this killing? What minor benefit did you gain? Gain a Resource."], 
"71-3" : ["Create a false Experience about an immortal Character, which helps you make peace with your memories of them."]
} 


#------------------------------------------------------------------------------------#
# This is the function that starts the game
#------------------------------------------------------------------------------------#

def gameStart():
    gameName = str(input("Let's begin with the name of your character: "))
    charDescription = str(input("Give me 2-3 short sentences about them before they became a vampire (250 Characters or less): "))

    # Ensure the description is 250 characters or less
    while len(charDescription) > 250:
        print("Needs to be shorter. Try again.")
        charDescription = str(input("Give me 2-3 short sentences about them (250 Characters or less): "))

    file_name = gameName + ".txt"

    # Check if the file already exists
    while os.path.exists(file_name):
        rename_option = input(f"The file '{file_name}' already exists. Do you want to rename it? (yes/no): ")

        if rename_option.lower() == 'yes':
            new_name = input("Enter the new file name: ")
            file_name = new_name + ".txt"
        else:
            # If 'no' is chosen, break out of the loop to overwrite the existing file
            print("The previous file has been overwritten. Let's begin...")
            break

    # Write to the file
    try:
        with open(file_name, "w") as f:
            f.write("This is the story of " + gameName + "\n\n" + charDescription)
            # debug
            # print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")




#------------------------------------------------------------------------------------#
# This is the MAIN FUNCTION of the game
#------------------------------------------------------------------------------------#

gameStart()


"""
roll = randint(1,10) - randint(1,6)
if roll < 1:                # roll cannot be negative
    roll = 0
    alt += alt              # with zero, alt is added
    if alt > 3:             # if already hit 3rd option, one is added and alt is reset
        roll = 1
        alt = 1
else:
    alt = 1                 # in roll > 0 , alt is reset

turn = story + roll

print (story)
print (roll)
print (turn)

storyEntry = str(turn)+"-"+str(alt)
print(storyEntry)
print(dict[storyEntry])
"""
