import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import Header from './components/navigator.tsx'
import Product from './components/Products.tsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Header />
      <Product ProductName="Laptop" price={45} />
    </>
  )
}

export default App
