define role1 = Character('标题', color="#ffffff", image="role1",kind=nvl)
define role2 = Character('“我”', color="#c8c8ff", image="role2")
define quote = Character(None,kind=nvl)
define narrator_nvl = Character(None, kind=nvl,color="white")
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label start:
scene white
quote "In the evening, the sun bid farewell to Beijing, and they reluctantly held the last horizontal line. In this world, man and beasts coexist, light and darkness dances together"
with Pause(3)
with dissolve


narrator_nvl "Chapter 1"
with Pause(3)
narrator_nvl "On February 22, the police reported a suicide. Fourteen days later, the diary of a police officer involved in the case was leaked online:"
narrator_nvl "At around 19:00 on February 21, a man committed suicide by jumping from an overpass. It is reported that the man’s name is Tang Lin, who was born in 2007 and is 35 years old this year. The motive is still unclear. According to on-site surveillance"
narrator_nvl "the possibility of homicide or abetment to suicide has been ruled out. We are trying to contact his family members."
narrator_adv "At 8 o\'clock on February 22, the man\'s family members rushed to the hospital."
narrator_adv "They did not dare to enter the ward. The two of them muttered to themselves and had no idea what to say. Later, they conducted an interview with the man\'s family members, but it did not go well and will be announced later."
narrator_adv "At 17:00 on February 22, Tang Lin was confirmed dead and moved to the morgue, awaiting cremation."
narrator_adv "At 19:00 on February 22, the man\'s parents appeared in a funeral shop, some money was left to the shop owner. At around 20:00, the two committed suicide by lying on the train track."
narrator_adv "On February 29, Tang Lin\'s funeral was held."

role2 "I sat at my computer desk, scrolling the mouse, browsing all this."
scene room
role2 "In the afternoon, drizzle falls on the corner of the street. People are like mushrooms growing out of the soil. The only way to identify cars at the intersection is the elongated red glass shards."
role2 "I opened the drawer and pulled out a stack of documents, a diary book on top displays: My Diary -Tang Lin"
narrator_adv "The book cover on the side of this diary says 2025-2042. This is a notebook that seems to record 18 years. It looks like it is used to record a baby\'s growth into adulthood. The cowhide cover looks very heavy, and many pages are filled with words. I decided to start from the beginning and take my time."
narrator_adv "Dear Diary, today is January 1, 2025, my mother gave this book as my birthday gift. She hoped that I could record the story starting from the age of eighteen, and thats why I am writing on this book. So where do I start? Oh, by the way, I will be eighteen years old in September this year, and the college entrance examination is six months away. Well, I’d better concentrate on preparing for the college entrance examination in these few months."
narrator_adv "June 17, 2025, the college entrance examination finally ended. Does this mean that my school life is over? By the way, I did well in the college entrance examination. I failed to solve the last mathematics question.Its really a shame because even Wang Ze finished it, I was obviously much better than him normally, but I practiced 100 questions like this before the exam, which was really a pity. As for Chinese, my essay might not link to the main idea, well, I am sure it will be considered correct. I can usually read English correctly, but this time it took me a long time to read. Maybe I was too nervous."
narrator_adv "June 18, 2025, I often see a black mass appearing in my life, or more accurately in my dream, but I didn’t know what kind of black it was. Well actually, I discovered it a few days ago, but I decided to write it down today. I\'m planning to go to the amusement park and play pirate ship the following days."
role2 "I continued to browse Tang Lin’s diary. There were obvious ripping marks on some pages, but most of them were intact. From 2025 to 2029 was the period when he was in college. From the book, I knew that Tang Lin was studying Foundation of Mathematics, so I intercepted these more interesting contents."
narrator_adv "Before that, I made the following judgment about Tang Lin\'s life trajectory. His way of cognizing things is different from ordinary people. It seems that he realized some key elements of human nature later than ordinary people. The obvious change was at the age of 18. Back then, between the ages of 18 and 35, he realized some of the things he had before the age of eighteen, and at the same time, he started to ponder, deduce, or developed the state of mind that people have from middle age to old age. In short, his life was chaotic."
narrator_adv "March 2nd, 2027, I was riding on the bicycle path of the university, and a person passed me by. I didn’t notice her because I was obsessed with thinking about the proof of Fermat’s last theorem, but I smelled her. The smell of her hair was full of distilled alcohol and spices. It was perfume. I love her hair, I love how she smells, everything is so fresh. I wanted to turn around and look, but it was too dangerous and I was scared, but I still missed her. Also, I am starting to have some understanding of the word \"love\". I feel my heart beating wildly. Does it mean that when a person sees a person\'s heart beating wildly, he loves her? Fear can also drive the heart. I can\'t tell whether I love her or not. Whether her feelings are love or fear, in short, she smells good."
narrator_adv "I met her again on March 7, 2027, in the school library. There was no exam approaching at that time, so there were very few people in the library, but going to the library has become my habit. I saw her wandering next to the science fiction column. She constantly picks up books from the bookshelf and puts them back. I saw \"Flowers for Algernon\", \"Galactic Empire\" and \"Back To The Moon\". When I got back, I had read all these books. I should let her get one."
narrator_adv "March 12th, 2027. Maybe my memory is wrong. The \"she\" may need to be changed to \"he\". I only know that \"he\" has a moderate length hair and smells good, but shouldn\'t only women wear perfume? But it doesn\'t matter anymore. I recently saw him holding a copy of \"Steppenwolf\" and I immediately went to the library and borrowed the book. I want myself to read this book every night, hopefully."
narrator_adv "September 14th, 2027, \"Solitude is independence. It had been my wish and with the years I had attained it. It was cold. Oh, cold enough! But it was also still, wonderfully still and vast like the cold stillness of space in which the stars revolve.\" I almost forgot the reason I read  Steppenwolf. Maybe it\'s because of him, but now I\'m obsessed with Steppenwolf, I wander around society like Steppenwolf, I live like Steppenwolf. But why do I say this? These sentences are beautiful."
narrator_adv "On July 19, 2028, I no longer loved him, how dare he talks loudly in the library! I hate people like this. My mother told me that homosexuality was dirty. She also scolded me and said I was disgusting. I didn\'t dare to love him anymore. By the way, I graduated and decided to take the postgraduate entrance examination. Wish me luck"
role2 "During this period, Tang Lin seemed to have just gained a preliminary understanding of gender, literature, and love. According to a psychological evaluation test conducted by the university, Tang Lin in 2028 had all the mental maturity of a college student. But through interviews with their parents, we discovered some problems. Here is the following:"
