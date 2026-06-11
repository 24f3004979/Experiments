import express, { Request, Response } from 'express';
import cors from 'cors';
import { mockProducts } from './data.js';

const app = express();
const PORT = process.env.PORT || 5000;

// Enable JSON middleware and cross-origin resource requests
app.use(cors());
app.use(express.json());

// Endpoint for listing all the products while called with :)
app.get('/api/products', (req: Request, res: Response) => {
  res.json(mockProducts);
  console.log(res.json(mockProducts)); // Checking how it goes :)
});


app.listen(PORT, () => {
  console.log(`Experimental API running at http://localhost:${PORT}`);
});

