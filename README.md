# DDDWriter

DDDWriter is a Django-based project implementing Domain-Driven Design (DDD) principles with Onion Architecture. This project is an experiment to explore how DDD can be effectively applied in Django, without relying on Django Rest Framework (DRF), and instead using Django-Ninja for API development.

## Project Structure

The project is organized into distinct modules, each representing a core architectural layer of the application:

- `blog`: The blog module implementing DDD principles.
- `user`: The user module implementing DDD principles.
- `shared`: Contains shared utilities and infrastructure components.

### Project Directory Layout
```
src
├── shared
│ ├── domain
│ └── infrastructure
│ ├── django
│ └── repository
│ ├── mapper
│ └── rdb
├── blog
│ ├── application
│ │ └── use_case
│ │ ├── command
│ │ └── query
│ ├── domain
│ │ ├── entity
│ │ ├── exception
│ │ └── value_object
│ ├── infrastructure
│ │ ├── database
│ │ │ ├── migrations
│ │ │ ├── models
│ │ │ └── repository
│ │ └── django
│ └── presentation
│ └── rest
│ ├── api
│ ├── containers
│ ├── request
│ └── response
├── user
└── tests
```

## Features

- **Domain-Driven Design (DDD)**: Emphasizes the separation of domain logic from infrastructure concerns.
- **Onion Architecture**: Ensures a clean separation of concerns and promotes a modular structure.
- **Django-Ninja**: Provides a simple and effective way to build APIs without DRF.
- **Repository Pattern**: Abstracts data access, allowing for flexibility and easier testing.
- **Entity Mapping**: Maps between Django models and domain entities using a well-defined interface.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/dddwriter.git
   cd dddwriter

## Usage
APIs: Access the APIs through endpoints defined in the presentation layer.
Administration: Use Django’s built-in admin interface for managing blog and user entities.

## Contributing
Fork the Repository: Click on the "Fork" button in the top-right corner of the repository page.
Create a Branch: Create a new branch for your changes.
Make Changes: Implement your changes and ensure they adhere to the project's coding standards.
Submit a Pull Request: Create a pull request detailing your changes.
