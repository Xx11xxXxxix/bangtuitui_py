import React from 'react';
import { createBrowserRouter, Navigate, RouteObject } from 'react-router-dom';
import Login from '../pages/login/login';
import RoleList from '../pages/rolelist';
import ProductPage from '../pages/product';  
import NeteaseLogin from '../pages/netease';

const AuthLayout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const token = localStorage.getItem('token');
  const pathname = window.location.pathname;
  
  // 白名单
  const whiteList = ['/login', '/netease'];
  
  if (!token && !whiteList.includes(pathname)) {
    return <Navigate to="/login" replace />;
  }
  
  return <>{children}</>;
};

const routes: RouteObject[] = [
  {
    path: '/login',
    element: <Login />
  },
  {
    path: '/',
    element: <AuthLayout>
      <RoleList />
    </AuthLayout>,
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
      },
      {
        path: 'netease',
        element: <NeteaseLogin />
      }
    ]
  },
  {
    path: '*',
    element: <Navigate to="/rolelist" replace />
  }
];

const wrapRouteElement = (route: RouteObject): RouteObject => {
  if (route.children) {
    return {
      ...route,
      children: route.children.map(childRoute => wrapRouteElement(childRoute))
    };
  }

  // 白名单
  if (route.path === '/login' || route.path === '/netease') {
    return route;
  }

  return {
    ...route,
    element: route.element ? (
      <AuthLayout>
        {route.element}
      </AuthLayout>
    ) : route.element
  };
};

const processedRoutes = routes.map(route => wrapRouteElement(route));

const router = createBrowserRouter(processedRoutes);

export default router;