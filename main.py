from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
from elevenlabslib import *

ELEVENLABS_API_KEY = "##########"
bot = Bot(token='##########')
dp = Dispatcher(bot)
user = ElevenLabsUser(ELEVENLABS_API_KEY)
voice = user.get_voices_by_name("Rachel")[0]

button1 = InlineKeyboardButton(text="Badminton", callback_data="Badminton")
button2 = InlineKeyboardButton(text="Tennis", callback_data="Tennis")
button3 = InlineKeyboardButton(text="Table Tennis", callback_data="Table Tennis")
button4 = InlineKeyboardButton(text="Squash", callback_data="Squash")
button5 = InlineKeyboardButton(text="Hiking", callback_data="Hiking")
button6 = InlineKeyboardButton(text="Trekking", callback_data="Trekking")
button7 = InlineKeyboardButton(text="Cardio", callback_data="Cardio")
button8 = InlineKeyboardButton(text="Gym Tracks", callback_data="Gym Tracks")
button9 = InlineKeyboardButton(text="Camping", callback_data="Camping")
button10 = InlineKeyboardButton(text="Skiing", callback_data="Skiing")
button11 = InlineKeyboardButton(text="Wildlife", callback_data="Wildlife")
button12 = InlineKeyboardButton(text="Cycle", callback_data="Cycle")
button13 = InlineKeyboardButton(text="Road Cycle", callback_data="Road Cycle")
button14 = InlineKeyboardButton(text="MTB Cycle", callback_data="MTB Cycle")
button15 = InlineKeyboardButton(text="Fishing", callback_data="Fishing")
button16 = InlineKeyboardButton(text="Horse Riding", callback_data="Horse Riding")
button17 = InlineKeyboardButton(text="Swimming", callback_data="Swimming")
button18 = InlineKeyboardButton(text="FootBall", callback_data="FootBall")
button19 = InlineKeyboardButton(text="Cricket", callback_data="Cricket")
button20 = InlineKeyboardButton(text="Surfing", callback_data="Surfing")
button21 = InlineKeyboardButton(text="Running", callback_data="Running")
button22 = InlineKeyboardButton(text="Golf", callback_data="Golf")
button23 = InlineKeyboardButton(text="SkateBoard", callback_data="SkateBoard")
button24 = InlineKeyboardButton(text="Roller skating", callback_data="Roller skating")
button25 = InlineKeyboardButton(text="Men Winter Collections", callback_data="Men Winter Collections")
button26 = InlineKeyboardButton(text="Women Winter Collection", callback_data="Women Winter Collection")
button27 = InlineKeyboardButton(text="Kids Winter Collection & Winter Accessories",
                                callback_data="Kids Winter Collection & Winter Accessories")

keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3, button4, button5, button6, button7, button8,
                                             button9, button10, button11, button12, button13, button14, button15,
                                             button16, button17, button18, button19, button20, button21, button22,
                                             button23, button24, button25, button26, button27)

button28 = InlineKeyboardButton(text="Badminton Racket", callback_data="Badminton Racket")
button29 = InlineKeyboardButton(text="Shuttle cock", callback_data="Shuttle cock")
button30 = InlineKeyboardButton(text="Badminton shoes", callback_data="Badminton shoes")
button31 = InlineKeyboardButton(text="Non Marking shoes", callback_data="Non Marking shoes")
button32 = InlineKeyboardButton(text="Badminton Tshirts", callback_data="Badminton Tshirts")
button33 = InlineKeyboardButton(text="Badminton shorts", callback_data="Badminton shorts")
button34 = InlineKeyboardButton(text="Racket cover", callback_data="Racket cover")
button35 = InlineKeyboardButton(text="Badminton grip", callback_data="Badminton grip")
button36 = InlineKeyboardButton(text="Badminton net", callback_data="Badminton net")
button37 = InlineKeyboardButton(text="Racket string", callback_data="Racket string")
keyboard_inline_1 = InlineKeyboardMarkup().add(button28, button29, button30, button31, button32, button33, button34,
                                               button35, button36, button37)

button38 = InlineKeyboardButton(text="Tennis Clothing", callback_data="Tennis Clothing")
button39 = InlineKeyboardButton(text="Socks", callback_data="Socks")
button40 = InlineKeyboardButton(text="Tennis Rackets", callback_data="Tennis Rackets")
button41 = InlineKeyboardButton(text="Tennis Balls", callback_data="Tennis Balls")
button42 = InlineKeyboardButton(text="Tennis Shoes", callback_data="Tennis Shoes")
button43 = InlineKeyboardButton(text="Tennis bag", callback_data="Tennis bag")
button44 = InlineKeyboardButton(text="Tennis Accessories", callback_data="Tennis Accessories")
button45 = InlineKeyboardButton(text="Beach tennis", callback_data="Beach tennis")
button46 = InlineKeyboardButton(text="Men Tennis apparels", callback_data="Men Tennis apparels")
button47 = InlineKeyboardButton(text="Women Tennis Apparels", callback_data="Women Tennis Apparels")
keyboard_inline_2 = InlineKeyboardMarkup().add(button38, button39, button40, button41, button42, button43, button44,
                                               button45, button46, button47)

button48 = InlineKeyboardButton(text="Table Tennis Tables", callback_data="Table Tennis Tables")
button49 = InlineKeyboardButton(text="TT Rackets", callback_data="TT Rackets")
button50 = InlineKeyboardButton(text="TT Balls", callback_data="TT Balls")
button51 = InlineKeyboardButton(text="TT Nets", callback_data="TT Nets")
button52 = InlineKeyboardButton(text="TT Racket covers", callback_data="TT Racket covers")
button53 = InlineKeyboardButton(text="Table Tennis accessories", callback_data="Table Tennis accessories")
button54 = InlineKeyboardButton(text="Table Tennis clothing", callback_data="Table Tennis clothing")
button55 = InlineKeyboardButton(text="Table Tennis shoes", callback_data="Table Tennis shoes")
button56 = InlineKeyboardButton(text="Table Tennis socks", callback_data="Table Tennis socks")
button57 = InlineKeyboardButton(text="TT collections", callback_data="TT collections")
keyboard_inline_3 = InlineKeyboardMarkup().add(button48, button49, button50, button51, button52, button53, button54,
                                               button55, button56, button57)

button58 = InlineKeyboardButton(text="Squash Rackets", callback_data="Squash Rackets")
button59 = InlineKeyboardButton(text="Squash Balls", callback_data="Squash Balls")
button60 = InlineKeyboardButton(text="Squash Kit bags", callback_data="Squash Kit bags")
button61 = InlineKeyboardButton(text="Squash Accessories", callback_data="Squash Accessories")
button62 = InlineKeyboardButton(text="Squash clothing", callback_data="Squash clothing")
button63 = InlineKeyboardButton(text="Squash shoes", callback_data="Squash shoes")
button64 = InlineKeyboardButton(text="Squash collections", callback_data="Squash collections")
keyboard_inline_4 = InlineKeyboardMarkup().add(button58, button59, button60, button61, button62, button63, button64)

button65 = InlineKeyboardButton(text="Fleece", callback_data="Fleece")
button66 = InlineKeyboardButton(text="Sweaters", callback_data="Sweaters")
button67 = InlineKeyboardButton(text="Rain Jacket", callback_data="Rain Jacket")
button68 = InlineKeyboardButton(text="Hiking shoes", callback_data="Hiking shoes")
button69 = InlineKeyboardButton(text="Sandals", callback_data="Sandals")
button70 = InlineKeyboardButton(text="Socks", callback_data="Socks")
button71 = InlineKeyboardButton(text="Backpack", callback_data="Backpack")
button72 = InlineKeyboardButton(text="Hiking Backpack", callback_data="Hiking Backpack")
button73 = InlineKeyboardButton(text="Sunglasses", callback_data="Sunglasses")
button74 = InlineKeyboardButton(text="Bottles", callback_data="Bottles")
keyboard_inline_5 = InlineKeyboardMarkup().add(button65, button66, button67, button68, button69, button70, button71,
                                               button72, button73, button74)

button75 = InlineKeyboardButton(text="Trekking Boots", callback_data="Trekking Boots")
button76 = InlineKeyboardButton(text="Trekking Backpack", callback_data="Trekking Backpack")
button77 = InlineKeyboardButton(text="Travel backpack", callback_data="Travel backpack")
button78 = InlineKeyboardButton(text="Winter Jackets", callback_data="Winter Jackets")
button79 = InlineKeyboardButton(text="Down Jackets", callback_data="Down Jackets")
button80 = InlineKeyboardButton(text="Trekking Poles", callback_data="Trekking Poles")
button81 = InlineKeyboardButton(text="Travel Shirts", callback_data="Travel Shirts")
button82 = InlineKeyboardButton(text="Shorts", callback_data="Shorts")
button83 = InlineKeyboardButton(text="Trousers", callback_data="Trousers")
button84 = InlineKeyboardButton(text="Headlamps", callback_data="Headlamps")
keyboard_inline_6 = InlineKeyboardMarkup().add(button75, button76, button77, button78, button79, button80, button81,
                                               button82, button83, button84)

button85 = InlineKeyboardButton(text="Fitness Equipment", callback_data="Fitness Equipment")
button86 = InlineKeyboardButton(text="Treadmills", callback_data="Treadmills")
button87 = InlineKeyboardButton(text="Cross Trainers", callback_data="Cross Trainers")
button88 = InlineKeyboardButton(text="Elliptical", callback_data="Elliptical")
button89 = InlineKeyboardButton(text="Exercise bikes", callback_data="Exercise bikes")
button90 = InlineKeyboardButton(text="Spin Bikes", callback_data="Spin Bikes")
button91 = InlineKeyboardButton(text="Rowing Machine", callback_data="Rowing Machine")
button92 = InlineKeyboardButton(text="Steppers", callback_data="Steppers")
button93 = InlineKeyboardButton(text="Trampoline", callback_data="Trampoline")
button94 = InlineKeyboardButton(text="Cardio Apparel", callback_data="Cardio Apparel")
keyboard_inline_7 = InlineKeyboardMarkup().add(button85, button86, button87, button88, button89, button90, button91,
                                               button92, button93, button94)

