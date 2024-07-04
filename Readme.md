# VendorVerse

![VendorVerse](https://res.cloudinary.com/dbui0ebjv/image/upload/v1720023878/VendorVerse_aj3ivc.png)
VendorVerse is a multivendor e-commerce platform designed to streamline supply chain management, having a deep set of features, a dynamic frontend for user interactions and provide a seamless experience for both vendors and customers.

## 📚 **Table of Contents**

-   [Project Overview](#project-overview)
-   [Features](#features)
-   [Technologies Used](#technologies-used)
-   [Installation](#installation)
-   [Backend](#backend)
    -   [Structure](#structure)
    -   [Dependencies](#dependencies)
    -   [Endpoints](#endpoints)
-   [Frontend](#frontend)
    -   [Structure](#structure)
    -   [Dependencies](#dependencies)
-   [Contributing](#contributing)

## ✨ **Features**

### 🧭 Navigation Bar

The Navigation Bar provides easy access to various sections of the platform, including:

-   **Sign In / Sign Up**: Quick access to authentication features.
-   **Logout**: Easily log out from your account.
-   **Vendor Dashboard**: Navigate to the vendor dashboard.
-   **User Dashboard**: Navigate to the user dashboard.
-   **Search Bar**: Search for products across the platform.
-   **Cart Icon**: Shows cart item count.

### 🔒 User Authentication

Secure login and registration for users and vendors using JWT token authorization.

This user-friendly dashboard provides all the tools needed to streamline store management and enhance business performance.

### 🛍️ Shop Page

The Shop Page allows users to browse and purchase products with ease:

-   **Product Listings**: View a comprehensive list of available products.
-   **Category Selection**: Filter products by categories to find what you're looking for.
-   **Trending Products**: Explore a dedicated section for trending products

### 📊 Vendor Dashboard

The Vendor Dashboard offers a comprehensive suite of features designed to help vendors manage their online stores efficiently:

-   📦 **Product Listings**: View and manage all offered products with detailed order information.
-   📊 **Sales Tracking**: Monitor total sales and monthly earnings.
-   📈 **Revenue Analysis**: Visualize revenue trends with interactive diagrams.
-   ⭐ **Reviews**: Access and respond to product reviews.
-   ➕ **Add New Products**: Easily add new products to the shop.
-   🎟️ **Discount Coupons**: Create and manage discount coupons.
-   🔔 **Notifications**: Stay informed with a notification area that lists all notifications, including read and unread counts.
-   ⚙️ **Settings**: Customize your vendor profile and store settings.

## 📋 User Dashboard

The User Dashboard provides users with a comprehensive suite of tools to manage their shopping experience efficiently:

-   🛒 **Order Management**: View and track all your orders with detailed order information.
-   🧾 **Invoice Printing**: Print invoices and detailed order summaries for your records.
-   📑 **Wishlist**: Manage your wishlist and save products for future purchases.
-   🔔 **Notifications**: Stay informed with a notification system that lists all notifications, including read and unread counts.
-   ⚙️ **Account Settings**: Customize your profile and account settings, including editing personal information.

This user-friendly dashboard ensures that users have all the necessary tools to manage their shopping activities smoothly and efficiently.

### 📝 Product Detail Page

The Product Detail Page provides detailed information and features for each product:

-   **Image Gallery**: View a gallery of product images.
-   **Product Specifications**: Detailed product specifications and information.
-   **Review Rating and Count**: See the overall review rating and the number of reviews.
-   **Vendor Profile**: View the profile of the vendor selling the product.
-   **Customer Reviews**: Read reviews and comments left by other customers.
-   **Write Reviews**: Write your own reviews and rate the product.
-   **Add to Cart**: Add the product to your shopping cart for purchase.

### 🛒 Cart Page

The Cart Page provides an overview and management of items added to the cart:

-   **Item List**: View all items added to the cart in a detailed list.
-   **Remove Items**: Remove items from the cart.
-   **Quantity Adjustment**: Adjust the quantity of each item in the cart.
-   **Cart Summary**: View a summary of all costs, including item costs, taxes, and total amount.
-   **Personal and Shipping Information**: Enter and manage personal details and shipping information for the order.

### 🧾 Checkout Page

The Checkout Page ensures a smooth and secure final step for completing purchases:

-   **Shipping Address Review**: Review all entered shipping details from the cart page and confirm their accuracy.
-   **Order Summary**: View a comprehensive summary of the order, including itemized costs and total amount.
-   **Coupon Field**: Enter discount coupons which are immediately applied to the order summary.
-   **Payment Methods**: Choose the preferred payment method with integrations for:
    -   **Stripe**: Redirects to the Stripe Checkout page, supporting card payments, Link, and Google Pay.
    -   **PayPal**: Redirects to the PayPal Checkout page for secure payment.

### 🏆 Payment Success Page

The Payment Success Page provides users with real-time updates on their payment status and order details upon completing a purchase:

-   **Real-Time Updates**: Users receive immediate feedback on the payment process, including the status of payment confirmation and order creation.
-   **Payment Confirmation**: Users are notified once their payment has been successfully processed and confirmed.
-   **Order Information**: A summary of the order, including itemized details and total amount paid, is displayed.
-   **Download and Print Invoice**: Users can download and print a PDF of their order invoice for their records.
-   **Order Status Signal**: Clear indicators signal to users that their payment has been completed successfully and the order has been created.
-   **Automated HTML Confirmation Emails**: Both users and vendors receive automated HTML emails confirming the order and payment details.
-   **Notifications**: Users and vendors receive notifications about the order status, which can be viewed in their respective dashboards (Vendor Dashboard and User Dashboard).

This feature ensures that users have a smooth and transparent checkout experience, providing them with all the necessary information and confirmation for their purchase.

### 📦 Footer

The Footer provides essential information and quick links to help users navigate VendorVerse and stay connected:

-   **Social Media**: Connect with us on various social networks.
-   **About Us**: Discover what VendorVerse offers and our mission to connect diverse vendors and customers.
-   **Useful Links**: Access important links like Privacy Policy, Job Offers, Cooperation, and more.
-   **Product Categories**: Explore various categories such as Books, Clothing, Electronics, and more.
-   **Support**: Find support through our Help Center, FAQ, and Community sections.

This feature ensures that users can easily access important information and stay connected with VendorVerse through social media and useful links.

## Installation

### Prerequisites

-   **Node.js** (v14 or later) for the frontend
    -   Ensure you have npm (Node Package Manager) installed, which comes with Node.js.
-   **Python** (v3.8 or later) for the backend
    -   It's recommended to use a virtual environment to manage dependencies.
-   **PostgreSQL** (running locally or on a cloud service)
    -   Ensure you have created a database for the project and have the connection details (username, password, database name, host, and port).
-   **pip** (Python package installer) to install backend dependencies
-   **Git** to clone the repository and manage version control

These prerequisites will ensure that you have the necessary tools to install and run the project dependencies.

## Technologies Used

### Backend

-   **Python**: Programming language
-   **Django**: Web framework
-   **Django REST Framework**: API framework
-   **PostgreSQL**: Database
-   **JWT**: JSON Web Tokens for authentication
-   **Gunicorn**: WSGI HTTP Server for UNIX
-   **Boto3**: Amazon Web Services SDK for Python
-   **Psycopg2**: PostgreSQL database adapter for Python
-   **Stripe**: Payment processing platform
-   **Anymail**: Integrates with various email backends
-   **Django Storages**: A collection of custom storage backends for Django

### Additional Dependencies

-   **asgiref**
-   **black**
-   **certifi**
-   **charset-normalizer**
-   **click**
-   **colorama**
-   **dj-database-url**
-   **django-cors-headers**
-   **django-jazzmin**
-   **djangorestframework-simplejwt**
-   **drf-yasg**
-   **idna**
-   **inflection**
-   **jmespath**
-   **mypy-extensions**
-   **packaging**
-   **pathspec**
-   **platformdirs**
-   **python-dateutil**
-   **python-dotenv**
-   **pytz**
-   **PyYAML**
-   **requests**
-   **s3transfer**
-   **setuptools**
-   **shortuuid**
-   **six**
-   **sqlparse**
-   **typing_extensions**
-   **tzdata**
-   **uritemplate**
-   **urllib3**

This section now provides a comprehensive overview of the key technologies and additional dependencies used in the project.

### Frontend

-   **React**: JavaScript library for building user interfaces
-   **Vite**: Frontend build tool
-   **Zustand**: State management
-   **Axios**: HTTP client for API requests

### Additional Dependencies

-   **@ckeditor/ckeditor5-build-classic**: Rich text editor
-   **@ckeditor/ckeditor5-react**: React integration for CKEditor
-   **@paypal/react-paypal-js**: PayPal integration for React
-   **chart.js**: JavaScript charting library
-   **dayjs**: Date and time library
-   **framer-motion**: Animation library for React
-   **html2pdf.js**: Client-side PDF generation
-   **js-cookie**: Handling cookies in JavaScript
-   **jwt-decode**: Decode JSON Web Tokens
-   **moment**: Date and time manipulation library
-   **react-chartjs-2**: React wrapper for Chart.js
-   **react-hook-form**: Form handling in React
-   **react-icons**: Icons for React
-   **react-photo-album**: Photo gallery for React
-   **react-router-dom**: Routing library for React
-   **sweetalert2**: Beautiful, responsive, customizable, and accessible replacement for JavaScript's popup boxes
-   **yet-another-react-lightbox**: Lightbox component for React

### Development Dependencies

-   **@types/react**: TypeScript definitions for React
-   **@types/react-dom**: TypeScript definitions for React DOM
-   **@vitejs/plugin-react**: Official Vite plugin for React
-   **eslint**: Pluggable JavaScript linter
-   **eslint-plugin-react**: React specific linting rules for ESLint
-   **eslint-plugin-react-hooks**: ESLint rules for React hooks
-   **eslint-plugin-react-refresh**: ESLint plugin for React Fast Refresh
-   **prettier**: Code formatter
-   **simple-zustand-devtools**: Devtools for Zustand state management
-   **vite-plugin-static-copy**: Plugin for copying static files in Vite
