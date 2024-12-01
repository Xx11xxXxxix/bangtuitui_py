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
import NeteaseUserInfo from '@/components/netease_userInfo';

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
      {/* 左侧 Logo 和折叠按钮 */}
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <div style={{ 
          width: 200, 
          height: 64, 
          display: 'flex', 
          alignItems: 'center', 
          paddingLeft: 24,
          borderRight: '1px solid #f0f0f0'
        }}>
          <h1 style={{ margin: 0, fontSize: 20, fontWeight: 'bold' }}>灌灌灌灌灌</h1>
        </div>
        <div className="trigger" style={{ padding: '0 24px', cursor: 'pointer' }}>
          {collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
        </div>
      </div>

      {/* 右侧用户信息 */}
      <div style={{ display: 'flex', alignItems: 'center', paddingRight: 24 }}>
        <NeteaseUserInfo />
        <div style={{ marginLeft: 24, display: 'flex', alignItems: 'center' }}>
          <UserOutlined style={{ fontSize: 16 }} />
          <span style={{ marginLeft: 8 }}>管理员</span>
        </div>
      </div>
    </Header>

    <Layout>
      {/* 侧边栏 */}
      <Sider
        trigger={null}
        collapsible
        collapsed={collapsed}
        style={{
          background: '#fff',
          position: 'fixed',
          left: 0,
          top: 64,
          height: 'calc(100vh - 64px)',
          zIndex: 10,
          boxShadow: '2px 0 8px 0 rgba(29,35,41,.05)'
        }}
        width={200}
      >
        <Menu
          mode="inline"
          theme="light"
          defaultSelectedKeys={[location.pathname]}
          defaultOpenKeys={menuItems.map(item => item.path)}
          style={{ 
            height: '100%', 
            borderRight: 0,
            paddingTop: 16 
          }}
          items={transformMenuItems(menuItems)}
          onClick={handleMenuClick}
        />
      </Sider>


      {/* 主内容区 */}
      <Layout style={{ 
        marginLeft: collapsed ? 80 : 200,
        marginTop: 64,
        padding: '24px',
        background: '#f0f2f5'
      }}>
        <Content style={{
          background: '#fff',
          padding: 24,
          minHeight: 'calc(100vh - 112px)',
          borderRadius: 4,
          boxShadow: '0 1px 2px 0 rgba(0,0,0,0.03)'
        }}>
            <Outlet />
          </Content>
        </Layout>
      </Layout>
    </Layout>
  );
};

export default RoleList;