button95 = InlineKeyboardButton(text="Gym Track pants", callback_data="Gym Track pants")
button96 = InlineKeyboardButton(text="Gym Shorts", callback_data="Gym Shorts")
button97 = InlineKeyboardButton(text="Men Tracksuits", callback_data="Men Tracksuits")
button98 = InlineKeyboardButton(text="Women Gym suits", callback_data="Women Gym suits")
button99 = InlineKeyboardButton(text="Sports Bra", callback_data="Sports Bra")
button100 = InlineKeyboardButton(text="Gym Tops", callback_data="Gym Tops")
button101 = InlineKeyboardButton(text="Women fitness jacket", callback_data="Women fitness jacket")
keyboard_inline_8 = InlineKeyboardMarkup().add(button95, button96, button97, button98, button99, button100, button101)

button102 = InlineKeyboardButton(text="Tents", callback_data="Tents")
button103 = InlineKeyboardButton(text="Chairs", callback_data="Chairs")
button104 = InlineKeyboardButton(text="Tables", callback_data="Tables")
button105 = InlineKeyboardButton(text="Furnitures", callback_data="Furnitures")
button106 = InlineKeyboardButton(text="Sleeping Bags", callback_data="Sleeping Bags")
button107 = InlineKeyboardButton(text="Mattresses", callback_data="Mattresses")
button108 = InlineKeyboardButton(text="Camping Accessories", callback_data="Camping Accessories")
button109 = InlineKeyboardButton(text="Cooksets", callback_data="Cooksets")
keyboard_inline_9 = InlineKeyboardMarkup().add(button102, button103, button104, button105, button106, button107,
                                               button108, button109)

button110 = InlineKeyboardButton(text="Men Thermals", callback_data="Men Thermals")
button111 = InlineKeyboardButton(text="Women Thermals", callback_data="Women Thermals")
button112 = InlineKeyboardButton(text="Beanies", callback_data="Beanies")
button113 = InlineKeyboardButton(text="Gloves", callback_data="Gloves")
button114 = InlineKeyboardButton(text="Winter Accessories", callback_data="Winter Accessories")
button115 = InlineKeyboardButton(text="Warmers", callback_data="Warmers")
button116 = InlineKeyboardButton(text="Junior Jackets", callback_data="Junior Jackets")
button117 = InlineKeyboardButton(text="Junior Beanies", callback_data="Junior Beanies")
button118 = InlineKeyboardButton(text="Ski jackets", callback_data="Ski jackets")
keyboard_inline_10 = InlineKeyboardMarkup().add(button110, button111, button112, button113, button114, button115,
                                                button116, button117, button118)

button119 = InlineKeyboardButton(text="Camo Tshirts", callback_data="Camo Tshirts")
button120 = InlineKeyboardButton(text="Camo Trousers", callback_data="Camo Trousers")
button121 = InlineKeyboardButton(text="Camo Bermudas", callback_data="Camo Bermudas")
button122 = InlineKeyboardButton(text="Camo Caps", callback_data="Camo Caps")
button123 = InlineKeyboardButton(text="Gum Boots", callback_data="Gum Boots")
button124 = InlineKeyboardButton(text="Binoculars", callback_data="Binoculars")
button125 = InlineKeyboardButton(text="Knifes", callback_data="Knifes")
button126 = InlineKeyboardButton(text="Shelter", callback_data="Shelter")
button127 = InlineKeyboardButton(text="Umbrellas", callback_data="Umbrellas")
button128 = InlineKeyboardButton(text="Pouches", callback_data="Pouches")
keyboard_inline_11 = InlineKeyboardMarkup().add(button119, button120, button121, button122, button123, button124,
                                                button125, button126, button127, button128)

button129 = InlineKeyboardButton(text="Bike Racks", callback_data="Bike Racks")
button130 = InlineKeyboardButton(text="Cycles", callback_data="Cycles")
button131 = InlineKeyboardButton(text="Mountain Bikes", callback_data="Mountain Bikes")
button132 = InlineKeyboardButton(text="Hybrid Cycles", callback_data="Hybrid Cycles")
button133 = InlineKeyboardButton(text="Road Bikes", callback_data="Road Bikes")
button134 = InlineKeyboardButton(text="Kids Cycle", callback_data="Kids Cycle")
button135 = InlineKeyboardButton(text="Cycle Accessories", callback_data="Cycle Accessories")
keyboard_inline_12 = InlineKeyboardMarkup().add(button129, button130, button131, button132, button133, button134,
                                                button135)

button136 = InlineKeyboardButton(text="Bike Racks", callback_data="Bike Racks")
button130 = InlineKeyboardButton(text="Cycles", callback_data="Cycles")
button131 = InlineKeyboardButton(text="Mountain Bikes", callback_data="Mountain Bikes")
button132 = InlineKeyboardButton(text="Hybrid Cycles", callback_data="Hybrid Cycles")
button133 = InlineKeyboardButton(text="Road Bikes", callback_data="Road Bikes")
button134 = InlineKeyboardButton(text="Kids Cycle", callback_data="Kids Cycle")
button135 = InlineKeyboardButton(text="Cycle Accessories", callback_data="Cycle Accessories")
keyboard_inline_13 = InlineKeyboardMarkup().add(button136, button130, button131, button132, button133, button134,
                                                button135)

button137 = InlineKeyboardButton(text="Bike Racks", callback_data="Bike Racks")
button138 = InlineKeyboardButton(text="Cycles", callback_data="Cycles")
button139 = InlineKeyboardButton(text="Mountain Bikes", callback_data="Mountain Bikes")
button140 = InlineKeyboardButton(text="Hybrid Cycles", callback_data="Hybrid Cycles")
button141 = InlineKeyboardButton(text="Road Bikes", callback_data="Road Bikes")
button142 = InlineKeyboardButton(text="Kids Cycle", callback_data="Kids Cycle")
button143 = InlineKeyboardButton(text="Cycle Accessories", callback_data="Cycle Accessories")
keyboard_inline_14 = InlineKeyboardMarkup().add(button137, button138, button139, button140, button141, button142,
                                                button143)

button144 = InlineKeyboardButton(text="Fishing Rods", callback_data="Fishing Rods")
button145 = InlineKeyboardButton(text="Fishing Reels", callback_data="Fishing Reels")
button146 = InlineKeyboardButton(text="Hooks", callback_data="Hooks")
button147 = InlineKeyboardButton(text="Lures", callback_data="Lures")
button148 = InlineKeyboardButton(text="Fishing lines", callback_data="Fishing lines")
button149 = InlineKeyboardButton(text="Fishing Accessories", callback_data="Fishing Accessories")
button150 = InlineKeyboardButton(text="Fishing Camp Furnitures", callback_data="Fishing Camp Furnitures")
button151 = InlineKeyboardButton(text="Fishing ponchos", callback_data="Fishing ponchos")
button152 = InlineKeyboardButton(text="Fishing GIlet", callback_data="Fishing GIlet")
keyboard_inline_15 = InlineKeyboardMarkup().add(button144, button145, button146, button147, button148, button149,
                                                button150, button151, button152)

button153 = InlineKeyboardButton(text="Horse riding helmets", callback_data="Horse riding helmets")
button154 = InlineKeyboardButton(text="Breeches", callback_data="Breeches")
button155 = InlineKeyboardButton(text="Horse riding boots", callback_data="Horse riding boots")
button156 = InlineKeyboardButton(text="Horse riding gloves", callback_data="Horse riding gloves")
button157 = InlineKeyboardButton(text="Leather saddle", callback_data="Leather saddle")
button158 = InlineKeyboardButton(text="Cloth saddle", callback_data="Cloth saddle")
keyboard_inline_16 = InlineKeyboardMarkup().add(button153, button154, button155, button156, button157, button158)

button159 = InlineKeyboardButton(text="Swimming costumes", callback_data="Swimming costumes")
button160 = InlineKeyboardButton(text="Swimming cap", callback_data="Swimming cap")
button161 = InlineKeyboardButton(text="Swimming goggles", callback_data="Swimming goggles")
button162 = InlineKeyboardButton(text="Towels", callback_data="Towels")
button163 = InlineKeyboardButton(text="Bathrobes", callback_data="Bathrobes")
button164 = InlineKeyboardButton(text="Flipflops", callback_data="Flipflops")
button165 = InlineKeyboardButton(text="Swimming equipments", callback_data="Swimming equipments")
button166 = InlineKeyboardButton(text="Aqua learning", callback_data="Aqua learning")
button167 = InlineKeyboardButton(text="Buoyancy aids", callback_data="Buoyancy aids")
keyboard_inline_17 = InlineKeyboardMarkup().add(button159, button160, button161, button162, button163, button164,
                                                button165, button166, button167)

button168 = InlineKeyboardButton(text="Football", callback_data="Football")
button169 = InlineKeyboardButton(text="Football shoes", callback_data="Football shoes")
button170 = InlineKeyboardButton(text="Football bag", callback_data="Football bag")
button171 = InlineKeyboardButton(text="Football Jersey", callback_data="Football Jersey")
button172 = InlineKeyboardButton(text="Football shorts", callback_data="Football shorts")
button173 = InlineKeyboardButton(text="Football Socks", callback_data="Football Socks")
button174 = InlineKeyboardButton(text="Goal Posts", callback_data="Goal Posts")
button175 = InlineKeyboardButton(text="Training accessories", callback_data="Training accessories")
button176 = InlineKeyboardButton(text="Goalkeeper Kit", callback_data="Goalkeeper Kit")
button177 = InlineKeyboardButton(text="Football Equipment", callback_data="Football Equipment")
keyboard_inline_18 = InlineKeyboardMarkup().add(button168, button169, button170, button171, button172, button173,
                                                button174, button175, button176, button177)

button178 = InlineKeyboardButton(text="Tennis Cricket bat", callback_data="Tennis Cricket bat")
button179 = InlineKeyboardButton(text="English Willow Bat", callback_data="English Willow Bat")
button180 = InlineKeyboardButton(text="Kids cricket bat", callback_data="Kids cricket bat")
button181 = InlineKeyboardButton(text="Cricket ball", callback_data="Cricket ball")
button182 = InlineKeyboardButton(text="Cricket accessories", callback_data="Cricket accessories")
button183 = InlineKeyboardButton(text="Adult cricket shoes", callback_data="Adult cricket shoes")
button184 = InlineKeyboardButton(text="Kids cricket shoes", callback_data="Kids cricket shoes")
button185 = InlineKeyboardButton(text="Cricket track pants", callback_data="Cricket track pants")
button186 = InlineKeyboardButton(text="Cricket jersey", callback_data="Cricket jersey")
keyboard_inline_19 = InlineKeyboardMarkup().add(button178, button179, button180, button181, button182, button183,
                                                button184, button185, button186)

