# Application structure working flow

main.tsx
  Main entry point element which loads other componenets into the react dom for the root element.

App.tsx
  Assemble componenets for the final hydration through main.tsx
  Assembling all components together for the final assembly

  App() function
    returns
      constant values [count , setCount] = useState(0)

      Count varaiable with its seting function for setting updating the count variable
