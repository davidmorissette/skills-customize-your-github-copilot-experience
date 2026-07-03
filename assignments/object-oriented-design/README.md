# 📘 Assignment: Object-Oriented Design

## 🎯 Objective

Learn how to model a real-world system with Python classes, using inheritance and composition to organize relationships between objects.

## 📝 Tasks

### 🛠️ Design Base and Derived Classes

#### Description
Create a class hierarchy for library items: a base class `LibraryItem` and derived classes `Book` and `Movie`. Each item should store title, year, and availability.

#### Requirements
Completed program should:

- Define `LibraryItem` with `title`, `year`, and `available` attributes
- Define `Book` and `Movie` subclasses inheriting from `LibraryItem`
- Add a `display_info()` method that prints item details
- Create at least one `Book` and one `Movie` instance and display their info

### 🛠️ Build a Library Manager

#### Description
Create a `Library` class to manage items, adding, listing, and loaning items using the item objects.

#### Requirements
Completed program should:

- Define `Library` with an item list to store library objects
- Add methods `add_item(item)`, `list_items()`, `checkout_item(title)`, and `return_item(title)`
- Use `Library` to add items, list items, check out one item, and return it
- Print status changes so users can see availability