button187 = InlineKeyboardButton(text="Board shorts", callback_data="Board shorts")
button188 = InlineKeyboardButton(text="Frisbee", callback_data="Frisbee")
button189 = InlineKeyboardButton(text="Surfboards", callback_data="Surfboards")
button190 = InlineKeyboardButton(text="Wetsuits", callback_data="Wetsuits")
button191 = InlineKeyboardButton(text="Bodyboards", callback_data="Bodyboards")
button192 = InlineKeyboardButton(text="Kites", callback_data="Kites")
button193 = InlineKeyboardButton(text="Snorkelling", callback_data="Snorkelling")
button194 = InlineKeyboardButton(text="Scuba diving", callback_data="Scuba diving")
button195 = InlineKeyboardButton(text="Kayaks", callback_data="Kayaks")
button196 = InlineKeyboardButton(text="Standup paddle", callback_data="Standup paddle")
keyboard_inline_20 = InlineKeyboardMarkup().add(button187, button188, button189, button190, button191, button192,
                                                button193, button194, button195, button196)

button197 = InlineKeyboardButton(text="Running shoes", callback_data="Running shoes")
button198 = InlineKeyboardButton(text="Jogging shoes", callback_data="Jogging shoes")
button199 = InlineKeyboardButton(text="Trail Running shoes", callback_data="Trail Running shoes")
button200 = InlineKeyboardButton(text="Running Tshirts", callback_data="Running Tshirts")
button201 = InlineKeyboardButton(text="Running shorts", callback_data="Running shorts")
button202 = InlineKeyboardButton(text="Running Tights", callback_data="Running Tights")
button203 = InlineKeyboardButton(text="Running Accessories", callback_data="Running Accessories")
button204 = InlineKeyboardButton(text="Sports watch", callback_data="Sports watch")
button205 = InlineKeyboardButton(text="Weighing scale", callback_data="Weighing scale")
button206 = InlineKeyboardButton(text="Earphones", callback_data="Earphones")
keyboard_inline_21 = InlineKeyboardMarkup().add(button197, button198, button199, button200, button201, button202,
                                                button203, button204, button205, button206)

button207 = InlineKeyboardButton(text="Golf clubs", callback_data="Golf clubs")
button208 = InlineKeyboardButton(text="Golf trolleys", callback_data="Golf trolleys")
button209 = InlineKeyboardButton(text="Golf balls", callback_data="Golf balls")
button210 = InlineKeyboardButton(text="Golf accessories", callback_data="Golf accessories")
button211 = InlineKeyboardButton(text="Polo Tshirts", callback_data="Polo Tshirts")
button212 = InlineKeyboardButton(text="Golf Trouser", callback_data="Golf Trouser")
button213 = InlineKeyboardButton(text="Golf shoes", callback_data="Golf shoes")
button214 = InlineKeyboardButton(text="Golf caps", callback_data="Golf caps")
button215 = InlineKeyboardButton(text="Golf shorts", callback_data="Golf shorts")
keyboard_inline_22 = InlineKeyboardMarkup().add(button207, button208, button209, button210, button211, button212,
                                                button213, button214, button215)

button216 = InlineKeyboardButton(text="Skateboard", callback_data="Skateboard")
button217 = InlineKeyboardButton(text="Long boards", callback_data="Long boards")
button218 = InlineKeyboardButton(text="Waveboard", callback_data="Waveboard")
button219 = InlineKeyboardButton(text="Skateboard shoes", callback_data="Skateboard shoes")
button220 = InlineKeyboardButton(text="Skateboard accessories", callback_data="Skateboard accessories")
button221 = InlineKeyboardButton(text="Kids scooters", callback_data="Kids scooters")
button222 = InlineKeyboardButton(text="Adult scooters", callback_data="Adult scooters")
button223 = InlineKeyboardButton(text="Spares", callback_data="Spares")
button224 = InlineKeyboardButton(text="Scooter helmets", callback_data="Scooter helmets")
keyboard_inline_23 = InlineKeyboardMarkup().add(button216, button217, button218, button219, button220, button221,
                                                button222, button223, button224)

button225 = InlineKeyboardButton(text="Quad Roller skates", callback_data="Quad Roller skates")
button226 = InlineKeyboardButton(text="Inline skates", callback_data="Inline skates")
button227 = InlineKeyboardButton(text="Kids Inline skates", callback_data="Kids Inline skates")
button228 = InlineKeyboardButton(text="Adult Inline skates", callback_data="Adult Inline skates")
button229 = InlineKeyboardButton(text="Skating Helmets", callback_data="Skating Helmets")
button230 = InlineKeyboardButton(text="Skating guards", callback_data="Skating guards")
button231 = InlineKeyboardButton(text="Skating bags", callback_data="Skating bags")
button232 = InlineKeyboardButton(text="Skating spares accessories", callback_data="Skating spares accessories")
keyboard_inline_24 = InlineKeyboardMarkup().add(button225, button226, button227, button228, button229, button230,
                                                button231, button232)

button233 = InlineKeyboardButton(text="Men Sweaters", callback_data="Men Sweaters")
button234 = InlineKeyboardButton(text="Men Fleece Jacket", callback_data="Men Fleece Jacket")
button235 = InlineKeyboardButton(text="Men Pullover", callback_data="Men Pullover")
button236 = InlineKeyboardButton(text="Men Sweatshirt", callback_data="Men Sweatshirt")
button237 = InlineKeyboardButton(text="Men Hoodies", callback_data="Men Hoodies")
button238 = InlineKeyboardButton(text="Men Winter Coat", callback_data="Men Winter Coat")
button239 = InlineKeyboardButton(text="Men Winter Jacket", callback_data="Men Winter Jacket")
button240 = InlineKeyboardButton(text="Men Puffer Jacket", callback_data="Men Puffer Jacket")
button241 = InlineKeyboardButton(text="Men Down Jacket", callback_data="Men Down Jacket")
button242 = InlineKeyboardButton(text="Men Snow Jacket", callback_data="Men Snow Jacket")
button243 = InlineKeyboardButton(text="Men Bomber Jacket", callback_data="Men Bomber Jacket")
button244 = InlineKeyboardButton(text="Winter Shoes", callback_data="Winter Shoes")
button245 = InlineKeyboardButton(text="Men Winter Shoes", callback_data="Men Winter Shoes")
button246 = InlineKeyboardButton(text="Snow Socks", callback_data="Snow Socks")
button247 = InlineKeyboardButton(text="Men Winter Outfits", callback_data="Men Winter Outfits")
button248 = InlineKeyboardButton(text="Men Winter Tshirt", callback_data="Men Winter Tshirt")
button249 = InlineKeyboardButton(text="Men Thermals", callback_data="Men Thermals")
button250 = InlineKeyboardButton(text="Men Warm Trouser", callback_data="Men Warm Trouser")
keyboard_inline_25 = InlineKeyboardMarkup().add(button233, button234, button235, button236, button237, button238,
                                                button239, button240, button241, button242, button243, button244,
                                                button245, button246, button247, button248, button249, button250)

button251 = InlineKeyboardButton(text="Women Sweaters", callback_data="Women Sweaters")
button252 = InlineKeyboardButton(text="Women Fleece Jacket", callback_data="Women Fleece Jacket")
button253 = InlineKeyboardButton(text="Women Pullover", callback_data="Women Pullover")
button254 = InlineKeyboardButton(text="Women Sweatshirt", callback_data="Women Sweatshirt")
button255 = InlineKeyboardButton(text="Women Jackets", callback_data="Women Jackets")
button256 = InlineKeyboardButton(text="Women Winter Jacket", callback_data="Women Winter Jacket")
button257 = InlineKeyboardButton(text="Women Puffer Jacket", callback_data="Women Puffer Jacket")
button258 = InlineKeyboardButton(text="Women Down Jacket", callback_data="Women Down Jacket")
button259 = InlineKeyboardButton(text="Women Snow Jacket", callback_data="Women Snow Jacket")
button260 = InlineKeyboardButton(text="Women Bomber Jacket", callback_data="Women Bomber Jacket")
button261 = InlineKeyboardButton(text="Women Snow Shoes", callback_data="Women Snow Shoes")
button262 = InlineKeyboardButton(text="Women Winter Outfits", callback_data="Women Winter Outfits")
button263 = InlineKeyboardButton(text="Women Thermals", callback_data="Women Thermals")
button264 = InlineKeyboardButton(text="Women Warm Trouser", callback_data="Women Warm Trouser")
keyboard_inline_26 = InlineKeyboardMarkup().add(button251, button252, button253, button254, button255, button256,
                                                button257, button258, button259, button260, button261, button262,
                                                button263, button264)

button265 = InlineKeyboardButton(text="Kids Sweater", callback_data="Kids Sweater")
button266 = InlineKeyboardButton(text="Kids Winter Jacket", callback_data="Kids Winter Jacket")
button267 = InlineKeyboardButton(text="Kids Thermals", callback_data="Kids Thermals")
button268 = InlineKeyboardButton(text="Kids Beanies", callback_data="Kids Beanies")
button269 = InlineKeyboardButton(text="Kids Winter Accessories", callback_data="Kids Winter Accessories")
button270 = InlineKeyboardButton(text="Winter Caps", callback_data="Winter Caps")
button271 = InlineKeyboardButton(text="Winter Gloves", callback_data="Winter Gloves")
button272 = InlineKeyboardButton(text="Neckwarmer", callback_data="Neckwarmer")
button273 = InlineKeyboardButton(text="Sunglasses", callback_data="Sunglasses")
button274 = InlineKeyboardButton(text="Sleeping bags", callback_data="Sleeping bags")
button275 = InlineKeyboardButton(text="Warmers", callback_data="Warmers")
button276 = InlineKeyboardButton(text="Snowshoeing", callback_data="Snowshoeing")
button277 = InlineKeyboardButton(text="Insulated Bottles", callback_data="Insulated Bottles")
keyboard_inline_27 = InlineKeyboardMarkup().add(button265, button266, button267, button268, button269, button270,
                                                button271, button272, button273, button274, button275, button276,
                                                button277)

button278 = InlineKeyboardButton(text="Men's", callback_data="Men's")
button279 = InlineKeyboardButton(text="Women's", callback_data="Women's")
button280 = InlineKeyboardButton(text="Boy's", callback_data="Boy's")
keyboard_inline_28 = InlineKeyboardMarkup().add(button278, button279, button280)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("/Restart", "/OfficialWebsite")



