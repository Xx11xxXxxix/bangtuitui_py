import React from 'react';
import { createBrowserRouter, Navigate, RouteObject } from 'react-router-dom';
import Login from '../pages/login/login';
import RoleList from '../pages/rolelist';
import ProductPage from '../pages/product';  

const routes: RouteObject[] = [
  {
    path: '/login',
    element: <Login />
  },
  {
    path: '/',
    children: [
      {
        path: '/',
        element: <Navigate to="/rolelist" replace />
      },
      {
        path: 'rolelist',
        element: <RoleList />
      },
      {
        path: 'product',
        element: <ProductPage />
      }
    ]
  },
  {
    path: '*',
    element: <Navigate to="/login" replace />
  }
];

const router = createBrowserRouter(routes);

export default router;