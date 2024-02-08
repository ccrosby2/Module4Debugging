#Cierra Crosby
#2/7/2024
#Instructor Antonio Tovar
#This program create a collection of these authors and prints a statement for the year they decease.
#This program also print the collection in the following format: "Charles Dickens died in 1870."
#The program prints the following famous people and the year the decease Charles Dickens 1870,  William Thackeray 1863,  Anthony Trollope, 1882, and Gerard Manley Hopkins 1889

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}
for author, date in authors.items():
    print( "%s" % author + " died in " + "%s" % date)

