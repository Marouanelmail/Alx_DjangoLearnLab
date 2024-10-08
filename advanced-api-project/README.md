# Django Book Management API

This project is a Django-based API that manages books and authors. It allows users to create, update, list, and delete books, as well as view book details.

## Book Views

The following views handle CRUD operations for the `Book` model:

- **Book ListView** (`/books/`): Retrieves a list of all books.
- **Book DetailView** (`/books/<int:pk>/`): Retrieves details for a specific book by ID.
- **Book CreateView** (`/books/add/`): Allows authenticated users to add a new book.
- **Book UpdateView** (`/books/<int:pk>/edit/`): Allows authenticated users to edit an existing book.
- **Book DeleteView** (`/books/<int:pk>/delete/`): Allows authenticated users to delete a book.

## Custom Logic in Views

- **CreateView and UpdateView**: The `form_valid` method has been overridden to include custom validation for the `publication_year` field, ensuring it cannot be set in the future.

## Permissions

The following permission restrictions are applied:
- Create, Update, and Delete views are restricted to authenticated users.
- List and Detail views are publicly accessible.

## Testing the API

You can test the API using tools like Postman or curl.

### Example curl commands:

- **List all books**:
  ```bash
  curl http://localhost:8000/books/


## Running the Project

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Apply migrations using `python manage.py migrate`.
4. Run the development server: `python manage.py runserver`.

## Advanced Query Capabilities

The Book API supports advanced query features:

### Filtering

- **Title**: Filter by title using `?title=<keyword>`.
- **Author**: Filter by author using `?author=<keyword>`.
- **Publication Year**: Filter by publication year using `?publication_year=<year>`.

### Searching

- **Search**: Use the `search` parameter to search by title or author name: `?search=<keyword>`.

### Ordering

- **Ordering**: Order results by title or publication year using `?ordering=<field>` where `<field>` is either `title` or `publication_year`.

**Examples**:

- List all books by J.K. Rowling: `GET /api/books/?author=J.K.%20Rowling`
- Search for books containing 'Harry' in the title: `GET /api/books/?search=Harry`
- Order books by publication year: `GET /api/books/?ordering=publication_year`

## Testing API Endpoints

### Test Setup
- **Test Framework**: Uses Django's built-in test framework.
- **Test Database**: A separate test database is used.

### Test Cases
- **Creating a Book**: Tests the POST request to create a new book.
- **Updating a Book**: Tests the PUT request to update an existing book.
- **Deleting a Book**: Tests the DELETE request to remove a book.
- **Listing Books**: Tests the GET request to retrieve all books.
- **Filtering Books**: Tests the filtering functionality for books.
- **Searching Books**: Tests the search functionality for books.
- **Ordering Books**: Tests the ordering functionality for books.

### Running Tests
Execute tests with:
```bash
python manage.py test api