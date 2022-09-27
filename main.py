# ------------------------------------------------------
#        Name:  Linh Pham
#       Peers: N/A
#  References: N/A
# ------------------------------------------------------
import distributor
from random import randint

#######################################################################
## Testing Area
test_mode = False


def myTests():
    printHeaderOrder()
    pass


#######################################################################


def getRandomCitation(library: list) -> str:
    """ This function selects a book at random from the library and returns the citation information for that book.
  :param library:(list) a list of books in the library
  :return :(str) a random book

  >>>getRandomCitation(library)
  Jon Meacham. Voices in Our Blood: America's Best on the  Civil Rights Movement. Random House Publishing Group, 576,   Jan-03.
  """
    # for i in range (len(library)):
    num = randint(1, len(library) - 1)
    title = library[num]['title']
    authors = library[num]['authors']
    publisher = library[num]['publisher']
    pages = library[num]['pages']
    pubdate = library[num]['pubdate']
    inf = getCitationInformation(title, authors, publisher, pages, pubdate)
    return inf


def printLibrary(library: list) -> None:
    """ This function prints out the citation information for each book in the library in order. 
      For each book, an index (starting at 1) should first be printed prior to the citation information.  
  :param library:(list) a list of books in the library
  :return :(None) the citation information for each book in the library in order
  
  >>>printLibrary(library)
  1 Yvonne Vera. Opening Spaces: An Anthology of Contemporary African Women's Writing. Heinemann, Sep-99, 186
2 The Caine Prize for African Writing. The Caine Prize for African Writing 2010: 11th Annual Collection. New Internationalist, Aug-10, 208
3 Roger D. Abrahams. African Folktales. Knopf Doubleday Publishing Group, Aug-83, 207
4 Vincent Carretta. Unchained Voices: An Anthology of Black Authors in the English-Speaking World of the Eighteenth Century. University Press of Kentucky, Dec-03, 416
  """
    for books in library:
      print(str(library.index(books)) + " " + getCitationInformation(books))
    pass


def removeBook(library: list, index: int) -> None:
    """ This function removes the entry at the index specified from the library list. 
      The indexes 1..n appear when the user selects the PRINT operation.
  :param library:(list) the list of books in the library
  :return : None

  >>>my_library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel Myerson', 'authors': 'Joel Myerson, Joel Myerson', 
  'publisher': 'Oxford University Press, USA', 'pubdate': 'Dec-00', 'pages': '752'}, 
  {'title': 'Bombshells: War Stories and Poems by Women on the Homefront', 'firstAuthor': 'Missy Martin', 'authors': 'Missy Martin (Editor), 
  Jesse Loren', 'publisher': 'OmniArts, LLC', 'pubdate': 'Jan-07', 'pages': '163'}, {'title': 'Imagination And Spirit', 
  'firstAuthor': 'J. Brent Bill', 'authors': 'J. Brent Bill (Editor), Shari Pickett Veach (Designed by), C. Michael Curtis (Foreword by), 
  J. Brent Bill', 'publisher': 'Friends United Press', 'pubdate': 'Feb-06', 'pages': '292'}]
  >>>removeBook(my_library, 2)
  # the book#2 is removed from list
  """
    if index in range(1, len(library) + 1):
        try:
            library.remove(library[index - 1])
        except IndexError:
            print("Sorry, can't pop that.")
    return
    pass


def createBookDictionary(title: str, firstAuthor: str, authors: str,
                         publisher: str, pubdate: str, pages: str) -> dict:
    """ This function takes in the information for title, firstAuthor, authors, publisher, pages, and pubdate, 
      all as strings. The function creates a dictionary for the book with the following keys: 
      'title', 'firstAuthor', 'authors', 'publisher', 'pubdate', 'pages'. 
      Returns a dictionary holding the information for one book.
  :param title, firstAuthor, authors, publisher, pubdate, pages:(str) the values in the book
  :return : a dictionary for the book

  >>>createBookDictionary("Opening Spaces: An Anthology of Contemporary African Women's Writing", "Yvonne Vera" ,"Yvonne Vera (Editor)", "Heinemann", "Sep-99", "186")
  {'title': "Opening Spaces: An Anthology of Contemporary African Women's Writing", 'firstAuthor': 'Yvonne Vera', 'authors': 'Yvonne Vera (Editor)', 'publisher': 'Heinemann', 'pubdate': 'Sep-99', 'pages': '186'}
  """
    book_dict = {}
    book_dict['title'] = title
    book_dict['firstAuthor'] = firstAuthor
    book_dict['authors'] = authors
    book_dict['publisher'] = publisher
    book_dict['pubdate'] = pubdate
    book_dict['pages'] = pages
    return book_dict

    for key, value in book_dict.items():
        print(key, value)


