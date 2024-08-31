import React, { useState } from 'react';
import { View, Text, TextInput, Button, Image, StyleSheet, Alert, ScrollView } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import { Video } from 'expo-av';  // Use expo-av for video playback

const fetchImage = async (text) => {
  try {
    const response = await fetch('http://localhost:5000/generate-image', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error('Failed to fetch image:', error);
    throw error;
  }
};

const fetchVideo = async (text) => {
  try {
    const response = await fetch('http://localhost:5000/generate-video', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Failed to fetch video:', error);
    throw error;
  }
};


export default function App() {
  const [imageUri, setImageUri] = useState('');
  const [videoUri, setVideoUri] = useState('');
  const [imageText, setImageText] = useState('');
  const [videoText, setVideoText] = useState('');


  const handleGenerateImage = async () => {
    try {
      const data = await fetchImage(imageText);
      setImageUri(data.image_url);
    } catch (error) {
      Alert.alert('Error', 'Failed to generate image');
    }
  };

  const handleGenerateVideo = async () => {
    try {
      const data = await fetchVideo(videoText);
      setVideoUri(data.video_url);
    } catch (error) {
      Alert.alert('Error', 'Failed to generate video');
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Text to Image & Video Generator</Text>

      <View style={styles.column}>
        <Text style={styles.label}>Enter text for image generation:</Text>
        <TextInput
          style={styles.input}
          value={imageText}
          onChangeText={setImageText}
          placeholder="Type something for image..."
        />
        <Button title="Generate Image" onPress={handleGenerateImage} />



        {imageUri ? (
          <View style={styles.result}>
            <Text style={styles.resultTitle}>Generated Image:</Text>
            <Image source={{ uri: imageUri }} style={styles.image} />
          </View>
        ) : null}
      </View>

      <View style={styles.column}>
        <Text style={styles.label}>Enter text for video generation:</Text>
        <TextInput
          style={styles.input}
          value={videoText}
          onChangeText={setVideoText}
          placeholder="Type something for video..."
        />
        <Button title="Generate Video" onPress={handleGenerateVideo} />


        {videoUri ? (
          <View style={styles.result}>
            <Text style={styles.resultTitle}>Generated Video:</Text>
            <Video
              source={{ uri: videoUri }}
              style={styles.video}
              useNativeControls
              resizeMode="contain"
            />
          </View>
        ) : null}
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f7f9fc',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  column: {
    width: '100%',
    maxWidth: 600,
    backgroundColor: '#fff',
    padding: 20,
    borderRadius: 10,
    marginBottom: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
  },
  label: {
    fontWeight: 'bold',
    marginBottom: 8,
    color: '#555',
  },
  input: {
    width: '100%',
    padding: 10,
    marginBottom: 20,
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 5,
    fontSize: 16,
  },
  result: {
    alignItems: 'center',
    marginTop: 20,
  },
  resultTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  image: {
    width: '100%',
    height: 150,
    borderRadius: 10,
  },
  video: {
    width: '100%',
    height: 200,
  },
});
