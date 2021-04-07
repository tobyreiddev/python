import book
import author

author = author.Author(name="author name", firstName="greg", nationality="Australian")

book = book.Book("book title", 1, author)

book.lend("testUser")