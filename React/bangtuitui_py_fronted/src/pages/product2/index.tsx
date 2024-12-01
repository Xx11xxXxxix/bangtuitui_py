import React, { useState } from 'react';
import { Input, Button, List, message } from 'antd';
import axios from 'axios';

interface Song {
  id: number;
  name: string;
}

const Product2Page: React.FC = () => {
  const [artistId, setArtistId] = useState('');
  const [songs, setSongs] = useState<Song[]>([]);
  const [loading, setLoading] = useState(false);

  const fetchTopSongs = async () => {
    if (!artistId) {
      message.warning('请输入艺术家ID');
      return;
    }

    setLoading(true);
    try {
      const musicU = localStorage.getItem('netease_cookie'); 
      const response = await axios.get(`http://localhost:3000/recommend/songs?cookie=MUSIC_U=${musicU}`);

      setSongs(response.data.songs || []);
    } catch (error) {
      message.error('获取歌曲失败');
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4">
      <div className="mb-4 flex gap-2">
        <Input
          placeholder="请输入艺术家ID"
          value={artistId}
          onChange={(e) => setArtistId(e.target.value)}
          style={{ width: 200 }}
        />
        <Button type="primary" onClick={fetchTopSongs} loading={loading}>
          获取热门歌曲
        </Button>
      </div>

      <List
        loading={loading}
        bordered
        dataSource={songs}
        renderItem={(song) => (
          <List.Item>
            <div>{song.name}</div>
          </List.Item>
        )}
      />
    </div>
  );
};

export default Product2Page;