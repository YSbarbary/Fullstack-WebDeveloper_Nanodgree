import fresh_tomatoes
# fresh_tomatoes is the html file for the movie trailers website
import media
# movies instances
Toy_Story = media.Movie("Toy Story 3",
                        "A story of a boy and his toys that come to life",
                        "Lee Unkrich",
                        "John Lasseter (story), Andrew Stanton (story)",
                        "Tom Hanks, Tim Allen, Joan Cusack",
                        "8.4",
                        "http://ia.media-imdb.com/images/"
                         "M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

Avatar = media.Movie("Avatar",
                     "A marine on an alient planet",
                     "James Cameron",
                     "James Cameron",
                     "Sam Worthington, Zoe Saldana, Sigourney Weaver",
                     "7.9",
                     "http://goo.gl/cbYLTi",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

Beauty_and_the_Beast = media.Movie("Beauty and the Beast",
                                   "Can She Lift the Curse on His Life?",
                                   "Masakazu Higuchi, Chinami Namba",
                                   "Jacob Grimm",
                                   "Susan Silo",
                                   "5.7",
                                   "http://goo.gl/NMkjAi",
                                   "https://www.youtube.com/watch?v=tRlzmyveDHE")

Lion_King = media.Movie("Lion King",
                        "Will the King Return to Pride Rock?",
                        "Roger Allers, Rob Minkoff",
                        "Irene Mecchi , Jonathan Roberts ",
                        "Matthew Broderick, Jeremy Irons",
                        "8.5",
                        "http://goo.gl/RVJscY",
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")

UP = media.Movie("UP",
                 "Loves goes on a great adventure",
                 "Pete Docter, Bob Peterson",
                 "Pete Docter, Bob Peterson",
                 "Edward Asner, Jordan Nagai, John Ratzenberger",
                 "8.3",
                 "https://goo.gl/UoH0DM",
                 "https://www.youtube.com/watch?v=ORFWdXl_zJ4")

Finding_Nemo = media.Movie("Finding_Nemo",
                           "An adventure at sea",
                           "Andrew Stanton, Lee Unkrich",
                           "Andrew Stanton , Andrew Stanton",
                           "Albert Brooks, Ellen DeGeneres, Alexander Gould",
                           "8.2",
                           "http://goo.gl/EBzM09",
                           "https://www.youtube.com/watch?v=gcwv1Gflh4Q")
# movies Array
movies = [Toy_Story, Avatar, Beauty_and_the_Beast, Lion_King, UP, Finding_Nemo]

fresh_tomatoes.open_movies_page(movies)
