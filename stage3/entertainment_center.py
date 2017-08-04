import media
import fresh_tomatoes

movies = []

######## Create instances of the class movie and store them in themovie list #######

toy_story = media.Movie ("Toy Story",
						 "A story about a boy and his toys that come to life",
						 "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						 "https://www.youtube.com/watch?v=vwyZH85NQC4")

movies.append(toy_story)

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "http://www.youtube.com/watch?v=-9ceBgWV8io")

movies.append(avatar)

terminator = media.Movie ("Terminator",
						  "a cyborg assassin is sent back in time to kill Sarah Connor",
						  "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg",
						  "https://www.youtube.com/watch?v=c4Jo8QoOTQ4")

movies.append(terminator)

good_morning_vietnam = media.Movie ("good morning vietnam",
						  			"A story about a radio DJ during the vietnam war",
						  			"https://upload.wikimedia.org/wikipedia/en/d/d0/Good_Morning%2C_Vietnam.jpg",
						  			"https://www.youtube.com/watch?v=3mJoHqmtFcQ")

movies.append(good_morning_vietnam)

mad_max = media.Movie ("Mad Max",
					"A vengeful policeman becomes embroiled in a feud with a vicious motorcycle gang",
					"https://upload.wikimedia.org/wikipedia/en/5/5a/MadMazAus.jpg",
					"https://www.youtube.com/watch?v=caHnaRq8Qlg")

movies.append(mad_max)

apocalypse_now = media.Movie ("Apocalypse Now",
					"A secret mission to assassinate Colonel Kurtz, a renegade who is presumed insane",
					"https://upload.wikimedia.org/wikipedia/en/c/c2/Apocalypse_Now_poster.jpg",
					"https://www.youtube.com/watch?v=0HEiqAsrVMQ")

movies.append(apocalypse_now)

et = media.Movie ("E.T",
				  "A baby Alien lost on earth",
				  "https://upload.wikimedia.org/wikipedia/en/6/66/E_t_the_extra_terrestrial_ver3.jpg",
			      "https://www.youtube.com/watch?v=_7-2PB4jj2o")

movies.append(et)

dead_poets_society = media.Movie ("Dead Poets Society",
				  				  "The story of an English teacher who inspires his students through his teaching of poetry",
				  				  "https://upload.wikimedia.org/wikipedia/en/4/49/Dead_poets_society.jpg",
			      				  "https://www.youtube.com/watch?v=wrBk780aOis")

movies.append(dead_poets_society)

Lethal_weapon = media.Movie ("Lethal weapon",
				  			"A pair of mismatched LAPD detectives work together as partners",
				  			"https://upload.wikimedia.org/wikipedia/en/d/d9/Lethal_weapon1.jpg",
			      			"https://www.youtube.com/watch?v=bKeW-MGu-qQ")

movies.append(Lethal_weapon)


#### Produce fresh_tomatoes.html file which will be created in the current directory #####

fresh_tomatoes.open_movies_page(movies)

