import React, { useState } from 'react';
import { Button, Modal, Spin, message, Card, Row, Col } from 'antd';
const NeteaseUserInfo: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [userInfo, setUserInfo] = useState<any>(null);
  const [accountInfo, setAccountInfo] = useState<any>(null);
  const [visible, setVisible] = useState(false);

  const getUserInfo = async () => {
    setLoading(true);
    try {
      const neteaseCookie = localStorage.getItem('netease_cookie');
      if (!neteaseCookie) {
        message.error('登陆去');
        return;
      }

      // 提取 MUSIC_U
      const musicU = extractMusicU(neteaseCookie);
      
      const response = await fetch(
        `http://127.0.0.1:8000/netease/get_user_info?cookie=MUSIC_U=${musicU}`
      );
      const data = await response.json();

      if (data.code === 200) {
        setUserInfo(data.profile);
        setAccountInfo(data.account);
        setVisible(true);
      } else {
        message.error(data.msg || '被风控了');
      }
    } catch (error) {
      message.error('看后端去');
    } finally {
      setLoading(false);
    }
  };

  const extractMusicU = (cookie: string) => {
    const match = cookie.match(/MUSIC_U=([^;]+)/);
    return match ? match[1] : '';
  };

  return (
    <>
      <Button 
        onClick={getUserInfo} 
        loading={loading}
        type="primary"
      >
        看你的往南号
      </Button>

      <Modal
        title="看你的往南号"
        open={visible}
        onOk={() => setVisible(false)}
        onCancel={() => setVisible(false)}
        width={800}
        style={{ top: 20 }}
      >
          {userInfo && accountInfo ? (
        <div style={{ maxHeight: '70vh', overflow: 'auto' }}>
          <Card title="基本信息" style={{ marginBottom: 16 }}>
            <Row gutter={[16, 16]}>
              <Col span={12}>用户ID: {userInfo.userId}</Col>
              <Col span={12}>昵称: {userInfo.nickname}</Col>
              <Col span={12}>用户名: {userInfo.userName}</Col>
              <Col span={12}>性别: {userInfo.gender === 1 ? '男' : userInfo.gender === 2 ? '女' : '未设置'}</Col>
              <Col span={12}>签名: {userInfo.signature || '无'}</Col>
              <Col span={12}>生日: {new Date(userInfo.birthday).toLocaleDateString()}</Col>
              <Col span={12}>省份: {userInfo.province}</Col>
              <Col span={12}>城市: {userInfo.city}</Col>
            </Row>
          </Card>

          <Card title="账户信息" style={{ marginBottom: 16 }}>
            <Row gutter={[16, 16]}>
              <Col span={12}>账户ID: {accountInfo.id}</Col>
              <Col span={12}>账户类型: {accountInfo.type}</Col>
              <Col span={12}>VIP类型: {accountInfo.vipType}</Col>
              <Col span={12}>账户状态: {accountInfo.status}</Col>
              <Col span={12}>创建时间: {new Date(accountInfo.createTime).toLocaleString()}</Col>
              <Col span={12}>Token版本: {accountInfo.tokenVersion}</Col>
            </Row>
          </Card>

          <Card title="详细信息">
            <Row gutter={[16, 16]}>
              <Col span={12}>
                头像: <img src={userInfo.avatarUrl} alt="头像" style={{ width: 50, height: 50 }} />
              </Col>
              <Col span={12}>
                背景图: <img src={userInfo.backgroundUrl} alt="背景" style={{ width: 100 }} />
              </Col>
              <Col span={12}>创建时间: {new Date(userInfo.createTime).toLocaleString()}</Col>
              <Col span={12}>最后登录: {new Date(userInfo.lastLoginTime).toLocaleString()}</Col>
              <Col span={12}>最后登录IP: {userInfo.lastLoginIP}</Col>
              <Col span={12}>用户类型: {userInfo.userType}</Col>
              <Col span={12}>DJ状态: {userInfo.djStatus}</Col>
              <Col span={12}>认证状态: {userInfo.authStatus}</Col>
              <Col span={12}>默认头像: {userInfo.defaultAvatar ? '是' : '否'}</Col>
              <Col span={12}>是否关注: {userInfo.followed ? '是' : '否'}</Col>
              <Col span={12}>互相关注: {userInfo.mutual ? '是' : '否'}</Col>
              <Col span={12}>是否认证: {userInfo.authenticated ? '是' : '否'}</Col>
              <Col span={12}>是否主播: {userInfo.anchor ? '是' : '否'}</Col>
            </Row>
          </Card>
        </div>
      ) : (
        <Spin />
        )}
      </Modal>
    </>
  );
};

export default NeteaseUserInfo;