import random

# Stats

life = 25
energy = 15
square = 808
tracker = 0
path = []

# Help

help = {'hoarse' : {'yes' : 'Your throat is too dry.', 'no' : {1 : 'Hello?!', 2 : 'Is anyone there?', 3: 'Someone help me, please!' }}}
help_counter = 1

# Attacked

attacked = {1 : 'You are cut deeply', 2 : 'You\'ve been bit!', 3 : 'Bones are crunching.', 4 : 'All you hear are your own screams.', 5 : 'The creatures shakes you like a rag doll.'}
fight_success = {1 : 'Nice hit! Keep fighting.', 2 : 'That one landed. It howls in pain.', 3 : 'Good shot! Right across the jaw.', 4 : 'Bones crunch. Yours or theirs. It isn\'t clear.', 5 : 'If you give up, you\'re as good as dead.'}
poison_text = {1 : 'You\'re beginning to feel sick.', 2 : 'Your bite wound is throbbing more every minute.', 3 : 'Your vision is blurry, you are poisoned.', 4: 'That was probably a venomous snake, you should find help soon.', 5 : 'You are dizzy, the venom is taking hold.'}
first_attack = True
wolf_text = {1 : 'The moon is much brighter for some reason.', 2 : 'Your wounds are throbbing.', 3 : 'It is becoming much easier to see in the dark.', 4 : 'You are hungry, a gnawing in your gut.', 5 : 'You\'ve been out here too long, the wilderness calls.'}
inspect_text = {'0701' : {'direction' : 'S', 'S' : 'There is a tangle of branches and vines. It will take some effort to push through.', 'Yes' : 'You make it through but not without a few extra scratches.', 'passed' : False},
                '0603' : {'direction' : 'S', 'S' : 'There is no path but it appears as if someone has gone this way.', 'Yes' : 'You twisted your ankle on exposed roots. Take it easy, it should be ok.'},
                '0603' : {'direction' : 'E', 'E' : 'It would be difficult but you could slip between the trees here.', 'Yes' : 'You made it but not without getting stuck. Your knee is swelling.', 'passed' : False},
                '0603' : {'direction' : 'N', 'N' : 'The ground is overgrown and covered with thorns but it might be passable.', 'Yes' : 'You are cut and bleeding.', 'passed' : False},
                '0503' : {'direction' : 'S', 'S' : 'The ground here is overgrown. There may be a way through these thorns.', 'Yes' : 'You are cut and bleeding.', 'passed' : False},
                '0703' : {'direction' : 'N', 'N' : 'It is treacherous but you might be able to make it.', 'Yes' : 'You slipped on a rock, no permanent damage but you\'re going to be sore.', 'passed' : False},
                '0604' : {'direction' : 'W', 'W' : 'There is no solid ground here. It\'s your decision to proceed...or not.', 'Yes' : 'You made it but you pulled something struggling in the mud. You\'ll be slower for now.', 'passed' : False},
                '0304' : {'direction' : 'S', 'S' : 'This is not the main trail. It looks hard to get through.', 'Yes' : 'You took a few scrapes on the way but made it through.', 'passed' : False},
                '0404' : {'direction' : 'N', 'N' : 'This is a difficult path, be careful.', 'Yes' : 'You make it with a few new bruises.', 'passed' : False},
                '0804' : {'direction' : 'S', 'S' : 'There is a sound from the other side. You\'ll have to make your own trail.', 'Yes' : 'You manage to blaze a trail but not without injury.', 'passed' : False},
                '0807' : {'direction' : 'E', 'E' : 'There looks like a passage here but it\'s treacherous.', 'Yes' : 'You spill out into the field where you began. Scratched, bruised but you\'ll survive...probably.', 'passed' : False},
                '0808' : {'direction' : 'W', 'W' : 'The overgrowth is dense. You\'ll have to fight your way through.', 'Yes' : 'You took some damage but found this place, somehow.', 'passed' : False},
                '0607' : {'direction' : 'E', 'E' : 'It is not an easy passage but anything is better than here.', 'Yes' : 'You made it with a new gash on your arm. The bleeding isn\'t too bad.', 'passed' : False},
                '0608' : {'direction' : 'W', 'W' : 'There is a dark and foreboding space beyond but it might be possible to get through.', 'Yes' : 'You took a deep cut to the arm but it won\'t bleed much.', 'passed' : False},
                '0711' : {'direction' : 'N', 'N' : 'The trees are close together, but it looks like maybe there is something on the other side. It could be dangerous.', 'Yes' : 'Ow! You twisted your knee sliding through but still made it.', 'passed' : False},
                '0611' : {'direction' : 'S', 'S' : 'The trail seems to end here, you\'ll have to make your own.', 'Yes' : 'You may have sprained your knee but you stumble through.', 'passed' : False},
                '0412' : {'direction' : 'N', 'N' : 'You will have to make your own way. I looks tough.', 'Yes' : 'Thorns stab at your flesh. You\'re bleeding.', 'passed' : False},
                '0312' : {'direction' : 'S', 'S' : 'This is not the main path, this isn\'t any path. It\'s dangerous to continue.', 'Yes' : 'Well...that hurt. But, you made it.', 'passed' : False},
                '0910' : {'direction' : 'E', 'E' : 'Piled limbs block the way. You\'ll have to climb through.', 'Yes' : 'A sharp limb stabbed you in the side.', 'passed' : False},
                '0911' : {'direction' : 'W', 'W' : 'A pile of limbs and debris blocks the way.Something sharp punctured your ribs. It\'s warm and wet now.', 'Yes' : '', 'passed' : False},
                '0713' : {'direction' : 'S', 'S' : 'It will be difficult and dangerous but probably safer than here.', 'Yes' : 'You made it through, scraped and scratched.', 'passed' : False},
                '0813' : {'direction' : 'N', 'N' : 'There is no option, you\'ll have to make a path to go further.', 'Yes' : 'Scratched and scraped but free of the trees, you made it.', 'passed' : False},
                }

escaped = False
escape_list = ['N','S','E','W']
yes = ['Yes','yes','Y','y']
no = ['No','no','N','n']
wolf = False
poison = False
p_counter = 0
w_counter = 0
change_counter = 0
stick = True
stick_squares = ['0708','0309','0615','0802','1004']

#Maps

