import { useState } from 'react'
import reactLogo from './assets/react.svg'
import { RouterProvider } from 'react-router-dom';
import viteLogo from '/vite.svg'
import router from './router';
import './App.css'

function App() {
  return <RouterProvider router={router} />;
}

 

export default App
