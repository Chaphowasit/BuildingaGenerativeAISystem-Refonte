import React, { useState } from 'react';

const App = () => {
  const [imageUrl, setImageUrl] = useState<string | null>(null);
  const [videoUrl, setVideoUrl] = useState<string | null>(null);
  const [text, setText] = useState<string>('');

  const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:5000'; 

  const generateImage = async () => {
    try {
      const response = await fetch(`${apiUrl}/generate-image`, { // Use environment variable for API URL
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      setImageUrl(data.image_url);
      console.log(data.image_url);
    } catch (error) {
      console.error('Error generating image:', error);
    }
  };

  const generateVideo = async () => {
    try {
      const response = await fetch(`${apiUrl}/generate-video`, { // Use environment variable for API URL
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      setVideoUrl(data.video_url);
      console.log(data.video_url);
    } catch (error) {
      console.error('Error generating video:', error);
    }
  };

  return (
    <div style={styles.container}>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text"
      />
      <button onClick={generateImage}>Generate Image</button>
      {imageUrl && (
        <div>
          <h3>Generated Image:</h3>
          <img src={imageUrl} alt="Generated" style={{ maxWidth: '100%', height: 'auto' }} />
        </div>
      )}

      <button onClick={generateVideo}>Generate Video</button>
      {videoUrl && (
        <div>
          <h3>Generated Video:</h3>
          <video controls width="600" style={{ maxWidth: '100%', height: 'auto' }}>
            <source src={videoUrl} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      )}
    </div>
  );
};

type FlexDirection = 'row' | 'row-reverse' | 'column' | 'column-reverse';

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column' as FlexDirection,
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    padding: '20px',
  },
};

export default App;
