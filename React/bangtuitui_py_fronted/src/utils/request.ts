import axios from 'axios';
import { message } from 'antd';

const request = axios.create({
  timeout: 5000
});

// 请求拦截器
request.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  error => {
    console.error(error);
    return Promise.reject(error);
  }
);

// 响应拦截器
request.interceptors.response.use(
  response => {
    const res = response.data;
    if (res.code !== 1) {
      message.error(res.msg || '请求失败');
      // 401: 未登录或token过期
      if (res.code === 0) {
        localStorage.removeItem('token');
        localStorage.removeItem('userInfo');
        window.location.href = '/login';
      }
      return Promise.reject(res);
    }
    return res;
  },
  error => {
    console.error(error);
    message.error('网络错误，请稍后重试');
    return Promise.reject(error);
  }
);

export default request;