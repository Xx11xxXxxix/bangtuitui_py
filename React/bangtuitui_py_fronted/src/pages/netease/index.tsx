import React, { useEffect, useState } from 'react';
import { Card, Spin, message } from 'antd';
import { useNavigate } from 'react-router-dom';
const neteaseLogin: React.FC = () => {
    const [qrImage, setQrImage] = useState<string>('');
    const [unikey, setUnikey] = useState<string>('');
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    useEffect(() => {
      const neteaseCookie = localStorage.getItem('netease_cookie');
      if (neteaseCookie) {
          message.success('已登录网易云账号');
          navigate('/rolelist');
          return;
      }
      getQrCode();
  }, [navigate]);


  const getQrCode = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/netease/netEase_login/');
      const htmlText = await response.text();
      
      // 二维码
      const imgMatch = htmlText.match(/src="data:image\/png;base64,([^"]+)"/);
      const unikeyMatch = htmlText.match(/<span id="unikey">([^<]+)<\/span>/);
      
      if (imgMatch && imgMatch[1]) {
        setQrImage(`data:image/png;base64,${imgMatch[1]}`);
      }
      
      if (unikeyMatch && unikeyMatch[1]) {
        setUnikey(unikeyMatch[1]);
      }
      
      setLoading(false);
    } catch (error) {
      console.error('看后端接口去:', error);
      setLoading(false);
    }
  };

  const checkStatus = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/netease/check_status/?key=${unikey}`);
      const data = await response.json();
      
      if (data.code === 803) {
        // Done
        localStorage.setItem('netease_cookie', data.cookie);
        navigate('/');
      } else if (data.code === 800) {
        // 二维码过期
        getQrCode();
      }
    } catch (error) {
      console.error('接口错了:', error);
    }
  };

  useEffect(() => {
    getQrCode();
  }, []);

  useEffect(() => {
    if (unikey) {
      //轮询等几把wenjie下辈子也写不完
      const timer = setInterval(checkStatus, 5000);//5s一次够了
      return () => clearInterval(timer);
    }
  }, [unikey]);

  return (
    <div className="flex h-screen items-center justify-center bg-gray-100">
      <Card style={{ width: 300 }}>
        <div className="text-center">
          <h2 className="mb-6 text-xl font-bold">往南扫码</h2>
          {loading ? (
            <Spin tip="等会...撒比node延迟1分钟多" />
          ) : (
            <div>
              <img 
                src={qrImage} 
                alt="二维码" 
                style={{ width: '200px', height: '200px', margin: '0 auto' }}
              />
              <p className="mt-4 text-gray-500">todo 加多个网易账号绑定主账号</p>
            </div>
          )}
        </div>
      </Card>
    </div>
  );
};

export default neteaseLogin;