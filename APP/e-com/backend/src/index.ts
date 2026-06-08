import express, { Request, Response } from 'express';
import cors from 'cors';
import { mockProducts } from './data.js';

const app = express();
const PORT = process.env.PORT || 5000;

// Enable JSON middleware and cross-origin resource requests
app.use(cors());
app.use(express.json());

// Endpoint to fetch all listings
app.get('/api/products', (req: Request, res: Response) => {
  res.json(mockProducts);
});

// Endpoint to fetch a singular item by numerical ID parameter
app.get('/api/products/:id', (req: Request, res: Response) => {
  const productId = parseInt(req.params.id, 10);
  const item = mockProducts.find(p => p.id === productId);
  
  if (!item) {
    res.status(404).json({ error: "Target catalog item not found" });
    return;
  }
  res.json(item);
});

// Mock checkout verification route
app.post('/api/checkout', (req: Request, res: Response) => {
  const { items } = req.body;

  if (!items || !Array.isArray(items) || items.length === 0) {
    res.status(400).json({ success: false, message: "Validation error: Shopping cart is empty." });
    return;
  }

  // Generate an arbitrary sandbox reference ID 
  const executionId = `ORD-${Math.floor(100000 + Math.random() * 900000)}`;
  
  res.status(201).json({
    success: true,
    message: "Sandbox transaction logged successfully.",
    orderId: executionId,
    itemCount: items.length
  });
});

app.listen(PORT, () => {
  console.log(`Experimental API running at http://localhost:${PORT}`);
});

