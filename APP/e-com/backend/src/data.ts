export interface Product {
  id: number;
  ProductName: string;
  price: number;
  image: string;
}

export const mockProducts: Product[] = [
  {
    id: 1,
    ProductName: "Laptop",
    price: 129.99,
    image: "/images/dark.jpg"
  },
  {
    id: 2,
    ProductName: "Laptop Pro Max",
    price: 89.50,
    image: "/images/darker.jpg"
  },
  {
    id: 3,
    ProductName: "RR CAR",
    price: 59.00,
    image: "/images/gaddi.jpg"
  },
];

