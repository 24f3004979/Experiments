
// Product Props required for the componenets fro telling about data flow

interface ProductProps {
  ProductName: string;
  price: number;
  photo: string;
}

export default function Product({ ProductName, price, photo }: ProductProps) {
  return (
    <div className="Product-Component" style={style.component}>
      <h3>Product Name : {ProductName}</h3>
      <img src={photo} style={style.img} />
      <p> Prize : {price}</p>
      <button onClick={(): string => AddToCart(ProductName)}>
        + Add to Cart
      </button>
    </div>
  );
}


const style = {
  component: {
    height: '20rem',
    width: '20rem',
    padding: '2%',
    backgroundColor: 'black',
    color: 'white',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    margin: '5%',
    gap: '2rem',
    borderRadius: '5px'
  },
  img: {
    width: '14rem',
    borderRadius: '5px',
    height: '10rem',
    flexShrink: 0
  }
}

// Making this working with the backend api calls
function AddToCart(ProductName: string): void {
  console.log(`Adding to cart : ${ProductName}`);
}
