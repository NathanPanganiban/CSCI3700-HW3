## Team Members
Nathan Panganiban, Terrence Vaughn

## Quick Start

## Clone the Repository:

git clone https://github.com/NathanPanganiban/CSCI3700-HW3.git


## Enter project directory

cd CSCI3700-HW3


## Install Dependencies

pip3 install -r requirements.txt


## Enter PostgreSQL

sudo -u postgres psql


## Populate Database

CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR(100) NOT NULL
);

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR(100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a) VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b) VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');



## Exit PostgreSQL

\q


## Run Flask Application

python3 -m venv python_venv

python3 main.py


## Access Database Information:

http://127.0.0.1:5000/api/update_basket_a

http://127.0.0.1:5000/api/unique

## Photo Display of Unique Fruits in Table

<img width="1440" alt="Screenshot 2024-10-31 at 10 23 02 AM" src="https://github.com/user-attachments/assets/8948c431-321b-47ac-b642-4ff483ce4edd">

