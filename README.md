# DDDWriter

DDDWriter is a Domain-Driven Design (DDD) implementation in Django, focusing on demonstrating how DDD principles can be integrated with Django's powerful features without relying on Django Rest Framework (DRF). Instead, this project utilizes Django-Ninja for API development, providing a lightweight alternative to DRF with a clear separation of concerns as advocated by DDD.

## Requirements
- Django
- Django-Ninja

## Points to Note
- The project layout is influenced by common DDD project structures, ensuring that domain logic is cleanly separated from infrastructural concerns.
- It emphasizes decoupling the domain model from the persistence layer, using repository patterns and custom mappers.

## Project Structure
```
src
├── shared (Shared utilities and core configurations)
│   ├── domain (Domain models and business logic)
│   └── infrastructure (Infrastructure implementations including ORM and API frameworks)
│       ├── django (Django configurations and settings)
│       └── repository (Data access layer implementation)
│           ├── mapper (Data mappers for converting database models to domain entities)
│           └── rdb (Relational database implementations)
├── blog (Blog module applying DDD principles)
│   ├── application (Application services handling use cases)
│   │   └── use_case (Specific business cases like creating or retrieving blog posts)
│   │       ├── command (Commands that change the state of the domain)
│   │       └── query (Queries that read the state of the domain without changes)
│   ├── domain (Core blog domain logic and rules)
│   │   ├── entity (Entities like BlogPost that are core to the blog's business logic)
│   │   ├── exception (Custom exceptions for blog operations)
│   │   └── value_object (Value objects that hold attributes but have no conceptual identity)
│   ├── infrastructure (Infrastructure specific to the blog module)
│   │   ├── database (Database ORM models and migration scripts)
│   │       ├── migrations (Database migrations for the blog module)
│   │       ├── models (ORM models representing the blog's database schema)
│   │       └── repository (Repository implementations for accessing blog data)
│   │           ├── mapper (Mappers for translating between domain and ORM models)
│   │           └── rdb (Repository implementation for relational database interactions)
│   └── presentation (API and user interface components)
│       └── rest (RESTful API endpoints exposing the functionality of the blog module)
│           ├── api (Controller methods that handle requests and responses)
│           ├── containers (Dependency injection containers or service locators)
│           ├── request (Request DTOs defining the API input structures)
│           └── response (Response DTOs defining the API output structures)
├── user
│   └── (User module applying similar DDD principles)
│       ├── application
│       │   └── use_case
│       │       ├── command
│       │       └── query
│       ├── domain
│       │   ├── entity
│       │   └── exception
│       ├── infrastructure
│       │   ├── database
│       │   │   ├── migrations
│       │   │   ├── models
│       │   │   └── repository
│       │   └── django
│       └── presentation
│           └── rest
│                ├── api
│                ├── containers
│                ├── request
│                └── response
├── comment
│   └── (User module applying similar DDD principles)
│       ├── application
│       │   └── use_case
│       │       ├── command
│       │       └── query
│       ├── domain
│       │   ├── entity
│       │   └── exception
│       ├── infrastructure
│       │   ├── database
│       │   │   ├── migrations
│       │   │   ├── models
│       │   │   └── repository
│       │   └── django
│       └── presentation
│           └── rest
│                ├── api
│                ├── containers
│                ├── request
│                └── response
└── tests (Unit and integration tests)
```

## Installation
To set up the project locally, clone the repository and install the required dependencies:

```bash
git clone https://github.com/miladkoohi/dddwriter.git
cd dddwriter
pip install -r requirements.txt



Make sure to replace `https://github.com/miladkoohi/dddwriter.git` with the actual URL of your repository to ensure that others can correctly clone and start the project.
