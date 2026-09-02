"""The twenty autumn run sheets, as data.

Both the Markdown page and the printed A4 sheet are built from this file, so a
change to a session is made once. Anything that is true of every night lives in
plan/session-guide.md and is not repeated here.

A theme is four sessions: two Tuesdays and two Thursdays. Tuesday teaches and
pushes. Thursday uses it at match pace and eases off before Saturday.
"""

THEMES = [
    {
        "key": "1-starting",
        "name": "Starting",
        "shape": "The sit",
        "aim": "Get out of any position fast, with the first step going forward.",
    },
    {
        "key": "2-endurance",
        "name": "Endurance",
        "shape": "The plank",
        "aim": "Keep running at a pace he can hold, and know what that pace feels like.",
    },
    {
        "key": "3-sprints",
        "name": "Sprints",
        "shape": "The big step",
        "aim": "Run fast and tall, with the arms driving front to back.",
    },
    {
        "key": "4-stopping",
        "name": "Stopping",
        "shape": "The bow",
        "aim": "Stop dead in two steps without falling forward. The theme that stops injuries.",
    },
    {
        "key": "5-jumping",
        "name": "Jumping",
        "shape": "The landing",
        "aim": "Land quietly, with the knees bent and the knees apart.",
    },
]

PUSH = "Push night. Teach it slowly, then put the pace up"
EASE = "Ease off night. Match pace, then send them home fresher"