maps = { 
        '0304' : {
                'welcome' : {1 : 'This is the end of a well maintained trail in the woods.', 2 : 'The main trail ends here.'},
                'move' : {'N' : False, 'S' : 0, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'It looks like this area has been abandoned.Maybe there is passage here.', 'E' : 'More trail.', 'W' : 'It\'s too dense. There\'s no way through.'},
                'listen' : {'Danger' : 'It\'s close, just out of range. Whatever *it* is.', 'No Danger' : 'You can almost hear the echoes of hundreds of hikers who have passed this way but not quite.'},
                'help' : {'Regular' : 'Your voice carries fat and clear. No response.', 'Tracker' : 'A snarl in the dark.'}
                },
        '0305' : {
                'welcome' : {1 : 'This trail goes on into the night. It is easy to walk and wide.', 2 : 'This appears to be a section of the main hiking trail through these woods.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'There is no path here.', 'E' : 'A long corridor of nothing and a dirt path to follow.', 'W' : 'This could go for feet or miles, it\'s impossible to know from here.'},
                'listen' : {'danger' : 'It feels like someone is standing just outside the light, walking with you.', 'no danger' : 'The crunch of feet on dirt as you walk. Nothing more.'},
                'help' : {'Regular' : 'Something explodes from the bushes! It\'s coming at you. It\'s a rat...it squeaks and scampers away.', 'Tracker' : 'Your shouts are like a beacon, pin-pointing your location.'}
                },
        '0306' : {
                'welcome' : {1 : 'The trail is mostly straight, rising and falling with the terrain, subtle turns here and there.', 2 : 'A section of hiking trail meandering through the woods, unobstructed.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'There is no path here.', 'E' : 'As far as you can see this trail continues.', 'W' : 'More well traveled hiking trail.'},
                'listen' : {'danger' : 'Listen...something nearby.', 'no danger' : 'Listen! something in the bushes...'},
                'help' : {'Regular' : 'It\'s as if your own voice calls you forward.', 'Tracker' : 'The darkness is breathing.'}
                },
        '0307' : {
                'welcome' : {1 : 'The path is wide here, allowing a break in the tree cover. Enough light to see past the edge of the forest but only just.', 2 : 'You can die from more than one kind of exposure, there is plenty here as the hiking trail opens up a bit.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'There is no path here.', 'E' : 'You are either looking toward the beginning or the end of this trail.', 'W' : 'A tunnel in the trees continues unimpeded.'},
                'listen' : {'danger' : 'You are very much alone, why doesn\'t it feel like that?', 'no danger' : 'Even the wind is quiet now, just lonely steps over rock and dirt.'},
                'help' : {'Regular' : 'Your voice just keeps going, finding an inevitable exit...jealous?', 'Tracker' : 'Sharp crack in the distance, perhaps you\'ve been spotted.'}
                },
        '0308' : {
                'welcome' : {1 : 'A divergence in paths here. Equally wide, equally well traveled. Move east or venture south?', 2 : 'Life is full of choices. Which of these trails to take, might be the most important.'},
                'move' : {'N' : False, 'S' : 0, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'A wide swath of clearing, a frequently used trail by the looks of things.', 'E' : 'A small crest and a gap in the trees it appears like.', 'W' : 'It goes at least as far as you can see...which isn\'t far.'},
                'listen' : {'danger' : 'Every tick, every crack sounds like danger and there are plenty.', 'no danger' : 'This would be a great place to rest in the daytime.'},
                'help' : {'Regular' : 'Like emissaries your call spreads in three directions at once. No responses though.', 'Tracker' : 'You\'ve alerted three directions to your exact location.'}
                },
        '0309' : {
                'welcome' : {1 : 'It feels like you\'re getting close to something. The foliage is different here.', 2 : 'one way is surely the right way but which is it? The trees are look less dense, right?'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'There is no path here.', 'E' : 'The trail dips, roots and rocks dot the path.', 'W' : 'An intersection in the woods. Wide, open, empty.'},
                'listen' : {'danger' : 'Scuffing in the dirt, to your right, in the trees.', 'no danger' : 'Bats overhead, almost silent.'},
                'help' : {'Regular' : 'Was that something? No...maybe.', 'Tracker' : 'Movement up ahead, quiet but still there.'}
                },
        '0310' : {
                'welcome' : {1 : 'The walls tighten up a bit. Trees move in, you could almost touch them on both sides. Or something could touch you.', 2 : 'This is a narrow point in the trail, great spot for an ambush.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'There is no path here.', 'E' : 'The trees wide again but there\'s a dark shadow across the trail.', 'W' : 'It\'s hard to see anything. The path rises, blocking what\'s there..'},
                'listen' : {'danger' : 'It\'s not just the leaves rustling.', 'no danger' : 'Your labored breaths are great for keeping time to.'},
                'help' : {'Regular' : 'Something....something out there. Maybe you\'re close.', 'Tracker' : 'The wolves respond.'}
                },
        '0311' : {
                'welcome' : {1 : 'There\'s a tree on the trail. Maybe you can try to climb over it. The ground is wet but with what isn\'t clear. ', 2 : 'How likely is it this giant tree just fell over and no one noticed. It looks pretty fresh.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'There is no path here.', 'E' : 'Nothing but darkness beyond the trunk of a massive fallen tree.', 'W' : 'A narrow passage and night beyond that.'},
                'listen' : {'danger' : 'Trees make handy hiding places.', 'no danger' : 'The night hums with silence.'},
                'help' : {'Regular' : 'Like this tree, no one is around to hear you if you fall.', 'Tracker' : 'You can call for help but anyone can answer.'}
                },
        '0312' : {
                'welcome' : {1 : 'It\'s like night and day, except it\'s still night. The path widens before you, downhill from here.', 2 : 'This massive tree came up by the roots. It\'s presence a reminder that nothing lasts forever.'},
                'move' : {'N' : False, 'S' : 0, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'Message', 'E' : 'A smooth passage with a gentle downhill slope.', 'W' : 'A massive tree trunk blocks this way. Maybe you can climb over?'},
                'listen' : {'danger' : 'There is something in the distance but it\'s difficult to make out.', 'no danger' : 'Does that sound like...laughing?'},
                'help' : {'Regular' : 'Might be your echo, might be nothing at all.', 'Tracker' : 'Sounds like footsteps on a trail but it isn\'t this one.'}
                },
        '0313' : {
                'welcome' : {1 : 'A howl pierces the night. The predators are out.  This area is wide, clean and easy going.', 2 : 'It\'s almost too easy to pass through here. Nothing blocks your way.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'There is no path here.', 'E' : 'There\'s a slight turn and shadows eat the trail. One foot in front of the other.', 'W' : 'It\'s uphill but the way is clear and easy to walk.'},
                'listen' : {'danger' : 'Maybe you\'ve been in here too long but it sounds like someone RIGHT beside you.', 'no danger' : 'This would be pleasant in the daytime.'},
                'help' : {'Regular' : 'Definitely a response that time.', 'Tracker' : 'That\'s the thump of your heart, audible in the night.'}
                },
        '0314' : {
                'welcome' : {1 : 'If the trash is any indicator, people have been here, recently. This trail is smooth and littered with water bottles, cigarette butts.', 2 : 'The trees are less dense, the sky more open. Is that an apple?'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'There is no path here.', 'E' : 'You must be heading out but darkness swallow the trail ahead, it\'s hard to know why.', 'W' : 'A smooth, gentle uphill climb.'},
                'listen' : {'danger' : 'There are plenty of noises ahead and more than a fe from behind as well.', 'no danger' : 'If you try hard you can hear something on the breeze but it\'s faint.'},
                'help' : {'Regular' : 'Definitely a response that time. But what was it? Where was it...', 'Tracker' : 'You hear enough to know you didn\'t make it here first.'}
                },
        '0315' : {
                'welcome' : {1 : 'The trail is clearly a main drag. Well worn and open but the treelines suggests and end, very soon.', 2 : 'This is a people area. The signs of recent inhabitation everywhere. But this is not the end, clearly.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'There is no path here.', 'E' : 'It\'s getting darker not brighter.', 'W' : 'Just the rise of a hill, an easy enough climb if you go slow.'},
                'listen' : {'danger' : 'Maybe someone IS still here.', 'no danger' : 'The quietest it will ever be until life returns.'},
                'help' : {'Regular' : 'There it is again.', 'Tracker' : 'If they wanted to help,they would call back, right?'}
                },
        '0316' : {
                'welcome' : {1 : 'It\'s almost pitch black. The trail, though wide is black around the edges and appears to come to an end not far from here.', 2 : 'Rocks and dirt and a darkness creeping in from the edges. This is not the exit.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'There is no path here.', 'E' : 'If you squint you see...nothing.', 'W' : 'A well maintained, hiking trail.'},
                'listen' : {'danger' : 'That was a rumble, loud and familiar....not thunder.', 'no danger' : 'Are those...voices?'},
                'help' : {'Regular' : 'There! Something...north? It\'s only black there.', 'Tracker' : 'Two responses. One to the north....one to the south. It\'s black both ways.'}
                },
        '0317' : {
                'welcome' : {1 : 'It\'s so dark your eyes struggle to adjust. The trail turns, leading west or south. What is that sound in the distance?', 2 : 'HOne of these ways is the exit, which means the other leads deeper into the forest.'},
                'move' : {'N' : False, 'S' : 0, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'The trail continues, leveling off but what is that shadow ahead?', 'E' : 'It\'s too dense. There\'s no way through.', 'W' : 'Still dark but just a bit brighter. It looks like a hill starts here.'},
                'listen' : {'danger' : 'That huffing isn\'t just you. You are not alone.', 'no danger' : 'It sounds like talking...but could be anything. Maybe there\'s a river nearby.'},
                'help' : {'Regular' : 'A call back. Someone is out there!', 'Tracker' : 'Your plea is drowned by a roar that fills the night. It\'s coming this way.'}
                },
        '0403' : {
                'welcome' : {1 : 'There was clearly a trail here at one point. It has been allowed to grow over. The forest is reclaiming this space.', 2 : 'HIt feels kind of creepy walking here. This used to be somewhere well used.'},
                'move' : {'N' : False, 'S' : 0, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'This area contnues, it will be tricky to get through.', 'E' : 'An overgrown trail.', 'W' : 'It\'s too dense. There\'s no way through.'},
                'listen' : {'danger' : 'It\'s hard to make out but there\'s something out there.', 'no danger' : 'It\'s so quiet it\'s unsettling.'},
                'help' : {'Regular' : 'Silence', 'Tracker' : 'Are there bears out here?'}
                },
        '0404' : {
                'welcome' : {1 : 'This is an abandoned trail. It\'s been a long time since anyone traveled this way.', 2 : 'No one has been here for ages.'},
                'move' : {'N' : 0, 'S' : False, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'A highly trafficked trail in the woods.', 'S' : 'There is no path here.', 'E' : 'There is no path here.', 'W' : 'A neglected trail in the woods.'},
                'listen' : {'danger' : 'A growl, not far away.', 'no danger' : 'It\'s quiet, almost peaceful here.'},
                'help' : {'Regular' : 'Try moving into the open.', 'Tracker' : 'Heavy breathing, close.'}
                },
        '0408' : {
                'welcome' : {1 : 'A wide open trail meets with another path. Well maintained.', 2 : 'Which way did you go before? All routes look the same here.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'Another path crosses this one.', 'S' : 'A wide, unobstructed way forward.', 'E' : 'There is no path here.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'There was definitely a sound beyond the tree line.', 'no danger' : 'Birds chitter...or are those bats?'},
                'help' : {'Regular' : 'It is so big out here alone.', 'Tracker' : 'Why does that sound like running?'}
                },
        '0412' : {
                'welcome' : {1 : 'A rarely used path between trees. It\'s dark and hard to follow.', 2 : 'This trail hasn\'t been used in a long time.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'There is a break in the trees this way.', 'S' : 'If there is a way, it\'s hard to follow.', 'E' : 'It\'s too dense. There\'s no way through.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'You\'re not the only one in this part of the forest.', 'no danger' : 'Small creatures scurry overhead.'},
                'help' : {'Regular' : 'This isn\'t working.', 'Tracker' : 'Limbs crack overhead.'}
                },
        '0417' : {
                'welcome' : {1 : 'The trail continues. It\'s wide and well taken care of. There is a sign.', 2 : 'This feels like the beginning...or the end of a trail.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'Short grass, wide path, fresh tracks.', 'S' : 'It feels like you\'ve seen this place before.', 'E' : 'It\'s too dense. There\'s no way through.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'Ahead, steady breath of something huge awaits. Proceed with caution.', 'no danger' : 'Are those voices?'},
                'help' : {'Regular' : 'You must be close.', 'Tracker' : 'You\'re not going to make it out of here like that.'}
                },
        '0503' : {
                'welcome' : {1 : 'This looks a it used to be a trail but it\'s overgrown now.', 2 : 'This was a trail once but it\'s in disrepair now.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'A section of the woods long forgotten and overgrown.', 'S' : 'The path widens again.', 'E' : 'There is no path here.', 'W' : 'It\'s too dense. There\'s no way through.'},
                'listen' : {'danger' : 'Why does it sounds like your steps echo louder here?', 'no danger' : 'A squirrel darts through the brush.'},
                'help' : {'Regular' : 'Nothing but echoes', 'Tracker' : 'That wasn\'t a squirrel.'}
                },
        '0508' : {
                'welcome' : {1 : 'A wide swath in the woods extends north and south. Something shoots across the path ahead.', 2 : 'This trail looks well worn. There must be a way out.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'Message', 'S' : 'Message', 'E' : 'There is no path here.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'There is something in the shadows, waiting.', 'no danger' : 'A flurry of activity in the bushes, then gone.'},
                'help' : {'Regular' : 'Your call fills this area. No response comes.', 'Tracker' : 'Silence is deafening.'}
                },
        '0511' : {
                'welcome' : {1 : 'It\'s hard to find a way through. This is barely even a path anymore.', 2 : 'Go where you\'ve been before. This path disappears and reappears often.'},
                'move' : {'N' : False, 'S' : 0, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'A narrow trail and dense forest.', 'E' : 'The path continues...sort of.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'It\'s too quiet here.', 'no danger' : 'It\'s hard to anything in here.'},
                'help' : {'Regular' : 'Your voice won\'t escape foliage this thick.', 'Tracker' : 'A roar loud enough to chill your bones.'}
                },
        '0512' : {
                'welcome' : {1 : 'This trail is tight, sometimes barely there. It\'s easy to lose your way.', 2 : 'What is this for? Who might use a hidden trail...'},
                'move' : {'N' : 0, 'S' : False, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s starting to open up a bit more.', 'S' : 'There is no path here.', 'E' : 'There is no path here.', 'W' : 'More winding, barely visible tracks.'},
                'listen' : {'danger' : 'Why aren\'t there more birds?', 'no danger' : 'Everything seems closer in here.'},
                'help' : {'Regular' : 'No one answers, probably a good thing.', 'Tracker' : 'There\'s a large presence behind you.'}
                },
        '0517' : {
                'welcome' : {1 : 'There\'s a curve in the trail. This is a wide hiking path, well worn.', 2 : 'Two choices here, one has to be the way out.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'A well worn path in the woods.', 'S' : 'What...is that?', 'E' : 'There might be a light up ahead, the forest is less dense here.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'Whatever that sound is...it isn\'t human.', 'no danger' : 'Familiar sounds carry. It\'s not clear which direction they come from.'},
                'help' : {'Regular' : 'It sounds hollow. There\'s an exit nearby.', 'Tracker' : 'A branch snaps.'}
                },
        '0518' : {
                'welcome' : {1 : 'This looks like the beginning of the trail, there is a break in the trees up ahead.', 2 : 'Take the opportunity and leave. This is the end of the trail.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'The trail is ending, you\'re almost free.', 'W' : 'Deeper into the woods. The path begins to darken.'},
                'listen' : {'danger' : 'Is that a car door? And something else...', 'no danger' : 'Shh...voices.'},
                'help' : {'Regular' : 'Was that an answer?', 'Tracker' : 'There\'s growling but it keeps its distance.'}
                },
        '0519' : {
                'welcome' : {1 : 'The trail opens here. Freedom awaits!', 2 : 'It\'s time to leave.'},
                'move' : {'N' : False, 'S' : False, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'The way out. Finally!', 'W' : 'Back into the woods. Not a good plan.'},
                'listen' : {'danger' : 'Something lurking, it seems leery.', 'no danger' : 'Sounds like people, close.'},
                'help' : {'Regular' : 'Someone responds. It\'s too far to make out the words.', 'Tracker' : 'Run, run for it now.'}
                },
        '0601' : {
                'welcome' : {1 : 'A curve in the trail. This is a deep part of the woods.', 2 : 'No one comes here anymore. Perhaps it\'s time to leave.'},
                'move' : {'N' : False, 'S' : 0, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'The trail turns south but starts to narrow here.', 'E' : 'Back towards the main trail.', 'W' : 'It\'s too dense. There\'s no way through.'},
                'listen' : {'danger' : 'What was that?', 'no danger' : 'You are very deep in the woods. Is that a wolf?'},
                'help' : {'Regular' : 'There is no one out here.', 'Tracker' : 'A howl in the distance seems too much like a response.'}
                },
        '0602' : {
                'welcome' : {1 : 'A lesser used but established trail in the woods. ', 2 : 'This trail is old but well used...once.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'The path curves north.', 'W' : 'It looks like this may come to an end soon.'},
                'listen' : {'danger' : 'It sounds like a large animal...sniffing.', 'no danger' : 'Something moves in the underbrush.'},
                'help' : {'Regular' : 'No answer.', 'Tracker' : 'There is something moving in the shadows...which direction is unclear.'}
                },
        '0603' : {
                'welcome' : {1 : 'There\s a wider trail.  People have been here, though not recently.', 2 : 'Is this the way out? This a lesser used trail but well worn and obvious in the wood.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'You have to look but there\'s a way through.', 'S' : 'There are so many hidden paths, perhaps this is one.', 'E' : 'That way is dark and smells terrible.', 'W' : 'The path continues deeper into the woods...or is this the way out?'},
                'listen' : {'danger' : 'The animals are quiet.', 'no danger' : 'The sounds of night surround you but none seem dangerous at this time.'},
                'help' : {'Regular' : 'The sound your hear is your own desperation.', 'Tracker' : 'Leaves rustle, high, not low to the ground.'}
                },
        '0604' : {
                'welcome' : {1 : 'The edge of a swamp. It gets dark and dangerous here.', 2 : 'Only the brave would come this way again.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'There is no path here.', 'E' : 'There is no way, you\'ll have to make one.', 'W' : 'Through a twisting path, there\'s a trail ahead.'},
                'listen' : {'danger' : 'There is someone or something else, close.', 'no danger' : 'Silence to the west, the opposite to the east.'},
                'help' : {'Regular' : 'You are alone here.', 'Tracker' : 'What do bears sound like?'}
                },
        '0605' : {
                'welcome' : {1 : 'The ground is gone, only gnarled roots and exposed stones to stand on. Careful, they\'re slippery.', 2 : 'This a dangerous place. There is nowhere stand. Keep your balance or you\'ll end up in the muck.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'There is no path here.', 'E' : 'A strip of land provides precarious passage.', 'W' : 'You\'ll have to hug the trees to go this way.'},
                'listen' : {'danger' : 'Maybe something jumped in the water. Maybe you\'re being followed.', 'no danger' : 'Murky water laps the shore.'},
                'help' : {'Regular' : 'Everything here can hear you, none are going to help.', 'Tracker' : 'It sounds like something crossing the swamp, straight this way.'}
                },
        '0606' : {
                'welcome' : {1 : 'You can make it if you\'re careful. One false step leads to murky depths.', 2 : 'Only thing dumber than coming here, is coming back.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'There is no path here.', 'E' : 'A narrow precarious path edging on swamp.', 'W' : 'Little more than rocks and roots to stand on.'},
                'listen' : {'danger' : 'Dripping, in the swamp...what is that?', 'no danger' : 'Every creature of the night seems to be out.'},
                'help' : {'Regular' : 'No answer.', 'Tracker' : 'Something splashes behind you. Move, quickly.'}
                },
        '0607' : {
                'welcome' : {1 : 'A strip of land between marsh and old growth trees. You can barely pass.', 2 : 'Watch your step. There\'s not much passable land here. '},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'There is no path here.', 'E' : 'A passage to an open field beyond.', 'W' : 'It takes care to pass through here. A murky swamp swallows the land.'},
                'listen' : {'danger' : 'A splash in the water, darkness covers the source.', 'no danger' : 'You are serenaded by bullfrogs.'},
                'help' : {'Regular' : 'Message', 'Tracker' : 'Message'}
                },
        '0608' : {
                'welcome' : {1 : 'A path stretches north, it looks well traveled. The way is wide and easy.', 2 : 'This place would look different in the light. Probably a nice spot for a pic nic.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'This way continues. The way is easy.', 'S' : 'An open field.', 'E' : 'There is no path here.', 'W' : 'It\'s too dark. You\'ll need to look closer.'},
                'listen' : {'danger' : 'It\'s too exposed. Whatever is out there is difficult to pin down.', 'no danger' : 'Nothing unusual here.'},
                'help' : {'Regular' : 'A shout in the dark, nothing more.', 'Tracker' : 'Breathing, heavy, close.'}
                },
        '0611' : {
                'welcome' : {1 : 'A thin passage through the trees. you can\'t see through the foliage.', 2 : 'This might be a shortcut, it might be a footpath from years ago.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'You have to twist around trees but it\'s passable.', 'S' : 'A large open field.', 'E' : 'There is no path here.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'You\'re not the only thing moving in these woods.', 'no danger' : 'It\'s quiet and lonely through here.'},
                'help' : {'Regular' : 'If there\'s a response, you don\'t hear it.', 'Tracker' : 'A branch snaps a few feet away.'}
                },
        '0615' : {
                'welcome' : {1 : 'A curve in the trail, this was definitely made for a purpose. Limbs overhead block the sky.', 2 : 'The trail curves here. This isn\'t the kind of place you want to spend time in.'},
                'move' : {'N' : False, 'S' : 0, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'A trail cuts through the trees. A well worn path.', 'E' : 'This dark trail continues, insulated from the trees surrounding it.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'Growling from the shadows.', 'no danger' : 'Nothing but small animals.'},
                'help' : {'Regular' : 'Your voice doesn\'t carry far but there\'s something familiar in the distance.', 'Tracker' : 'Something very large moves not far away.'}
                },
        '0616' : {
                'welcome' : {1 : 'A section of game trail. Frequently used. Well hidden.', 2 : 'This is a convenient but dangerous path. Tread carefully.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'A narrow shortcut through the woods.', 'W' : 'A dirt path and clear cut through the woods. It turns ahead.'},
                'listen' : {'danger' : 'You\'re not the only one on this trail.', 'no danger' : 'Small animals scurry nearby. Nothing to be concerned about.'},
                'help' : {'Regular' : 'No response.', 'Tracker' : 'Move...now.'}
                },
        '0617' : {
                'welcome' : {1 : 'This is a trail. Most likely used by a large animal. It doesn\'t look like humans have been through here.', 2 : 'An animal\'s passage through the woods.'},
                'move' : {'N' : 0, 'S' : False, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'A well traveled path in the woods.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'It\'s too dense. There\'s no way through.', 'W' : 'This path cuts through a dense section of the wood.'},
                'listen' : {'danger' : 'Something uses this trail and it sounds like it isn\'t far.', 'no danger' : 'There are new sounds here...something familiar.'},
                'help' : {'Regular' : 'Wait...what was that?', 'Tracker' : 'Something is coming but it doesn\'t sound friendly.'}
                },
        '0701' : {
                'welcome' : {1 : 'The path gets very close here. You\'re headed into a new part of these woods.', 2 : 'A narrow passage between gaps in the trees.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'A turn in the trail. The way you came before.', 'S' : 'A thicket of briars blocks the way.', 'E' : 'There is no path here.', 'W' : 'It\'s too dense. There\'s no way through.'},
                'listen' : {'danger' : 'Whatever is in here with you, it move through the trees nearby.', 'no danger' : 'It\'s quiet this deep in the forest.'},
                'help' : {'Regular' : 'Your voice sounds meek, alone.', 'Tracker' : 'A snarl from the trees.'}
                },
        '0703' : {
                'welcome' : {1 : 'The edge of a swamp. It smells of decay and death.', 2 : 'This is no place to get lost. Pick a way and get out before the bog sucks you down.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'Back into the forest...for better or worse.', 'S' : 'Deeper into the swamp. Nothing but danger and death this way.', 'E' : 'There is no path here.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'The wildlife is quiet. Maybe they know something.', 'no danger' : 'If it crawls, swims or creeps in the dark, it\'s here.'},
                'help' : {'Regular' : 'Your call bounces around, then dies.', 'Tracker' : 'A series of wet stomps, come from close by.'},
                'snake' : {'Before you can jump away, a stinging pain pierces your leg. You\'ve been bit. The venomous(?) snake is gone as quickly as it appeared.'}
                },
        '0708' : {
                'welcome' : {1 : 'Dark forest to the left, exposure to the right. Neither seems safe right now.', 2 : 'On the edge of an impenetrable forest, with open field on all sides.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'It\'s narrow but maybe a way out.', 'S' : 'That is where you began.', 'E' : 'An expanse of moonlit field, overgrowth and shadows.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'A howl in the distance. Loud and long.', 'no danger' : 'A howl from somewhere far off.'},
                'help' : {'Regular' : 'Your own voice returns from...everywhere.', 'Tracker' : 'Heavy breathing in the dark...right behind you.'}
                },
        '0709' : {
                'welcome' : {1 : 'This appears to be the middle of whatever this place is. Moon light illuminates the empty spaces but avoids the edges altogether.', 2 : 'The edge of the main expanse, again. This may be the only bright spot in these woods.'},
                'move' : {'N' : False, 'S' : 0, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'Back to where you started.', 'E' : 'This edge continues, heading east into the night.', 'W' : 'It looks like another border may be coming up.'},
                'listen' : {'danger' : 'Ever feel like you\'re being followed?', 'no danger' : 'Silence.'},
                'help' : {'Regular' : 'Only whispers.', 'Tracker' : 'A deep gutteral growl greets you in response.'}
                },
        '0710' : {
                'welcome' : {1 : 'This is the edge of the largest part of this area. A smaller but still wide path goes east.', 2 : 'Maybe you\'re walking in circles. This is the opening you began in.'},
                'move' : {'N' : False, 'S' : 0, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'The edge of this place leading to an exceptionally dark corner of the forest.', 'E' : 'A more secluded part of this area.', 'W' : 'A wide expanse of nothing but bad feelings.'},
                'listen' : {'danger' : 'Something waits, just beyond the shadows.', 'no danger' : 'This place is quiet. All sounds seem far away.'},
                'help' : {'Regular' : 'This space is huge, your voice echoes.', 'Tracker' : 'There is definitely something else out there.'}
                },
        '0711' : {
                'welcome' : {1 : 'It\'s open, too open. The moonlight reveals a break in the trees too wide to see either side of.', 2 : 'It\'s easy to get lost in the woods. Easier when there aren\'t any landmarks. Just open space.'},
                'move' : {'N' : 0, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'An area darker than the rest. Might be worth looking into.', 'S' : 'There is no path here.', 'E' : 'The clearing continues.', 'W' : 'The edges disappear, as this area opens wide. A moonlit expanse bordered by shadows and trees.'},
                'listen' : {'danger' : 'Whatever lurks here stays to the shadows, out of sight.', 'no danger' : 'The call of an owl, distant. The chirp of crickets, close.'},
                'help' : {'Regular' : 'Message', 'Tracker' : 'Message'}
                },
        '0712' : {
                'welcome' : {1 : 'A wide opening in the woods. If there\'s anything beyond the trees it\'s impossible to see.', 2 : 'It is very exposed. Only two ways to go.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'There is no path here.', 'E' : 'Signs of a struggle ahead.', 'W' : 'This wide stretch continues unobstructed.'},
                'listen' : {'danger' : 'You are not alone here and exposed. What IS that sound? Raspy...close.', 'no danger' : 'The rush of wind across tall grass.'},
                'help' : {'Regular' : 'The lack of response makes it clear, no one is coming to help you.', 'Tracker' : 'Was that a howl...or just the wind?'}
                },
        '0713' : {
                'welcome' : {1 : 'Something gruesome happened here. Blood stains the grass. Little bits of what\'s left scattered around.', 2 : 'Better to move quickly through here. This kill is still fresh.'},
                'move' : {'N' : False, 'S' : 0, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'A worn section in the dirt indicates there may be something there.', 'E' : 'There is no path here.', 'W' : 'A wider opening in the woods. Trees in the distance on both sides.'},
                'listen' : {'danger' : 'danger message', 'no danger' : 'no danger message'},
                'help' : {'Regular' : 'Message', 'Tracker' : 'Message'}
                },
        '0715' : {
                'welcome' : {1 : 'There is a narrow passage in the trees. Something has traveled throug here. Footprints you\'ve never seen in the mud. Large ones.', 2 : 'Whatever passes through here moves quick. Lot\'s of broken branches. There\'s a musty smell.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'A narrow path continues.', 'S' : 'Through the brush, a break in the woods, a clearing of some kind.', 'E' : 'There is no path here.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'There is movement nearby, hard to tell what from.', 'no danger' : 'Just the crack of limbs as you move through the trees.'},
                'help' : {'Regular' : 'It\'s too tight in here for sound to travel.', 'Tracker' : 'There\'s something in the darkness, moving close.'}
                },
        '0801' : {
                'welcome' : {1 : 'The woods are open here but something is running. Close to the ground, in the tall grass. It went east.', 2 : 'It\'s easy to lose track of directions in the open like this, where shadow closes in on all sides. The moonlight isn\'t doing much to help.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'A way out, a trail in the woods, like any other.', 'S' : 'Grass is matted here, something came through recently.', 'E' : 'More of the same and something moving away, fast.', 'W' : 'It\'s too dense. There\'s no way through.'},
                'listen' : {'danger' : 'Movement in the underbrush.', 'no danger' : 'Wind and an owl in the distance.'},
                'help' : {'Regular' : 'The clearing must not be very big but you hear no response.', 'Tracker' : 'There\'s a new brush in the weeds. This is moving quickly.'}
                },
        '0802' : {
                'welcome' : {1 : 'This appears to be the northeast edge of a clearing. There is no clear path beyond here. But at least you can see the stars.', 2 : 'This looks like a great place to sit and cry. You are concealed in two directions. The grassy range reveals nothing but black.'},
                'move' : {'N' : False, 'S' : 0, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'More open grassy space.', 'E' : 'There is no path here.', 'W' : 'The opening of this area, where you came in.'},
                'listen' : {'danger' : 'You\'ve been hearing yourself panting so long you never noticed it wasn\'t all yours.', 'no danger' : 'Wind through tall blades. A quiet, unsettling shush.'},
                'help' : {'Regular' : 'You are alone here.', 'Tracker' : 'Another howl in the distance. But not distant enough.'}
                },
        '0803' : {
                'welcome' : {1 : 'A curve in the trail. This looks to circle around the main swamp, hugging the shore...what there is of it.', 2 : 'A murky bend in the trial. Stay close to the shallow side. Who knows what\'s in there.'},
                'move' : {'N' : 0, 'S' : False, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'The trail continues north, it looks dryer, safer.', 'S' : 'There is no path here.', 'E' : 'Mud and muck await you and maybe worse.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'What sound does a rabbit hear before he gets eaten?', 'no danger' : 'The hum and croak of swamplands, a symphony at night.'},
                'help' : {'Regular' : 'Message', 'Tracker' : 'Message'}
                },
        '0804' : {
                'welcome' : {1 : 'Swamp water is ankle deep here. It takes all your strength to pull free of the muck. ', 2 : 'you are becoming one with the sludge. Slowly pulled into its depths.'},
                'move' : {'N' : False, 'S' : 0, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'An expanse of murky brownish green water glistens in the night. Something splashes far away, ripples of green slime.', 'S' : 'There may be something there. It\'s hard to tell.', 'E' : 'Nothing but mud and sludge. Dark trees tower overhead blocking moonlight.', 'W' : 'It is starting to look more like a forest this way.'},
                'listen' : {'danger' : 'There are too many sounds to pick just one. Mostly insects and small animals. Mostly.', 'no danger' : 'The wildlife here crescendos into an almost deafening chorus...then stops.'},
                'help' : {'Regular' : 'In the swamp, no one can hear you scream.', 'Tracker' : 'You sound more like a dinner bell.'}
                },
        '0805' : {
                'welcome' : {1 : 'Each step is wet in the deep muck. Your shoes are heavy with caked on mud.', 2 : 'It will be difficult to find your body if you don\'t make it out. It will probably sink into the mud and decay.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'There is no path here.', 'E' : 'A dark and murky swamp path.', 'W' : 'There may be trees up ahead. This can\'t go on forever. Can it?'},
                'listen' : {'danger' : 'You\'re not alone and it will be very hard to run here.', 'no danger' : 'Cicadas and bullfrogs.'},
                'help' : {'Regular' : 'Your voice sounds more desperate than usual.', 'Tracker' : 'I wouldn\'t do that again. You hear something coming this way.'}
                },
        '0806' : {
                'welcome' : {1 : 'Deep in the swamp. The smell is overpowering. Bugs cling to your exposed flesh as your feet sink with each step.', 2 : 'Why would anyone come here twice? The mud sucks at your shoes. Putrid scents fill your nostrils.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'A moss covered pond, looks more like a neglected swimming pool.', 'S' : 'There is no path here.', 'E' : 'Dense, dark swamp and thick low weeds.', 'W' : 'Black night, dark mud like sludge, footprints...maybe.'},
                'listen' : {'danger' : 'Between the sounds of mud slurping in your footsteps, something else follows in time.', 'no danger' : 'Swamp creatures buzz and croak and click in the night.'},
                'help' : {'Regular' : 'Message', 'Tracker' : 'Message'}
                },
        '0807' : {
                'welcome' : {1 : 'This is footpath, nothing more. The ground is moist and sinks under your weight.', 2 : 'It smells like swamp gas here. At least, you hope that\'s what it is. The ground is wet and releases new vapors with eveyr step.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'There is no path here.', 'E' : 'A large clearing in the woods.', 'W' : 'A muddy, wet path through the marsh.'},
                'listen' : {'danger' : 'Something splashes nearby. Then, silence.', 'no danger' : 'Frogs croak ominously.'},
                'help' : {'Regular' : 'It\'s hard to tell all the directions your voice comes back from.', 'Tracker' : 'You hear wet stomps, slow, steady. They\'re stalking you.'}
                },
        '0808' : {'welcome' : {1 : 'You\'re on the edge of a field. It\'s too dark to see the other side. Tall grass sways.', 2 : 'You\'re back where you started.'},
                'move' : {'N' : 0, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'The clearing disappears into darkness.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'A dark clearing in the woods.', 'W' : 'It\'s hard to tell. There may be something here.'},
                'listen' : {'danger' : 'Did you hear a twig break?', 'no danger' : 'Just the wind.'},
                'help' : {'Regular' : 'Your voice carries on the breeze, then...gone.', 'Tracker' : 'You shouldn\'t do that again.'},
                 },
        '0809' : {'welcome' : {1 : 'There\'s a musky scent here. Faint. It disappears quickly.', 2 : 'That smell again.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'A dark clearing in the woods.', 'S' : 'Somehow it\'s even darker this way. Like even moonlight avoids this area.', 'E' : 'Tall grass, shadows that swallow the night.', 'W' : 'The edge of the clearing, maybe.'},
                'listen' : {'danger' : 'Does that sound like...breathing?', 'no danger' : 'It\'s quiet. Too quiet.'},
                'help' : {'Regular' : 'You can hear your echo off distance trees your eyes can\'t see.', 'Tracker' : 'Shh! What was that?'},
                 },
        '0810' : {'welcome' : {1 : 'The far edge of this clearing. It\'s cold over here.', 2 : 'Dense forest lines the edge of a large clearing. It does not feel welcoming.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'This space opens again. The tree lines pulls away to the right.', 'S' : 'It is foreboding. Dark and still.', 'E' : 'It\'s too dense. There\'s no way through.', 'W' : 'A large dark clearing in the woods. Tall grass, recently trampled.'},
                'listen' : {'danger' : 'It sounds like an animal...but bigger.', 'no danger' : 'Wind blows through the tall grass. Old trees creak as they sway.'},
                'help' : {'Regular' : 'Sounds plays tricks out here. No one calls back.', 'Tracker' : 'Save your breath...and run.'},
                 },
        '0813' : {'welcome' : {1 : 'A narrow trail. A few feet wide snakes through the overgrowth. Are you safe or trapped? It\'s hard to tell.', 2 : 'A winding trail, purpose made but for what?'},
                'move' : {'N' : 0, 'S' : False, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'The trail opens onto a darkened clearing in the woods.', 'S' : 'There is no path here.', 'E' : 'The trail twists and continues east.', 'W' : 'There is no path here.'},
                'listen' : {'danger' : 'You hear quick snapping sounds on all sides. It\'s too hard to tell what they belong to.', 'no danger' : 'An owl somewhere close by. It\'s call is haunting.'},
                'help' : {'Regular' : 'Just the echo of your voice on close walls.', 'Tracker' : 'A quick rustle of leaves. You are not alone.'},
                 },
        '0814' : {'welcome' : {1 : 'This is a space barely big enough for a human being. Who would make this trail?', 2 : 'It\'s a narrow path in the trees. Something made this on purpose.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'There is no path here.', 'E' : 'An opening, a bigger space beyond.', 'W' : 'The path continues. Small but passable.'},
                'listen' : {'danger' : 'There is huffing. Like a beast close by.', 'no danger' : 'You\'re alone for now. All is quiet.'},
                'help' : {'Regular' : 'The narrow space funnels your voice toward the trailhead. Nothing.', 'Tracker' : 'Growling. Close.'},
                 },
        '0815' : {'welcome' : {1 : 'A large open space in the woods. No clear way in or out. It smells here, musty, like an animal lives here.', 2 : 'The creature\'s den. It stinks. Do not stay long.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There are no paths. There may be something if you look closer.', 'S' : 'A crawl space in some vines, nothing more.', 'E' : 'Hard to tell, maybe something is there, maybe there isn\'t.', 'W' : 'You\'ll have to look closer.'},
                'listen' : {'danger' : 'That heavy breathing isn\'t coming. It\'s already here.', 'no danger' : 'Even the insects are quiet here. But your heart is beating loud.'},
                'help' : {'Regular' : 'Your voice sounds panicked in this space.', 'Tracker' : 'Whatever lives here, it\'s back now. A deep growl from the darkness tells you you\'re out of time.'},
                 },
        '0816' : {'welcome' : {1 : 'This is a narrow trail in the woods. No one has been here for a long time.', 2 : 'Vines and branches make it hard to move quickly.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'A footpath that continues, uninterrupted.', 'W' : 'A clearing in the woods. If you dare expose yourself.'},
                'listen' : {'danger' : 'Something large passes unseen, nearby.', 'no danger' : 'Birds and crickets. It seems safe, for now.'},
                'help' : {'Regular' : 'No response, you\'re alone.', 'Tracker' : 'Pick a direction...and run.'},
                 },
        '0817' : {'welcome' : {1 : 'This trail is narrow, rarely used. Branches block your way as move forward.', 2 : 'A narrow path, overgrown and seldom used.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'The way continues.', 'W' : 'Back towards the last clearing.'},
                'listen' : {'danger' : 'It sounds like someone else is moving nearby.', 'no danger' : 'This part of the forest sounds different, more active.'},
                'help' : {'Regular' : 'Your shouts run ahead. Nothing comes back.', 'Tracker' : 'Something moves behind you.'},
                 },
        '0818' : {'welcome' : {1 : 'This is a dead end. Nowhere else to go from here.', 2 : 'Still no escape, only dense forest and thick vines.'},
                'move' : {'N' : False, 'S' : False, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'It\'s too dense. There\'s no way through.', 'W' : 'A narrow trail in the woods.'},
                'listen' : {'danger' : 'danger message', 'no danger' : 'no danger message'},
                'help' : {'Regular' : 'Message', 'Tracker' : 'Message'},
                 },
        '0901' : {'welcome' : {1 : 'It\'s a grisly sight, even in the dark. There is blood everywhere. A bear, maybe? It smells so bad.', 2 : 'It smells so bad here. Try not to look at the blood.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'The path into the this place.', 'S' : 'It\'s too dark too see anything.', 'E' : 'The clearing continues, grass lays down where something came through recently.', 'W' : 'It\'s too dense. There\'s no way through.'},
                'listen' : {'danger' : 'It sounds like something big is moving through the trees. Or is that your imagination?', 'no danger' : 'No creature dares make a sound here.'},
                'help' : {'Regular' : 'Your call fills the night. No answer.', 'Tracker' : 'Your voice carries. Something low and primal carries back with it.'},
                 },
        '0902' : {'welcome' : {1 : 'A corner of this clearing. It stinks here but it\'s worse to the west.', 2 : 'Violence stains this place.'},
                'move' : {'N' : 0, 'S' : False, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'You can continue in the tall grass a little further.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'It\'s too dense. There\'s no way through.', 'W' : 'Trampled grass leads into the dark.The stench comes from there.'},
                'listen' : {'danger' : 'It sounds like something is moving just outside the light.', 'no danger' : 'A wind rustles leaves. Crickets in weeds.'},
                'help' : {'Regular' : 'Your voice carries far. No response comes.', 'Tracker' : 'Shh! What was that?'},
                 },
        '0904' : {'welcome' : {1 : 'This narrow trail has been used a lot and recently. It is a few feet wide with mud and rocks to walk on.', 2 : 'A muddy path in the woods. Not overgrown like the rest.'},
                'move' : {'N' : 0, 'S' : 0, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'There is a clearing through there. That is where you started.', 'S' : 'The trail continues but looks like it ends soon.', 'E' : 'It\'s too dense. There\'s no way through.', 'W' : 'It\'s too dense. There\'s no way through.'},
                'listen' : {'danger' : 'An eerie sound, it seems to follow you.', 'no danger' : 'There is water nearby. Somewhere up ahead.'},
                'help' : {'Regular' : 'The sound carries like a train in a tunnel.', 'Tracker' : 'Was that a howl?'},
                 },
        '0909' : {'welcome' : {1 : 'The edge of the forest. There\'s no way out here. It\'s almost too dark to see', 2 : 'You\'re just walking in circles.'},
                'move' : {'N' : 0, 'S' : False, 'E' : 0, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'The clearing continues, this looks familiar.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'Something has been through here. The grass is laying down. Squinting doesn\'t help anything.', 'W' : 'It\'s too dense. There\'s no way through.'},
                'listen' : {'danger' : 'Just your own heart pounding.', 'no danger' : 'Nothing makes a sound here.'},
                'help' : {'Regular' : 'There is no one else here.', 'Tracker' : 'You should\'t do that again.'},
                 },
        '0910' : {'welcome' : {1 : 'A dark corner of the clearing. Nothing good happens here.', 2 : 'Fear lives here. A clearing opens up ahead, use it.'},
                'move' : {'N' : 0, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'A dark clearing in the woods.', 'S' : 'There is no path here.', 'E' : 'Branches and sticks block the way. There might be a way through.', 'W' : 'A short distance of trampled grass and dark.'},
                'listen' : {'danger' : 'There is sound nearby. Inhuman. Low and rumbling.', 'no danger' : 'There is no sound here.'},
                'help' : {'Regular' : 'Your voice echoes off the trees nearby.', 'Tracker' : 'Something responded...something not human.'},
                 },
        '0911' : {'welcome' : {1 : 'A narrow passage in the woods opens up. Barely wide enough move through sideways.', 2 : 'It\'s tight in here.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is no path here.', 'S' : 'There is no path here.', 'E' : 'The path gets somehow narrower', 'W' : 'An opening in the wood. A clearing beyond.'},
                'listen' : {'danger' : 'Twigs crunch nearby.', 'no danger' : 'You can only hear your own breathing.'},
                'help' : {'Regular' : 'Message', 'Tracker' : 'Message'},
                 },
        '0912' : {'welcome' : {1 : 'It\'s too tight to move easily. Branches scratch your skin.', 2 : 'It is cramped and dangerous here.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'The passage seems to get smaller.', 'W' : 'The path opens a little. Still very tight.'},
                'listen' : {'danger' : 'Something is close, very close.', 'no danger' : 'It\'s hard to hear anything in this small space.'},
                'help' : {'Regular' : 'It\'s too dense. No one can hear you in here.', 'Tracker' : 'You\'re met with a deep, unnatural growl.'},
                 },
        '0913' : {'welcome' : {1 : 'You have to kneel here. It\'s impossible to stand up in here.', 2 : 'It\'s low and tight. Thorns scrape you as you move.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'It gets smaller. You might have to crawl.', 'W' : 'The path opens, only a little bit.'},
                'listen' : {'danger' : 'Heavy breathing...it is not your own.', 'no danger' : 'The sound of branches snapping as you push through.'},
                'help' : {'Regular' : 'It\'s like shouting in a phone booth.', 'Tracker' : 'A noise somewhere close by.'},
                 },
        '0914' : {'welcome' : {1 : 'The path continues to shrink, forcing you to slide through sideways.', 2 : 'You can make it through but barely. It\'s going to be tight.'},
                'move' : {'N' : False, 'S' : False, 'E' : 0, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'It\'s too dense. There\'s no way through.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'There\'s barely any room here. It\'ll be tight.', 'W' : 'A slightly larger space, but barely.'},
                'listen' : {'danger' : 'Something big is close. Very close.', 'no danger' : 'The sounds of a forest at night.'},
                'help' : {'Regular' : 'No sound escapes here.', 'Tracker' : 'You shouldn\'t do that again.'},
                 },
        '0915' : {'welcome' : {1 : 'The path seems to end here. A tiny alcove, barely tall enough to stand in. vines and limbs seal you in from all sides.', 2 : 'This cramped space feels like a place to hide but you shouldn\'t stay here.'},
                'move' : {'N' : 0, 'S' : False, 'E' : False, 'W' : 0},
                'counter' : 0,
                'look' : {'N' : 'There is an opening this direction, you might can fit through.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'It\'s too dense. There\'s no way through.', 'W' : 'A narrow but slightly larger space.'},
                'listen' : {'danger' : 'Whatever you\'ve been hearing is close now. Very very close.', 'no danger' : 'This area is insulated from sound. Beyond you hear...nothing.'},
                'help' : {'Regular' : 'The thick walls of vines deaden the sound.', 'Tracker' : 'Something is coming. Quick.'},
                 },
        '1001' : {'welcome' : {1 : 'It\'s a dead end. The path ends in a dense wall of trees and shadow.', 2 : 'There is nothing here. No way through.'},
                'move' : {'N' : 0, 'S' : False, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'Back the way you came. A trail in the woods. Blood stained grass.', 'S' : 'It\'s too dense. There\'s no way through.', 'E' : 'It\'s too dense. There\'s no way through.', 'W' : 'It\'s too dense. There\'s no way through.'},
                'listen' : {'danger' : 'You are not alone. Something moves nearby.', 'no danger' : 'Do you hear...water?'},
                'help' : {'Regular' : 'Your own echo seems to lead you away from here.', 'Tracker' : 'A snarl, loud and close.'},
                },
        '1004' : {'welcome' : {1 : 'The trail ends here at a rocky shore and the glistening waters of a moonlight river.', 2 : 'Many things come to the river at night. It seems peaceful, for now.'},
                'move' : {'N' : 0, 'S' : False, 'E' : False, 'W' : False},
                'counter' : 0,
                'look' : {'N' : 'A narrow path in the woods.', 'S' : 'The current is fast, there\'s no way to cross here.', 'E' : 'It\'s too dense. There\'s no way through.', 'W' : 'It\'s too dense. There\'s no way through.'},
                'listen' : {'danger' : 'It\'s hard to hear over the water but that sounds like footsteps.', 'no danger' : 'the gentle ripple of water passing by.'},
                'help' : {'Regular' : 'Your voice carries into the darkness, downstream and fades away.', 'Tracker' : 'Suddenly, you are not alone. There is something in the darkness with you.'},
                 }, 
        }


# Directions

direction = 'N'

directions ={
            'north' : ('N','n','North','north'),
            'south' : ('S','s','South','south'),
            'east' : ('E','e','East','east'),
            'west' : ('W','w','West','west')
            }

credits = 'Created by: Gestalt Media.'

# Move

def move():
    global square
    global path
    global direction
    global tracker
    global escaped
    global escape_list
    global inspect_text
    global stick
    global stick_squares
    tracker = tracker + 0.25
    square = int(square)
    visited()
    
# Escaped
    if escaped == True:
        direction = random.choice(escape_list)
        while maps[str(format(square, '04d'))]['move'][direction] is False:
                direction = random.choice('N','S','E','W')
        else:
                pass
                
                
    else:
        direction = input('Which direction?')
    escaped = False
# Move
    square = int(square)
# Sign

    if str(format(square, '04d')) == '0417':
        read_sign = input('Read the sign?')
        if read_sign in yes:
            print('\n','Welcome to the Forest of Elif','\n', 'The park closes at sunset.','\n', 'Trails are dangerous at night.','\n')
        else:
            print('Ok.')
    else:
        square = int(square)
    
# Stick  
    if str(format(square, '04d')) in stick_squares:                
        pick_up = input('You found a stick...keep it?')
        if pick_up in yes:
                stick = True
                square = int(square)
                print('You have...a stick')
        else:
                print('\n','Eh, just leave here it then.','\n')
    else:
        square = int(square)
        pass
        
 
    
# North
    if direction in directions['north']:
        direction = 'N'

# Inspect Trigger
        if str(format(square, '04d')) in inspect_text and direction in inspect_text[str(format(square, '04d'))]['direction']:
            inspect()
        else:
            square = int(square)
            pass
    
        if maps[str(format(square, '04d'))]['move'][direction] is not False:
                path += direction
                square = square - 100
                square = str(format(square, '04d'))
                if maps[square]['counter'] == 0:
                    print('\n', maps[square]['welcome'][1],'\n')
                elif maps[square]['counter'] > 0:
                    print('\n', maps[square]['welcome'][2],'\n')
                else:
                    pass
                main()
        elif maps[str(format(square, '04d'))]['move'][direction] == False:
                print("You can\'t go there.")
        else:
                print('Try again.')
                move()

# South   
    if direction in directions['south']:
        direction = 'S'
        
# Inspect Trigger
        if str(format(square, '04d')) in inspect_text and direction in inspect_text[str(format(square, '04d'))]['direction']:
            inspect()
        else:
            square = int(square)
            pass

        if maps[str(format(square, '04d'))]['move'][direction] is not False:
                path += direction
                square = square + 100
                square = str(format(square, '04d'))
                if maps[square]['counter'] == 0:
                    print('\n', maps[square]['welcome'][1],'\n')
                elif maps[square]['counter'] > 0:
                    print('\n', maps[square]['welcome'][2],'\n')
                else:
                    pass
                main()
        elif maps[str(format(square, '04d'))]['move'][direction] == False:
                print("You can\'t go there.")    
                
# East
    if direction in directions['east']:
        direction = 'E'
        
# Inspect Trigger
        if str(format(square, '04d')) in inspect_text and direction in inspect_text[str(format(square, '04d'))]['direction']:
            inspect()
        else:
            square = int(square)
            pass
 
        if maps[str(format(square, '04d'))]['move'][direction] is not False:
                path += direction
                square = square + 1
                square = str(format(square, '04d'))
                if maps[square]['counter'] == 0:
                    print('\n', maps[square]['welcome'][1],'\n')
                elif maps[square]['counter'] > 0:
                    print('\n', maps[square]['welcome'][2],'\n')
                else:
                    pass
                main()
        elif maps[str(format(square, '04d'))]['move'][direction] == False:
                print("You can\'t go there.")  
                
# West                
    if direction in directions['west']:
        direction = 'W'   

# Inspect Trigger
        if str(format(square, '04d')) in inspect_text and direction in inspect_text[str(format(square, '04d'))]['direction']:
            inspect()
        else:
            square = int(square)
            pass
 
        if maps[str(format(square, '04d'))]['move'][direction] is not False:
                path += direction
                square = square - 1
                square = str(format(square, '04d'))
                if maps[square]['counter'] == 0:
                    print('\n', maps[square]['welcome'][1],'\n')
                elif maps[square]['counter'] > 0:
                    print('\n', maps[square]['welcome'][2],'\n')
                else:
                    pass
                main()
        elif maps[str(format(square, '04d'))]['move'][direction] == False:
                print("You can\'t go there.")  

def visited():
        global square
        square = int(square)
        if str(format(square, "04d")) in maps:
            maps[str(format(square, "04d"))]["counter"] = maps[str(format(square, "04d"))]["counter"] + 1   
        else:
            pass
        
def stats():
        global square
        stats = f'\nYou have been here {maps[str(format(square, "04d"))]["counter"]} times. \nYour health is {life}/25 \nYour strength is {energy}/15 \nYour path traveled is {path}\n'
        print(stats)
      
def callForHelp():
        global help_counter
        global tracker
        help_counter = help_counter + 1
        tracker = tracker + 0.5
        if help_counter < 5:
                print('\n',help['hoarse']['no'][random.randint(1,3)])
        else:
                print('\n',help['hoarse']['yes'],'\n')
                main()

# Attack
def attack():
    global first_attack
    if first_attack == True:
        print('A large creature explodes from the darkness. It\'s on you in an instant. It snarls and gnashes at you while its enormous weight pins you down.')
    else:
        pass
    while life > 0:
        print('You\'re being attacked!')
        escape()
        if escaped == True:
                main()
    else:
        print('You have died.')
        print(credits)
        exit = input('Press any key to exit.')
        exit()
    
    first_attack = False

# Escape
def escape():
    global life
    global escaped
    global tracker
    global wolf
    global stick
    fight_back = 0
    while life > 0:
        fight = input('Fight or Escape?\n1: Fight!\n2: Run away!')
# Fight
        if fight == '1' and stick == True:
                escaped = True
                stick = False
                tracker = 1
                print('\n','You fought him off. Good thing you had that stick...but it broke so...maybe run?','\n')                
                move()
        else:
                pass
        
        if fight == '1':
            success = random.randint(0,1)
            if success == 0:
                life = life - 1
                print('\n', attacked[random.randint(1,5)], '\n')
                print('Life: ',life,'\n')
            elif success == 1:
                fight_back = fight_back + 1
                if fight_back < 2:
                    print('\n',fight_success[random.randint(1,5)],'\n')
                    print('Life: ',life,'\n')
                    print(fight_back)
                else:
                    tracker = 0
                    print('\n','You fought him off! Time to leave this place.','\n')
                    print(fight_back)
                    move()
                    
            else:
                pass
# Run Away              
        elif fight == '2':
            run_success = random.randint(0,1)
            if run_success == 0:
                wolf = True
                life = life - 1
                print('\n',attacked[random.randint(1,5)],'\n')
                print('Life: ',life)
            elif run_success == 1:
                escaped = True
                tracker = 1
                print('\n','You escaped!','\n')
                
                move()

def wolf_func():
        global wolf
        global change_counter
        global w_counter
        if change_counter == 25:
                print('You can\'t deny it any longer. A longing from deep within rises as the moon appears, a beacon in the night. The sound of your own bones cracking is muffled only by your screams which pierce the night, twist and tear open into a howl that lingers long after you\'ve fallen to the dirt, a mass. Minutes pass before you stir, then  you\'re up again. Reborn, faster, bigger, stronger and ready to kill. What was that? Prey!')
        if wolf == True:
                change_counter += 1
                w_counter += 1
                if w_counter >= 5:
                        w_count = random.randint(1,5)
                        print(wolf_text[w_count])
                        w_counter = 0
        else:             
                pass
        
def poison():
        global poison
        global p_counter
        global life
        if poison == True:
                life = life - 0.5
                p_counter += 1
                if p_counter >= 5:
                        p_count = random.randint(1,5)
                        print(poison_text[p_count])
                        p_counter = 0
        else:             
                pass

def inspect():
        global direction
        global square
        square = int(square)
        if str(format(square, '04d')) in inspect_text:
                print(inspect_text[str(format(square, '04d'))][direction])
                YN = input('Continue?')
                if YN in yes:
                        print(inspect_text[str(format(square, '04d'))]['Yes'])
                else:
                        pass
                
def main():
    global life
    global square
    global help_counter
    global tracker
    global p_counter
    global w_counter
    global energy
    if tracker >= 5:
            attack()
            poison()
    else:
            pass
    square = int(square)
    
# Help Counter

    if help_counter > 0:
            help_counter = help_counter - 1
    else:
            pass
    
# Visited

    visited()
    
# While Loop

    while life > 0:
        choice = input('What will you do? 1:Look around  2:Listen  3:Move  4:Rest (See Status)  5:Call for help ')
        
# Choices 

        if choice == '1':
            look = input('Where do you want to look? (N,S,E,W)')
            if look in directions['north']:
                    look_direction = 'N'
            elif look in directions['south']:
                    look_direction = 'S'
            elif look in directions['east']:
                    look_direction = 'E'
            elif look in directions['west']:
                    look_direction = 'W'
            else:
                    print('Try again.')
                    pass

            if look in directions['north'] and direction in directions['south'] or look in directions['south'] and direction in directions['north'] or look in directions['east'] and direction in directions['west'] or look in directions['west'] and direction in directions['east']:
                print('\nThe way you came.\n')
                
            elif look_direction in directions['north']:
                print('\n',f'{maps[str(format(square, "04d"))]["look"][look_direction]}','\n')
                
            elif look_direction in directions['south']:
                print('\n',f'{maps[str(format(square, "04d"))]["look"][look_direction]}','\n')
                
            elif look_direction in directions['east']:
                print('\n',f'{maps[str(format(square, "04d"))]["look"][look_direction]}','\n')           
        
            elif look_direction in directions['west']:
                print('\n',f'{maps[str(format(square, "04d"))]["look"][look_direction]}','\n') 
            else:
                print('Try again.')
                pass
    
        elif choice == '2':
            if tracker >= 3:
                print('\n', maps[str(format(square, '04d'))]['listen']['danger'], '\n')
                
            else:
                print('\n', maps[str(format(square, '04d'))]['listen']['no danger'], '\n')

        elif choice == '3':
            if energy > 0:
                square = int(square)
                life = life - 0.25
                energy = energy - 0.5
                move()
            else:
                print('You need to rest.')
    
        elif choice == '4':
                if life <= 24:
                    life = life + 1
                else:
                    life = 25
                if energy <= 12:
                    energy = energy + 3
                else:
                    energy = 15

                if poison == True:
                        p_counter += 0.5
                else:
                        pass
                if wolf == True:
                        w_counter += 0.5
                else:
                        pass
                stats()

        elif choice == '5':
            callForHelp()
            if tracker >= 3:
                print('\n', maps[str(format(square, '04d'))]['help']['Tracker'], '\n')
                
            else:
                print('\n', maps[str(format(square, '04d'))]['help']['Regular'], '\n')

    else:
        print('You died.')    
        print(credits)
    
def start():
    name = input('What is your name?')
    print('\n','Welcome, ' + name + '. You are alone in a dark wood. It\'s not clear how you got here, your memory is a little fuzzy but be not afraid. With wits, cunning and a little assistance you might survive the night.','\n')    

start()
main()