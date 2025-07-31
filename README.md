ecommerce-frontend/
├── public/
│   └── index.html
├── src/
│   ├── App.js
│   ├── api.js
│   └── index.js
├── .env
├── package.json
└── README.md
{
  "name": "ecommerce-frontend",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "axios": "^1.6.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  }
}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>eCommerce Frontend</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
import axios from 'axios';

const API = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
});

export const fetchProducts = () => API.get('/products');
import React, { useEffect, useState } from 'react';
import { fetchProducts } from './api';

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProducts()
      .then((res) => {
        setProducts(res.data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Failed to fetch products:", err);
        setLoading(false);
      });
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>🛍️ Product List</h1>
      {loading ? (
        <p>Loading products...</p>
      ) : products.length === 0 ? (
        <p>No products found.</p>
      ) : (
        <ul>
          {products.map((product) => (
            <li key={product.id}>
              <strong>{product.name}</strong> - ₹{product.retail_price}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
# 🛒 eCommerce Frontend (React)

This is a simple React frontend to fetch and display products from an eCommerce backend API.

## 🧱 Tech Stack

- React (v18)
- Axios
- Environment-based API integration

## 📦 Features

- Fetch product list from backend
- Display product name and price
- Auto-load on page refresh

## 🚀 Getting Started

1. Install dependencies:
