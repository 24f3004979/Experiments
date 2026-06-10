
// Product Props required for the componenets fro telling about data flow

interface ProductProps {
  ProductName: string;
  price: number;
}

export default function Product({ ProductName, price }: ProductProps) {
  return (
    <div className="Product-Component">
      <h3>Product Name : {ProductName}</h3>
      <p> Prize : {price}</p>
      <button onClick={(): string => AddToCart(ProductName)}>
        +
      </button>
    </div>
  );
}


function AddToCart(ProductName: string): void {
  console.log(`Adding to cart : ${ProductName}`);
}
