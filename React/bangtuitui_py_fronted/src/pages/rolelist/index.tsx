import React, { useEffect, useState } from 'react';
import { Outlet, useNavigate, useLocation } from 'react-router-dom';
import {  Menu, Spin } from 'antd';
import { Layout} from 'antd';
import {
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  HomeOutlined,
  ShoppingOutlined,
  UserOutlined,
  SettingOutlined,
  AppstoreOutlined
} from '@ant-design/icons';
import type { MenuProps } from 'antd';
import type { MenuItem } from '../types/menu';

const { Header, Sider, Content } = Layout;

// 扩展图标映射
const IconMap = {
  '首页': <HomeOutlined />,
  '轮播图': <AppstoreOutlined />,
  '商品': <ShoppingOutlined />,
  '会员': <UserOutlined />,
  '设计': <SettingOutlined />,
};

const RoleList: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const [collapsed, setCollapsed] = useState(false);
  const [menuItems, setMenuItems] = useState<MenuItem[]>([]);
  const [loading, setLoading] = useState(true);

  const transformMenuItems = (items: MenuItem[]): MenuProps['items'] => {
    return items.map(item => ({
      key: item.path,
      icon: IconMap[item.name] || <AppstoreOutlined />,
      label: item.name,
      children: item.children && item.children.length > 0
        ? transformMenuItems(item.children)
        : undefined,
      disabled: !item.is_show
    }));
  };
  // 菜单树
  const buildMenuTree = (items: MenuItem[]): MenuItem[] => {
    const map = new Map<number, MenuItem>();
    const result: MenuItem[] = [];

    items.forEach(item => {
      map.set(item.access_id, { ...item, children: [] });
    });

    items.forEach(item => {
      const node = map.get(item.access_id)!;
      if (item.parent_id === 0) {
        result.push(node);
      } else {
        const parent = map.get(item.parent_id);
        if (parent) {
          parent.children = parent.children || [];
          parent.children.push(node);
        }
      }
    });

    return result;
  };

  const fetchMenus = async () => {
    try {
      const response = await fetch('http://localhost:8000/authRole/user/getRoleList', {
        headers: {
          'token': `localStorage.getItem('token')`,
          'token': localStorage.getItem('token')
        }
      });
      const result = await response.json();
      
      if (result.code === 1) {
        const menuTree = buildMenuTree(result.data);
        setMenuItems(menuTree);
      }
    } catch (error) {
      console.error('接口错i了:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchMenus();
  }, []);

  const handleMenuClick: MenuProps['onClick'] = ({ key }) => {
    navigate(key);
  };

  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center">
        <Spin size="large" tip="ddd..." />
      </div>
    );
  }

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{ 
        padding: 0, 
        background: '#fff', 
        height: 64,
        boxShadow: '0 1px 4px rgba(0,21,41,.08)',
        position: 'fixed',
        zIndex: 1,
        width: '100%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between'
      }}>
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <div style={{ 
            width: 256, 
            height: 64, 
            display: 'flex', 
            alignItems: 'center', 
            justifyContent: 'center',
            borderRight: '1px solid #f0f0f0'
          }}>
            <h1 style={{ margin: 0, fontSize: 20, fontWeight: 'bold' }}>灌灌灌灌灌</h1>
          </div>
          {React.createElement(
            collapsed ? MenuUnfoldOutlined : MenuFoldOutlined,
            {
              className: 'trigger',
              style: { padding: '0 24px', fontSize: 18, cursor: 'pointer' },
              onClick: () => setCollapsed(!collapsed),
            }
          )}
        </div>
        <div style={{ padding: '0 24px' }}>
          <UserOutlined style={{ fontSize: 18 }} />
          <span style={{ marginLeft: 8 }}>管理员</span>
        </div>
      </Header>
      <Layout style={{ marginTop: 64 }}>
        <Sider
          trigger={null}
          collapsible
          collapsed={collapsed}
          style={{
            overflow: 'auto',
            height: '100vh',
            position: 'fixed',
            left: 0,
            top: 64,
            bottom: 0,
            background: '#fff'
          }}
          width={256}
        >
          <Menu
            mode="inline"
            theme="light"
            defaultSelectedKeys={[location.pathname]}
            defaultOpenKeys={menuItems.map(item => item.path)}
            style={{ height: '100%', borderRight: 0 }}
            items={transformMenuItems(menuItems)}
            onClick={handleMenuClick}
          />
        </Sider>
        <Layout style={{ padding: '24px', marginLeft: collapsed ? 80 : 256 }}>
          <Content
            style={{
              padding: 24,
              margin: 0,
              minHeight: 280,
              background: '#fff',
              borderRadius: 4,
              transition: 'all 0.2s'
            }}
          >
            <Outlet />
          </Content>
        </Layout>
      </Layout>
    </Layout>
  );
};

export default RoleList;