def addBook(library: list, book: dict) -> None:
    """ This function adds a book dictionary to the library list.
  :param library, book:(list, dict) the library list
  :return :None (the list with one more book dictionary)

  >>>my_library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel Myerson', 'authors': 'Joel Myerson, Joel Myerson', 
  'publisher': 'Oxford University Press, USA', 'pubdate': 'Dec-00', 'pages': '752'}, 
  {'title': 'Bombshells: War Stories and Poems by Women on the Homefront', 'firstAuthor': 'Missy Martin', 'authors': 'Missy Martin (Editor), 
  Jesse Loren', 'publisher': 'OmniArts, LLC', 'pubdate': 'Jan-07', 'pages': '163'}, {'title': 'Imagination And Spirit', 
  'firstAuthor': 'J. Brent Bill', 'authors': 'J. Brent Bill (Editor), Shari Pickett Veach (Designed by), C. Michael Curtis (Foreword by), 
  J. Brent Bill', 'publisher': 'Friends United Press', 'pubdate': 'Feb-06', 'pages': '292'}]
  >>>rand_book = {'title': "Opening Spaces: An Anthology of Contemporary African Women's Writing", 'firstAuthor': 'Yvonne Vera', 'authors': 'Yvonne Vera (Editor)', 'publisher': 'Heinemann', 'pubdate': 'Sep-99', 'pages': '186'}
  >>>addBook(my_library, rand_book)
  None
  #the book is added to the list
  """
    library.append(book)
    print ("Your book has been added!")
    pass


def setupLibrary(numBooks: int) -> list:
    """ This function sets up the book library to store all your books. numBooks is the number of books 
      the user wants to have initialized in the library, in the range of 0..100. 
      Returns the newly created library. If numBooks is zero, this function should return an empty list.
  :param numBooks:(int) the number of books the user wants to have initialized in the library
  :return :(list) the newly created library

  >>>setupLibrary(18)
  [{'title': 'The Complete Works of Kate Chopin', 'author': 'Kate Chopin', 'authors': 'Kate Chopin, Per Seyersted (Editor), Edmund Wilson', 'publisher': 'Louisiana State University Press', 'pages': '1032', 'pubdate': 'May-06'}]
  """
    # def getRandomBook():
    #   num = randint(1,len(book_list)-1)
    #   return book_list[num]
    book_list = []
    random_book = {}
    # dictionary_keys = ['title', 'author', 'authors', 'publisher', 'pages', 'pubdate']
    while numBooks != 0:
        book = distributor.getRandomBook()
        title = book[0]
        author = book[1]
        authors = book[2]
        publisher = book[5]
        pages = book[7]
        pubdate = book[6]
        random_book['title'] = title
        random_book['author'] = author
        random_book['authors'] = authors
        random_book['publisher'] = publisher
        random_book['pages'] = pages
        random_book['pubdate'] = pubdate
        book_list.append(random_book)
        return book_list
    else:
        return []


def getTitles(library: list) -> list:
    """ This function returns a list of the book titles in the library, sorted in alphabetical order.
  :param library:(list) a list of books in the library
  :return :(list) a list of the book titles in the library, sorted in alphabetical order
  
  >>> my_library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel Myerson', 'authors': 'Joel Myerson, Joel Myerson', 
  'publisher': 'Oxford University Press, USA', 'pubdate': 'Dec-00', 'pages': '752'}, 
  {'title': 'Bombshells: War Stories and Poems by Women on the Homefront', 'firstAuthor': 'Missy Martin', 'authors': 'Missy Martin (Editor), 
  Jesse Loren', 'publisher': 'OmniArts, LLC', 'pubdate': 'Jan-07', 'pages': '163'}, {'title': 'Imagination And Spirit', 
  'firstAuthor': 'J. Brent Bill', 'authors': 'J. Brent Bill (Editor), Shari Pickett Veach (Designed by), C. Michael Curtis (Foreword by), 
  J. Brent Bill', 'publisher': 'Friends United Press', 'pubdate': 'Feb-06', 'pages': '292'}]
  >>> print(getTitles(my_library))
  ['Bombshells: War Stories and Poems by Women on the Homefront', 'Imagination And Spirit', 'Transcendentalism: A Reader']
  """
    book_titles = []
    for i in range(len(library)):
        titles = library[i]['title']
        book_titles.append(titles)
        book_titles.sort()
    return book_titles