@dp.callback_query_handler(
    text=["Badminton Racket", "Shuttle cock", "Badminton shoes", "Non Marking shoes", "Badminton Tshirts",
          "Badminton shorts", "Racket cover", "Badminton grip", "Badminton net", "Racket string"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Badminton Racket":
        await call.message.answer("https://www.decathlon.in/badminton/badminton-racket-17482?id=17482&type=c")
    if call.data == "Shuttle cock":
        await call.message.answer("https://www.decathlon.in/badminton/badminton-shuttlecocks-17500?id=17500&type=c")
    if call.data == "Badminton shoes":
        await call.message.answer("https://www.decathlon.in/badminton/badminton-shoe-17509?id=17509&type=c")
    if call.data == "Non Marking shoes":
        await call.message.answer("https://www.decathlon.in/badminton/badminton-shoe-17509?id=17509&type=c")
    if call.data == "Badminton Tshirts":
        await call.message.answer("https://www.decathlon.in/badminton/badminton-apparels-20125?id=20125&type=c")
    if call.data == "Badminton shorts":
        await call.message.answer("https://www.decathlon.in/badminton/badminton-apparels-20125?id=20125&type=c")
    if call.data == "Racket cover":
        await call.message.answer(
            "https://www.decathlon.in/badminton-covers-accessories/badminton-covers-kit-bags-20143?id=20143&type=c")
    if call.data == "Badminton grip":
        await call.message.answer(
            "https://www.decathlon.in/badminton-covers-accessories/badminton-grips-17494?id=17494&type=c")
    if call.data == "Badminton net":
        await call.message.answer(
            "https://www.decathlon.in/badminton-covers-accessories/badminton-net-17497?id=17497&type=c")
    if call.data == "Racket string":
        await call.message.answer(
            "https://www.decathlon.in/badminton-covers-accessories/badminton-strings-17488?id=17488&type=c")


@dp.callback_query_handler(
    text=["Tennis Clothing", "Socks", "Tennis Rackets", "Tennis Balls", "Tennis Shoes", "Tennis bag",
          "Tennis Accessories", "Beach tennis", "Men Tennis apparels", "Women Tennis Apparels"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Tennis Clothing":
        await call.message.answer("https://www.decathlon.in/tennis/tennis-clothing-17545?id=17545&type=c")
    if call.data == "Socks":
        await call.message.answer("https://www.decathlon.in/tennis/socks-17569?id=17569&type=c")
    if call.data == "Tennis Rackets":
        await call.message.answer("https://www.decathlon.in/tennis/tennis-rackets-17572?id=17572&type=c")
    if call.data == "Tennis Balls":
        await call.message.answer("https://www.decathlon.in/tennis/tennis-balls-17563?id=17563&type=c")
    if call.data == "Tennis Shoes":
        await call.message.answer("https://www.decathlon.in/tennis/tennis-shoes-21291?id=21291&type=c")
    if call.data == "Tennis bag":
        await call.message.answer("https://www.decathlon.in/tennis/tennis-covers-bags-17560?id=17560&type=c")
    if call.data == "Tennis Accessories":
        await call.message.answer("https://www.decathlon.in/tennis/tennis-accessories-leisure-club-equipment-17566?id=17566&type=c")
    if call.data == "Beach tennis":
        await call.message.answer("https://www.decathlon.in/tennis/beach-tennis-rackets-21811?id=21811&type=c")
    if call.data == "Men Tennis apparels":
        await call.message.answer("https://www.decathlon.in/tennis/tennis-for-men-21324?id=21324&type=c")
    if call.data == "Women Tennis Apparels":
        await call.message.answer("https://www.decathlon.in/tennis/tennis-for-women-21347?id=21347&type=c")



@dp.callback_query_handler(
    text=["Table Tennis Tables", "TT Rackets", "TT Balls", "TT Nets", "TT Racket covers", "Table Tennis accessories",
          "Table Tennis clothing", "Table Tennis shoes", "Table Tennis socks", "TT collections"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Table Tennis Tables":
        await call.message.answer("https://www.decathlon.in/table-tennis/table-tennis-tables-21244?id=21244&type=c")
    if call.data == "TT Rackets":
        await call.message.answer("https://www.decathlon.in/table-tennis/table-tennis-rackets-16669?id=16669&type=c")
    if call.data == "TT Balls":
        await call.message.answer("https://www.decathlon.in/table-tennis/table-tennis-balls-16663?id=16663&type=c")
    if call.data == "TT Nets":
        await call.message.answer("https://www.decathlon.in/table-tennis/table-tennis-nets-21245?id=21245&type=c")
    if call.data == "TT Racket covers":
        await call.message.answer("https://www.decathlon.in/table-tennis/table-tennis-racket-covers-16666?id=16666&type=c")
    if call.data == "Table Tennis accessories":
        await call.message.answer("https://www.decathlon.in/table-tennis/table-tennis-accessories-21316?id=21316&type=c")
    if call.data == "Table Tennis clothing":
        await call.message.answer("https://www.decathlon.in/all-sports/squash-1117?id=1117&type=c")
    if call.data == "Table Tennis shoes":
        await call.message.answer("https://www.decathlon.in/table-tennis/table-tennis-shoes-21299?id=21299&type=c")
    if call.data == "Table Tennis socks":
        await call.message.answer("https://www.decathlon.in/table-tennis/socks-21293?id=21293&type=c")
    if call.data == "TT collections":
        await call.message.answer("https://www.decathlon.in/all-sports/table-tennis-12620?id=12620&type=c")



@dp.callback_query_handler(
    text=["Squash Rackets", "Squash Balls", "Squash Kit bags", "Squash Accessories", "Squash clothing", "Squash shoes",
          "Squash collections"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
        This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
        This is the link for {call.data}: """)
    if call.data == "Squash Rackets":
        await call.message.answer("https://www.decathlon.in/squash/squash-rackets-21289?id=21289&type=c")
    if call.data == "Squash Balls":
        await call.message.answer("https://www.decathlon.in/squash/squash-balls-21288?id=21288&type=c")
    if call.data == "Squash Kit bags":
        await call.message.answer("https://www.decathlon.in/squash/squash-kit-bags-21298?id=21298&type=c")
    if call.data == "Squash Accessories":
        await call.message.answer("https://www.decathlon.in/squash/squash-accessories-21290?id=21290&type=c")
    if call.data == "Squash clothing":
        await call.message.answer("https://www.decathlon.in/squash/squash-clothing-21281?id=21281&type=c")
    if call.data == "Squash shoes":
        await call.message.answer("https://www.decathlon.in/squash/squash-shoes-21287?id=21287&type=c")
    if call.data == "Squash collections":
        await call.message.answer("https://www.decathlon.in/all-sports/squash-1117?id=1117&type=c")


@dp.callback_query_handler(
    text=["Fleece", "Sweaters", "Rain Jacket", "Hiking shoes", "Sandals", "Socks", "Backpack", "Hiking Backpack",
          "Sunglasses", "Bottles"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Fleece":
        await call.message.answer("https://www.decathlon.in/clothing/fleeces-and-sweaters-15705?id=15705&type=c")
    if call.data == "Sweaters":
        await call.message.answer("https://www.decathlon.in/clothing/fleeces-and-sweaters-15705?id=15705&type=c")
    if call.data == "Rain Jacket":
        await call.message.answer("https://www.decathlon.in/backpacks/travel-and-trekking-backpack-15648?id=15648&type=c")
    if call.data == "Hiking shoes":
        await call.message.answer("https://www.decathlon.in/clothing/raincoat-and-poncho-15693?id=15693&type=c")
    if call.data == "Sandals":
        await call.message.answer(
            "https://www.decathlon.in/footwear/sandals-18235?icm=HTSportpage&icn=dropdown_sandals&id=18235&type=c")
    if call.data == "Socks":
        await call.message.answer(
            "https://www.decathlon.in/equipment-and-accessories/hiking-trekking-poles-15624?id=15624&type=c")
    if call.data == "Backpack":
        await call.message.answer(
            "https://www.decathlon.in/backpacks/hiking-bags-and-backpack-15711?icm=HTSportpage&icn=dropdown_hiking-bags-and-backpacks&id=15711&type=c")
    if call.data == "Hiking Backpack":
        await call.message.answer(
            "https://www.decathlon.in/backpacks/hiking-bags-and-backpack-15711?icm=HTSportpage&icn=dropdown_hiking-bags-and-backpacks&id=15711&type=c")
    if call.data == "Sunglasses":
        await call.message.answer(
            "https://www.decathlon.in/equipment-and-accessories/sunglasses-15933?icm=HTSportpage&icn=dropdown_sunglasses&id=15933&type=c")
    if call.data == "Bottles":
        await call.message.answer(
            "https://www.decathlon.in/equipment-and-accessories/water-bottles-and-hydration-15717?icm=HTSportpage&icn=dropdown_waterbottle-and-backpacks&id=15717&type=c")


@dp.callback_query_handler(
    text=["Trekking Boots", "Trekking Backpack", "Travel backpack", "Winter Jackets", "Down Jackets", "Trekking Poles",
          "Travel Shirts", "Shorts", "Trousers", "Headlamps"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Trekking Boots":
        await call.message.answer("https://www.decathlon.in/footwear/hiking-and-trekking-boots-15651?id=15651&type=c")
    if call.data == "Trekking Backpack":
        await call.message.answer(
            "https://www.decathlon.in/backpacks/travel-and-trekking-backpack-15648?id=15648&type=c")
    if call.data == "Travel backpack":
        await call.message.answer(
            "https://www.decathlon.in/backpacks/travel-and-trekking-backpack-15648?id=15648&type=c")
    if call.data == "Winter Jackets":
        await call.message.answer(
            "https://www.decathlon.in/clothing/winter-jackets-and-down-jackets-15630?id=15630&type=c")
    if call.data == "Down Jackets":
        await call.message.answer(
            "https://www.decathlon.in/footwear/sandals-18235?icm=HTSportpage&icn=dropdown_sandals&id=18235&type=c")
    if call.data == "Trekking Poles":
        await call.message.answer(
            "https://www.decathlon.in/equipment-and-accessories/hiking-trekking-poles-15624?id=15624&type=c")
    if call.data == "Travel Shirts":
        await call.message.answer(
            "https://www.decathlon.in/backpacks/hiking-bags-and-backpack-15711?icm=HTSportpage&icn=dropdown_hiking-bags-and-backpacks&id=15711&type=c")
    if call.data == "Shorts":
        await call.message.answer("https://www.decathlon.in/clothing/pants-and-shorts-15690?id=15690&type=c")
    if call.data == "Trousers":
        await call.message.answer("https://www.decathlon.in/clothing/pants-and-shorts-15690?id=15690&type=c")
    if call.data == "Headlamps":
        await call.message.answer(
            "https://www.decathlon.in/equipment-and-accessories/headlamp-and-torch-15642?id=15642&type=c")


@dp.callback_query_handler(
    text=["Fitness Equipment", "Treadmills", "Cross Trainers", "Elliptical", "Exercise bikes", "Spin Bikes",
          "Rowing Machine", "Steppers", "Trampoline", "Cardio Apparel"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Fitness Equipment":
        await call.message.answer("https://www.decathlon.in/cardio-fitness/fitness-equipment-5732?id=5732&type=c")
    if call.data == "Treadmills":
        await call.message.answer("https://www.decathlon.in/fitness-equipment/treadmills-2625?id=2625&type=c")
    if call.data == "Cross Trainers":
        await call.message.answer(
            "https://www.decathlon.in/fitness-equipment/elliptical-and-cross-trainers-2629?id=2629&type=c")
    if call.data == "Elliptical":
        await call.message.answer(
            "https://www.decathlon.in/fitness-equipment/elliptical-and-cross-trainers-2629?id=2629&type=c")
    if call.data == "Exercise bikes":
        await call.message.answer("https://www.decathlon.in/fitness-equipment/exercise-bikes-2633?id=2633&type=c")
    if call.data == "Spin Bikes":
        await call.message.answer("https://www.decathlon.in/fitness-equipment/spin-bike-2637?id=2637&type=c")
    if call.data == "Rowing Machine":
        await call.message.answer("https://www.decathlon.in/fitness-equipment/rowing-machines-18439?id=18439&type=c")
    if call.data == "Steppers":
        await call.message.answer("https://www.decathlon.in/fitness-equipment/steps-steppers-2645?id=2645&type=c")
    if call.data == "Trampoline":
        await call.message.answer("https://www.decathlon.in/fitness-equipment/trampoline-18727?id=18727&type=c")
    if call.data == "Cardio Apparel":
        await call.message.answer(
            "https://www.decathlon.in/fitness-cardio-clothes/men-clothes-2672?icm=fitnesscardiosportpage&icn=mensgymapparelminibanner&id=2672&type=c")


@dp.callback_query_handler(
    text=["Gym Shorts", "Gym Track pants", "Men Tracksuits", "Women Gym suits", "Sports Bra", "Gym Tops",
          "Women fitness jacket"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Gym Shorts":
        await call.message.answer("https://www.decathlon.in/men-clothes/fitness-shorts-13436?id=13436&type=c")
    if call.data == "Gym Track pants":
        await call.message.answer("https://www.decathlon.in/men-clothes/fitness-track-pants-13442?id=13442&type=c")
    if call.data == "Men Tracksuits":
        await call.message.answer("https://www.decathlon.in/men-clothes/men-s-tracksuits-13445?id=13445&type=c")
    if call.data == "Women Gym suits":
        await call.message.answer("https://www.decathlon.in/fitness-cardio-clothes/women-clothes-2668?id=2668&type=c")
    if call.data == "Sports Bra":
        await call.message.answer("https://www.decathlon.in/women-clothes/fitness-sports-bra-2686?id=2686&type=c")
    if call.data == "Gym Tops":
        await call.message.answer("https://www.decathlon.in/women-clothes/fitness-tops-5735?id=5735&type=c")
    if call.data == "Women fitness jacket":
        await call.message.answer("https://www.decathlon.in/women-clothes/fitness-jackets-13451?id=13451&type=c")


@dp.callback_query_handler(
    text=["Tents", "Chairs", "Tables", "Furnitures", "Sleeping Bags", "Mattresses", "Camping Accessories", "Cooksets"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Tents":
        await call.message.answer("https://www.decathlon.in/camping/tents-shelters-15687?id=15687&type=c")
    if call.data == "Chairs":
        await call.message.answer("https://www.decathlon.in/camping/camping-furniture-15720?id=15720&type=c")
    if call.data == "Tables":
        await call.message.answer("https://www.decathlon.in/camping/camping-furniture-15720?id=15720&type=c")
    if call.data == "Furnitures":
        await call.message.answer("https://www.decathlon.in/camping/camping-furniture-15720?id=15720&type=c")
    if call.data == "Sleeping Bags":
        await call.message.answer(
            "https://www.decathlon.in/it-s-time-to-unfreeze/winter-accessories-21890?id=21890&type=c")
    if call.data == "Mattresses":
        await call.message.answer("https://www.decathlon.in/camping/sleeping-bag-and-mattress-15699?id=15699&type=c")
    if call.data == "Camping Accessories":
        await call.message.answer("https://www.decathlon.in/camping/camp-cooking-equipment-15708?id=15708&type=c")
    if call.data == "Cooksets":
        await call.message.answer("https://www.decathlon.in/camping/camp-cooking-equipment-15708?id=15708&type=c")


@dp.callback_query_handler(
    text=["Men Thermals", "Women Thermals", "Beanies", "Gloves", "Winter Accessories", "Warmers", "Junior Jackets",
          "Junior Beanies", "Ski jackets"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Men Thermals":
        await call.message.answer("https://www.decathlon.in/men-ski-clothing/men-thermals-10883?id=10883&type=c")
    if call.data == "Women Thermals":
        await call.message.answer("https://www.decathlon.in/women-ski-clothing/women-thermals-10943?id=10943&type=c")
    if call.data == "Beanies":
        await call.message.answer(
            "https://www.decathlon.in/ski-clothing-accessories/hats-beanies-and-headbands-10928?id=10928&type=c")
    if call.data == "Gloves":
        await call.message.answer(
            "https://www.decathlon.in/ski-clothing-accessories/gloves-and-mittens-5007?id=5007&type=c")
    if call.data == "Winter Accessories":
        await call.message.answer(
            "https://www.decathlon.in/it-s-time-to-unfreeze/winter-accessories-21890?id=21890&type=c")
    if call.data == "Warmers":
        await call.message.answer(
            "https://www.decathlon.in/p/8376613/warmers/introductory-set-of-2-x-hands-and-2-x-feet-warmers")
    if call.data == "Junior Jackets":
        await call.message.answer("https://www.decathlon.in/kids-ski-clothing/kids-ski-jackets-10910?id=10910&type=c")
    if call.data == "Junior Beanies":
        await call.message.answer(
            "https://www.decathlon.in/ski-clothing-accessories/hats-beanies-and-headbands-10928?id=10928&type=c")
    if call.data == "Ski jackets":
        await call.message.answer(
            "https://www.decathlon.in/men-ski-clothing/men-ski-jackets-10877?icm=WEDZESP&icn=Menskijackets&id=10877&type=c")


@dp.callback_query_handler(
    text=["Camo Tshirts", "Camo Trousers", "Camo Bermudas", "Camo Caps", "Gum Boots", "Binoculars", "Knifes", "Shelter",
          "Umbrellas", "Pouches"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Camo Tshirts":
        await call.message.answer("https://www.decathlon.in/camo-clothing/camo-t-shirts-shirts-18691?id=18691&type=c")
    if call.data == "Camo Trousers":
        await call.message.answer(
            "https://www.decathlon.in/camo-clothing/camo-trousers-bermuda-shorts-15005?id=15005&type=c")
    if call.data == "Camo Bermudas":
        await call.message.answer(
            "https://www.decathlon.in/camo-clothing/camo-trousers-bermuda-shorts-15005?id=15005&type=c")
    if call.data == "Camo Caps":
        await call.message.answer(
            "https://www.decathlon.in/camo-clothing/camo-caps-hats-gloves-belts-15008?id=15008&type=c")
    if call.data == "Gum Boots":
        await call.message.answer("https://www.decathlon.in/wildlife-watching/gumboots-shoes-2849?id=2849&type=c")
    if call.data == "Binoculars":
        await call.message.answer(
            "https://www.decathlon.in/camo-accessories/binoculars-spotting-scopes-14996?id=14996&type=c")
    if call.data == "Knifes":
        await call.message.answer("https://www.decathlon.in/camo-accessories/knives-multi-tool-15591?id=15591&type=c")
    if call.data == "Shelter":
        await call.message.answer("https://www.decathlon.in/camo-accessories/camo-shelters-14999?id=14999&type=c")
    if call.data == "Umbrellas":
        await call.message.answer("https://www.decathlon.in/camo-accessories/camo-shelters-14999?id=14999&type=c")
    if call.data == "Pouches":
        await call.message.answer(
            "https://www.decathlon.in/camo-accessories/camo-backpack-pockets-waist-bags-2868?id=2868&type=c")


@dp.callback_query_handler(
    text=["Bike Racks", "Cycles", "Mountain Bikes", "Hybrid Cycles", "Road Bikes", "Kids Cycle", "Cycle Accessories"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Bike Racks":
        await call.message.answer(
            "https://www.decathlon.in/cycling-accessories/car-racks-and-pannier-racks-18157?id=18157&type=c")
    if call.data == "Cycles":
        await call.message.answer("https://www.decathlon.in/cycling/cycles-18186?id=18186&type=c&id=1818618186&type=c")
    if call.data == "Mountain Bikes":
        await call.message.answer("https://www.decathlon.in/cycles/mountain-bikes-18188?id=18188&type=c")
    if call.data == "Hybrid Cycles":
        await call.message.answer("https://www.decathlon.in/cycling/cycles-18186?id=18186&type=c&id=1818618186&type=c")
    if call.data == "Road Bikes":
        await call.message.answer("https://www.decathlon.in/cycles/road-bikes-18192?id=18192&type=c")
    if call.data == "Kids Cycle":
        await call.message.answer("https://www.decathlon.in/cycles/kids-cycles-18187?id=18187&type=c")
    if call.data == "Cycle Accessories":
        await call.message.answer("https://www.decathlon.in/cycling/cycle-accessories-18153?id=18153&type=c")


@dp.callback_query_handler(
    text=["Fishing Rods", "Fishing Reels", "Hooks", "Lures", "Fishing lines", "Fishing Accessories",
          "Fishing Camp Furnitures", "Fishing ponchos", "Fishing GIlet"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Fishing Rods":
        await call.message.answer("https://www.decathlon.in/fishing/fishing-rods-15840?id=15840&type=c")
    if call.data == "Fishing Reels":
        await call.message.answer(
            "https://www.decathlon.in/fishing/fishing-reels-lines-15849?icn=fishing&icm=reels&linesminibanner=&id=15849&type=c")
    if call.data == "Hooks":
        await call.message.answer("https://www.decathlon.in/fishing/fishing-hooks-lures-15858?id=15858&type=c")
    if call.data == "Lures":
        await call.message.answer("https://www.decathlon.in/fishing/fishing-hooks-lures-15858?id=15858&type=c")
    if call.data == "Fishing lines":
        await call.message.answer(
            "https://www.decathlon.in/fishing/fishing-reels-lines-15849?icn=fishing&icm=reels&linesminibanner=&id=15849&type=c")
    if call.data == "Fishing Accessories":
        await call.message.answer(
            "https://www.decathlon.in/fishing/fishing-accessories-15864?icn=fishing&icm=fishingaccessoriesminibanner&id=15864&type=c")
    if call.data == "Fishing Camp Furnitures":
        await call.message.answer(
            "https://www.decathlon.in/p/968079/accessories/bedchair-fullbreak-carp-fishing?id=968079&type=p")
    if call.data == "Fishing ponchos":
        await call.message.answer(
            "https://www.decathlon.in/p/8384509/fishing-accessories/pocket-poncho-waterproof-fishing-poncho-dark-blue?id=8384509&type=p")
    if call.data == "Fishing GIlet":
        await call.message.answer(
            "https://www.decathlon.in/p/8384229/accessories/fishing-gilet-500-khakhi?id=8384229&type=p")


@dp.callback_query_handler(
    text=["Horse riding helmets", "Breeches", "Horse riding boots", "Horse riding gloves", "Leather saddle",
          "Cloth saddle"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Horse riding helmets":
        await call.message.answer(
            "https://www.decathlon.in/p/961392/extra-cover/100-horse-riding-helmet-black?id=961392&type=p")
    if call.data == "Breeches":
        await call.message.answer(
            "https://www.decathlon.in/p/8562331/horse-riding-breeches/100-horse-riding-jodhpurs-black?id=8562331&type=p")
    if call.data == "Horse riding boots":
        await call.message.answer(
            "https://www.decathlon.in/p/3568836/horse-riding-winter/schooling-adult-horse-riding-boots-black?id=3568836&type=p")
    if call.data == "Horse riding gloves":
        await call.message.answer(
            "https://www.decathlon.in/p/8520227/gloves/500-horse-riding-gloves-black?id=8520227&type=p")
    if call.data == "Leather saddle":
        await call.message.answer(
            "https://www.decathlon.in/p/8324691/horse-riding-saddles/paddock-horse-riding-all-purpose-175quote-adjustable-tree-leather-saddle-brown?id=8324691&type=p")
    if call.data == "Cloth saddle":
        await call.message.answer(
            "https://www.decathlon.in/p/8353087/saddle-pads/horse-pony-saddle-cloth-100-black?id=8353087&type=p")


@dp.callback_query_handler(
    text=["Swimming costumes", "Swimming cap", "Swimming goggles", "Towels", "Bathrobes", "Flipflops",
          "Swimming equipments", "Aqua learning", "Buoyancy aids"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Swimming costumes":
        await call.message.answer("https://www.decathlon.in/swimming/swimming-costumes-12782?id=12782&type=c")
    if call.data == "Swimming cap":
        await call.message.answer("https://www.decathlon.in/swimming-equipment/swim-caps-12791?id=12791&type=c")
    if call.data == "Swimming goggles":
        await call.message.answer(
            "https://www.decathlon.in/swimming-equipment/swimming-goggles-masks-12800?id=12800&type=c")
    if call.data == "Towels":
        await call.message.answer("https://www.decathlon.in/swimming-equipment/microfiber-towels-12797?id=12797&type=c")
    if call.data == "Bathrobes":
        await call.message.answer("https://www.decathlon.in/swimming-equipment/swimming-bathrobes-5633?id=5633&type=c")
    if call.data == "Flipflops":
        await call.message.answer("https://www.decathlon.in/surfing/flip-flop-beach-shoes-21199")
    if call.data == "Swimming equipments":
        await call.message.answer(
            "https://www.decathlon.in/swimming-equipment/swimming-equipment-s-accessories-21278?id=21278&type=c")
    if call.data == "Aqua learning":
        await call.message.answer("https://www.decathlon.in/swimming/aqua-learning-12773?id=12773&type=c")
    if call.data == "Buoyancy aids":
        await call.message.answer(
            "https://www.decathlon.in/buoyancy-aid-vests-and-boots/buoyancy-aids-and-boots-1909?id=1909&type=c")


@dp.callback_query_handler(
    text=["Football", "Football shoes", "Football bag", "Football Jersey", "Football shorts", "Football Socks",
          "Goal Posts", "Training accessories", "Goalkeeper Kit", "Football Equipment"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Football":
        await call.message.answer("https://www.decathlon.in/football/footballs-16058?id=16058&type=c")
    if call.data == "Football shoes":
        await call.message.answer("https://www.decathlon.in/football/football-shoes-16043?id=16043&type=c")
    if call.data == "Football bag":
        await call.message.answer("https://www.decathlon.in/football/football-bags-16073?id=16073&type=c")
    if call.data == "Football Jersey":
        await call.message.answer("https://www.decathlon.in/football/football-jersey-16085?id=16085&type=c")
    if call.data == "Football shorts":
        await call.message.answer("https://www.decathlon.in/football/football-shorts-16082?id=16082&type=c")
    if call.data == "Football Socks":
        await call.message.answer("https://www.decathlon.in/football/football-socks-21134?id=21134&type=c")
    if call.data == "Goal Posts":
        await call.message.answer("https://www.decathlon.in/football/football-goals-16055?id=16055&type=c")
    if call.data == "Training accessories":
        await call.message.answer("https://www.decathlon.in/football/football-training-16103?id=16103&type=c")
    if call.data == "Goalkeeper Kit":
        await call.message.answer("https://www.decathlon.in/football/goalkeeper-16061?id=16061&type=c")
    if call.data == "Football Equipment":
        await call.message.answer("https://www.decathlon.in/football/football-equipment-16088?id=16088&type=c")


@dp.callback_query_handler(
    text=["Tennis Cricket bat", "English Willow Bat", "Kids cricket bat", "Cricket ball", "Cricket accessories",
          "Adult cricket shoes", "Kids cricket shoes", "Cricket track pants", "Cricket jersey"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Tennis Cricket bat":
        await call.message.answer(
            "https://www.decathlon.in/cricket-bats-balls/tennis-cricket-bats-and-balls-21231?id=21231&type=c")
    if call.data == "English Willow Bat":
        await call.message.answer(
            "https://www.decathlon.in/cricket-bats-balls/leather-cricket-bats-and-balls-21233?id=21233&type=c")
    if call.data == "Kids cricket bat":
        await call.message.answer("https://www.decathlon.in/cricket-bats-balls/kids-cricket-bats-18220?id=18220&type=c")
    if call.data == "Cricket ball":
        await call.message.answer("https://www.decathlon.in/cricket-bats-balls/cricket-balls-22088?id=22088&type=c")
    if call.data == "Cricket accessories":
        await call.message.answer("https://www.decathlon.in/cricket/accessories-21874?id=21874&type=c")
    if call.data == "Adult cricket shoes":
        await call.message.answer("https://www.decathlon.in/cricket/accessories-21874?id=21874&type=c")
    if call.data == "Kids cricket shoes":
        await call.message.answer("https://www.decathlon.in/cricket-shoes/kids-cricket-shoes-17155?id=17155&type=c")
    if call.data == "Cricket track pants":
        await call.message.answer("https://www.decathlon.in/cricket-clothing/cricket-trackpants-21687?id=21687&type=c")
    if call.data == "Cricket jersey":
        await call.message.answer(
            "https://www.decathlon.in/cricket-clothing/cricket-t-shirts-jerseys-21686?id=21686&type=c")


@dp.callback_query_handler(
    text=["Board shorts", "Frisbee", "Surfboards", "Wetsuits", "Bodyboards", "Kites", "Snorkelling", "Scuba diving",
          "Kayaks", "Standup paddle"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Board shorts":
        await call.message.answer("https://www.decathlon.in/surfing/boardshorts-21194?id=21194&type=c")
    if call.data == "Frisbee":
        await call.message.answer("https://www.decathlon.in/all-sports/boomerang-frisbee-11063?id=11063&type=c")
    if call.data == "Surfboards":
        await call.message.answer("https://www.decathlon.in/surfing/surfboards-and-accessories-19096?id=19096&type=c")
    if call.data == "Wetsuits":
        await call.message.answer("https://www.decathlon.in/surfing/surf-shorties-and-wetsuits-19093?id=19093&type=c")
    if call.data == "Bodyboards":
        await call.message.answer("https://www.decathlon.in/all-sports/bodyboard-13169?id=13169&type=c")
    if call.data == "Kites":
        await call.message.answer("https://www.decathlon.in/all-sports/kites-landkites-11030?id=11030&type=c")
    if call.data == "Snorkelling":
        await call.message.answer(
            "https://www.decathlon.in/snorkeling-and-diving/masks-snorkels-and-fins-11969?id=11969&type=c")
    if call.data == "Scuba diving":
        await call.message.answer(
            "https://www.decathlon.in/snorkeling-and-diving/scuba-diving-gear-21126?id=21126&type=c")
    if call.data == "Kayaks":
        await call.message.answer("https://www.decathlon.in/kayak/kayaks-16927?id=16927&type=c")
    if call.data == "Standup paddle":
        await call.message.answer("https://www.decathlon.in/all-sports/stand-up-paddle-sup-13463?id=13463&type=c")


@dp.callback_query_handler(
    text=["Running shoes", "Jogging shoes", "Trail Running shoes", "Running Tshirts", "Running shorts",
          "Running Tights", "Running Accessories", "Sports watch", "Weighing scale", "Earphones"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Running shoes":
        await call.message.answer("https://www.decathlon.in/running-shoes/jogging-shoes-15098?id=15098&type=c")
    if call.data == "Jogging shoes":
        await call.message.answer("https://www.decathlon.in/running-shoes/jogging-shoes-15098?id=15098&type=cs")
    if call.data == "Trail Running shoes":
        await call.message.answer("https://www.decathlon.in/running-shoes/trail-running-shoes-15092?id=15092&type=c")
    if call.data == "Running Tshirts":
        await call.message.answer("https://www.decathlon.in/running-apparels/running-t-shirt-21858?id=21858&type=c")
    if call.data == "Running shorts":
        await call.message.answer("https://www.decathlon.in/running-apparels/running-shorts-21860?id=21860&type=c")
    if call.data == "Running Tights":
        await call.message.answer("https://www.decathlon.in/running-apparels/running-tights-21859?id=21859&type=c")
    if call.data == "Running Accessories":
        await call.message.answer("https://www.decathlon.in/accessories/jogging-accessories-15065?id=15065&type=c")
    if call.data == "Sports watch":
        await call.message.answer("https://www.decathlon.in/sports-accessories/sports-watches-17257?id=17257&type=c")
    if call.data == "Weighing scale":
        await call.message.answer("https://www.decathlon.in/electronics/weighing-scale-15074?id=15074&type=c")
    if call.data == "Earphones":
        await call.message.answer("https://www.decathlon.in/electronics/earphones-mp3-19315?id=19315&type=c")


@dp.callback_query_handler(
    text=["Golf clubs", "Golf trolleys", "Golf balls", "Golf accessories", "Polo Tshirts", "Golf Trouser", "Golf shoes",
          "Golf caps", "Golf shorts"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Golf clubs":
        await call.message.answer("https://www.decathlon.in/golf/golf-clubs-sets-1521?id=1521&type=c")
    if call.data == "Golf trolleys":
        await call.message.answer("https://www.decathlon.in/golf/golf-bags-trolleys-18847?id=18847&type=c")
    if call.data == "Golf balls":
        await call.message.answer("https://www.decathlon.in/golf/golf-balls-accessories-1575?id=1575&type=c")
    if call.data == "Golf accessories":
        await call.message.answer(
            "https://www.decathlon.in/golf-balls-accessories/golf-at-home-accessories-1587?id=1587&type=c")
    if call.data == "Polo Tshirts":
        await call.message.answer(
            "https://www.decathlon.in/golf-clothing-footwear/golf-polo-shirts-18679?id=18679&type=c")
    if call.data == "Golf Trouser":
        await call.message.answer(
            "https://www.decathlon.in/golf-clothing-footwear/golf-trousers-bermuda-shorts-18688?id=18688&type=c")
    if call.data == "Golf shoes":
        await call.message.answer("https://www.decathlon.in/fitness-equipment/rowing-machines-18439?id=18439&type=c")
    if call.data == "Golf caps":
        await call.message.answer("https://www.decathlon.in/golf-clothing-footwear/golf-belts-caps-1617?id=1617&type=c")
    if call.data == "Golf shorts":
        await call.message.answer(
            "https://www.decathlon.in/p/8575395/men-s-shorts/men-s-golf-shorts-mw500-turquoise?id=8575395&type=p&utm_medium=banner&utm_campaign=POTM_golfshorts")


@dp.callback_query_handler(
    text=["Skateboard", "Long boards", "Waveboard", "Skateboard shoes", "Skateboard accessories", "Kids scooters",
          "Adult scooters", "Spares", "Scooter helmets"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Skateboard":
        await call.message.answer(
            "https://www.decathlon.in/skateboard-longboards-waveboards/skateboards-collection-18574?id=18574&type=c")
    if call.data == "Long boards":
        await call.message.answer(
            "https://www.decathlon.in/skateboard-longboards-waveboards/longboard-cruiser-collection-18514?id=18514&type=c")
    if call.data == "Waveboard":
        await call.message.answer(
            "https://www.decathlon.in/skateboard-longboards-waveboards/waveboard-collection-18541?id=18541&type=c")
    if call.data == "Skateboard shoes":
        await call.message.answer(
            "https://www.decathlon.in/skateboard-longboards-waveboards/skateboard-shoes-18577?id=18577&type=c")
    if call.data == "Skateboard accessories":
        await call.message.answer(
            "https://www.decathlon.in/skateboard-longboards-waveboards/skateboard-accessories-18586?id=18586&type=c")
    if call.data == "Kids scooters":
        await call.message.answer("https://www.decathlon.in/all-sports/scooters-18262?id=18262&type=c")
    if call.data == "Adult scooters":
        await call.message.answer("https://www.decathlon.in/scooters/adult-kick-scooters-18283?id=18283&type=c")
    if call.data == "Spares":
        await call.message.answer("https://www.decathlon.in/scooters/scooter-spare-parts-18280?id=18280&type=c")
    if call.data == "Scooter helmets":
        await call.message.answer("https://www.decathlon.in/scooters/scooter-helmets-and-guards-18265?id=18265&type=c")


@dp.callback_query_handler(
    text=["Quad Roller skates", "Inline skates", "Kids Inline skates", "Adult Inline skates", "Skating Helmets",
          "Skating guards", "Skating bags", "Skating spares accessories"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Quad Roller skates":
        await call.message.answer(
            "https://www.decathlon.in/roller-inline-skates/quad-roller-skates-18304?id=18304&type=c")
    if call.data == "Inline skates":
        await call.message.answer(
            "https://www.decathlon.in/roller-inline-skates/inline-roller-skates-18352?id=18352&type=c")
    if call.data == "Kids Inline skates":
        await call.message.answer(
            "https://www.decathlon.in/inline-roller-skates/kid-s-inline-skates-18355?id=18355&type=c")
    if call.data == "Adult Inline skates":
        await call.message.answer(
            "https://www.decathlon.in/inline-roller-skates/adult-s-inline-skates-18358?id=18358&type=c")
    if call.data == "Skating Helmets":
        await call.message.answer(
            "https://www.decathlon.in/skating-helmets-and-guards/skating-helmets-18298?id=18298&type=c")
    if call.data == "Skating guards":
        await call.message.answer(
            "https://www.decathlon.in/skating-helmets-and-guards/skating-guards-18301?id=18301&type=c")
    if call.data == "Skating bags":
        await call.message.answer("https://www.decathlon.in/skate-bags-accessories/skating-bags-18292?id=18292&type=c")
    if call.data == "Skating spares accessories":
        await call.message.answer(
            "https://www.decathlon.in/skate-bags-accessories/spare-parts-wheels-screws-18367?id=18367&type=c")


@dp.callback_query_handler(
    text=["Men Sweaters", "Men Fleece Jacket", "Men Pullover", "Men Sweatshirt", "Men Hoodies", "Men Winter Coat",
          "Men Winter Jacket", "Men Puffer Jacket", "Men Down Jacket", "Men Snow Jacket", "Men Bomber Jacket",
          "Winter Shoes", "Men Winter Shoes", "Snow Socks", "Men Winter Outfits", "Men Winter Tshirt", "Men Thermals",
          "Men Warm Trouser"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Men Sweaters":
        await call.message.answer("https://www.decathlon.in/men-winter-collection/men-sweaters-22568?id=22568&type=c")
    if call.data == "Men Fleece Jacket":
        await call.message.answer("https://www.decathlon.in/men-sweaters/men-fleece-22571?id=22571&type=c")
    if call.data == "Men Pullover":
        await call.message.answer("https://www.decathlon.in/men-sweaters/men-pullover-22572?id=22572&type=c")
    if call.data == "Men Sweatshirt":
        await call.message.answer("https://www.decathlon.in/men-sweaters/men-sweatshirts-22569?id=22569&type=c")
    if call.data == "Men Hoodies":
        await call.message.answer("https://www.decathlon.in/men-sweaters/men-hoodies-22570?id=22570&type=c")
    if call.data == "Men Winter Coat":
        await call.message.answer("https://www.decathlon.in/men-winter-collection/men-jacket-22562?id=22562&type=c")
    if call.data == "Men Winter Jacket":
        await call.message.answer("https://www.decathlon.in/men-jacket/men-winter-jacket-22565?id=22565&type=c")
    if call.data == "Men Puffer Jacket":
        await call.message.answer("https://www.decathlon.in/men-jacket/men-puffer-jacket-22567?id=22567&type=c")
    if call.data == "Men Down Jacket":
        await call.message.answer("https://www.decathlon.in/men-jacket/men-down-jacket-22564?id=22564&type=c")
    if call.data == "Men Snow Jacket":
        await call.message.answer("https://www.decathlon.in/men-jacket/men-snow-jacket-22563?id=22563&type=c")
    if call.data == "Men Bomber Jacket":
        await call.message.answer("https://www.decathlon.in/men-jacket/men-heavy-winter-jacket-22566?id=22566&type=c")
    if call.data == "Winter Shoes":
        await call.message.answer(
            "https://www.decathlon.in/men-winter-collection/winter-shoes-22559?id=22559&type=chttps://www.decathlon.in/men-winter-collection/winter-shoes-22559?id=22559&type=c")
    if call.data == "Men Winter Shoes":
        await call.message.answer("https://www.decathlon.in/winter-shoes/men-winter-shoes-22561?id=22561&type=c")
    if call.data == "Snow Socks":
        await call.message.answer("https://www.decathlon.in/ski-clothing-accessories/winter-socks-5008?id=5008&type=c")
    if call.data == "Men Winter Outfits":
        await call.message.answer(
            "https://www.decathlon.in/men-winter-collection/men-winter-outfits-22555?id=22555&type=c")
    if call.data == "Men Winter Tshirt":
        await call.message.answer(
            "https://www.decathlon.in/men-winter-outfits/men-merino-outfits-22557?id=22557&type=c")
    if call.data == "Men Thermals":
        await call.message.answer("https://www.decathlon.in/men-winter-outfits/men-thermals-22556?id=22556&type=c")
    if call.data == "Men Warm Trouser":
        await call.message.answer("https://www.decathlon.in/men-winter-outfits/men-winter-pants-22558?id=22558&type=c")


@dp.callback_query_handler(
    text=["Women Sweaters", "Women Fleece Jacket", "Women Pullover", "Women Sweatshirt", "Women Jackets",
          "Women Winter Jacket", "Women Puffer Jacket", "Women Down Jacket", "Women Snow Jacket", "Women Bomber Jacket",
          "Women Snow Shoes", "Women Winter Outfits", "Women Thermals", "Women Warm Trouser"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Women Sweaters":
        await call.message.answer(
            "https://www.decathlon.in/women-winter-collection/women-sweaters-22544?id=22544&type=c")
    if call.data == "Women Fleece Jacket":
        await call.message.answer("https://www.decathlon.in/women-sweaters/women-fleece-22546?id=22546&type=c")
    if call.data == "Women Pullover":
        await call.message.answer("https://www.decathlon.in/women-sweaters/women-pullover-22545?id=22545&type=c")
    if call.data == "Women Sweatshirt":
        await call.message.answer("https://www.decathlon.in/women-sweaters/women-sweatshirts-22547?id=22547&type=c")
    if call.data == "Women Jackets":
        await call.message.answer(
            "https://www.decathlon.in/women-winter-collection/women-jackets-22548?id=22548&type=c")
    if call.data == "Women Winter Jacket":
        await call.message.answer("https://www.decathlon.in/women-jackets/women-winter-jacket-22550?id=22550&type=c")
    if call.data == "Women Puffer Jacket":
        await call.message.answer("https://www.decathlon.in/women-jackets/women-puffer-jackets-22551?id=22551&type=c")
    if call.data == "Women Down Jacket":
        await call.message.answer("https://www.decathlon.in/women-jackets/women-down-jacket-22549?id=22549&type=c")
    if call.data == "Women Snow Jacket":
        await call.message.answer("https://www.decathlon.in/women-jackets/women-snow-jackets-22552?id=22552&type=c")
    if call.data == "Women Bomber Jacket":
        await call.message.answer(
            "https://www.decathlon.in/women-jackets/women-heavy-winter-jackets-22553?id=22553&type=ct")
    if call.data == "Women Snow Shoes":
        await call.message.answer("https://www.decathlon.in/winter-shoes/women-winter-shoes-22560?id=22560&type=c")
    if call.data == "Women Winter Outfits":
        await call.message.answer(
            "https://www.decathlon.in/women-winter-outfits/women-merino-outfits-22576?id=22576&type=c")
    if call.data == "Women Thermals":
        await call.message.answer("https://www.decathlon.in/women-winter-outfits/women-thermals-22575?id=22575&type=c")
    if call.data == "Women Warm Trouser":
        await call.message.answer(
            "https://www.decathlon.in/women-winter-outfits/women-winter-pants-22577?id=22577&type=c")


@dp.callback_query_handler(
    text=["Kids Sweater", "Kids Winter Jacket", "Kids Thermals", "Kids Beanies", "Kids Winter Accessories",
          "Winter Caps", "Winter Gloves", "Neckwarmer", "Sunglasses", "Sleeping bags", "Warmers", "Snowshoeing",
          "Insulated Bottles"])
async def random_value(call: types.CallbackQuery):
    await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
    response_text = f""" You have Selected {call.data}.
This is the link for {call.data}: """
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_squash_collections.mp3', 'wb') as f:
        f.write(response_byte_audio)
    await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_squash_collections.mp3', 'rb'))
    await call.message.answer(f""" You have Selected {call.data}.
This is the link for {call.data}: """)
    if call.data == "Kids Sweater":
        await call.message.answer("https://www.decathlon.in/kids-tops/kids-fleeces-and-pullovers-17080?id=17080&type=c")
    if call.data == "Kids Winter Jacket":
        await call.message.answer("https://www.decathlon.in/kids-tops/kids-jackets-17077?id=17077&type=c")
    if call.data == "Kids Thermals":
        await call.message.answer("https://www.decathlon.in/kids-underwear/kids-base-layer-17134?id=17134&type=c")
    if call.data == "Kids Beanies":
        await call.message.answer("https://www.decathlon.in/junior-beanies-22032?id=22032&type=c")
    if call.data == "Kids Winter Accessories":
        await call.message.answer("https://www.decathlon.in/junior-winter-accessories-22027?id=22027&type=cs")
    if call.data == "Winter Caps":
        await call.message.answer(
            "https://www.decathlon.in/ski-clothing-accessories/hats-beanies-and-headbands-10928?id=10928&type=c")
    if call.data == "Winter Gloves":
        await call.message.answer(
            "https://www.decathlon.in/ski-clothing-accessories/gloves-and-mittens-5007?id=5007&type=c")
    if call.data == "Neckwarmer":
        await call.message.answer(
            "https://www.decathlon.in/ski-clothing-accessories/neck-warmers-10931?id=10931&type=c")
    if call.data == "Sunglasses":
        await call.message.answer("https://www.decathlon.in/sports-sunglasses/sunglasses-17317?id=17317&type=c")
    if call.data == "Sleeping bags":
        await call.message.answer("https://www.decathlon.in/sleeping-bags-22035?id=22035&type=c")
    if call.data == "Warmers":
        await call.message.answer("https://www.decathlon.in/protection-and-accessories/warmers-19918?id=19918&type=c")
    if call.data == "Snowshoeing":
        await call.message.answer("https://www.decathlon.in/snowshoeing-22077?id=22077&type=c")
    if call.data == "Insulated Bottles":
        await call.message.answer(
            "https://www.decathlon.in/equipment-and-accessories/water-bottles-and-hydration-15717?icm=HTSportpage&icn=dropdown_waterbottle-and-backpacks&id=&type=c")


@dp.callback_query_handler(
    text=["Badminton", "Tennis", "Table Tennis", "Squash", "Hiking", "Trekking", "Cardio", "Gym Tracks", "Camping",
          "Skiing", "Wildlife", "Cycle", "Road Cycle", "MTB Cycle", "Fishing", "Horse Riding", "Swimming", "FootBall",
          "Cricket", "Surfing", "Running", "Golf", "SkateBoard", "Roller skating", "Men Winter Collections",
          "Women Winter Collection", "Kids Winter Collection & Winter Accessories"])
async def random_value(call: types.CallbackQuery):
    options_mapping = {
        "Badminton": ("Badminton", keyboard_inline_1),
        "Tennis": ("Tennis", keyboard_inline_2),
        "Table Tennis": ("Table Tennis", keyboard_inline_3),
        "Squash": ("Squash", keyboard_inline_4),
        "Hiking": ("Hiking", keyboard_inline_5),
        "Trekking": ("Trekking", keyboard_inline_6),
        "Cardio": ("Cardio", keyboard_inline_7),
        "Gym Tracks": ("Gym Tracks", keyboard_inline_8),
        "Camping": ("Camping", keyboard_inline_9),
        "Skiing": ("Skiing", keyboard_inline_10),
        "Wildlife": ("Wildlife", keyboard_inline_11),
        "Cycle": ("Cycle", keyboard_inline_12),
        "Road Cycle": ("Road Cycle", keyboard_inline_13),
        "MTB Cycle": ("MTB Cycle", keyboard_inline_14),
        "Fishing": ("Fishing", keyboard_inline_15),
        "Horse Riding": ("Horse Riding", keyboard_inline_16),
        "Swimming": ("Swimming", keyboard_inline_17),
        "FootBall": ("FootBall", keyboard_inline_18),
        "Cricket": ("Cricket", keyboard_inline_19),
        "Surfing": ("Surfing", keyboard_inline_20),
        "Running": ("Running", keyboard_inline_21),
        "Golf": ("Golf", keyboard_inline_22),
        "SkateBoard": ("SkateBoard", keyboard_inline_23),
        "Roller skating": ("Roller Skating", keyboard_inline_24),
        "Men Winter Collections": ("Men's Winter Collections", keyboard_inline_25),
        "Women Winter Collection": ("Women's Winter Collection", keyboard_inline_26),
        "Kids Winter Collection & Winter Accessories": ("Kids' Winter Collection & Winter Accessories", keyboard_inline_27),
    }

    if call.data in options_mapping:
        option_text, option_keyboard = options_mapping[call.data]
        await bot.send_chat_action(chat_id=call.message.chat.id, action=types.ChatActions.TYPING)
        response_text = f"You have selected {option_text}. Here is the list of items under {option_text}."
        response_byte_audio = voice.generate_audio_bytes(response_text)

        with open('response_elevenlabs.mp3', 'wb') as f:
            f.write(response_byte_audio)

        await bot.send_voice(chat_id=call.message.chat.id, voice=open('response_elevenlabs.mp3', 'rb'))
        await call.message.answer(response_text, reply_markup=option_keyboard)



@dp.message_handler(commands=['start', 'help', 'Restart'])
async def welcome(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action=types.ChatActions.TYPING)
    response_text = """Hello, Welcome to Decathlon Bot
    
    I can help you for Shopping in Decathlon. If you are new to the Bot, Please see the manual.

You can control me by sending these commands:
/start - start to place the new order
/Items - displays list of items in Decathlon
            """
    response_byte_audio = voice.generate_audio_bytes(response_text)

    with open('response_elevenlabs.mp3', 'wb') as f:
        f.write(response_byte_audio)

    await bot.send_voice(chat_id = message.chat.id , voice=open('response_elevenlabs.mp3', 'rb'))
    await message.answer("Hello, Welcome to Decathlon Bot ", reply_markup=keyboard1)
    await message.answer("""I can help you for Shopping in Decathlon. If you are new to the Bot, Please see the manual.

    You can control me by sending these commands:
    /start - start to place the new order
    /Items - displays list of items in Decathlon
                """)

@dp.message_handler(commands=['OfficialWebsite'])
async def welcome(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action=types.ChatActions.TYPING)
    response_text = """ This is official Website of Decathlon, Click on the Link below to go into Decathlon website: """
    response_byte_audio = voice.generate_audio_bytes(response_text)

    with open('response_elevenlabs.mp3', 'wb') as f:
        f.write(response_byte_audio)

    await bot.send_voice(chat_id=message.chat.id, voice=open('response_elevenlabs.mp3', 'rb'))
    await message.answer(""" This is official Website of Decathlon, Click on the Link below to go into Decathlon website: """)
    await message.answer("https://www.decathlon.in/")



@dp.message_handler(commands=['Items'])
async def random_answer(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action=types.ChatActions.TYPING)
    response_text = """ You have entered items tag 
     Select Items Category below: """
    response_byte_audio = voice.generate_audio_bytes(response_text)

    with open('response_elevenlabs.mp3', 'wb') as f:
        f.write(response_byte_audio)

    await bot.send_voice(chat_id=message.chat.id, voice=open('response_elevenlabs.mp3', 'rb'))
    await message.answer("""You have entered items tag 
    Select Items Category below: """, reply_markup=keyboard_inline)


@dp.message_handler()
async def kb_answer(message: types.Message):
    await bot.send_chat_action(chat_id=message.chat.id, action=types.ChatActions.TYPING)
    response_text = """Hello, Welcome to Decathlon Bot

        I can help you for Shopping in Decathlon. If you are new to the Bot, Please see the manual.

    You can control me by sending these commands:
    /start - start to place the new order
    /Items - displays list of items in Decathlon
                """
    response_byte_audio = voice.generate_audio_bytes(response_text)

    with open('response_elevenlabs.mp3', 'wb') as f:
        f.write(response_byte_audio)

    await bot.send_voice(chat_id=message.chat.id, voice=open('response_elevenlabs.mp3', 'rb'))
    await message.answer("Hello! Welcome to Decathlon Chatbot!")
    await message.answer("""I can help you for Shopping in Decathlon. If you are new to the Bot, Please see the manual.

    You can control me by sending these commands:
    /start - start to place the new order
    /Items - displays list of items in Decathlon
                """)


executor.start_polling(dp)