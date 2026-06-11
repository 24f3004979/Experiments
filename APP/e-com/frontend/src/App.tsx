import { useState, useEffect } from 'react'
import './App.css'
import Header from './components/navigator.tsx'
import Product from './components/Products.tsx'


function App() {

  const [products, setProducts] = useState<any[]>([]);

  useEffect((): any => {
    fetch('http://localhost:5000/api/products')
      .then((res) => res.json())
      .then((data) => {
        // Saving data by seting products varuable with its setter
        setProducts(data);
      })
      .catch((err) => console.log(err));
  }, []);

  // Try to list out all of the information from the backend call
  console.log(products);

  // TODO: Making routing and buy function working into the main application :)

  return (
    <>
      <Header />
      <h1>Product Listed</h1>
      {products.map((product) => (

        < Product ProductName={product.ProductName} price={product.price} photo={product.photo} />
      ))}
    </>
  )
}

export default App