def saveToFile(library: list, saveAll: bool, file_name: str) -> None:
    """ This function writes library data to a file based on the given file name.
      It either writes the titles in the library when saveAll is False or
      the formatted output when saveAll is True.
  :param library, saveAll, file_name:(list, bool, str)  the list of books in the library, the file, and a boolean expression to make the function either write the titles in the library when saveAll is False or the formatted output when saveAll is True.
  :return : None
  #the data is written into a file.
  
  >>> my_library = [{'title': 'Transcendentalism: A Reader', 'firstAuthor': 'Joel Myerson', 'authors': 'Joel Myerson, Joel Myerson', 
  'publisher': 'Oxford University Press, USA', 'pubdate': 'Dec-00', 'pages': '752'}]
  >>> saveToFile(my_library, False, test.txt)
  "Transcendentalism: A Reader;" is written to test.txt
  """
    file = open(file_name, "w")
    if saveAll == True:
        library = library.getCitationInformation()
        file.write(library)
    else:
      for items in library:
        titties = getTitles(library)[0] + ";"
        file.write(titties)
        file.close()
    pass


#######################################################################
## DO NOT EDIT ANYTHING BELOW HERE
def getCitationInformation(title: str, authors: str, publisher: str,
                           pages: str, date: str) -> str:
    """ This function returns the stylized citation for the book information passed as parameters.
  :param title: (str) full title of the book
  :param authors: (str) full list of authors full names
  :param publisher: (str) name of publishers
  :param pages: (str) number of pages
  :param date: (str) date of publication
  :return : (str) the formatted string of the citation
  
  >>> getCitationInformation("Voices in Our Blood: America's Best on the Civil Rights Movement", "Jon Meacham", 
  "Random House Publishing Group", "576", "Jan-03")
  Jon Meacham. Voices in Our Blood: America's Best on the Civil Rights Movement. Random House Publishing Group, 576, Jan-03.  
  """
    return authors + ". " + title + ". " + publisher + ", " + pages + ", " + date + "."


def printHeaderOrder() -> None:
    """ This function has been added so that you can see how to call functions from the distributor module.
  """
    header = distributor.getHeader()
    print(f'Column names are {", ".join(header)}.')


def main() -> None:
    """ This function handles user input and the operations for the library.
  """
    option = ""
    library = []
    initial_books = int(
        input(
            "How many books do you initially want in your library (0..100)?:"))
    if initial_books < 0 or initial_books > 100:
        option = "QUIT"
    else:
        library = setupLibrary(initial_books)

    while option != "QUIT":
        option = input(
            "Select an option (ADD, REMOVE, PRINT, TITLES, RECOMMEND, SAVE, QUIT): "
        ).upper()

        if option == "ADD":
            title = input("Title:")
            firstAuthor = input("First Author:")
            authors = input("All Authors:")
            publisher = input("Publisher:")
            pubdate = input("Publication Date:")
            pages = input("Page Numbers:")
            book_entry = createBookDictionary(title, firstAuthor, authors,
                                              publisher, pubdate, pages)
            addBook(library, book_entry)

        elif option == "REMOVE":
            index = int(input("Which # would you like to remove? "))
            removeBook(library, index)

        elif option == "PRINT":
            printLibrary(library)

        elif option == "TITLES":
            titles = getTitles(library)
            for item in titles:
                print(item, end="; ")
            print("END")

        elif option == "RECOMMEND":
            print("I recommend you read", getRandomCitation(library))

        elif option == "SAVE":
            save_option = input("Select an option (TITLES, ALL): ").upper()
            file_name = input(
                "Enter the files name to save the library (without an extension): "
            )
            if save_option == "TITLES" and file_name:
                saveToFile(library, False, file_name + ".txt")
            elif save_option == "ALL":
                saveToFile(library, True, file_name + ".txt")
            else:
                print("Invalid Input")

    print("Goodbye!")


if __name__ == "__main__":
    if (test_mode):
        myTests()
    else:
        main()
