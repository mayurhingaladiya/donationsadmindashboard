# Donations Admin Dashboard

## Overview

The Donations Admin Dashboard is a web application designed to streamline the management of donations, contributors, and charities. It provides an intuitive interface for administrators to add, view, and manage donations while keeping track of contributors and charities associated with each donation.

## Features

- **Contributors Management**: 
  - Add, edit, and delete contributors.
  - View a list of all contributors with their details.

- **Charities Management**: 
  - Add and view details of various charities.
  - Keep track of charity descriptions and names.
  - Only via the django admin interface (as users should not be able to create charites)

- **Donations Management**:
  - Add donations linked to specific contributors and charities.
  - View a comprehensive list of donations
  - Track donation amounts and dates.

- **Responsive Design**:
  - The dashboard is designed to be user-friendly and responsive, providing a seamless experience across devices.

- **Data Visualization**:
  - Visual representation of donations through charts to help analyze contributions and charity performance.

## Tech Stack

- **Frontend**: Vue.js, Bootstrap
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL (or any compatible database)

## Getting Started

## Create conda environment

After cloning this repository, create a conda environment for this project and activate the environment:

```console
$ conda create --name donationapp python=3.11
$ conda activate donationapp
```

## Django backend

The `backend` folder contains a [Django project](https://docs.djangoproject.com/en/stable/intro/tutorial01/) and was created with:

```console
(donationapp)$ django-admin startproject backend
```

### Install backend (Python) dependencies

With the conda environment active, install the backend (Python) dependencies:

```console
(donationapp)$ cd backend
(donationapp)$ pip install -r requirements.txt
```

The main backend dependencies (see requirements.txt) are the Django framework itself (Django) and [django-cors-headers](https://pypi.org/project/django-cors-headers/) which is needed for CORS requests (since the request origin address http://localhost:5713 is different from the address that sent the JavaScript code to the browser http://localhost:8000).

### Start backend server

To start the backend server cd into the backend folder where the manage.py file is (if not already there)

```console
(donationapp)$ cd backend
```

and run

```console
(donationapp)$ python manage.py runserver
```

The server will start on http://localhost:8000

### API app

An "api" Django app has already been created with the command

```console
$ python manage.py startapp api
```

and can be tested by visiting http://localhost:8000/api/test.json

## Vue frontend

The `frontend` folder contains a [Vue/Vite project](https://vitejs.dev/guide/) and was created with:

```console
(donationapp)$ npm create vite@latest
```

### Install frontend (JavaScript) dependencies

To install the frontend (JavaScript) dependencies cd into the frontend folder

```console
(donationapp)$ cd frontend
```

and run:

```console
(donationapp)$ npm install
```

The main frontend dependencies (see package.json) are [vue](https://vuejs.org/guide/introduction.html) and [bootstrap](https://getbootstrap.com/docs/5.0/getting-started/download/).

### Start frontend server

To start the frontend server run

```console
(donationapp)$ npm run dev
```

and the server will start on http://localhost:5173
