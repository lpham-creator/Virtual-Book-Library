Homework Assignment 7: Neilson Library 
---

*Notes: This homework assignment should be completed in identified pairs (not more than two students), but may be done individually as well. Pairs should use our pair programming methodology and switch roles every 15-20 minutes. As a pair, you should create a team in Replit and then you will have one submission.*

*Start all assignments in this class at least four days before the deadline. This will enable you to get help when needed and ensure your success in this course.*

Please read the entire assignment description prior to starting any part. 
You should complete the functions of this assignment one at a time and test the functions as you go.

---

## Overview and Learning Objective

![Neilson Library](assets/neilson.png)
_Photo Credit: Smith College_ 

In honor of the one-year anniversary of the opening of the Neilson Library, we will create a virtual book library.

The goal of this assignment is for you to practice using lists and dictionaries to create the specified library interface. This is the first assignment that uses multiple files.

Using your interface, the user should be able to:
* add a book
* delete an existing book
* recommend a random book to the user
* print all the books
* print only the book titles
* save some of the library data to a file

---

We have given you substantial starter code and written the `main()` function for you. The library consists of a list of dictionaries. Each dictionary will store the information for one book and will use the keys: "title", "firstAuthor", "authors", "publisher", "pubdate", "pages". To make your library work, you must complete the functions specified below:

1. `createBookDictionary(title, firstAuthor, authors, publisher, pubdate, pages)`: This function takes in the information for title, firstAuthor, authors, publisher, pages, and pubdate, all as strings. The function creates a dictionary for the book with the following keys: 'title', 'firstAuthor', 'authors', 'publisher', 'pubdate', 'pages'. Returns a dictionary holding the information for one book.
2. `setupLibrary(numBooks)`: This function takes a given number of books (`numBooks`) from distributor and sets up a library to store them. numBooks is the number of books the user wants to have initialized in the library, in the range of 0..100. Returns the newly created library (which is a list of book dictionaries). *If numBooks is zero, this function should return an empty list.* (Hint: check `distributor.py` to find a function to randomly pick a book from `book-database.csv`)
3. `printLibrary(library)`: This function prints out the citation information for each book in the library in order. For each book, an index (starting at 1) should first be printed prior to the citation information. (Hint: use the stylized citation of `getCitationInformation` function in main.py)
4. `addBook(library, book)`: This function adds a book dictionary to the library list.
5. `removeBook(library, index)`: This function removes the entry at the index specified from the library list. *The indexes 1..n appear when the user selects the PRINT operation.* Make sure the function does not break when a user specifies an index of a book that does not exist.
6. `getTitles(library)`: This function returns a list of the book titles in the library, sorted in alphabetical order.
7. `getRandomCitation(library)`: This function selects a book at random from the library and returns the citation information for that book. (Hint: use the stylized citation of `getCitationInformation` function in main.py)
8. `saveToFile(library,  saveAll, file_name)`: This function takes as input the library and a file_name. _Note: `main()` appends `.txt` to the file name before calling this function._ If `saveAll` is True, then this function writes the output of the `PRINT` operation to the file; otherwise, it writes the result of the `TITLES` operation to the file.

The following functions are already written for you:

* `main()`: This function handles user input and the operations for the library.
* `getCitationInformation(title, authors, publisher, pages, date)`: This function returns the stylized citation for the book information passed as parameters.
* `printHeaderOrder()`: This function has been added so that you can see how to call functions from the distributor module (see below).

We have also included the `distributor.py` module to help you fill your library with book information. **Do not edit** `distributor.py`. This module has the following functions of interest:

* `distributor.getHeader()`: This function returns the order of information in the book lists returned from the distributor module. 
* `distributor.getRandomBook()`: This function returns a list with the information for one book, see the header for the order of information.
* `distributor.getRandomBookList(numBooks)`: This function returns a list of lists with the information for numBooks book, see the header for the order of information.

*There is more data in the header and lists returned from the distributor module than you will keep for your library. We suggest printing out the return of these functions a few times to further understand their behavior.*

--- 

## Doc Strings
To get full credit for this assignment, you are required to complete the doc string for every function in main.py (with the exception of the `myTests` function), using the doc string format we learned in class. For each function, your doc string must include:

* a short description of the function
* list and description of any parameters (or inputs) to the function, including their type
* list and description of any return value of the function, including its type
* **one** example of a call to the function from the console (`>>>`) 

---

## Helpful Advice / Rules

* You are prohibited from using additional `import` commands in this assignment.
* `Replit Unit Tests` have been provided to guide you in your work, you should also add your own tests in the `myTests` function.
* The starter code runs without syntax errors, play with it before implementing your functions.
* Prior to the final submission, remove all print statements added for testing purposes.
* All input statements are placed in the main() function. 
* No variables should be initialized outside the provided functions.
* You must add your own comments for each function, as well as inline where necessary.

---

## Grading criteria (25 pts):

Do not edit or delete `feedback.md` or `distributor.py`.
After your assignment has been reviewed, your grade (and rubric) will be put in this file.

* Completing each function (16 points)
* Doc Strings (4 points)
* Readability (3 points)
    + uses appropriate, informative variable names
    + has additional comments where needed
* The basics* (2 points)

*The basics includes that your submission runs without syntax errors, and includes a complete header at the top of each file, as well as following the helpful advice / rules and ensuring that `test_mode = False` when you submit.


## Submissions

Your submission must include the complete course header at the top of each file.
When you have completed your assignment, ensure that `test_mode = False`, run the `Replit Unit Tests` one more time then click `Submit` at the top.

See *Late Work Policy* posted to Moodle for details about late submissions.

---

*Note: This is a refreshed assignment this year. If you find errors (typos) or if parts are confusing, please ask clarifying questions.*

---

© Alicia M. Grubb 2022