SESSIONS = [
    # ------------------------------------------------------------------ starting
    {
        "n": 1, "date": "Tuesday 25 August", "short": "Tue 25 Aug", "slug": "01-tue-25-aug",
        "theme": 0, "code": "Hurling", "kind": PUSH, "match": "Football, Saturday 29 August",
        "line": "The first night at the station. Half the job tonight is teaching them where to stand.",
        "kit": ["12 cones, six lanes, 15 metres", "25 discs beside the lanes", "Hurls down for now"],
        "layout": "lanes-15m", "figure": "move-first-step",
        "parts": [
            ("0 to 2", "Wake up game", "Sprint to the nearest cone", [
                "They jog inside the grid with their hands empty.",
                'Shout "cone". Every boy sprints to the nearest of the twelve cones, stops beside it, and jogs again.',
                "Five goes. Move yourself about so the nearest cone keeps changing.",
            ]),
            ("2 to 8", "Movement", "Two starts", [
                "Six lanes, four boys to a lane, one wave goes on every whistle.",
                'Standing start. "Feet apart, one foot in front, lean until you have to run."',
                'Rolling start. They jog five metres, and on the whistle they sprint the rest.',
                "Four waves of each. Nobody runs back down the middle of a lane.",
            ]),
            ("8 to 13", "Body shape", "The sit", [
                "A disc each, an arm's length apart. Say each line out loud and let them copy you.",
                '1. "Feet under your shoulders, toes pointing a bit out."',
                '2. "Push your backside back and down, like you are sitting on a low stool."',
                '3. "Chest up, heels flat on the ground."',
                '4. "Hold. One, two, three, four, five." Then stand up.',
                "Ten of them, slowly. This is the shape of every start and every stop all year.",
            ]),
            ("13 to 17", "Challenge game", "Standing race", [
                "Pairs of roughly the same size, one pair to a lane, both in a standing start.",
                "On the whistle they race ten metres. Six races, a new partner each time.",
                "Nothing written down and no winners announced.",
            ]),
        ],
        "coach": "The first step goes forward, not up.",
        "watch": ["Boys who bounce upright before they run. They have wasted a step.",
                  "Heels lifting in the sit. Move his feet a bit wider."],
        "wet": "Everything here works in the wet. Keep them off the ground.",
    },
    {
        "n": 2, "date": "Thursday 27 August", "short": "Thu 27 Aug", "slug": "02-thu-27-aug",
        "theme": 0, "code": "Football", "kind": EASE, "match": "Football, Saturday 29 August",
        "line": "Match in two days. Same two starts, faster, and nothing new.",
        "kit": ["12 cones, six lanes, 15 metres", "25 discs beside the lanes", "A ball each"],
        "layout": "lanes-15m", "figure": "shape-sit",
        "parts": [
            ("0 to 2", "Wake up game", "Beat the bib", [
                "They jog in the grid. You hold a bib up where they can all see it.",
                "Throw it. Every boy sprints to get a hand to it first, then jogs again.",
                "Six or seven throws, and throw it in a different direction every time.",
            ]),
            ("2 to 8", "Movement", "Two starts, with a ball", [
                "The same standing start and rolling start as Tuesday, ball in hand.",
                "Four waves of each at match pace. No teaching and no stopping a boy in the lane.",
                "Let them run. Tonight is for using it, not fixing it.",
            ]),
            ("8 to 13", "Body shape", "The sit", [
                "A disc each. Ten slow sits, five seconds held at the bottom of each.",
                "Then walk round while they hold and try to make them laugh. If a boy wobbles, he was not really holding it.",
                "Say the four lines again for anyone who missed Tuesday.",
            ]),
            ("13 to 17", "Finish", "No challenge game", [
                "There is a match on Saturday, so this is where the night stops.",
                "Walk them in. Ask three boys to name the shape and to show it.",
                "Hand them to the next station on time.",
            ]),
        ],
        "coach": "Nothing. Watch them and let them run.",
        "watch": ["A boy whose start falls apart the moment the ball is in his hands. That is normal at this age."],
        "wet": "No change. Nothing tonight goes on the ground.",
    },
    {
        "n": 3, "date": "Tuesday 1 September", "short": "Tue 1 Sep", "slug": "03-tue-01-sep",
        "theme": 0, "code": "Football", "kind": PUSH, "match": "Hurling, Saturday 5 September",
        "line": "Two more starts go in tonight, and the pace goes up. Four days to the next match.",
        "kit": ["12 cones, six lanes, 15 metres", "25 discs, four colours", "Hands free"],
        "layout": "lanes-15m", "figure": "move-first-step",
        "parts": [
            ("0 to 2", "Wake up game", "Colour dash", [
                "Scatter the discs in four colours through the grid. They jog between them.",
                'Call a colour. Every boy sprints to stand beside a disc of that colour, then jogs again.',
                "Eight or nine calls. Call the same colour twice in a row once, to catch them out.",
            ]),
            ("2 to 8", "Movement", "Four starts", [
                "Standing and rolling, one wave each, to settle them in.",
                "Sitting start. He sits on the line facing down the lane, hands off the ground.",
                "Backwards start. He stands facing away, turns on the whistle, and goes.",
                "Three waves of each new one. Slow the first wave right down.",
            ]),
            ("8 to 13", "Body shape", "The sit", [
                "A disc each. Ten slow sits, then hold the bottom for ten seconds.",
                "Then the nudge test. Hold the sit while you press gently on one shoulder.",
                'Tell them out loud: "This is the shape you start in and it is the shape you stop in."',
            ]),
            ("13 to 17", "Challenge game", "Race off the ground", [
                "Pairs, one pair to a lane, both sitting on the start line facing down the lane.",
                "On the whistle they get up and race ten metres.",
                "Six races. Change partner each time and swap which side they sit on.",
            ]),
        ],
        "coach": "Getting off the ground without using the hands.",
        "watch": ["Boys rolling onto their front to get up. Show them how to plant one foot and drive.",
                  "Knees falling in during the sit."],
        "wet": "The sitting start becomes a crouch start. Everything else stands.",
    },
    {
        "n": 4, "date": "Thursday 3 September", "short": "Thu 3 Sep", "slug": "04-thu-03-sep",
        "theme": 0, "code": "Hurling", "kind": EASE, "match": "Hurling, Saturday 5 September",
        "line": "Last night of the theme. Nothing new, a match in two days, and the sit gets checked.",
        "kit": ["12 cones, six lanes, 15 metres", "25 discs beside the lanes", "A hurl each"],
        "layout": "lanes-15m", "figure": "shape-sit",
        "parts": [
            ("0 to 2", "Wake up game", "Number starts", [
                "They jog. Give the four starts a number and say them once: 1 standing, 2 rolling, 3 sitting, 4 backwards.",
                'Call a number. Every boy drops into that start where he stands and sprints five metres.',
                "Eight calls. By the end nobody should need to think about it.",
            ]),
            ("2 to 9", "Movement", "All four starts, with a hurl", [
                "One wave at each start with a hurl in hand, at match pace.",
                "Then two free goes where each boy picks the start he likes best.",
                "No coaching. Stand at the finish and watch the first three steps.",
            ]),
            ("9 to 15", "Body shape", "The sit, checked", [
                "They should drop into it without a demonstration. Find out whether they can.",
                'Say only "sit" and count to five. Do that six times across the six minutes.',
                "Then the hurl held across the shoulders for the last three.",
            ]),
            ("15 to 17", "Finish", "Name the shape", [
                "Walk them in.",
                'Ask three boys: "What is the shape called, and where do you use it?"',
                "Tell them the theme changes on Tuesday.",
            ]),
        ],
        "coach": "Nothing. Watch, and find out who knows the shape.",
        "watch": ["Any boy who still needs to be shown the sit. Note it, and pick it up inside the next theme."],
        "wet": "The sitting start becomes a crouch start.",
    },
    # ----------------------------------------------------------------- endurance
    {
        "n": 5, "date": "Tuesday 8 September", "short": "Tue 8 Sep", "slug": "05-tue-08-sep",
        "theme": 1, "code": "Hurling", "kind": PUSH, "match": "Football, Saturday 12 September",
        "line": "New theme. This is not fitness work and it is not a race. It is teaching them one pace and how to find it.",
        "kit": ["10 cones, one loop about 25 by 12 metres", "25 discs inside the loop", "Hands free"],
        "layout": "loop-grid", "figure": "move-pace",
        "parts": [
            ("0 to 2", "Wake up game", "Follow the hand", [
                "They jog anywhere inside the loop. Nobody stops for two minutes.",
                "Raise your hand and they speed up. Lower it and they slow down. Flat hand means jog.",
                "Take them up and down four or five times, and never all the way to a sprint.",
            ]),
            ("2 to 8", "Movement", "The loop at talking pace", [
                "All 25 run the loop the same way at once. Slower boys cut the corners inside.",
                'Teach the test first: "If you can tell me your name and your club while you run, that is the pace."',
                "Ninety seconds running, thirty seconds walking. Three goes.",
                "Run beside three different boys and ask them. Send anyone who cannot answer down a gear.",
            ]),
            ("8 to 13", "Body shape", "The plank", [
                "A disc each. New shape, so build it in front of them.",
                '1. "Elbows under your shoulders, forearms flat on the ground."',
                '2. "Legs straight out behind you, up on your toes."',
                '3. "Straight from your head to your heels. Backside down."',
                "Fifteen seconds, rest, three times. Knees down for anyone who sags.",
            ]),
            ("13 to 17", "Challenge game", "The two minute loop", [
                "Two minutes of running, everybody counting his own laps.",
                "The group adds them up at the end and that number is the target for session 7.",
                "Nobody's own number is asked for out loud.",
            ]),
        ],
        "coach": "Finding one pace and holding it.",
        "watch": ["Boys who sprint the first lap and walk the third. That is the whole fault of this theme.",
                  "A sagging back in the plank. Knees down instead."],
        "wet": "The plank becomes the sit, held for twenty seconds. The running is unchanged.",
    },
    {
        "n": 6, "date": "Thursday 10 September", "short": "Thu 10 Sep", "slug": "06-thu-10-sep",
        "theme": 1, "code": "Football", "kind": EASE, "match": "Football, Saturday 12 September",
        "line": "Match in two days, so the running gets shorter and nothing new goes in.",
        "kit": ["10 cones, one loop about 25 by 12 metres", "25 discs inside the loop", "A ball each"],
        "layout": "loop-grid", "figure": "shape-plank",
        "parts": [
            ("0 to 2", "Wake up game", "Traffic in the box", [
                "Everybody moving inside the loop, and nobody stops for the whole two minutes.",
                'Call the way they move: "jog", "sideways", "backwards", "skip", "big steps", "jog".',
                "Change the call about every fifteen seconds. Keep the pace easy.",
            ]),
            ("2 to 8", "Movement", "The loop with a ball", [
                "Two goes of ninety seconds at talking pace, with a ball in hand, two minutes walking between.",
                "Same rule as Tuesday. If he cannot answer you, he is going too hard.",
                "Two goes tonight, not three. There is a match on Saturday.",
            ]),
            ("8 to 13", "Body shape", "The plank", [
                "A disc each. Fifteen seconds, rest, three times.",
                "On the third one, lift one hand off the ground for five seconds, then the other.",
                "If his hips swing when the hand comes up, he was not tight to begin with.",
            ]),
            ("13 to 17", "Finish", "No challenge game", [
                "Walk one lap of the loop together, talking.",
                'Ask two boys: "Could you still talk on that last run?"',
                "Hand them on. They should leave fresher than they arrived.",
            ]),
        ],
        "coach": "Nothing. Ask the talking question and listen to the answer.",
        "watch": ["Any boy who is quiet and red faced. He is going too hard and will not say so."],
        "wet": "The plank becomes the sit, held for twenty seconds.",
    },
    {
        "n": 7, "date": "Tuesday 15 September", "short": "Tue 15 Sep", "slug": "07-tue-15-sep",
        "theme": 1, "code": "Football", "kind": PUSH, "match": "Hurling, Saturday 19 September",
        "line": "The hardest night of the theme. Change of direction goes in on top of the running.",
        "kit": ["24 cones, six lanes with turns at 5, 10 and 15 metres", "25 discs", "12 tennis balls, 4 bibs"],
        "layout": "shuttle-grid", "figure": "shape-plank",
        "parts": [
            ("0 to 2", "Wake up game", "Rob the nest", [
                "Four teams, one in each corner, with all the tennis balls in a pile in the middle.",
                "One boy from each team runs at a time, takes one ball, runs back, and the next boy goes.",
                "When the middle is empty they may take from another team's corner. Two minutes, no winner called.",
            ]),
            ("2 to 8", "Movement", "Shuttles", [
                "Six lanes with a cone at 5, 10 and 15 metres. Four boys to a lane.",
                'Call a distance. The front boy runs out to that cone, touches it, and runs back at the same speed.',
                "Keep it continuous for sixty seconds, then thirty seconds rest. Four goes.",
                "Same pace out and back. A boy who sprints out and walks back has missed the point.",
            ]),
            ("8 to 13", "Body shape", "The plank", [
                "A disc each. Twenty seconds, rest, three times.",
                "Then the side plank, on one elbow, ten seconds each side.",
                "Backside down, not up. That is the only thing to fix.",
            ]),
            ("13 to 17", "Challenge game", "Team relay", [
                "Five teams of five. Each boy runs one lap of the loop and tags the next.",
                "Every boy runs twice. Call the group lap total from session 5 and see if they beat it.",
                "The teams are mixed up every round, so nobody is stuck on a losing team.",
            ]),
        ],
        "coach": "The same speed out and back.",
        "watch": ["Boys slowing to a walk before the turn cone rather than running through it.",
                  "The pace going up tonight. It never goes up on a Thursday."],
        "wet": "Move the turn cones in a metre. Wet grass and a hard turn is how ankles go.",
    },
    {
        "n": 8, "date": "Thursday 17 September", "short": "Thu 17 Sep", "slug": "08-thu-17-sep",
        "theme": 1, "code": "Hurling", "kind": EASE, "match": "Hurling, Saturday 19 September",
        "line": "Last night of the theme and a match in two days. Watch, do not teach.",
        "kit": ["10 cones, one loop about 25 by 12 metres", "25 discs inside the loop", "A hurl each"],
        "layout": "loop-grid", "figure": "move-pace",
        "parts": [
            ("0 to 2", "Wake up game", "Shadow jog in threes", [
                "Threes, one behind the other, jogging anywhere inside the loop.",
                "The leader picks the pace and the direction and the other two copy him exactly.",
                "Change the leader every forty seconds. Tell them the leader may not sprint.",
            ]),
            ("2 to 9", "Movement", "The loop with a hurl", [
                "Two goes of ninety seconds at talking pace with a hurl in hand.",
                "Two minutes walking between, and the walk is part of it.",
                "Stand in one place and let them come past you. Say nothing.",
            ]),
            ("9 to 15", "Body shape", "The plank", [
                "In pairs. One holds the plank, the other counts out loud to twenty and watches his back.",
                "Swap. Three each.",
                'The counter has one job: "Is his backside up or down?"',
            ]),
            ("15 to 17", "Finish", "Who could still talk", [
                "Walk them in.",
                'Ask three boys: "On the second run, could you still talk?"',
                "Tell them the theme changes on Tuesday and it is sprinting.",
            ]),
        ],
        "coach": "Nothing. Find out who has learned the pace.",
        "watch": ["A boy who now paces himself without being told. That is the theme having worked."],
        "wet": "The plank becomes the sit, held for twenty seconds.",
    },
    # ------------------------------------------------------------------- sprints
    {
        "n": 9, "date": "Tuesday 22 September", "short": "Tue 22 Sep", "slug": "09-tue-22-sep",
        "theme": 2, "code": "Hurling", "kind": PUSH, "match": "Football, Saturday 26 September",
        "line": "New theme. Sprinting is a skill before it is a race, so tonight is about the arms and staying tall.",
        "kit": ["12 cones, six lanes, 15 metres", "25 discs beside the lanes", "Hands free"],
        "layout": "lanes-15m", "figure": "move-arms",
        "parts": [
            ("0 to 2", "Wake up game", "Wave sprints", [
                "They jog anywhere in the grid.",
                'Shout "go". Every boy sprints ten metres in the direction he is already facing, then jogs again.',
                "Six goes, with about fifteen seconds of jogging between each one.",
            ]),
            ("2 to 8", "Movement", "Running tall", [
                "Six lanes, waves of six, 15 metres at about three quarter pace. This is not a race and say so.",
                '1. "Stand tall. Do not let your body fold in the middle."',
                '2. "Elbows bent. Hand goes from your pocket to your chin and back."',
                '3. "Keep your hands on your own side of your body."',
                "Six waves. Stand at the side and watch the arms, not the legs.",
            ]),
            ("8 to 13", "Body shape", "The big step", [
                "A disc each, and room in front of him. New shape, so build it in front of them.",
                '1. "Big step forward off the disc, longer than a walking step."',
                '2. "Bend both knees and drop your back knee towards the ground."',
                '3. "Front knee stays over your front foot. Do not let it fall inwards."',
                '4. "Push off the front foot to stand up."',
                "Eight each leg, slowly. Stand in front of a boy and look straight down his front leg.",
            ]),
            ("13 to 17", "Challenge game", "Pair races", [
                "Pairs of roughly the same size, one pair to a lane, standing start.",
                "Fifteen metres. Six races, a new partner each time.",
                "Now they will run properly fast, which is why the technique came first.",
            ]),
        ],
        "coach": "Hands stay on their own side of the body.",
        "watch": ["Arms swinging across the chest. Show them the picture and run beside them.",
                  "Heads rolling from side to side."],
        "wet": "No change. Nothing tonight goes on the ground.",
    },
    {
        "n": 10, "date": "Thursday 24 September", "short": "Thu 24 Sep", "slug": "10-thu-24-sep",
        "theme": 2, "code": "Football", "kind": EASE, "match": "Football, Saturday 26 September",
        "line": "Match in two days. Same running, faster, fewer goes, nothing new.",
        "kit": ["12 cones, six lanes, 15 metres", "25 discs beside the lanes", "A ball each, 5 bibs"],
        "layout": "lanes-15m", "figure": "shape-big-step",
        "parts": [
            ("0 to 2", "Wake up game", "Stuck in the mud", [
                "Five boys in bibs are the taggers, everyone else runs inside the grid.",
                "A tagged boy stands still in the big step, front knee bent, and holds it.",
                "Another boy frees him by tapping his shoulder. Change the taggers once. Two minutes.",
            ]),
            ("2 to 8", "Movement", "Running tall with a ball", [
                "Four waves of six over 15 metres at match pace, ball in hand.",
                "One arm is carrying, so the other arm has to do the work properly. Say that once.",
                "No teaching and nobody stopped in the lane.",
            ]),
            ("8 to 13", "Body shape", "The big step", [
                "A disc each. Eight each leg, slowly, with the back knee going low.",
                "Then hold the bottom of one for five seconds on each leg.",
                "Walk down the line and look straight at the front knee of every boy.",
            ]),
            ("13 to 17", "Finish", "Two free sprints", [
                "Two waves at whatever pace they like over the full fifteen metres.",
                "Then walk them in and ask two boys to name the shape.",
                "Hand them on. Match on Saturday.",
            ]),
        ],
        "coach": "Nothing. Watch the arms of the boys who were bad on Tuesday.",
        "watch": ["The carrying arm pulling the body across itself. It is common and it is fixable later."],
        "wet": "No change.",
    },
    {
        "n": 11, "date": "Tuesday 29 September", "short": "Tue 29 Sep", "slug": "11-tue-29-sep",
        "theme": 2, "code": "Football", "kind": PUSH, "match": "Hurling, Saturday 3 October",
        "line": "The hardest night of the theme. Full speed, full rest, and something to react to.",
        "kit": ["16 cones: six lanes plus two gates at 12 metres", "25 discs", "Hands free"],
        "layout": "two-gates", "figure": "move-arms",
        "parts": [
            ("0 to 2", "Wake up game", "Reaction line", [
                "Two lines of boys, back to back down the middle of the grid, an arm's length apart.",
                'Name one line "blue" and one "red". Call a colour: that line runs, the other line chases for five metres.',
                "Eight calls. Mix up how long you leave between the call and the last one.",
            ]),
            ("2 to 8", "Movement", "Full speed", [
                "Six lanes, waves of six, 15 metres flat out. This is the only night in the theme they go flat out.",
                "Full rest between waves. A boy should be walking back and breathing easy before he goes again.",
                "Four or five waves, no more. Quality goes first when they are tired and there is no point past that.",
            ]),
            ("8 to 13", "Body shape", "The big step", [
                "A disc each, hands on the head or a hurl held across the shoulders.",
                "Six each leg. Taking the hands away makes the balance harder and shows up the weak side.",
                "Most boys have a bad side and have never noticed. Tell them which one theirs is.",
            ]),
            ("13 to 17", "Challenge game", "Two gates", [
                "One gate of cones to the left at 12 metres and one to the right. Boys start on the middle line.",
                'He sets off. When he is about three metres in, shout "one" or "two" and he runs through that gate.',
                "One boy at a time from each of three starts, so three going at once. Six goes each.",
            ]),
        ],
        "coach": "Reacting without slowing down.",
        "watch": ["Boys who slow to a walk to work out which gate. Call it earlier for them.",
                  "The pace goes up tonight. It never goes up on a Thursday."],
        "wet": "Shorten the gates to ten metres so nobody has to turn hard on wet grass.",
    },
    {
        "n": 12, "date": "Thursday 1 October", "short": "Thu 1 Oct", "slug": "12-thu-01-oct",
        "theme": 2, "code": "Hurling", "kind": EASE, "match": "Hurling, Saturday 3 October",
        "line": "Last night of the theme, a match in two days, and the big step gets checked.",
        "kit": ["12 cones, six lanes, 15 metres", "25 discs beside the lanes", "A hurl each, 12 bibs"],
        "layout": "lanes-15m", "figure": "shape-big-step",
        "parts": [
            ("0 to 2", "Wake up game", "Tails", [
                "Twelve boys tuck a bib into the back of their shorts so most of it hangs out. The rest have no tail.",
                "The boys without a tail chase and try to take one. A boy who takes a tail wears it.",
                "A boy who loses his tail does five big steps, then goes hunting for another. Swap nobody, it sorts itself out. Two minutes.",
            ]),
            ("2 to 9", "Movement", "Four sprints with a hurl", [
                "Four waves of six over 15 metres with a hurl, at whatever pace they like.",
                "Full rest between. Walk back, breathe, go again.",
                "Stand at the finish line and watch the arms. Say nothing.",
            ]),
            ("9 to 15", "Body shape", "The big step, checked", [
                "They should drop into it without a demonstration. Find out whether they can.",
                'Say only "big step, left leg" and count to five. Then the right.',
                "Five each leg. Then ask one boy to show the group and to say what to watch for.",
            ]),
            ("15 to 17", "Finish", "Name the shape", [
                "Walk them in.",
                'Ask three boys: "What is the shape called, and what falls in if you do it badly?"',
                "Tell them the theme changes on Tuesday and it is stopping.",
            ]),
        ],
        "coach": "Nothing. Find out who knows the shape.",
        "watch": ["Any boy whose front knee still falls in. Note his name for the stopping theme, because it is the same fault."],
        "wet": "No change.",
    },
    # ------------------------------------------------------------------ stopping
    {
        "n": 13, "date": "Tuesday 6 October", "short": "Tue 6 Oct", "slug": "13-tue-06-oct",
        "theme": 3, "code": "Hurling", "kind": PUSH, "match": "Football, Saturday 10 October",
        "line": "The most important theme of the autumn. Most injuries at this age come out of a bad stop and nobody teaches it.",
        "kit": ["18 cones: six lanes, stop line at 10 metres, 5 metres of run off", "25 discs", "A hurl each"],
        "layout": "stop-line", "figure": "move-stop",
        "parts": [
            ("0 to 2", "Wake up game", "Traffic lights", [
                "They run inside the grid.",
                '"Green" is run. "Red" is stop dead and hold still. Anyone still moving after red does five sits.',
                "Seven or eight calls, and make some of the greens only two seconds long.",
            ]),
            ("2 to 8", "Movement", "Two steps to stop", [
                "The middle cone is the stop line. The five metres past it is room to run off, not somewhere to keep going.",
                'The rule all theme: "Two steps to stop. No more, and no falling over the line."',
                '1. "Run at the line." 2. "Last two steps, sink down." 3. "Knees bend, backside back, chest up." 4. "Hold still."',
                "Six waves walking, then six waves jogging. Nobody runs at it tonight.",
            ]),
            ("8 to 13", "Body shape", "The bow", [
                "A disc each. Second shape of the autumn and it is the shape a stop happens in. Say that out loud.",
                '1. "Stand tall, feet under your hips, knees soft."',
                '2. "Push your backside back, like you are closing a door with it."',
                '3. "Let your chest come forward and keep your back flat like a table."',
                '4. "Slide your hands down your legs. Stop when your back stops being flat."',
                "Ten of them. A hurl along the back is the check: it touches the backside, the back and the head at once.",
            ]),
            ("13 to 17", "Challenge game", "Stop on the number", [
                "As each wave runs in, hold up a number of fingers where they can see you.",
                "They stop on the line and shout the number back.",
                "If nobody gets it they were watching their feet. Six or seven waves.",
            ]),
        ],
        "coach": "Straight legs at the stop. It should look like sitting down into it.",
        "watch": ["Stopping upright and stiff. Stop the lane and show it again.",
                  "Count the two steps out loud with them. Two, not five."],
        "wet": "Wet grass makes them skid. Move the stop line in a metre and keep it at walking and jogging pace.",
    },
    {
        "n": 14, "date": "Thursday 8 October", "short": "Thu 8 Oct", "slug": "14-thu-08-oct",
        "theme": 3, "code": "Football", "kind": EASE, "match": "Football, Saturday 10 October",
        "line": "Match in two days. The same stop with a ball in hand, and nothing new.",
        "kit": ["18 cones: six lanes, stop line at 10 metres, 5 metres of run off", "25 discs", "A ball each"],
        "layout": "stop-line", "figure": "shape-bow",
        "parts": [
            ("0 to 2", "Wake up game", "Red, blue, green", [
                "The same as traffic lights with one call added.",
                '"Green" is run forward, "red" is stop dead, "blue" is run backwards until the next call.',
                "Ten calls. Blue is the one they will get wrong, so use it early and often.",
            ]),
            ("2 to 8", "Movement", "Stopping with a ball", [
                "Six waves, jogging in and stopping on the line in two steps, ball in hand.",
                "Then four waves at match pace.",
                "The ball changes nothing about the stop. If it does, he was not solid to begin with.",
            ]),
            ("8 to 13", "Body shape", "The bow", [
                "A disc each. Ten slow ones, five seconds held at the bottom of each.",
                "Then five with a partner watching from the side and calling flat or round.",
                "Say the four lines again for anyone who missed Tuesday.",
            ]),
            ("13 to 17", "Finish", "Three stops each", [
                "Three waves at match pace and that is the night.",
                "Walk them in and ask two boys to name the shape.",
                "Hand them on. They should leave fresher than they arrived.",
            ]),
        ],
        "coach": "Nothing. Watch the boys who stopped upright on Tuesday.",
        "watch": ["A boy who now sinks into the stop without being told. Tell him you saw it."],
        "wet": "Move the stop line in a metre and keep it at jogging pace.",
    },
    {
        "n": 15, "date": "Tuesday 13 October", "short": "Tue 13 Oct", "slug": "15-tue-13-oct",
        "theme": 3, "code": "Football", "kind": PUSH, "match": "Hurling, Saturday 17 October",
        "line": "The hardest night of the autumn. Full speed into the stop, and the strictest you will be all year.",
        "kit": ["18 cones: six lanes, stop line at 10 metres, 5 metres of run off", "25 discs", "Hands free"],
        "layout": "stop-line", "figure": "move-stop",
        "parts": [
            ("0 to 2", "Wake up game", "Statues", [
                "They run inside the grid. Call the name of a shape they know: sit, plank, big step, bow.",
                'Then shout "statue". Every boy stops dead and holds that shape where he stands until you say go.',
                "Six goes. Change the shape each time and hold each one for five seconds.",
            ]),
            ("2 to 8", "Movement", "Full speed into the stop", [
                "Two waves jogging to warm the stop up, then the rest at full speed.",
                "The rule does not change because the speed did. Two steps, chest up, hold still.",
                "Six waves. Any boy who cannot hold it goes back to jogging for the rest of the night. No argument.",
                "This is the strictest thing in the whole autumn and it is the one worth being strict about.",
            ]),
            ("8 to 13", "Body shape", "The bow on one leg", [
                "A disc each, one hand on a partner's shoulder for balance.",
                "Stand on one leg, push the backside back, and let the other leg go straight out behind.",
                "Five each leg. Most will wobble and that is fine. Back flat is the only rule.",
            ]),
            ("13 to 17", "Challenge game", "Stop and go again", [
                "He runs in, stops on the line, and holds.",
                'Then you call "left", "right" or "back" and he goes that way for five metres.',
                "Six waves. Now the stop has to be balanced enough to move out of, which is what a match asks for.",
            ]),
        ],
        "coach": "Two steps, at full speed, or he goes back to jogging.",
        "watch": ["Boys drifting over the line. The run off is not a place to keep running.",
                  "The pace goes up tonight. It never goes up on a Thursday."],
        "wet": "Keep it at jogging pace all night and do not apologise for it. A hard stop on wet grass is how ankles go.",
    },
    {
        "n": 16, "date": "Thursday 15 October", "short": "Thu 15 Oct", "slug": "16-thu-15-oct",
        "theme": 3, "code": "Hurling", "kind": EASE, "match": "Hurling, Saturday 17 October",
        "line": "Last night of the theme, a match in two days, and the bow gets checked.",
        "kit": ["18 cones: six lanes, stop line at 10 metres, 5 metres of run off", "25 discs", "A hurl each"],
        "layout": "stop-line", "figure": "shape-bow",
        "parts": [
            ("0 to 2", "Wake up game", "Musical discs", [
                "Scatter the discs through the grid, one for each boy. They jog between them without touching one.",
                'Shout "bow". Every boy gets to the nearest free disc, stands on it, and holds the bow until you say go.',
                "Seven goes. Take one disc away each time so somebody is always left out and does five sits.",
            ]),
            ("2 to 9", "Movement", "Stops with a hurl", [
                "Six waves at match pace with a hurl in hand.",
                "Then two free goes where each boy runs in at whatever speed he trusts himself to stop from.",
                "That choice tells you more about what he learned than any of the waves will.",
            ]),
            ("9 to 15", "Body shape", "The bow, checked", [
                "They should drop into it without a demonstration. Find out whether they can.",
                'Say only "bow" and count to five. Six times across the six minutes.',
                "Then the hurl along the back on the last two, and let them check each other.",
            ]),
            ("15 to 17", "Finish", "Name the shape", [
                "Walk them in.",
                'Ask three boys: "What is the shape called, and when do you use it in a match?"',
                "Tell them the theme changes on Tuesday and it is jumping.",
            ]),
        ],
        "coach": "Nothing. Find out who knows the shape.",
        "watch": ["Any boy still stopping upright after four nights. He needs a quiet word on his own, not in front of the group."],
        "wet": "Keep it at jogging pace.",
    },
    # ------------------------------------------------------------------- jumping
    {
        "n": 17, "date": "Tuesday 20 October", "short": "Tue 20 Oct", "slug": "17-tue-20-oct",
        "theme": 4, "code": "Hurling", "kind": PUSH, "match": "Football, Saturday 24 October",
        "line": "New theme, and nothing gets jumped over tonight. The hurdles stay in the bag until the landing is quiet on the spot.",
        "kit": ["4 corner cones", "25 discs, one per boy", "Hands free. Hurdles stay in the bag"],
        "layout": "spots", "figure": "shape-landing",
        "parts": [
            ("0 to 2", "Wake up game", "Silent bunny hops", [
                "Two feet together, hopping anywhere inside the grid. Landings must be silent.",
                "Walk about with your back turned and listen. Any boy you hear stands out for ten seconds.",
                "Two minutes. Tell them you are listening, not looking.",
            ]),
            ("2 to 8", "Movement", "Jump and land on the spot", [
                "A disc each, and nothing to jump over. Two feet to two feet, straight up and straight down.",
                '1. "Bend, swing your arms, jump."',
                '2. "Land on the front of your feet, then let your heels down."',
                '3. "Bend your knees as you land and keep them apart."',
                '4. "Freeze. Two seconds. No noise."',
                "Ten jumps, then ten more with you walking round listening.",
            ]),
            ("8 to 13", "Body shape", "The landing", [
                "The same shape, held. Jump, land, and freeze in it.",
                "Walk round and nudge a shoulder gently. If he wobbles, he was not really holding it.",
                "Ten of them. Noise and knees falling in are the whole theme, so say both out loud every time.",
            ]),
            ("13 to 17", "Challenge game", "The quietest group", [
                "Split them into three groups of eight. One group jumps, the other two turn their backs and listen.",
                "Ten jumps together. The listeners say how many they heard.",
                "Three rounds so every group jumps once. The listeners are strict, which is the point.",
            ]),
        ],
        "coach": "If you can hear him land, he is landing badly.",
        "watch": ["Straight legs on landing. He must bend to be quiet, so quiet does the coaching for you.",
                  "Knees falling in. Same fault as the sit and the big step."],
        "wet": "No change. Nothing tonight goes on the ground and nobody jumps over anything.",
    },
    {
        "n": 18, "date": "Thursday 22 October", "short": "Thu 22 Oct", "slug": "18-thu-22-oct",
        "theme": 4, "code": "Football", "kind": EASE, "match": "Football, Saturday 24 October",
        "line": "The hurdles come out, low ones only. Match in two days, so the numbers stay small.",
        "kit": ["12 cones, six lanes", "6 mini hurdles, 15 cm, one in each lane", "25 discs, a ball each"],
        "layout": "hurdles", "figure": "shape-landing",
        "parts": [
            ("0 to 2", "Wake up game", "Jump the line", [
                "Every boy stands on one of the lane lines, side on, feet together.",
                'Call "over" and "back". They jump the line and land silent each time, no pause.',
                "Then call it faster. Then call forwards and backwards over the line instead. Two minutes.",
            ]),
            ("2 to 8", "Movement", "Over the hurdle", [
                "One mini hurdle in the middle of each lane. Waves of six.",
                "Jog in, jump the hurdle with two feet, land on two feet, and hold it for two seconds.",
                "Six waves. He walks on only after he has held the landing.",
                "If a boy will not take off, take the hurdle away and let him jump a line on the grass.",
            ]),
            ("8 to 13", "Body shape", "The landing", [
                "A disc each. Ten jumps on the spot, landing held for three seconds each.",
                "Then five with a ball in hand, because that is what Saturday looks like.",
                "Nudge test on the last three.",
            ]),
            ("13 to 17", "Finish", "Three goes each", [
                "Three more waves over the hurdle at their own pace.",
                "Walk them in and ask two boys what makes a landing quiet.",
                "Hand them on. Match on Saturday.",
            ]),
        ],
        "coach": "Nothing. Listen from the side of the lanes.",
        "watch": ["A boy landing stiff and loud with a ball in his hands but quiet without it."],
        "wet": "Hurdles on wet grass slide. Push them into the ground, and if they still move, take them away and jump a line.",
    },
    {
        "n": 19, "date": "Tuesday 27 October", "short": "Tue 27 Oct", "slug": "19-tue-27-oct",
        "theme": 4, "code": "Football", "kind": PUSH, "match": "Hurling, Saturday 31 October",
        "line": "The hardest night of the theme. One foot landings, which is what actually happens in a match.",
        "kit": ["12 cones, six lanes", "6 mini hurdles, 15 cm", "25 discs, hands free"],
        "layout": "hurdles", "figure": "shape-landing",
        "parts": [
            ("0 to 2", "Wake up game", "Hopscotch discs", [
                "Scatter the discs about a stride apart through the grid.",
                "They travel across the grid by jumping from disc to disc, and they may not touch the grass.",
                "Two feet for the first minute, then one foot for the second. Silent, or he starts again.",
            ]),
            ("2 to 8", "Movement", "Landing on one foot", [
                "Waves of six over the mini hurdle. Two feet to take off, one foot to land.",
                "Hold the one foot landing for two seconds before he moves. That hold is the whole exercise.",
                "Three waves on the left foot, three on the right. Most boys have a bad side.",
                "Any boy who cannot hold it goes back to two feet for the rest of the night.",
            ]),
            ("8 to 13", "Body shape", "The landing on one foot", [
                "A disc each. Small hop straight up off one foot, land on the same foot, freeze for three seconds.",
                "Five each foot. Small hops. Height is not the point and it never was.",
                "Nudge test on the last two of each foot.",
            ]),
            ("13 to 17", "Challenge game", "Longest silent jump", [
                "Two feet to two feet, as far as he can, landing held still for three seconds.",
                "If he wobbles or you hear it, it does not count and he goes again.",
                "Six goes each. They will learn to jump shorter and land better, which is exactly right.",
            ]),
        ],
        "coach": "Hold the one foot landing for two seconds, or go back to two feet.",
        "watch": ["The knee falling in on a one foot landing. This is the single biggest injury sign at this age.",
                  "The pace goes up tonight. It never goes up on a Thursday."],
        "wet": "One foot landings on wet grass are not worth it. Stay on two feet all night.",
    },
    {
        "n": 20, "date": "Thursday 29 October", "short": "Thu 29 Oct", "slug": "20-thu-29-oct",
        "theme": 4, "code": "Hurling", "kind": EASE, "match": "Hurling, Saturday 31 October",
        "line": "Last night before Halloween and the last night of the autumn. All five shapes get named.",
        "kit": ["12 cones, six lanes", "6 mini hurdles, 15 cm", "25 discs, a hurl each"],
        "layout": "hurdles", "figure": "shape-landing",
        "parts": [
            ("0 to 2", "Wake up game", "Copy the jump", [
                "Pairs, spread through the grid. One boy makes up a jump and lands it.",
                "His partner copies it exactly, landing and all. Then they swap.",
                "Two minutes. Tell them a jump nobody can land quietly does not count.",
            ]),
            ("2 to 9", "Movement", "Hurdles at match pace", [
                "Waves of six over the hurdle with a hurl in hand.",
                "Each boy picks his own landing, two feet or one. Six waves.",
                "Stand at the side and listen. Say nothing.",
            ]),
            ("9 to 15", "Body shape", "All five shapes", [
                "A disc each. Call them in order and hold each for thirty seconds: the sit, the plank, the big step, the bow, the landing.",
                "No demonstration. They have had four nights on each of them.",
                "Then call them again in a mixed up order, ten seconds each.",
            ]),
            ("15 to 17", "Finish", "Name all five", [
                "Walk them in.",
                'Ask the group: "Name the five shapes." Then ask one boy to say what each one is for.',
                "That is the autumn finished. Tell them so.",
            ]),
        ],
        "coach": "Nothing. Find out how many of the five shapes they can name.",
        "watch": ["How many boys can name all five without help. That number is the honest score for the autumn."],
        "wet": "Two feet landings only, and the shapes on the ground become the sit and the bow.",
    },
]
