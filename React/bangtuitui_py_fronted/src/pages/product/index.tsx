import React, { useState, useEffect, useCallback } from 'react';
import { Button, message, List, Avatar, Pagination } from 'antd';
import axios from 'axios';

interface Artist {
  id: number;
  name: string;
}

interface Song {
  name: string;
  id: number;
  ar: Artist[];
  al: {
    name: string;
    picUrl: string;
  };
  url?: string; // 为每首歌添加 URL 字段
}

const ProductPage: React.FC = () => {
  const [songs, setSongs] = useState<Song[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const pageSize = 10;

  // 从本地存储获取 MUSIC_U 并自动加载
  useEffect(() => {
    const storedMusicU = localStorage.getItem('netease_cookie');
    if (storedMusicU) {
      fetchTopSongsWithUrls(storedMusicU);
    } else {
      message.warning('请先登录获取您的推荐歌曲');
    }
  }, []);

  // 获取推荐歌曲并自动获取 URL
  const fetchTopSongsWithUrls = useCallback(async (musicU: string) => {
    if (!musicU.trim()) {
      message.warning('用户凭据无效，请重新登录');
      return;
    }

    setLoading(true);
    try {
      const response = await axios.get(`http://localhost:3000/recommend/songs?cookie=${musicU}`);
      const dailySongs: Song[] = response.data.data?.dailySongs || [];

      // 获取所有歌曲的 URL
      const songsWithUrls = await Promise.all(
        dailySongs.map(async (song) => {
          const url = await fetchSongUrl(song.id, musicU);
          return { ...song, url };
        })
      );

      setSongs(songsWithUrls);
      console.log('Updated Songs with URLs:', songsWithUrls);
    } catch (error) {
      message.error('获取歌曲失败，请稍后再试');
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  }, []);

  // 获取单首歌曲 URL
  const fetchSongUrl = async (songId: number, musicU: string, level: string = 'standard') => {
    try {
      const response = await axios.get(
        `http://localhost:3000/song/url/v1?id=${songId}&level=${level}&cookie=${musicU}`
      );
      return response.data.data?.[0]?.url || null;
    } catch (error) {
      console.error(`获取歌曲 ${songId} 的 URL 失败`, error);
      return null;
    }
  };

  // 分页切换逻辑
  const handlePageChange = (page: number) => setCurrentPage(page);

  // 当前页歌曲数据
  const paginatedSongs = songs.slice((currentPage - 1) * pageSize, currentPage * pageSize);

  return (
    <div className="p-4">
      <div className="mb-4">
        <Button type="primary" onClick={() => window.location.reload()} loading={loading}>
          刷新推荐歌曲
        </Button>
      </div>

      <List
        loading={loading}
        bordered
        dataSource={paginatedSongs}
        renderItem={(song) => (
          <List.Item>
            <List.Item.Meta
              avatar={<Avatar src={song.al.picUrl} alt={song.al.name} />}
              title={
                <div>
                  <div>
                    <strong>歌曲名:</strong> {song.name} <span style={{ color: '#aaa' }}>（ID: {song.id}）</span>
                  </div>
                  <div style={{ fontSize: '0.9em', color: '#888' }}>
                    <strong>艺术家:</strong> {song.ar.map((artist) => artist.name).join(', ')}
                  </div>
                  {song.url && (
                    <div>
                      <a href={song.url} target="_blank" rel="noopener noreferrer">
                        点击跳转到歌曲 URL
                      </a>
                    </div>
                  )}
                </div>
              }
            />
          </List.Item>
        )}
      />

      <Pagination
        current={currentPage}
        pageSize={pageSize}
        total={songs.length}
        onChange={handlePageChange}
        style={{ marginTop: '16px', textAlign: 'center' }}
      />
    </div>
  );
};

export default ProductPage;
