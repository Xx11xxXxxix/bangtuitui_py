import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Input, Button, Form, message } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import axios from 'axios';

const Login = () => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [sendingCode, setSendingCode] = useState(false);

  const onLoginFinish = async (values: { username: string; password: string; mobile?: string; code?: string }) => {
    setLoading(true);
    try {
      const response = await axios.post('http://127.0.0.1:8000/user_login/login/', values);
      if (response.data.code === 1 && response.data.data) {
        localStorage.setItem('token', response.data.data.token);
        localStorage.setItem('userInfo', JSON.stringify(response.data.data.userInfo));
        message.success('Done');
        navigate('/rolelist');
      } else {
        message.error(response.data.msg || 'CUO');
      }
    } catch (error: any) {
      if (error.response) {
        message.error(error.response.data.msg || 'CUO');
      } else {
        message.error('sobad');
      }
    } finally {
      setLoading(false);
    }
  };
  const onSendCode = async (mobile: string) => {
    if (!mobile) {
      message.error('Nomobile');
      return;
    }
    setSendingCode(true);
    try {
      const response = await axios.post('http://127.0.0.1:8000/send_sms_code/', { mobile });
      if (response.data.code === 1) {
        message.success('Coded');
      } else {
        message.error(response.data.msg || 'bad');
      }
    } catch (error) {
      message.error('sobad');
    } finally {
      setSendingCode(false);
    }
  };
  //注册
  const onRegisterFinish = async (values: { username: string; password: string; mobile?: string; code?: string }) => {
    setLoading(true);
    try {
      const response = await axios.post('http://127.0.0.1:8000/register/', values);
      if (response.data.code === 1) {
        message.success('GOODregister');
        navigate('/login');
      } else {
        message.error(response.data.msg || 'SOBADregister!');
      }
    } catch (error: any) {
      message.error('sobad');
    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-100">
      <div className="flex space-x-8">
        <div className="w-full max-w-md rounded-lg bg-white p-8 shadow-lg">
          <h2 className="mb-6 text-center text-2xl font-bold text-gray-800">Login</h2>
          <Form name="login" onFinish={onLoginFinish} autoComplete="off" layout="vertical">
            <Form.Item name="mobile" rules={[{ required: true, message: 'mobile' }]}>
              <Input placeholder="mobile" size="large" />
            </Form.Item>
            <Form.Item name="username" rules={[{ required: true, message: 'username' }]}>
              <Input prefix={<UserOutlined />} placeholder="username" size="large" />
            </Form.Item>
            <Form.Item name="password" rules={[{ required: true, message: 'password' }]}>
              <Input.Password prefix={<LockOutlined />} placeholder="password" size="large" />
            </Form.Item>
            <Form.Item name="code" rules={[{ required: true, message: 'code' }]}>
              <Input
                placeholder="code"
                size="large"
                suffix={<Button onClick={() => onSendCode('mobile')}>{sendingCode ? 'Dengzhe' : 'SENDDDD!!!!!!!!!'}</Button>}
              />
            </Form.Item>
            <Form.Item>
              <Button type="primary" htmlType="submit" loading={loading} className="w-full" size="large">
                Login
              </Button>
            </Form.Item>
          </Form>
        </div>
        <div className="w-full max-w-md rounded-lg bg-white p-8 shadow-lg">
          <h2 className="mb-6 text-center text-2xl font-bold text-gray-800">Register</h2>
          <Form name="register" onFinish={onRegisterFinish} autoComplete="off" layout="vertical">
            <Form.Item name="mobile" rules={[{ required: true, message: 'Nomobile!!' }]}>
              <Input placeholder="mobile" size="large" />
            </Form.Item>
            <Form.Item name="username" rules={[{ required: true, message: 'Nousername' }]}>
              <Input prefix={<UserOutlined />} placeholder="Nousername" size="large" />
            </Form.Item>
            <Form.Item name="password" rules={[{ required: true, message: 'Nopassword' }]}>
              <Input.Password prefix={<LockOutlined />} placeholder="Nopassword" size="large" />
            </Form.Item>
            <Form.Item name="code" rules={[{ required: true, message: 'Nocode' }]}>
              <Input
                placeholder="Nocode"
                size="large"
                suffix={<Button onClick={() => onSendCode('mobile')}>{sendingCode ? 'Sending.......' : 'SEND!!!!!!!!!'}</Button>}
              />
            </Form.Item>
            <Form.Item>
              <Button type="primary" htmlType="submit" loading={loading} className="w-full" size="large">
                Register
              </Button>
            </Form.Item>
          </Form>
        </div>
      </div>
    </div>
  );
};

export default Login;
