export interface Product {
  id: number;
  title: string;
  price: number;
  description: string;
  category: string;
  image: string;
}

export const mockProducts: Product[] = [
  {
    id: 1,
    title: "Minimalist Wireless Headphones",
    price: 129.99,
    description: "High-fidelity sound engineered with active noise cancellation and 40-hour battery stamina.",
    category: "electronics",
    image: "https://unsplash.com"
  },
  {
    id: 2,
    title: "Ergonomic Mechanical Keyboard",
    price: 89.50,
    description: "Hot-swappable tactile linear switches with customizable RGB backlighting maps.",
    category: "electronics",
    image: "https://unsplash.com"
  },
  {
    id: 3,
    title: "Waterproof Commuter Backpack",
    price: 59.00,
    description: "Durable ballistic nylon weave featuring a dedicated padded 16-inch laptop pocket layout.",
    category: "accessories",
    image: "https://unsplash.com"
  },
  {
    id: 4,
    title: "Stainless Steel Smart Flask",
    price: 34.95,
    description: "Vacuum insulated travel container displaying real-time liquid temperature metrics.",
    category: "accessories",
    image: "https://unsplash.com"
  }
];

